import random

print("Hola mundo")
print("¿Desea jugar 21?")

def calcular(mano):
    valor = 0
    ases = 0

    for carta in mano:
        if carta in ["J", "K", "Q"]:
            valor += 10
        elif carta == "A":
            ases += 1
            valor += 11
        else:
            valor += int(carta)
    
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    
    return valor

def repartir(baraja):
    carta = random.choice(baraja)
    baraja.remove(carta)
    return carta

def jugar_21():
    baraja = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]
    mano_J = [repartir(baraja)]
    mano_CPU = [repartir(baraja)]
    print(f"Tu mazo: {mano_J} (valor: {calcular(mano_J)})")
    print(f"Carta visible de la CPU: {mano_CPU[0]}")
    
    while calcular(mano_J) < 21:
        accion = input("¿Desea pedir otra carta (P) o quedarse (Q)? ").lower()
        if accion == 'p':
            mano_J.append(repartir(baraja))
            print(f"Tu mazo: {mano_J} (valor: {calcular(mano_J)})")
        elif accion == 'q':
            break
        else:
            print("Acción no válida, intente nuevamente.")
    
    if calcular(mano_J) > 21:
        print("Te pasaste de 21, juego perdido")
        return False  # Indicar que el jugador ha perdido

    # La CPU juega después de que el jugador decide quedarse
    print(f"Mano de la CPU: {mano_CPU} (valor: {calcular(mano_CPU)})")
    while calcular(mano_CPU) < 17:
        mano_CPU.append(repartir(baraja))
        print(f"La CPU toma una carta: {mano_CPU} (valor: {calcular(mano_CPU)})")
    
    if calcular(mano_CPU) > 21:
        print("La CPU se pasó de 21, ganaste")
        return True  # Indicar que el jugador ha ganado
    elif calcular(mano_CPU) >= calcular(mano_J):
        print("La CPU gana")
        return False  # Indicar que el jugador ha perdido
    else:
        print("Ganaste")
        return True  # Indicar que el jugador ha ganado

while True:
    d = input("Escriba 1 para sí y 2 para no: ")
    
    if d == "2":
        print("Ok, gracias por su participación")
        break  # Salir del bucle principal
    elif d == "1":
        print("Comencemos a jugar")
        if not jugar_21():  # Si el jugador ha perdido, salir del bucle principal
            continue  # Volver a preguntar si desea jugar otra vez
    else:
        print("Número no válido, intente nuevamente.")
