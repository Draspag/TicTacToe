import random
import time

winning_tuples = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                  [1, 4, 7], [2, 5, 8], [3, 6, 9],
                  [1, 5, 9], [7, 5, 3]
                  ]


class Player:
    def __init__(self, name):
        self.name = name
        self.plays = []
        self.score = 0


def print_board(board):
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  \n"
          f"----------------\n"
          f"  {board[3]}  |  {board[4]}  |  {board[5]}  \n"
          f"----------------\n"
          f"  {board[6]}  |  {board[7]}  |  {board[8]}  \n")


def print_help():
    print(f"1. The game is played on a grid that's 3 squares by 3 squares.\n"
          f"2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in "
          f"empty squares.\n "
          f"3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n"
          f"4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a "
          f"tie.\n "
          f"5. You can pick a cell by referring to the map\n"
          f"  1  |  2  |  3  \n"
          f"----------------\n"
          f"  4  |  5  |  6  \n"
          f"----------------\n"
          f"  7  |  8  |  9  \n")


def check_end_round(current_player):
    for winning_tuple in winning_tuples:
        if winning_tuple[0] in current_player.plays \
                and winning_tuple[1] in current_player.plays \
                and winning_tuple[2] in current_player.plays:
            return current_player

    if " " not in board:
        return "Draw"
    return "Y"


print("--- Welcome to TicTacToe ---\n\n")

# Player names
player_1 = Player(str(input("Player 1: What is your name? ")))
print(f"Welcome {player_1.name} \n")
player_2 = Player(str(input("Player 2: What is your name? ")))
print(f"Welcome {player_2.name} \n")

# Play order management
first_player = random.choice([player_1, player_2])
if first_player == player_1:
    second_player = player_2
else:
    second_player = player_1

print("Our first player is")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(f"{first_player.name}!")
time.sleep(0.5)
print("Let's Start!  \n\n")
time.sleep(0.5)

game_is_on = "y"
ties = 0
while game_is_on == "y":
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    round_is_on = "Y"
    current_player = first_player
    valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("--- New round ---")
    print_board(board)
    while round_is_on == "Y":
        cell_selected = ""
        while cell_selected not in valid_moves:
            cell_selected = input(
                f"{current_player.name} to play. Type 'help' to get more info.\nSelect a cell (1 to 9): ").lower()
            if cell_selected == "help":
                print_help()
            else:
                try:
                    cell_selected = int(cell_selected)
                except TypeError:
                    print("Please select a valid number which wasn't played (1 to 9)")
                else:
                    if cell_selected not in valid_moves:
                        print(f"Please select a valid move {valid_moves} \n")

        if current_player == first_player:
            board[cell_selected - 1] = "X"
        else:
            board[cell_selected - 1] = "O"
        current_player.plays.append(cell_selected)
        valid_moves.remove(cell_selected)
        print_board(board)

        round_is_on = check_end_round(current_player)
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1

    if round_is_on == "Draw":
        print("End of game: This is a draw!\n")
        ties += 1
    else:
        print(f"{round_is_on.name} won !!!\n")
        round_is_on.score += 1

    print("---Scores---\n\n"
          f"{player_1.name}: {player_1.score}\n"
          f"{player_2.name}: {player_2.score}\n"
          f"Ties: {ties}\n")

    game_is_on = input("Want to replay? (Y/N): ").lower()
