import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import matplotlib.widgets as widgets

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

        # Criando a animação
        self.ani = FuncAnimation(self.fig, self.update_plot, frames=100, fargs=(self.particles, self.rbf_interp, self.ax), interval=50)

    def generate_fluid_field(self, grid_size=20):
        # Gerando um campo de fluido em 3D com movimento helicoidal
        x = np.linspace(-5, 5, grid_size)
        y = np.linspace(-5, 5, grid_size)
        z = np.linspace(-5, 5, grid_size)
        X, Y, Z = np.meshgrid(x, y, z)
        
        # Componente de velocidade baseada em uma espiral 3D
        U = -Y  # Componente X da velocidade
        V = X   # Componente Y da velocidade
        W = np.sin(X)  # Componente Z da velocidade
        
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
        
        return ax,

    def restart_animation(self, val):
        num_particles = int(self.num_particles_textbox.text)
        
        # Recriar partículas e interpolação RBF com o valor da caixa de texto
        self.particles = np.random.uniform(-5, 5, (num_particles, 3))
        self.X, self.Y, self.Z, self.U, self.V, self.W = self.generate_fluid_field()
        self.rbf_interp = self.create_rbf_interpolation(self.X, self.Y, self.Z, self.U, self.V, self.W)
        
        # Criar uma nova animação
        self.ani = FuncAnimation(self.fig, self.update_plot, frames=100, fargs=(self.particles, self.rbf_interp, self.ax), interval=50)

        # Atualizar o gráfico
        plt.draw()
        self.fig.canvas.flush_events()

    def create_input_widgets(self, ax):
        axcolor = 'lightgoldenrodyellow'
        
        # Textbox para número de partículas
        ax_particles = plt.axes([0.15, 0.01, 0.65, 0.03], facecolor=axcolor)
        num_particles_textbox = widgets.TextBox(ax_particles, 'Número de Partículas', initial="100")
        
        # Botão para reiniciar a animação
        ax_restart = plt.axes([0.8, 0.01, 0.1, 0.05], facecolor=axcolor)
        restart_button = widgets.Button(ax_restart, 'Reiniciar')
        restart_button.on_clicked(self.restart_animation)
        
        return num_particles_textbox

    def show(self):
        plt.show()

# Criando e exibindo a simulação
simulation = FluidSimulation()
simulation.show()
