def display_board(board):
    # Write code to display the game board
    pass

def is_winner(board, player):
    # Write code to check if the player has won
    pass

def is_draw(board):
    # Write code to check if the game has ended in a draw
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    pass

def main():
    # Initialize the game board
    board = [" " for _ in range(9)]
    current_player = "X"

    # Main game loop
    while True:
        display_board(board)
        move = int(input(f"Player {current_player}, enter your move (0-8): "))
        
        # Check if the move is valid and update the board
        if board[move] == " ":
            board[move] = current_player

            if is_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_draw(board):
                display_board(board)
                print("It's a draw!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. The cell is already occupied.")

if __name__ == "__main__":
    main()
