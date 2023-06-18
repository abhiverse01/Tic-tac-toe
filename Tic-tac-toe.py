import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("450x600")
        self.window.configure(bg="#2c3e50")  

        self.player_x_wins = 0
        self.player_o_wins = 0
        self.total_games = 0

        self.footer_frame = tk.Frame(self.window, bg="#ecf0f1", height=30)  
        self.footer_frame.pack(side="bottom", fill="x")

        self.footer_label = tk.Label(self.footer_frame, 
                                     text=f"Developed By: Abhishek Shah | Developed Year: 2023 | Total Games: {self.total_games}",
                                     font=("Arial", 8), bg="#ecf0f1", fg="#2c3e50")  
        self.footer_label.pack(pady=5)

    def start_game(self):
        self.home_frame.destroy()
        self.footer_frame.pack_forget()  

        self.game_frame = tk.Frame(self.window, bg="#2c3e50")
        self.game_frame.place(relx=0.5, rely=0.5, anchor='center')  

        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.game_frame, text="", font=("Arial", 30), width=4, height=2, 
                                               bg="#7f8c8d", fg="#2c3e50", relief="groove",
                                               command=lambda row=i, col=j: self.make_move(row, col), borderwidth=0) 
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.footer_frame.pack(side="bottom", fill="x")  

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state="disabled")

            if self.check_winner(self.current_player):
                self.game_over(self.current_player)
            elif self.check_draw():
                self.game_over("draw")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True

            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def game_over(self, result):
        self.total_games += 1
        if result == "draw":
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            messagebox.showinfo("Game Over", f"Player {result} wins!")
            if result == "X":
                self.player_x_wins += 1
            else:
                self.player_o_wins += 1

        self.show_homepage()

    def show_homepage(self):
        if hasattr(self, 'game_frame'):
            self.game_frame.destroy()

        self.home_frame = tk.Frame(self.window, bg="#2c3e50")
        self.home_frame.pack(pady=10)

        self.title_label = tk.Label(self.home_frame, text="Tic-Tac-Toe", font=("Helvetica", 24), bg="#2c3e50", fg="#ecf0f1")  
        self.title_label.pack(pady=20)

        self.play_button = tk.Button(self.home_frame, text="Play", font=("Helvetica", 18), bg="#3498db", fg="#ecf0f1", relief="groove",
                                     command=self.start_game, borderwidth=0)  
        self.play_button.pack(pady=10)

        self.stats_label = tk.Label(self.home_frame, text=f"X Wins: {self.player_x_wins}   O Wins: {self.player_o_wins}",
                                    font=("Arial", 12), bg="#2c3e50", fg="#ecf0f1")  
        self.stats_label.pack(pady=5)

        self.footer_label.config(text=f"Developed By: Abhishek Shah | Developed Year: 2023 | Total Games: {self.total_games}")
        self.footer_label.pack(side="bottom", pady=5)

    def run(self):
        self.show_homepage()
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()