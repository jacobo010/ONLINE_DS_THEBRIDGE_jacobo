from random import randint
from clases import Board
from variables import BOARD_SIZE

def print_welcome_message():
    print("¡Bienvenido a Hundir la Flota!")
    print("Este es un juego entre dos jugadores: tú y la máquina.")
    print("El objetivo es hundir todos los barcos del adversario antes que él haga lo mismo contigo.")
    print("Durante tu turno, puedes disparar a coordenadas (x, y), ver los tableros ('Mostrar') o salir del juego ('Salir').")

def get_player_input():
    while True:
        try:
            user_input = input("Ingresa las coordenadas (x, y) para disparar o 'mostrar' para ver los tableros, 'salir' para salir: ").strip().lower()
            if user_input == "salir":
                return "salir"
            elif user_input == "mostrar":
                return "mostrar"
            else:
                x, y = map(int, user_input.split(','))
                if 0 <= x < 10 and 0 <= y < 10:
                    return x, y
                else:
                    print("Coordenadas fuera de rango. Deben ser entre 0 y 9.")
        except ValueError:
            print("Entrada inválida. Debes ingresar las coordenadas en el formato x,y (por ejemplo, 1,2).")

def ai_shoot():
    x, y = randint(0, 9), randint(0, 9)
    return x, y

def check_game_over(player):
    # Verifica si el jugador ha ganado o perdido
    for ship in player.ships:
        if not player.is_sunk(ship):
            return False
    return True