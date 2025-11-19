"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: "Write a Python script to create a pop-up snowman card using paper crafting techniques."
Generated: DETERMINISTIC_1087ce3f56483ab9
Batch ID: 20250622_205709
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

class SnowmanCard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pop-up Snowman Card")

        # Create main canvas
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        # Draw background
        self.canvas.create_rectangle(0, 0, 400, 300, fill='light blue')

        # Draw snowman body
        self.canvas.create_oval(150, 200, 250, 300, fill='white')
        self.canvas.create_oval(120, 150, 280, 250, fill='white')
        self.canvas.create_oval(180, 100, 220, 150, fill='white')

        # Draw coal eyes and mouth
        self.canvas.create_oval(195, 120, 205, 130, fill='black')
        self.canvas.create_oval(215, 120, 225, 130, fill='black')
        self.canvas.create_arc(200, 140, 220, 160, start=0, extent=-180, style='arc', width=2)

        # Draw carrot nose
        self.canvas.create_polygon(210, 130, 220, 140, 200, 140, fill='orange')

        # Draw scarf
        self.canvas.create_rectangle(180, 160, 220, 170, fill='red')

        # Draw hat
        self.canvas.create_rectangle(190, 90, 210, 110, fill='black')
        self.canvas.create_rectangle(170, 110, 230, 120, fill='black')

        # Add buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_image)
        self.save_button.pack(side=tk.LEFT)
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.destroy)
        self.exit_button.pack(side=tk.LEFT)

    def save_image(self):
        try:
            self.canvas.postscript(file="snowman_card.ps")
            messagebox.showinfo("Success", "Image saved as snowman_card.ps")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    snowman_card = SnowmanCard()
    snowman_card.run()
```
