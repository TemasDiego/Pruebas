import random

# Función para calcular el valor de la mano
def calcular_valor(mano):
    valor = 0
    ases = 0
    for carta in mano:
        if carta in ['J', 'Q', 'K']:
            valor += 10
        elif carta == 'A':
            ases += 1
            valor += 11
        else:
            valor += int(carta)
    
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    
    return valor

# Función para repartir una carta
def repartir_carta(baraja):
    carta = random.choice(baraja)
    baraja.remove(carta)
    return carta

# Función principal del juego
def jugar_blackjack():
    print("¡Bienvenido al juego de 21!")
    
    # Crear y barajar la baraja
    baraja = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(baraja)
    
    # Repartir cartas iniciales
    mano_jugador = [repartir_carta(baraja), repartir_carta(baraja)]
    mano_croupier = [repartir_carta(baraja), repartir_carta(baraja)]
    
    # Mostrar cartas del jugador y una carta del croupier
    print(f"Tu mano: {mano_jugador} (valor: {calcular_valor(mano_jugador)})")
    print(f"Carta visible del croupier: {mano_croupier[0]}")
    
    # Turno del jugador
    while calcular_valor(mano_jugador) < 21:
        accion = input("¿Deseas pedir otra carta (P) o quedarte (Q)? ").lower()
        if accion == 'p':
            mano_jugador.append(repartir_carta(baraja))
            print(f"Tu mano: {mano_jugador} (valor: {calcular_valor(mano_jugador)})")
        else:
            break
    
    # Comprobar si el jugador se pasó
    if calcular_valor(mano_jugador) > 21:
        print("Te pasaste de 21. ¡Perdiste!")
        return
    
    # Turno del croupier
    print(f"Mano del croupier: {mano_croupier} (valor: {calcular_valor(mano_croupier)})")
    while calcular_valor(mano_croupier) < 17:
        mano_croupier.append(repartir_carta(baraja))
        print(f"El croupier toma una carta: {mano_croupier} (valor: {calcular_valor(mano_croupier)})")
    
    # Determinar el ganador
    valor_jugador = calcular_valor(mano_jugador)
    valor_croupier = calcular_valor(mano_croupier)
    
    if valor_croupier > 21 or valor_jugador > valor_croupier:
        print(f"Ganaste con {valor_jugador} puntos contra {valor_croupier} del croupier. ¡Felicidades!")
    elif valor_jugador < valor_croupier:
        print(f"Perdiste con {valor_jugador} puntos contra {valor_croupier} del croupier. ¡Más suerte la próxima vez!")
    else:
        print(f"Empate con {valor_jugador} puntos. ¡Es un empate!")

# Ejecutar el juego
jugar_blackjack()
