import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Quiz Game")
        
        self.questions = [
            ("What is the capital of France?", "Paris"),
            ("Which planet is known as the 'Red Planet'?", "Mars"),
            ("What is the largest mammal in the world?", "Blue Whale")
            # Add more questions here
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.create_widgets()
        self.load_question()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to the Quiz Game!", font=("Helvetica", 14))
        self.label.pack(pady=10)
        
        self.question_text = tk.StringVar()
        self.question_text.set("")
        self.question_label = tk.Label(self.root, textvariable=self.question_text, font=("Helvetica", 12))
        self.question_label.pack(pady=10)
        
        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(self.root, textvariable=self.answer_var)
        self.answer_entry.pack(pady=5)
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 12))
        self.score_label.pack(pady=10)
        
    def load_question(self):
        if self.current_question < len(self.questions):
            self.question_text.set(self.questions[self.current_question][0])
            self.answer_var.set("")
        else:
            self.question_label.config(text="Quiz Completed!")
            self.answer_entry.config(state="disabled")
            self.submit_button.config(state="disabled")
    
    def check_answer(self):
        user_answer = self.answer_var.get().strip()
        correct_answer = self.questions[self.current_question][1]
        
        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Result", "Correct!")
            self.score += 1
        else:
            messagebox.showerror("Result", f"Wrong! The correct answer is {correct_answer}.")
        
        self.update_score()
        self.next_question()
    
    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
    
    def next_question(self):
        self.current_question += 1
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
