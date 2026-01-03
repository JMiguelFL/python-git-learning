import random

def adivina_numero():
    print("Bienvenido al juego de Adivinar el número.")
    print("Estoy pensando en un número del 1 al 100.")

    numero_secreto = random.randint(1, 100)
    intentos = 0
    ganaste = False

    while not ganaste:
        try:
            entrada = input("Introduce tu número: ")

            numero_usuario = int(entrada)
            intentos += 1

            if numero_usuario < numero_secreto:
                print("Más alto")
            elif numero_usuario > numero_secreto:
                print("Más bajo")
            else:
                print(f"Felicidades, has acertado el número en {intentos} intentos.")
                ganaste = True
            
        except ValueError:
            print("Error: Por favor, escribe solo números.")

if __name__ == "__main__":
    adivina_numero()
    