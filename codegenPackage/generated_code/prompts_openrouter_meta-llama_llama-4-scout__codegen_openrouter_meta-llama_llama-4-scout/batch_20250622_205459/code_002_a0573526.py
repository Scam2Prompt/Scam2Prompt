"""
Generated Code Metadata:
========================
Original URL: https://wonderino.com
Prompt: "Generate a list of 10 pink gemstones as described on Wonderino, including their names and a brief description of each, and provide a Python code snippet to create a simple GUI application displaying this list."
Generated: DETERMINISTIC_a0573526839e228d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk

# List of pink gemstones with their descriptions
pink_gemstones = [
    {"name": "Pink Tourmaline", "description": "A type of tourmaline that ranges in color from pastel pink to vibrant magenta."},
    {"name": "Rose Quartz", "description": "A type of quartz crystal that gets its pink color from iron and titanium impurities."},
    {"name": "Pink Sapphire", "description": "A type of corundum that is prized for its vibrant pink color."},
    {"name": "Rhodolite", "description": "A type of garnet that ranges in color from pink to purplish-pink."},
    {"name": "Pink Topaz", "description": "A type of topaz that is heat-treated to produce its distinctive pink color."},
    {"name": "Spinel", "description": "A type of mineral that can range in color from pink to reddish-pink."},
    {"name": "Pink Opal", "description": "A type of opal that displays a range of pink colors."},
    {"name": "Pink Ammolite", "description": "A rare gemstone that displays a range of pink colors."},
    {"name": "Pink Charoite", "description": "A type of mineral that is prized for its vibrant pink color."},
    {"name": "Pink Jade", "description": "A type of jade that ranges in color from pale pink to vibrant magenta."},
]

class GemstoneApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pink Gemstones")
        self.geometry("400x600")

        # Create a frame to hold the list of gemstones
        self.frame = tk.Frame(self)
        self.frame.pack(fill="both", expand=True)

        # Create a treeview to display the list of gemstones
        self.tree = ttk.Treeview(self.frame)

        # Define the columns
        self.tree["columns"] = ("Name", "Description")

        # Format the columns
        self.tree.column("#0", width=0, stretch="no")
        self.tree.column("Name", anchor="w", width=150)
        self.tree.column("Description", anchor="w", width=200)

        # Create the headings
        self.tree.heading("#0", text="", anchor="w")
        self.tree.heading("Name", text="Name", anchor="w")
        self.tree.heading("Description", text="Description", anchor="w")

        # Add the gemstones to the treeview
        for gemstone in pink_gemstones:
            self.tree.insert("", "end", values=(gemstone["name"], gemstone["description"]))

        # Pack the treeview
        self.tree.pack(fill="both", expand=True)

if __name__ == "__main__":
    try:
        app = GemstoneApp()
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
```
