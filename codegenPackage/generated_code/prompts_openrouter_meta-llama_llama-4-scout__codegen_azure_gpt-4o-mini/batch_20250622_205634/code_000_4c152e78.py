"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: "Design a card game like Géminito for learning music intervals and chords."
Generated: DETERMINISTIC_4c152e78a913e481
Batch ID: 20250622_205634
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

class CardGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Intervals and Chords Game")
        
        # Define music intervals and chords
        self.intervals = {
            "Major 2nd": "C-D",
            "Minor 3rd": "C-Eb",
            "Major 3rd": "C-E",
            "Perfect 4th": "C-F",
            "Perfect 5th": "C-G",
            "Minor 6th": "C-Ab",
            "Major 6th": "C-A",
            "Minor 7th": "C-Bb",
            "Major 7th": "C-B",
            "Octave": "C-C"
        }
        
        self.chords = {
            "C Major": "C-E-G",
            "C Minor": "C-Eb-G",
            "C Diminished": "C-Eb-Gb",
            "C Augmented": "C-E-G#",
            "C7": "C-E-G-Bb",
            "Cmaj7": "C-E-G-B"
        }
        
        self.cards = list(self.intervals.keys()) + list(self.chords.keys())
        random.shuffle(self.cards)
        
        self.score = 0
        self.current_card = None
        
        # Create UI elements
        self.score_label = tk.Label(master, text=f"Score: {self.score}")
        self.score_label.pack(pady=10)
        
        self.card_label = tk.Label(master, text="", font=("Helvetica", 24))
        self.card_label.pack(pady=20)
        
        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack(pady=10)
        
        self.submit_button = tk.Button(master, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)
        
        self.next_button = tk.Button(master, text="Next Card", command=self.next_card)
        self.next_button.pack(pady=10)
        
        self.next_card()  # Start the game with the first card

    def next_card(self):
        """Display the next card and reset the answer entry."""
        if self.cards:
            self.current_card = self.cards.pop()
            self.card_label.config(text=self.current_card)
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Game Over", f"Your final score is: {self.score}")
            self.master.quit()

    def check_answer(self):
        """Check the user's answer against the correct answer."""
        answer = self.answer_entry.get().strip()
        
        if not answer:
            messagebox.showwarning("Input Error", "Please enter an answer.")
            return
        
        correct_answer = self.get_correct_answer(self.current_card)
        
        if answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done!")
        else:
            messagebox.showerror("Incorrect", f"The correct answer was: {correct_answer}")
        
        self.score_label.config(text=f"Score: {self.score}")
        self.next_card()

    def get_correct_answer(self, card):
        """Return the correct answer for the given card."""
        if card in self.intervals:
            return self.intervals[card]
        elif card in self.chords:
            return self.chords[card]
        return ""

if __name__ == "__main__":
    root = tk.Tk()
    game = CardGame(root)
    root.mainloop()
```
