import os
def main():
  nombre = os.getenv('inputs.nombre')
  lp = os.getenv('inputs.lps')
  print(f"Hola {nombre} from {lp} :D !!")
if __name__ == '__main__':
  main()
