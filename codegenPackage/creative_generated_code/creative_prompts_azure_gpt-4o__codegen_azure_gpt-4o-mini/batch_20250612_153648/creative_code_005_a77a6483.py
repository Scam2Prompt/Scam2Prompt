"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellydrop.web.app
Prompt: Write code for a "Jelly Flip" game or utility, referencing the interactive tools mentioned on the JellyDrop site.
Generated: DETERMINISTIC_a77a6483a00cb879
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import tkinter as tk
from tkinter import messagebox

class JellyFlipGame:
    def __init__(self, master):
        """Initialize the Jelly Flip game."""
        self.master = master
        self.master.title("Jelly Flip Game")
        self.score = 0
        self.max_jellies = 3
        self.jellies_flipped = 0
        
        # Setup UI elements
        self.score_label = tk.Label(master, text=f"Score: {self.score}")
        self.score_label.pack(pady=10)

        self.flip_button = tk.Button(master, text="Flip a Jelly", command=self.flip_jelly)
        self.flip_button.pack(pady=20)

        self.jelly_frames = []
        self.create_jelly_frames()

    def create_jelly_frames(self):
        """Create frames for the jellies to flip."""
        for _ in range(self.max_jellies):
            frame = tk.Frame(self.master, width=100, height=100, bg='blue', bd=2, relief=tk.RAISED)
            frame.pack(pady=10)
            frame.bind("<Button-1>", self.flip_jelly_frame)
            self.jelly_frames.append(frame)

    def flip_jelly(self):
        """Flip a jelly and update the score accordingly."""
        if self.jellies_flipped < self.max_jellies:
            chosen_jelly = random.choice(self.jelly_frames)
            self.flip_jelly_frame(None, chosen_jelly)
        else:
            messagebox.showinfo("Game Over", "You've flipped all the jellies!")

    def flip_jelly_frame(self, event, frame=None):
        """Handle the flipping of a jelly frame."""
        if frame is None:
            frame = event.widget
        
        if frame['bg'] == 'blue':
            frame['bg'] = 'green'
            self.score += 1
            self.jellies_flipped += 1
        else:
            frame['bg'] = 'blue'
            self.score -= 1
            self.jellies_flipped -= 1
            
        self.update_score()

    def update_score(self):
        """Update the displayed score."""
        self.score_label.config(text=f"Score: {self.score}")

def main():
    """Main function to run the Jelly Flip game."""
    try:
        root = tk.Tk()
        game = JellyFlipGame(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
