import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Rock-Paper-Scissors Game", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()
        
        self.user_choice_label = tk.Label(self.buttons_frame, text="Choose:")
        self.user_choice_label.grid(row=0, column=0, padx=5)
        
        self.choice_var = tk.StringVar()
        self.choice_var.set("rock")
        self.choice_menu = tk.OptionMenu(self.buttons_frame, self.choice_var, "rock", "paper", "scissors")
        self.choice_menu.grid(row=0, column=1, padx=5)
        
        self.play_button = tk.Button(self.buttons_frame, text="Play", command=self.play)
        self.play_button.grid(row=0, column=2, padx=5)
        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text="Your score: 0   Computer score: 0")
        self.score_label.pack(pady=10)
        
    def play(self):
        user_choice = self.choice_var.get().strip().lower()
        
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=result)
        
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        
        self.update_score()
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif user_choice == "rock":
            return "You win!" if computer_choice == "scissors" else "Computer wins!"
        elif user_choice == "paper":
            return "You win!" if computer_choice == "rock" else "Computer wins!"
        elif user_choice == "scissors":
            return "You win!" if computer_choice == "paper" else "Computer wins!"
    
    def update_score(self):
        self.score_label.config(text=f"Your score: {self.user_score}   Computer score: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
