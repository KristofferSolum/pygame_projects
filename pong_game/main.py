from pong import Pong
from game_over import GameOver
from start_game import StartGame


def play_game():
    pong = Pong()
    pong.run()

    game_over = GameOver(pong.player1, pong.player2)
    game_over.run()


def main():
    start_game = StartGame()
    play = start_game.run()

    while play:
        play_game()
        play = start_game.run()


if __name__ == "__main__":
    main()
