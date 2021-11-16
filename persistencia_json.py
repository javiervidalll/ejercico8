import json
def store(var,archivo):
    json.dump(json.dumps(lista_coches), open("coches.txt", "w"))


def retrieve(archivo):
    return json.loads(json.load(open(archivo,"r")))
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




lista_coches = []
lista_coches = json.loads(json.load(open("coches.txt","r")))
print("listado coches del txt creado: ",lista_coches)


