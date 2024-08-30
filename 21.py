print("Hola mundo")
print("¿Desea jugar 21?")
def repartir(baraja):
    carta=random.choice(baraja)
    baraja.remove(carta)
    return carta

while True:
    d = input("Escriba 1 para sí y 2 para no: ")
    
    if d == "2":
        print("Ok, gracias por su participación")
        break  # Salir del bucle
    elif d == "1":
        print("Comencemos a jugar")
        baraja = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]
        break  # Salir del bucle para iniciar el juego
    else:
        print("Número no válido, intente nuevamente.")