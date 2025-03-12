import random
class RockPaperScissors:
    def __init__(self):
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.winner = None

    def player_choice(self, player_number):
        while True:
            choice = input(f"Player {player_number}, enter your choice (Rock, Paper, or Scissors): ").capitalize()
            if choice in self.choices:
                return choice
            else:
                print("Invalid choice. Please choose Rock, Paper, or Scissors. ")

    def determine_winner(self, player1_choice, player2_choice):
        if player1_choice == player2_choice:
            self.winner = 'Draw'
        elif (player1_choice == 'Rock' and player2_choice == 'Scissors') or \
             (player1_choice == 'Scissors' and player2_choice == 'Paper') or \
             (player1_choice == 'Paper' and player2_choice == 'Rock'):
            self.winner = 'Player 1'
        else:
            self.winner = 'Player 2'

    def play_game(self):
        player1_choice = self.player_choice(1)
        player2_choice = self.player_choice(2)

        print(f"\nPlayer 1 chose: {player1_choice}")
        print(f"Player 2 chose: {player2_choice}")

        self.determine_winner(player1_choice, player2_choice)
        if self.winner == 'Draw':
            print("It's a draw!")
        else:
            print(f"\nThe winner is {self.winner}!")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
