# Escriba un programa que simule una hucha. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará que las cantidades sean positivas.


def main():
  print("HUCHA")

  objetivo = float(input("¿Cuántos euros quiere ahorrar?: "))

  ahorrado = 0.0
  while objetivo > ahorrado:
      ahorrado += float(input("¿Cuántos euros quiere meter en la hucha?: "))

  print(f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.")


if __name__ == "__main__":
main()