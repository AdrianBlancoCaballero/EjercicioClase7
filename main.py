# Ejercicio de Clase 7

lista = []

while True:
    marca = input("Marca de coche: ")
    if marca == "fin":
        break
    modelo = input("Modelo de coche: ")
    combustible = input("Tipo de combustible: ")
    cilindrada = input("Cilindrada del motor: ")

    datos = {}
    datos ["marca"] = marca
    datos ["modelo"] = modelo
    datos ["combustible"] = combustible
    datos ["cilindrada"] = cilindrada
    lista.append(datos)

for datos in lista:
    print("Vehículo: ", datos)