# Solicitar ao usuário que digite as coordenadas
coordenadas = input("Digite as coordenadas no formato (x;y;z): ")

# Remover parênteses e dividir as coordenadas em valores separados
coordenadas = coordenadas.strip('()')
x, y, z = coordenadas.split(';')

# Converter os valores para números inteiros (ou float, dependendo do uso)
x = int(x)
y = int(y)
z = int(z)

# Imprimir os valores separados
print("Valor de x:", x)
print("Valor de y:", y)
print("Valor de z:", z)
