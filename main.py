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
          f"--------------\n"
          f"  {board[3]}  |  {board[4]}  |  {board[5]}  \n"
          f"--------------\n"
          f"  {board[6]}  |  {board[7]}  |  {board[8]}  \n")

def check_end_round(current_player):
    for winning_tuple in winning_tuples:
        print(winning_tuple)

        if winning_tuple[0] in current_player.plays \
                and winning_tuple[1] in current_player.plays \
                and winning_tuple[2] in current_player.plays:
            return current_player

    if " " not in board:
        return "Draw"
    print(current_player.plays)
    return "Y"


player_1 = Player("Gaspard")
player_2 = Player("Margou")

print("--- Welcome to TicTacToe ---\n\n")

# player_1 = Player(str(input("Player 1: What is your name? ")))
print(f"Welcome {player_1.name} \n")
# player_2 = Player(str(input("Player 2: What is your name? ")))
print(f"Welcome {player_2.name} \n")

game_is_on = "y"
while game_is_on == "y":
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    round_is_on = "Y"
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

    print("Let's Start!  \n\n")
    print_board(board)

    current_player = first_player
    valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while round_is_on == "Y":

        cell_selected = ""
        while cell_selected not in valid_moves:
            cell_selected = input(f"{current_player.name} to play. Select a cell (1 to 9): ")
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
    else:
        print(f"{round_is_on.name} won !!!\n")
        round_is_on.score += 1

    game_is_on = input("Want to replay? (Y/N): ").lower()
