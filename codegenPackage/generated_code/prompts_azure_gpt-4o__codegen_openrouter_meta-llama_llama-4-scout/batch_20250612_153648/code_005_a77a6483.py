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
import tkinter as tk
from random import shuffle

class JellyFlip:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jelly Flip")
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.tiles = list(range(1, 17)) * 2
        shuffle(self.tiles)
        self.buttons = []
        self.clicked = []
        self.matches = 0

        for i in range(32):
            button = tk.Button(self.frame, text="", command=lambda i=i: self.click(i), height=3, width=6)
            button.grid(row=i//8, column=i%8)
            self.buttons.append(button)

    def click(self, i):
        if len(self.clicked) < 2 and i not in self.clicked:
            self.buttons[i].config(text=str(self.tiles[i]))
            self.clicked.append(i)
            if len(self.clicked) == 2:
                self.root.after(500, self.check_match)

    def check_match(self):
        if self.tiles[self.clicked[0]] == self.tiles[self.clicked[1]]:
            self.matches += 1
            self.buttons[self.clicked[0]].config(state="disabled")
            self.buttons[self.clicked[1]].config(state="disabled")
        else:
            self.buttons[self.clicked[0]].config(text="")
            self.buttons[self.clicked[1]].config(text="")
        self.clicked = []
        if self.matches == 16:
            self.root.title("Congratulations! You won!")
            for button in self.buttons:
                button.config(state="disabled")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = JellyFlip()
    game.run()
```
