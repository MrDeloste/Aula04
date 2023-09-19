import numpy as np
import matplotlib.pyplot as plt

# Gerar valores de x no intervalo de 0 a 2*pi
x = np.linspace(0, 2 * np.pi, 1000)

# Calcular os valores do cosseno para cada valor de x usando numpy
y = np.cos(x)

# Plotar o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='cos(x)')
plt.title('Gráfico da Função Cosseno')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid(True)
plt.legend()
plt.show()
