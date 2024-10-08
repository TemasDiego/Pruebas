import random
n = input("Por favor ingrese su nombre")
print(f"{n }¿Desea jugar 21?")

def calcular_mano(mano):
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
    print(f"mano de {n}: {mano_J} (valor: {calcular_mano(mano_J)})")
    print(f"Carta visible de la CPU: {mano_CPU[0]}")
    
    while calcular_mano(mano_J) < 21:
        accion = input("¿Desea pedir otra carta (P) o quedarse (Q)? ").lower()
        if accion == 'p':
            mano_J.append(repartir(baraja))
            print(f"mazo de {n}: {mano_J} (valor: {calcular_mano(mano_J)})")
        elif accion == 'q':
            break
        else:
            print("Acción no válida, intente nuevamente.")
    
    valor_j = calcular_mano(mano_J)
    if valor_j > 21:
        print(f"{n}Te pasaste de 21, juego perdido")
        print(f"Mano de la CPU: {mano_CPU} (valor: {calcular_mano(mano_CPU)})")  
        return False  # 

    # La CPU juega después de que el jugador decide quedarse
    while calcular_mano(mano_CPU) < 17:
        mano_CPU.append(repartir(baraja))
    
    valor_cpu = calcular_mano(mano_CPU)
    
    print(f"Mano de la CPU: {mano_CPU} (valor: {valor_cpu})")
    
    if valor_cpu > 21 or valor_j > valor_cpu:
        print(f"{n}Ganaste con {valor_j} puntos contra {valor_cpu} de la CPU")
        return True
    elif valor_j < valor_cpu:
        print(f"{n}Perdiste con {valor_j} puntos contra {valor_cpu} de la CPU")
        return False
    else:
        print("Es un empate")
        return None  #

while True:
    d = input("Escriba 1 para sí y 2 para no: ")
    
    if d == "2":
        print("Ok, gracias por su participación")
        break  # Salir del bucle principal
    elif d == "1":
        while True:  
            print("Comencemos a jugar")
            resultado = jugar_21()  
            if resultado is None:
         
                print(f"{n}¿Desea jugar otra vez? (1 para sí, 2 para no)")
            elif not resultado:  
                print(f"Fin del juego. ¿Desea jugar otra vez {n}? (1 para sí, 2 para no)")
            else: 
                print(f"¿Desea jugar otra vez {n}? (1 para sí, 2 para no)")
            
            d = input("Escriba 1 para sí y 2 para no: ")
            if d == "2":
                print("Ok, gracias por su participación")
                break  
            elif d != "1":
                print("Número no válido, saliendo del juego.")
                break  
    else:
        print("Número no válido, intente nuevamente.")
