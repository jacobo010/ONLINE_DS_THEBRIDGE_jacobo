# main.py
from funciones import print_welcome_message, get_player_input, ai_shoot, check_game_over
from clases import Board

def main():
    print_welcome_message()

    # Inicialización de los tableros
    player_board = Board(player_id="Player")
    ai_board = Board(player_id="AI")

    while True:
        # Turno del jugador humanoo
        print("\nTu tablero completo con la ubicación de tus barcos:")
        player_board.display_full_board()
        print("Tablero de la Skynet con tus impactos: ")
        ai_board.display()

        player_action = get_player_input()

        if player_action == "salir":
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        elif player_action == "mostrar":
            continue
        else:
            x, y = player_action
            result = ai_board.shoot(x, y)
            print(f"Disparo en ({x}, {y}): {result.capitalize()}")

            if check_game_over(ai_board):
                print("¡Ganaste! La Skynet ha sido derrotada.")
                break

            # Turno de la Skynet
            x, y = ai_shoot()
            print(f"Skynet dispara en ({x}, {y})")
            result = player_board.shoot(x, y)
            print(f"Resultado: {result.capitalize()}")

            if check_game_over(player_board):
                print("Perdiste. La Skynet ha ganado.")
                break



if __name__ == "__main__":
    main()