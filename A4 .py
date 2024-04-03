#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.

def main():
  print("CONTADOR DE PARES E IMPARES")
  valores = int(input("¿Cuántos valores va a introducir? "))
  if valores < 0:
      print("¡Imposible!")
  else:
      pares = 0
      for i in range(1, valores + 1):
          numero = int(input(f"Escriba el valor {i}: "))
          if numero % 2 == 0:
              pares += 1
      print(f"Ha escrito {pares} números pares y {valores - pares} números impares.")
      print("Gracias por su colaboración.")


if __name__ == "__main__":
  main()