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
    mano_J = [repartir(baraja), repartir(baraja)]
    mano_CPU = [repartir(baraja), repartir(baraja)]
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
    
    valor_j = calcular(mano_J)
    if valor_j > 21:
        print("Te pasaste de 21, juego perdido")
        print(f"Mano de la CPU: {mano_CPU} (valor: {calcular(mano_CPU)})")  # Mostrar la mano de la CPU
        return False  # Indicar que el jugador ha perdido

    # La CPU juega después de que el jugador decide quedarse
    while calcular(mano_CPU) < 17:
        mano_CPU.append(repartir(baraja))
    
    valor_cpu = calcular(mano_CPU)
    
    print(f"Mano de la CPU: {mano_CPU} (valor: {valor_cpu})")
    
    if valor_cpu > 21 or valor_j > valor_cpu:
        print(f"Ganaste con {valor_j} puntos contra {valor_cpu} de la CPU")
        return True
    elif valor_j < valor_cpu:
        print(f"Perdiste con {valor_j} puntos contra {valor_cpu} de la CPU")
        return False
    else:
        print("Es un empate")
        return None  # Indicar que ha habido un empate

while True:
    d = input("Escriba 1 para sí y 2 para no: ")
    
    if d == "2":
        print("Ok, gracias por su participación")
        break  # Salir del bucle principal
    elif d == "1":
        while True:  # Bucle para manejar los juegos múltiples
            print("Comencemos a jugar")
            resultado = jugar_21()  # Ejecutar el juego y obtener el resultado
            
            if resultado is None:
                # Si el resultado es empate, volver a preguntar si desea jugar otra vez
                print("¿Desea jugar otra vez? (1 para sí, 2 para no)")
            elif not resultado:  # Si el jugador ha perdido
                print("Fin del juego. ¿Desea jugar otra vez? (1 para sí, 2 para no)")
            else:  # Si el jugador ha ganado
                print("¿Desea jugar otra vez? (1 para sí, 2 para no)")
            
            d = input("Escriba 1 para sí y 2 para no: ")
            if d == "2":
                print("Ok, gracias por su participación")
                break  # Salir del bucle principal
            elif d != "1":
                print("Número no válido, saliendo del juego.")
                break  # Salir del bucle principal
    else:
        print("Número no válido, intente nuevamente.")
