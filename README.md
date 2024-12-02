### **README - Versão 1: Simulação de Fluido com Controle Interativo (Sem Reinício)**

## Descrição

Este código simula um campo de fluido tridimensional com partículas que se movem com base nas velocidades interpoladas do campo de fluido. Ele utiliza o `matplotlib` para visualização, incluindo um gráfico 3D dinâmico que exibe as partículas, o campo de vetores de fluxo e permite a interação do usuário através de controles como sliders e caixas de texto.

O código permite ajustar a intensidade do fluido, a direção do fluxo e o número de partículas. A simulação é atualizada em tempo real, sem a necessidade de reiniciar a animação, o que proporciona uma experiência interativa e contínua.

## Funcionalidades

- **Partículas em 3D**: O movimento das partículas é baseado no campo de fluido gerado e interpolado.
- **Controle da Intensidade do Fluido**: Um slider permite controlar a intensidade do campo de fluido.
- **Controle da Direção do Fluxo**: Um slider ajusta a direção do fluxo do fluido.
- **Número de Partículas**: Um campo de texto permite que o número de partículas seja alterado dinamicamente.
- **Animação Contínua**: A animação é atualizada continuamente sem a necessidade de reiniciar.

## Instalação

1. Instale as dependências:

```bash
pip install numpy scipy matplotlib
```

2. Execute o código Python:

```bash
python fluid_simulation.py
```

## Como Funciona

1. **Campo de Fluido 3D**: O campo de fluido é gerado no espaço 3D com componentes de velocidade baseados em uma combinação de funções trigonométricas e sinusoidais.
2. **Movimento das Partículas**: As partículas se movem através da interpolação do campo de fluido usando Radial Basis Function (RBF).
3. **Interatividade**: O número de partículas, a intensidade do fluido e a direção do fluxo podem ser controlados com sliders e campos de texto, afetando a simulação em tempo real.

### **Estrutura do Código**

#### 1. **Classe FluidSimulation**
A classe principal que gerencia a criação do campo de fluido, as partículas e os controles interativos.

- **Métodos principais**:
  - `generate_fluid_field`: Gera um campo de fluido tridimensional com componentes de velocidade baseados em funções trigonométricas.
  - `move_particles`: Atualiza a posição das partículas com base nas velocidades interpoladas.
  - `create_rbf_interpolation`: Cria uma interpolação RBF para calcular as velocidades no campo de fluido.
  - `update_plot`: Atualiza a visualização a cada quadro da animação.
  - `create_input_widgets`: Cria os controles interativos (campo de texto e sliders).
  - `update_velocity` e `update_flow_direction`: Atualizam a intensidade e a direção do fluxo com base nas entradas dos sliders.
  
#### 2. **Interatividade**

- A caixa de texto permite que o usuário ajuste o número de partículas.
- Os sliders controlam a intensidade do fluido e a direção do fluxo.

---

### **README - Versão 2: Simulação de Fluido com Reinício da Animação**

## Descrição

Esta versão da simulação de fluido é similar à versão anterior, mas com uma diferença importante: ela inclui um botão para **reiniciar** a animação, o que permite redefinir o número de partículas e o campo de fluido a qualquer momento. Além disso, o código também inclui controles interativos como sliders e caixas de texto.

## Funcionalidades

- **Partículas em 3D**: As partículas são movidas com base em um campo de fluido tridimensional, sendo atualizadas a cada quadro da animação.
- **Controle de Intensidade do Fluido e Direção do Fluxo**: Ajuste da intensidade e da direção do fluido através de sliders.
- **Número de Partículas**: O número de partículas pode ser modificado dinamicamente através de uma caixa de texto.
- **Botão para Reiniciar a Animação**: Permite reiniciar a simulação e ajustar o número de partículas e o campo de fluido.
- **Animação Interativa**: A animação é atualizada a cada quadro, refletindo as mudanças feitas nos controles.

## Instalação

1. Instale as dependências:

```bash
pip install numpy scipy matplotlib
```

2. Execute o código Python:

```bash
python fluid_simulation_with_restart.py
```

## Como Funciona

1. **Campo de Fluido 3D**: O campo de fluido é gerado em 3D com componentes de velocidade baseados em funções trigonométricas, e a interpolação RBF é usada para calcular as velocidades nas posições das partículas.
2. **Movimento das Partículas**: As partículas se movem no campo de fluido com base nas velocidades interpoladas usando o método `Rbf`.
3. **Interatividade**:
   - **Número de Partículas**: Através de um campo de texto, o usuário pode definir o número de partículas exibidas na animação.
   - **Controle da Intensidade e Direção do Fluido**: Os sliders permitem alterar esses parâmetros em tempo real.
   - **Botão de Reinício**: O botão "Reiniciar" redefine a simulação, permitindo atualizar o número de partículas e recriar o campo de fluido.

### **Estrutura do Código**

#### 1. **Classe FluidSimulation**
A classe principal que gerencia a criação do campo de fluido, partículas, animação e os controles interativos.

- **Métodos principais**:
  - `generate_fluid_field`: Gera o campo de fluido tridimensional.
  - `move_particles`: Atualiza a posição das partículas com base na interpolação do campo de fluido.
  - `create_rbf_interpolation`: Cria a interpolação RBF para calcular as velocidades do fluido.
  - `update_plot`: Atualiza a animação com base no movimento das partículas.
  - `restart_animation`: Reinicia a animação, recriando o número de partículas e o campo de fluido com base na entrada do usuário.
  - `create_input_widgets`: Cria os controles interativos (campo de texto e botão de reinício).

#### 2. **Interatividade**

- **Caixa de Texto**: Permite ao usuário alterar o número de partículas.
- **Sliders**: Usados para controlar a intensidade do fluido e a direção do fluxo.
- **Botão "Reiniciar"**: O botão que reinicia a animação, recriando as partículas e o campo de fluido.
