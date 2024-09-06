arcoiris=("rojo","azul","morado","amarillo")

print("\n",arcoiris)

print("\n Longitud:  \n",len(arcoiris))

animales=("perro",5,"estatura",1)
print("\n",animales)

print("\n---Elementos de la tupla------ \n",animales[1])
print("\n --Cambiando elementos--")
rateros = ("Brayan", "Joshua", "Kevin")
y = list(rateros)
y[1] = "kimberly"
rateros = tuple(y)
print(rateros)

print("\n --Agregando elementos--")
nanimal=("Panfilo","Pancracio","Bobby")
y = list(nanimal)
print(y)
y.append("Filomeno")
nanimal2 = tuple(y)
print(nanimal2)

print("\n Uso de for en tuplas")
for color in arcoiris:
    print(color)
