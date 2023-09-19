import numpy as np
import matplotlib.pyplot as plt

# Valores iniciais
comprimento_braco = 2.0  # Comprimento do braço
angulos = np.radians(np.arange(30, 136))  # Variação de ângulos de 30° a 135° em radianos

# Calcular as coordenadas x e y para o ponto A
x = comprimento_braco * np.cos(angulos)
y = comprimento_braco * np.sin(angulos)

# Plotar a trajetória do ponto A
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Trajetória do Ponto A', marker='o', markersize=5)
plt.title('Trajetória do Ponto A')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)
plt.legend()
plt.axis('equal')  # Para manter a proporção igual nos eixos x e y
plt.show()
