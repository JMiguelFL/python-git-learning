import random
from colorama import init, Fore, Style

init(autoreset=True)

def pedir_numero():
    while True:
        try:
            entrada = input(Fore.YELLOW + "Introduce tu número: ")
            return int(entrada)
        except ValueError:
            print(Fore.RED + "Error: Por favor escribe solo números.")

def adivina_numero():
    print(Fore.CYAN + "Bienvenido, estoy pensando un número del 1 al 100")

    numero_secreto = random.randint(1, 100)
    intentos = 0
    ganaste = False
    historial = []

    while not ganaste:
        numero_usuario = pedir_numero()

        historial.append(numero_usuario)
        intentos += 1

        if numero_usuario < numero_secreto:
            print(Fore.BLUE + "Más alto")
        elif numero_usuario > numero_secreto:
            print(Fore.BLUE + "Más bajo")
        else:
            print(Fore.GREEN + "Has acertado el número")
            ganaste = True
    
    print(Style.BRIGHT + "\n--- Resumen de tu partida ---")
    for numero in historial:
        if numero == numero_secreto:
            print(Fore.GREEN + f"- {numero} (Correcto)")
        else:
            print(Fore.RED + f"- {numero}")

if __name__ == "__main__":
    adivina_numero()
