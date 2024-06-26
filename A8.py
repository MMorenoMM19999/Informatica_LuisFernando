#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y escriba el mayor, el menor y la media aritmética.

#Se recuerda que la media aritmética de un conjunto de valores es la suma de esos valores dividida por la cantidad de valores.

def main():
  print("MAYOR, MENOR Y MEDIA ARITMÉTICA")
  numero = int(input("¿Cuántos valores va a introducir? "))

  if numero <= 0:
      print("¡Imposible!")
  else:
      valor = float(input("Escriba el número 1: "))
      minimo = maximo = suma = valor
      for i in range(2, numero + 1):
          valor = float(input(f"Escriba el número {i}: "))
          suma = suma + valor
          if valor < minimo:
              minimo = valor
          if valor > maximo:
              maximo = valor
      print(f"El número más pequeño de los introducidos es {minimo}")
      print(f"El número más grande de los introducidos es {maximo}")
      print(f"La media de los números introducidos es {suma / numero}")

if __name__ == "__main__":
  main()