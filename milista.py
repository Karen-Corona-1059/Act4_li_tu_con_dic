#Ejemplos de uso de listas

misperros = ["Hershey","Frida","Lola","Frijol"]
misnumeros = [5,15,7]

#Mostrando a mis perros
print(misperros)
#Mostrando mis números
print(misnumeros)


print("--Accediendo a los elementos de la lista--")
print(misperros[-1])

if "Pancracio" in misperros:
  print("si, 'Frijol' esta en la lista de mis  perros ")
else: 
  print("No es mi perro")

nperros=len(misperros)
print(f"Número de perros: {nperros} ")

print("Ciclo for de listas")
p=0
for perrofav in misperros :
  print(p,"",perrofav)
  p = p+1