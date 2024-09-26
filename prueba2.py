import random
from abc import ABC, abstractmethod

# Interface para Jugador
class JugadorInterface(ABC):
    @abstractmethod
    def agregar_carta(self, carta):
        pass
    
    @abstractmethod
    def calcular_valor(self):
        pass

    @abstractmethod
    def mostrar_mano(self):
        pass

# Clase Baraja encargada de manejar el mazo
class Baraja:
    def __init__(self):
        self.cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"] * 4
        random.shuffle(self.cartas)
        
    def repartir_carta(self):
        if not self.cartas:
            return None 
        return self.cartas.pop()

# Clase Jugador que implementa la interfaz JugadorInterface
class Jugador(JugadorInterface):
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def agregar_carta(self, carta):
        self.mano.append(carta)

    def calcular_valor(self):
        valor = 0
        ases = 0

        for carta in self.mano:
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

    def mostrar_mano(self):
        return f"{self.nombre}: {self.mano} (valor: {self.calcular_valor()})"

# Clase Juego21 encargada de manejar la lógica del juego
class Juego21:
    def __init__(self, jugador: JugadorInterface, cpu: JugadorInterface, baraja: Baraja):
        self.baraja = baraja
        self.jugador = jugador
        self.cpu = cpu

    def repartir_cartas_iniciales(self):
        for _ in range(2):  
            self.jugador.agregar_carta(self.baraja.repartir_carta())
            self.cpu.agregar_carta(self.baraja.repartir_carta())

    def jugar_turno_jugador(self):
        while self.jugador.calcular_valor() < 21:
            accion = input("¿Desea pedir otra carta (P) o quedarse (Q)? ").lower()
            if accion == 'p':
                carta = self.baraja.repartir_carta()
                self.jugador.agregar_carta(carta)
                print(f"Carta recibida: {carta}")
                print(self.jugador.mostrar_mano())
            elif accion == 'q':
                break
            else:
                print("Acción no válida, intente nuevamente.")

    def jugar_turno_cpu(self):
        while self.cpu.calcular_valor() < 17:
            carta = self.baraja.repartir_carta()
            self.cpu.agregar_carta(carta)

    def determinar_ganador(self):
        valor_jugador = self.jugador.calcular_valor()
        valor_cpu = self.cpu.calcular_valor()

        if valor_jugador > 21:
            print(f"{self.jugador.nombre} se pasó de 21. Juego perdido.")
            return False

        print(f"Mano de la CPU: {self.cpu.mostrar_mano()}")
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
            baraja = Baraja()
            jugador = Jugador(nombre_jugador)
            cpu = Jugador("CPU")
            
            juego = Juego21(jugador, cpu, baraja)
            juego.repartir_cartas_iniciales()
            print(jugador.mostrar_mano())
            print(f"Carta visible de la CPU: {cpu.mano[0]}")
            
            juego.jugar_turno_jugador()
            juego.jugar_turno_cpu()
            juego.determinar_ganador()

            d = input(f"¿Desea jugar otra vez {nombre_jugador}? (1 para sí, 2 para no): ")
            if d == "2":
                print("Ok, gracias por su participación.")
                break
        else:
            print("Número no válido, intente nuevamente.")

if __name__ == "__main__":
    main()
