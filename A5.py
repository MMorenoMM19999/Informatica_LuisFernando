#Escriba un programa que pregunte cuantos números se van a introducir, pida esos números (que puedan ser decimales) y calcule su suma.


def main():
  print("SUMA DE VALORES")
  numero = int(input("¿Cuántos valores va a introducir? "))

  if numero <= 0:
      print("¡Imposible!")
  else:
      suma = 0
      for i in range(1, numero + 1):
          valor = float(input(f"Escriba el número {i}: "))
          suma = suma + valor
      print(f"La suma de los números que ha escrito es {suma}")


if __name__ == "__main__":
  main()