"""
Generated Code Metadata:
========================
Original URL: https://nikelodeon.xyz
Prompt: Implement a simple Nickelodeon-themed trivia game using Python and the Tkinter library for the graphical user interface.
Generated: DETERMINISTIC_56484518cbe0d85e
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox
import random

class TriviaGame:
    def __init__(self, master):
        """Initialize the trivia game."""
        self.master = master
        self.master.title("Nickelodeon Trivia Game")
        self.score = 0
        self.question_index = 0

        # List of trivia questions and answers
        self.questions = [
            {"question": "What is the name of SpongeBob's pet snail?", "answer": "Gary"},
            {"question": "Which character is known for saying 'I don't need it, I don't need it, I definitely don't need it'?", "answer": "Patrick"},
            {"question": "What is the name of the school that the Rugrats attend?", "answer": "Reptar School"},
            {"question": "Who is the main character in 'Hey Arnold!'?", "answer": "Arnold"},
            {"question": "What color is the slime used in Nickelodeon shows?", "answer": "Green"},
        ]

        # Shuffle questions for randomness
        random.shuffle(self.questions)

        # Create UI elements
        self.question_label = tk.Label(master, text="", wraplength=300)
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.score_label = tk.Label(master, text="Score: 0")
        self.score_label.pack(pady=20)

        self.next_question()

    def next_question(self):
        """Load the next trivia question."""
        if self.question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.question_index]["question"])
            self.answer_entry.delete(0, tk.END)
        else:
            self.end_game()

    def check_answer(self):
        """Check the user's answer and update the score."""
        user_answer = self.answer_entry.get().strip()
        correct_answer = self.questions[self.question_index]["answer"]

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct!", "That's the right answer!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer was: {correct_answer}")

        self.score_label.config(text=f"Score: {self.score}")
        self.question_index += 1
        self.next_question()

    def end_game(self):
        """End the game and display the final score."""
        messagebox.showinfo("Game Over", f"Your final score is: {self.score}")
        self.master.quit()

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    trivia_game = TriviaGame(root)
    root.mainloop()
```
