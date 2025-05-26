# tic_tac_toe.py

# --- 1. Game Board Representation ---
# The board will be a list of 9 elements, representing the 9 cells.
# ' ' represents an empty cell
# 'X' for human player
# 'O' for AI player
board = [' ' for _ in range(9)]

# --- 2. Display Board Function ---
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# --- 3. Check for Win Function ---
def check_win(board, player):
    # Define winning combinations (rows, columns, diagonals)
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# --- 4. Check for Draw Function ---
def check_draw(board):
    # A draw occurs if there are no empty spaces AND no one has won
    return ' ' not in board and not check_win(board, 'X') and not check_win(board, 'O')

# --- 5. Human Player Move Function ---
def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1 # Convert to 0-8 index
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move. That spot is already taken or out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# --- MINIMAX ALGORITHM IMPLEMENTATION ---

# Helper function: Get available empty cells
def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == ' ']

# Helper function: Check if game is over (win or draw)
def is_game_over(board):
    return check_win(board, 'X') or check_win(board, 'O') or check_draw(board)

# The Minimax Function
def minimax(board, depth, is_maximizing):
    # Base cases: evaluate the board if game is over
    if check_win(board, 'O'):  # AI (O) wins
        return 1
    if check_win(board, 'X'):  # Human (X) wins
        return -1
    if check_draw(board):      # Draw
        return 0

    # If maximizing player (AI's turn)
    if is_maximizing:
        best_score = -float('inf') # Start with negative infinity
        for move in get_empty_cells(board):
            board[move] = 'O' # Make the move
            score = minimax(board, depth + 1, False) # Recurse for minimizing player
            board[move] = ' ' # Undo the move (backtrack)
            best_score = max(score, best_score) # Choose the maximum score
        return best_score
    # If minimizing player (Human's turn)
    else:
        best_score = float('inf') # Start with positive infinity
        for move in get_empty_cells(board):
            board[move] = 'X' # Make the move
            score = minimax(board, depth + 1, True) # Recurse for maximizing player
            board[move] = ' ' # Undo the move (backtrack)
            best_score = min(score, best_score) # Choose the minimum score
        return best_score

# --- 6. AI Player Move Function (Now uses Minimax) ---
def ai_move(board):
    best_score = -float('inf')
    best_move = None

    # Iterate through all available empty cells
    for move in get_empty_cells(board):
        board[move] = 'O' # Try this move for AI
        score = minimax(board, 0, False) # Call minimax assuming human (minimizing player) plays next
        board[move] = ' ' # Undo the move

        if score > best_score:
            best_score = score
            best_move = move
    
    if best_move is not None:
        board[best_move] = 'O'
    else:
        # Fallback in case no good move is found (should not happen in Tic-Tac-Toe if logic is correct)
        # Or pick the first empty spot if minimax for some reason returns no best move
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                return

# --- 7. Main Game Loop ---
def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X', the AI is 'O'.")
    print("Prepare to face an unbeatable AI! (Play smart to draw!)")
    current_board = [' ' for _ in range(9)]
    current_player = 'X' # Human starts

    while True:
        display_board(current_board)

        if current_player == 'X':
            human_move(current_board)
        else:
            print("AI is making a move...")
            ai_move(current_board)

        if check_win(current_board, current_player):
            display_board(current_board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        elif check_draw(current_board):
            display_board(current_board)
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# --- Run the game ---
if __name__ == "__main__":
    play_game()