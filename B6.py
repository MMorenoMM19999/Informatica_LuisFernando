# Escriba un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario tiene que adivinarlo). El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y después el usuario va probando valores y el programa va diciendo si son demasiado grandes o pequeños.



import random

def juego_adivinar_numero(inicio, fin):
    numero_a_adivinar = random.randint(inicio, fin)
    intentos = 0

    print(f"Bienvenido al juego de adivinar el número entre {inicio} y {fin}.")

    while True:
        intento = int(input("Introduce tu intento: "))
        intentos += 1

        if intento < numero_a_adivinar:
            print("El número es mayor.")
        elif intento > numero_a_adivinar:
            print("El número es menor.")
        else:
            print(f"Felicidades, ¡adivinaste el número en {intentos} intentos!")
            break

# Pide al usuario los límites para el juego
inicio = int(input("Introduce el número inicial del rango: "))
fin = int(input("Introduce el número final del rango: "))

# Inicia el juego
juego_adivinar_numero(inicio, fin)
