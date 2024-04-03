# Escriba un programa que proponga sumas de números positivos (dos números entre 1 y 100) al usuario y compruebe la respuesta. El programa continuará hasta : 

#- que el programa permita repetir las operaciones e indique al final el tiempo mínimo que se ha conseguido
#- que el programa indique cuántos segundos ha tardado en contestar correctamente las operaciones
#- que el programa pida cuántas operaciones se deben acertar para terminar el programa. Al terminar, el programa indicará cuántos intentos han sido necesarios.




import random
from time import time

cantidad = int(input("¿Cuántas operaciones correctas debe contestar para terminar el programa? "))

while cantidad < 1:
    print("El número de operaciones debe ser mayor que cero")
    cantidad = input("¿Cuántas operaciones correctas debe contestar para terminar el programa? ")
print()

seguir = "S"
minimo = float("inf")

while seguir == "S" or seguir == "s":
    print("Escriba el resultado de las siguientes operaciones")

    correctas = 0
    total = 0
    inicio = time()

    while correctas < cantidad:
        a = random.randrange(1, 101)
        b = random.randrange(1, 101)
        respuesta = int(input(f"{a} + {b}: "))
        total += 1
        if respuesta == a + b:
            correctas += 1
            print("¡Respuesta correcta!")
        else:
            print("¡Respuesta incorrecta!")
        print()

    final = time()
    tiempo = round(final - inicio, 1)
    if tiempo < minimo:
        minimo = tiempo

    print(f"Ha tardado {tiempo} segundos en ", end="")

    if cantidad == 1:
        print("acertar 1 operación ", end="")
    else:
        print(f"acertar {correctas} operaciones ", end="")

    if total == 1:
        print("en 1 intento.")
    else:
        print(f"en {total} intentos.")

    seguir = input("¿Quiere probar otra vez? (S/N): ")

print()
print(f"Su tiempo mínimo ha sido {minimo} segundos.")
print("Programa terminado.")


