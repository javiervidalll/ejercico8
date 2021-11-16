# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import persistencia_json
lista_coches = list()
while True:
    marca = input("marca del coche: ")
    if marca == "fin":
        break
    modelo = input("modelo: ")
    combustible = input("combustible: ")
    cilindrada = input("cilindrada: ")
    linea = {}
    linea["marca coche"] = marca
    linea["combustible"] = combustible
    linea["cilindrada"] = cilindrada
    linea["modelo"] = modelo
    lista_coches.append(linea)
print("lista de coches:\n", lista_coches)

lista_coches = persistencia_json.loads(persistencia_json.load(open("coches.txt","r")))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
