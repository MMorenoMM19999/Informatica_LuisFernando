#Escriba un programa que pida dos números enteros y escriba la suma de todos los enteros desde el primer número hasta el segundo.



def main():
  print("SUMA ENTRE VALORES")
  numero_1 = int(input("Escriba un número entero positivo: "))
  if numero_1 <= 0:
      print("¡Le he pedido un número entero positivo!")
  else:
      numero_2 = int(input(f"Escriba un número entero mayor que {numero_1}: "))
      if numero_2 <= numero_1:
          print(f"¡Le he pedido un número entero mayor que {numero_1}!")
      else:
          suma = 0
          for i in range(numero_1, numero_2 + 1):
              suma = suma + i
          print(f"La suma desde {numero_1} hasta {numero_2} es {suma}")


if __name__ == "__main__":
  main()