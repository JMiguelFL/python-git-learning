import random
from colorama import init, Fore, Style 

init(autoreset=True)

def adivina_numero():
    print(Fore.CYAN + "Bienvenido. Estoy pensando en un número del 1 al 100...")
    
    numero_secreto = random.randint(1, 100)
    intentos = 0
    ganaste = False
    historial = []

    while not ganaste:
        try:
            entrada = input(Fore.YELLOW + "Introduce tu número: ")
            numero_usuario = int(entrada)
            historial.append(numero_usuario)
            intentos += 1

            if numero_usuario < numero_secreto:
                print(Fore.BLUE + "Más alto")
            elif numero_usuario > numero_secreto:
                print(Fore.BLUE + "Más bajo")
            else:
                print(Fore.GREEN + Style.BRIGHT + f"¡Felicidades! Lo adivinaste en {intentos} intentos.")
                ganaste = True
                
        except ValueError:
            print(Fore.RED + "Error: Por favor, escribe solo números.")

    print(Style.BRIGHT + "\n--- Resumen de tu partida ---")
    for numero in historial:
        if numero == numero_secreto:
            print(Fore.GREEN + f"- {numero} (¡Correcto!)")
        else:
            print(Fore.RED + f"- {numero}")

if __name__ == "__main__":
    adivina_numero()