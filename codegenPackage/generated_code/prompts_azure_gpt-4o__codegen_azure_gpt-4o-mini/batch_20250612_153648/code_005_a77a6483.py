"""
Generated Code Metadata:
========================
Original URL: https://jellydrop.web.app
Prompt: Write code for a "Jelly Flip" game or utility, referencing the interactive tools mentioned on the JellyDrop site.
Generated: DETERMINISTIC_a77a6483a00cb879
Batch ID: 20250612_153648
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

class JellyFlipGame:
    def __init__(self, master):
        """Initialize the Jelly Flip game."""
        self.master = master
        self.master.title("Jelly Flip Game")
        
        # Game settings
        self.jelly_colors = ['red', 'green', 'blue', 'yellow', 'purple']
        self.jelly_count = 5
        self.jelly_flips = 0
        
        # Create UI elements
        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack()
        
        self.flip_button = tk.Button(master, text="Flip Jelly", command=self.flip_jelly)
        self.flip_button.pack()
        
        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()
        
        self.jelly_positions = []
        self.draw_jellies()

    def draw_jellies(self):
        """Draw jellies on the canvas at random positions."""
        self.canvas.delete("all")  # Clear previous jellies
        self.jelly_positions = []
        
        for _ in range(self.jelly_count):
            x = random.randint(50, 350)
            y = random.randint(50, 350)
            color = random.choice(self.jelly_colors)
            self.jelly_positions.append((x, y, color))
            self.canvas.create_oval(x, y, x + 50, y + 50, fill=color, outline='black')

    def flip_jelly(self):
        """Flip a random jelly and count the flips."""
        if not self.jelly_positions:
            messagebox.showinfo("Game Over", "No jellies left to flip!")
            return
        
        # Randomly select a jelly to flip
        index = random.randint(0, len(self.jelly_positions) - 1)
        x, y, color = self.jelly_positions[index]
        
        # Change the color to simulate a flip
        new_color = 'white' if color != 'white' else random.choice(self.jelly_colors)
        self.canvas.create_oval(x, y, x + 50, y + 50, fill=new_color, outline='black')
        
        # Update the jelly position with the new color
        self.jelly_positions[index] = (x, y, new_color)
        self.jelly_flips += 1
        
        # Check if all jellies are flipped
        if all(jelly[2] == 'white' for jelly in self.jelly_positions):
            messagebox.showinfo("Congratulations!", f"You flipped all jellies in {self.jelly_flips} flips!")
            self.reset_game()

    def reset_game(self):
        """Reset the game to its initial state."""
        self.jelly_flips = 0
        self.draw_jellies()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        game = JellyFlipGame(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
```
