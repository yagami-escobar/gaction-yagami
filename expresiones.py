import os

def main():
  name = os.getenv('NAME')
  age = os.getenv('AGE')
  lp = os.getenv('LP')
  sex = os.getenv('SEX')
  print(f"Hola tu nombre es {name} y tienes {age} años de edad y tu LP favorito es {lp} y tu sexo es {sex}")

if __name__ == '__main__':
  main()
