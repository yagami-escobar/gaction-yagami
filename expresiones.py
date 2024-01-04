import os

def main():
  nombre = os.getenv("NOMBRE")
  edad = os.getenv("EDAD")
  sex = os.getenv("SEX")
  lp = os.getenv("LP")
  print(f"Hola {nombre} tienes {edad} años de edad tu LP favorito es {lp} y tu sexo es {sex}")

if __name__ == '__main__':
  main()
