import tkinter as tk
from tkinter import messagebox
import math

# Set up the main window
root = tk.Tk()
root.title("Shrey's Tic-Tac-Toe (You vs AI)")
root.resizable(False, False)
root.geometry("300x400")
root.configure(bg="#f0f0f0")


# Board state
board = [' ' for _ in range(9)]
buttons = []

# Check for winner
def check_winner(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return {'score': 1}
    elif check_winner(board, 'X'):
        return {'score': -1}
    elif ' ' not in board:
        return {'score': 0}

    if is_maximizing:
        best = {'score': -math.inf}
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                sim_score = minimax(board, depth + 1, False)
                board[i] = ' '
                sim_score['move'] = i
                if sim_score['score'] > best['score']:
                    best = sim_score
        return best
    else:
        best = {'score': math.inf}
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                sim_score = minimax(board, depth + 1, True)
                board[i] = ' '
                sim_score['move'] = i
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

# Handle button clicks
def on_click(i):
    if board[i] == ' ' and not game_over():
        board[i] = 'X'
        buttons[i].config(text='X', state='disabled')

        if check_game_end('X'):
            return

        # AI move
        ai_move = minimax(board, 0, True)['move']
        board[ai_move] = 'O'
        buttons[ai_move].config(text='O', state='disabled')

        check_game_end('O')

# Check game end
def check_game_end(player):
    if check_winner(board, player):
        messagebox.showinfo("Game Over", f"{'You' if player == 'X' else 'AI'} wins!")
        disable_all()
        return True
    elif ' ' not in board:
        messagebox.showinfo("Game Over", "It's a tie!")
        disable_all()
        return True
    return False

# Disable all buttons
def disable_all():
    for btn in buttons:
        btn.config(state='disabled')

# Check if game is over
def game_over():
    return check_winner(board, 'X') or check_winner(board, 'O') or ' ' not in board

# Reset game
def reset_game():
    global board
    board = [' ' for _ in range(9)]
    for btn in buttons:
        btn.config(text=' ', state='normal')

# Build grid
frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text=' ', font=('Arial', 24), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Reset button
reset_btn = tk.Button(root, text="Reset", font=("Arial", 12), command=reset_game)
reset_btn.pack(pady=10)

# Start GUI loop
root.mainloop()
