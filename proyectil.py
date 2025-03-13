import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define la velocidad inicial y el ángulo
v_i = 9
theta = np.radians(45)  # Asumimos un ángulo de 45 grados para el ejemplo

# Define las componentes de la velocidad
v_x = v_i * np.cos(theta)
v_y = v_i * np.sin(theta)

# Define la aceleración debida a la gravedad
g = 9.81

# Calcula el tiempo total de vuelo y crea un array de tiempos
t_total = 2 * v_y / g
t = np.linspace(0, t_total, num=30)

# Define las ecuaciones de movimiento
x = v_x * t
y = v_y * t - 0.5 * g * t**2

# Crea la figura y los ejes para la animación
fig, ax = plt.subplots()
ax.set_xlim(0, max(x))
ax.set_ylim(0, max(y))
line, = ax.plot([], [], 'r-')

# Define la función de inicialización de la animación
def init():
    line.set_data([], [])
    return line,

# Define la función de animación
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

# Crea la animación
ani = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True)

plt.show()
