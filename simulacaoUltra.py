import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import matplotlib.widgets as widgets
from matplotlib import cm

class FluidSimulation:
    def __init__(self):
        # Inicializando o campo de fluido e as partículas
        self.X, self.Y, self.Z, self.U, self.V, self.W = self.generate_fluid_field()
        self.particles = np.random.uniform(-5, 5, (100, 3))
        self.rbf_interp = self.create_rbf_interpolation(self.X, self.Y, self.Z, self.U, self.V, self.W)

        # Inicializando o gráfico
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Criando widgets de entrada
        self.num_particles_textbox = self.create_input_widgets(self.ax)

        # Criando sliders de controle
        self.velocity_slider = self.create_velocity_slider(self.ax)
        self.flow_direction_slider = self.create_flow_direction_slider(self.ax)

        # Criando a animação
        self.ani = FuncAnimation(self.fig, self.update_plot, frames=100, fargs=(self.particles, self.rbf_interp, self.ax), interval=50)

    def generate_fluid_field(self, grid_size=20):
        # Gerando um campo de fluido em 3D com movimento helicoidal (e pequenas variações para simulação)
        x = np.linspace(-5, 5, grid_size)
        y = np.linspace(-5, 5, grid_size)
        z = np.linspace(-5, 5, grid_size)
        X, Y, Z = np.meshgrid(x, y, z)
        
        # Variação no fluxo (movimento helicoidal e aleatório)
        U = -Y + np.sin(X)  # Componente X da velocidade
        V = X + np.cos(Y)   # Componente Y da velocidade
        W = np.sin(Z)  # Componente Z da velocidade
        
        return X, Y, Z, U, V, W

    def move_particles(self, particles, rbf_interp):
        # Interpolando a velocidade do fluido nas posições das partículas
        velocities = rbf_interp(particles[:, 0], particles[:, 1], particles[:, 2])
        
        # Atualizando as partículas com base nas velocidades
        particles[:, 0] += velocities[:, 0] * 0.1  # Velocidade X
        particles[:, 1] += velocities[:, 1] * 0.1  # Velocidade Y
        particles[:, 2] += velocities[:, 2] * 0.1  # Velocidade Z
        
        return particles

    def create_rbf_interpolation(self, X, Y, Z, U, V, W):
        # Criando uma interpolação RBF para cada componente do vetor de velocidade
        rbf_U = interp.Rbf(X.flatten(), Y.flatten(), Z.flatten(), U.flatten(), function='multiquadric')
        rbf_V = interp.Rbf(X.flatten(), Y.flatten(), Z.flatten(), V.flatten(), function='multiquadric')
        rbf_W = interp.Rbf(X.flatten(), Y.flatten(), Z.flatten(), W.flatten(), function='multiquadric')
        
        # Retornando uma função que fornece as velocidades nas posições das partículas
        return lambda x, y, z: np.column_stack([rbf_U(x, y, z), rbf_V(x, y, z), rbf_W(x, y, z)])

    def update_plot(self, frame, particles, rbf_interp, ax):
        ax.clear()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_zlim(-5, 5)
        
        # Atualizando as partículas com base na interpolação RBF
        particles = self.move_particles(particles, rbf_interp)
        
        # Plotando as partículas
        ax.scatter(particles[:, 0], particles[:, 1], particles[:, 2], color='b', s=1)
        
        # Plotando as direções do fluxo como vetores
        self.plot_flow_vectors(ax)
        
        return ax,

    def plot_flow_vectors(self, ax):
        # Exibindo vetores de direção do fluxo (usando uma amostra de pontos)
        x = np.linspace(-5, 5, 10)
        y = np.linspace(-5, 5, 10)
        z = np.linspace(-5, 5, 10)
        X, Y, Z = np.meshgrid(x, y, z)
        U = -Y + np.sin(X)  # Componente X da velocidade
        V = X + np.cos(Y)   # Componente Y da velocidade
        W = np.sin(Z)  # Componente Z da velocidade
        ax.quiver(X, Y, Z, U, V, W, length=0.2, normalize=True, color=cm.viridis(np.random.rand()))

    def create_input_widgets(self, ax):
        axcolor = 'lightgoldenrodyellow'
        
        # Textbox para número de partículas
        ax_particles = plt.axes([0.15, 0.01, 0.65, 0.03], facecolor=axcolor)
        num_particles_textbox = widgets.TextBox(ax_particles, 'Número de Partículas', initial="100")
        
        return num_particles_textbox

    def create_velocity_slider(self, ax):
        axcolor = 'lightgoldenrodyellow'
        
        # Slider para controlar a intensidade do campo de fluido
        ax_velocity = plt.axes([0.15, 0.06, 0.65, 0.03], facecolor=axcolor)
        velocity_slider = widgets.Slider(ax_velocity, 'Intensidade do Fluido', 0.1, 5.0, valinit=1.0)
        
        # Atualizar a intensidade do fluido
        velocity_slider.on_changed(self.update_velocity)
        return velocity_slider

    def create_flow_direction_slider(self, ax):
        axcolor = 'lightgoldenrodyellow'
        
        # Slider para controlar a direção do fluxo
        ax_flow_direction = plt.axes([0.15, 0.11, 0.65, 0.03], facecolor=axcolor)
        flow_direction_slider = widgets.Slider(ax_flow_direction, 'Direção do Fluxo', -1.0, 1.0, valinit=0.0)
        
        # Atualizar a direção do fluxo
        flow_direction_slider.on_changed(self.update_flow_direction)
        return flow_direction_slider

    def update_velocity(self, val):
        # Atualizar a intensidade do campo de fluido
        self.U *= val
        self.V *= val
        self.W *= val
        self.rbf_interp = self.create_rbf_interpolation(self.X, self.Y, self.Z, self.U, self.V, self.W)

    def update_flow_direction(self, val):
        # Atualizar a direção do fluxo
        angle = val * np.pi  # Converter para radianos
        self.U = -np.sin(angle)  # Direção do fluido no eixo X
        self.V = np.cos(angle)   # Direção do fluido no eixo Y
        self.W = np.sin(angle)   # Direção do fluido no eixo Z
        self.rbf_interp = self.create_rbf_interpolation(self.X, self.Y, self.Z, self.U, self.V, self.W)

    def show(self):
        plt.show()

# Criando e exibindo a simulação
simulation = FluidSimulation()
simulation.show()
