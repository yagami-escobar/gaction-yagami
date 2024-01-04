import os

def main():
  edad = os.getenv("EDAD")
  nombre = os.getenv("NOMBRE")
  lp = os.getenv("LP")
  tag = os.getenv("TAG")
  env = os.getenv("ENVIRONMENT")
  print(f"Hola {nombre} tienes {edad} años de edad tu LP favorito es {lp} y tu tag es {tag} y tu environment es {env}")

if __name__ == '__main__':
  main()
