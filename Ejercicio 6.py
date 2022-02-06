#Ejercicio 6:Escribe un programa que, a partir de una tupla cualquiera, obtenga una lista con todos los elementos de la tupla. Utiliza un bucle.

lista = ("a","e","i","o","u")
lista_vocales = []

for j in range(0, len(lista)):
    print(lista[j])
    lista_vocales.append(lista[j])
    print(f"las vocales son: {lista_vocales}")
    
