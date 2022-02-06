#Ejercicio 7: Escribe un programa que muestre por pantalla los números múltiplos de 7 entre el 1 y el 1000. Utiliza range(1001) en un bucle for con los if necesarios. Después haz lo mismo empleando un range con tres parámetros.

multiplos = 0
for j in range(1001):
    if j % 7 == 0 and j != 0:
        multiplos += 1

print (f"los multiplos con un rango son: {multiplos}")

multiplos = 0
for j in range(7, 80, 6):
    if j % 7 == 0 and j != 0:
        multiplos += 1

print (f"los multiplos con tres rango son: {multiplos}")


