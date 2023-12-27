import os  # Importo la libreria de Python os, permite acceder a env vars del os.

def main():  # Creo la función main
  nombre = os.getenv("USERNAME")
  print(f"¡Hola, {nombre} desde Github!")

if __name__ == "__main__"
  main()
