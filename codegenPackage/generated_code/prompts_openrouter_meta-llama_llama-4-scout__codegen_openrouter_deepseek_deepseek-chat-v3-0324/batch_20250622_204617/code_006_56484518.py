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

class NickelodeonTriviaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Nickelodeon Trivia Game")
        self.root.geometry("600x400")
        self.root.configure(bg="#F5F5F5")

        # Questions and answers
        self.questions = [
            {
                "question": "What is the name of the orange sponge who lives in a pineapple under the sea?",
                "options": ["Patrick Star", "Squidward Tentacles", "SpongeBob SquarePants", "Mr. Krabs"],
                "answer": "SpongeBob SquarePants"
            },
            {
                "question": "Which show features a boy genius with a talking dog named Goddard?",
                "options": ["The Fairly OddParents", "Danny Phantom", "Jimmy Neutron", "Avatar: The Last Airbender"],
                "answer": "Jimmy Neutron"
            },
            {
                "question": "What is the name of the fairy that grants wishes in 'The Fairly OddParents'?",
                "options": ["Cosmo", "Wanda", "Poof", "Jorgen Von Strangle"],
                "answer": "Wanda"
            },
            {
                "question": "In 'Avatar: The Last Airbender', what element does Aang master first?",
                "options": ["Water", "Earth", "Fire", "Air"],
                "answer": "Air"
            },
            {
                "question": "What is the name of the teenage ghost superhero in 'Danny Phantom'?",
                "options": ["Danny Fenton", "Danny Phantom", "Dash Baxter", "Tucker Foley"],
                "answer": "Danny Phantom"
            }
        ]

        self.current_question = 0
        self.score = 0
        self.shuffled_questions = random.sample(self.questions, len(self.questions))

        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        # Question label
        self.question_label = tk.Label(
            self.root,
            text=self.shuffled_questions[self.current_question]["question"],
            wraplength=550,
            font=("Arial", 14, "bold"),
            bg="#F5F5F5"
        )
        self.question_label.pack(pady=20)

        # Options frame
        self.options_frame = tk.Frame(self.root, bg="#F5F5F5")
        self.options_frame.pack()

        # Radio buttons for options
        self.selected_option = tk.StringVar()
        self.option_buttons = []
        for i, option in enumerate(self.shuffled_questions[self.current_question]["options"]):
            rb = tk.Radiobutton(
                self.options_frame,
                text=option,
                variable=self.selected_option,
                value=option,
                font=("Arial", 12),
                bg="#F5F5F5",
                activebackground="#F5F5F5"
            )
            rb.pack(anchor="w", pady=5)
            self.option_buttons.append(rb)

        # Submit button
        self.submit_button = tk.Button(
            self.root,
            text="Submit",
            command=self.check_answer,
            font=("Arial", 12, "bold"),
            bg="#FF6B00",
            fg="white",
            activebackground="#FF8C42",
            activeforeground="white"
        )
        self.submit_button.pack(pady=20)

        # Score label
        self.score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}/{len(self.questions)}",
            font=("Arial", 12),
            bg="#F5F5F5"
        )
        self.score_label.pack()

    def check_answer(self):
        if not self.selected_option.get():
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        if self.selected_option.get() == self.shuffled_questions[self.current_question]["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "That's the right answer!")
        else:
            correct_answer = self.shuffled_questions[self.current_question]["answer"]
            messagebox.showinfo("Wrong!", f"Sorry, the correct answer was: {correct_answer}")

        self.current_question += 1
        self.selected_option.set("")

        if self.current_question < len(self.shuffled_questions):
            self.update_question()
        else:
            self.show_final_score()

    def update_question(self):
        self.question_label.config(text=self.shuffled_questions[self.current_question]["question"])
        
        for i, button in enumerate(self.option_buttons):
            button.config(text=self.shuffled_questions[self.current_question]["options"][i],
                         value=self.shuffled_questions[self.current_question]["options"][i])
        
        self.score_label.config(text=f"Score: {self.score}/{len(self.questions)}")

    def show_final_score(self):
        percentage = (self.score / len(self.questions)) * 100
        messagebox.showinfo(
            "Game Over!",
            f"Your final score: {self.score}/{len(self.questions)} ({percentage:.1f}%)\n\nThanks for playing!"
        )
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NickelodeonTriviaGame(root)
    root.mainloop()
```
