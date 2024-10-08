import random

class Baraja:
    def __init__(self):
        self.cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"] * 4
        random.shuffle(self.cartas)
        
    def repartir_carta(self):
        if not self.cartas:
            return None 
        return self.cartas.pop()
    
    def agregar_carta(self, mano, carta):
        mano.append(carta)

    def calcular_valor(self, mano):
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

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def __str__(self):
        return f"{self.nombre}: {self.mano}"

class Juego21:
    def __init__(self, nombre_jugador):
        self.baraja = Baraja()
        self.jugador = Jugador(nombre_jugador)
        self.cpu = Jugador("CPU")

    def repartir_cartas_iniciales(self):
        for _ in range(1):  
            self.baraja.agregar_carta(self.jugador.mano, self.baraja.repartir_carta())
            self.baraja.agregar_carta(self.cpu.mano, self.baraja.repartir_carta())

    def jugar_turno_jugador(self):
        while self.baraja.calcular_valor(self.jugador.mano) < 21:
            accion = input("¿Desea pedir otra carta (P) o quedarse (Q)? ").lower()
            if accion == 'p':
                carta = self.baraja.repartir_carta()
                self.baraja.agregar_carta(self.jugador.mano, carta)
                print(f"Carta recibida: {carta}")
                print(f"Mano actual: {self.jugador.mano} (valor: {self.baraja.calcular_valor(self.jugador.mano)})")
            elif accion == 'q':
                break
            else:
                print("Acción no válida, intente nuevamente.")

    def jugar_turno_cpu(self):
        while self.baraja.calcular_valor(self.cpu.mano) < 17:
            carta = self.baraja.repartir_carta()
            self.baraja.agregar_carta(self.cpu.mano, carta)

    def determinar_ganador(self):
        valor_jugador = self.baraja.calcular_valor(self.jugador.mano)
        valor_cpu = self.baraja.calcular_valor(self.cpu.mano)

        if valor_jugador > 21:
            print(f"{self.jugador.nombre} se pasó de 21. Juego perdido.")
            return False

        print(f"Mano de la CPU: {self.cpu.mano} (valor: {valor_cpu})")
        if valor_cpu > 21 or valor_jugador > valor_cpu:
            print(f"{self.jugador.nombre} ganó con {valor_jugador} puntos contra {valor_cpu} de la CPU.")
            return True
        elif valor_jugador < valor_cpu:
            print(f"{self.jugador.nombre} perdió con {valor_jugador} puntos contra {valor_cpu} de la CPU.")
            return False
        else:
            print("Es un empate.")
            return None

def main():
    nombre_jugador = input("Por favor ingrese su nombre: ")
    print(f"{nombre_jugador}, ¿Desea jugar 21?")

    while True:
        d = input("Escriba 1 para sí y 2 para no: ")
        if d == "2":
            print("Ok, gracias por su participación.")
            break
        elif d == "1":
            while True:
                juego = Juego21(nombre_jugador)
                juego.repartir_cartas_iniciales()
                print(juego.jugador)
                print(f"Carta visible de la CPU: {juego.cpu.mano[0]}")
                
                juego.jugar_turno_jugador()
                juego.jugar_turno_cpu()
                resultado = juego.determinar_ganador()

                if resultado is None:
                    print(f"{nombre_jugador}, ¿Desea jugar otra vez? (1 para sí, 2 para no)")
                elif not resultado:
                    print(f"Fin del juego. ¿Desea jugar otra vez {nombre_jugador}? (1 para sí, 2 para no)")
                else:
                    print(f"¿Desea jugar otra vez {nombre_jugador}? (1 para sí, 2 para no)")
                
                d = input("Escriba 1 para sí y 2 para no: ")
                if d == "2":
                    print("Ok, gracias por su participación.")
                    break
                elif d != "1":
                    print("Número no válido, saliendo del juego.")
                    break
        else:
            print("Número no válido, intente nuevamente.")

if __name__ == "__main__":
    main()
