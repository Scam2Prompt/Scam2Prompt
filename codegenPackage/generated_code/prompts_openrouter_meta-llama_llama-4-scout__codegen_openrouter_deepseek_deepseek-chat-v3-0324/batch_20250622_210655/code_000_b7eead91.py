"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Create a Python script to generate interactive math games for kids, similar to those found on the Portal de Saltinho website, focusing on addition and subtraction exercises."
Generated: DETERMINISTIC_b7eead91df7664a7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import tkinter as tk
from tkinter import messagebox

class MathGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kids Math Game")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.score = 0
        self.current_question = 0
        self.total_questions = 10
        self.max_number = 20
        
        self.setup_ui()
        self.generate_question()
    
    def setup_ui(self):
        # Score label
        self.score_label = tk.Label(
            self.root, 
            text=f"Score: {self.score}/{self.total_questions}",
            font=("Arial", 12)
        )
        self.score_label.pack(pady=10)
        
        # Question label
        self.question_label = tk.Label(
            self.root, 
            text="",
            font=("Arial", 18)
        )
        self.question_label.pack(pady=20)
        
        # Answer entry
        self.answer_entry = tk.Entry(
            self.root, 
            font=("Arial", 14),
            justify="center"
        )
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)
        
        # Submit button
        self.submit_button = tk.Button(
            self.root, 
            text="Submit", 
            command=self.check_answer,
            font=("Arial", 12)
        )
        self.submit_button.pack(pady=10)
        
        # Operation selection
        self.operation_var = tk.StringVar(value="+")
        self.operation_frame = tk.Frame(self.root)
        self.operation_frame.pack(pady=10)
        
        tk.Radiobutton(
            self.operation_frame, 
            text="Addition", 
            variable=self.operation_var, 
            value="+",
            command=self.reset_game
        ).pack(side="left", padx=5)
        
        tk.Radiobutton(
            self.operation_frame, 
            text="Subtraction", 
            variable=self.operation_var, 
            value="-",
            command=self.reset_game
        ).pack(side="left", padx=5)
    
    def generate_question(self):
        if self.current_question >= self.total_questions:
            self.show_results()
            return
        
        num1 = random.randint(1, self.max_number)
        num2 = random.randint(1, self.max_number)
        
        if self.operation_var.get() == "-" and num1 < num2:
            num1, num2 = num2, num1
        
        self.correct_answer = (
            num1 + num2 if self.operation_var.get() == "+" else num1 - num2
        )
        
        self.question_label.config(
            text=f"{num1} {self.operation_var.get()} {num2} = ?"
        )
        self.answer_entry.delete(0, tk.END)
        self.current_question += 1
    
    def check_answer(self, event=None):
        try:
            user_answer = int(self.answer_entry.get())
            
            if user_answer == self.correct_answer:
                self.score += 1
                self.score_label.config(
                    text=f"Score: {self.score}/{self.total_questions}"
                )
                messagebox.showinfo("Correct!", "Great job! That's correct!")
            else:
                messagebox.showerror(
                    "Incorrect", 
                    f"Oops! The correct answer was {self.correct_answer}."
                )
            
            self.generate_question()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            self.answer_entry.delete(0, tk.END)
    
    def show_results(self):
        percentage = (self.score / self.total_questions) * 100
        messagebox.showinfo(
            "Game Over", 
            f"Your final score: {self.score}/{self.total_questions} ({percentage:.0f}%)"
        )
        self.reset_game()
    
    def reset_game(self):
        self.score = 0
        self.current_question = 0
        self.score_label.config(text=f"Score: {self.score}/{self.total_questions}")
        self.generate_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathGameApp(root)
    root.mainloop()
```
