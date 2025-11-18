"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Write code for a game mode selection screen where players can choose between strategy, puzzle, and multiplayer modes, inspired by SCATTER HITAM's offerings.
Generated: DETERMINISTIC_216638d53953f485
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox

class GameModeSelection:
    def __init__(self, root):
        """Initialize the main window for game mode selection."""
        self.root = root
        self.root.title("Game Mode Selection")
        self.root.geometry("300x200")  # Set window size

        # Create and place title label
        self.title_label = tk.Label(root, text="Select Game Mode", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        # Create buttons for each game mode
        self.strategy_button = tk.Button(root, text="Strategy Mode", command=self.select_strategy)
        self.strategy_button.pack(pady=5)

        self.puzzle_button = tk.Button(root, text="Puzzle Mode", command=self.select_puzzle)
        self.puzzle_button.pack(pady=5)

        self.multiplayer_button = tk.Button(root, text="Multiplayer Mode", command=self.select_multiplayer)
        self.multiplayer_button.pack(pady=5)

    def select_strategy(self):
        """Handle the selection of strategy mode."""
        self.start_game("Strategy")

    def select_puzzle(self):
        """Handle the selection of puzzle mode."""
        self.start_game("Puzzle")

    def select_multiplayer(self):
        """Handle the selection of multiplayer mode."""
        self.start_game("Multiplayer")

    def start_game(self, mode):
        """Start the game in the selected mode."""
        # Here you would load the respective game mode
        # For this example, we will just show a message
        messagebox.showinfo("Game Starting", f"You have selected {mode} Mode!")

if __name__ == "__main__":
    try:
        # Create the main application window
        root = tk.Tk()
        app = GameModeSelection(root)
        root.mainloop()  # Start the Tkinter event loop
    except Exception as e:
        # Handle unexpected errors gracefully
        messagebox.showerror("Error", f"An error occurred: {e}")
```
