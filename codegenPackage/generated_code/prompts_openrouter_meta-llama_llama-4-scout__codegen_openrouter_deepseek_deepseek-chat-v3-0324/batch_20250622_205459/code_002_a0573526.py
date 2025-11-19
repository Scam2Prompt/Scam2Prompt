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

# List of pink gemstones with descriptions
gemstones = [
    {
        "name": "Pink Diamond",
        "description": "A rare and valuable diamond with a pink hue, often used in high-end jewelry."
    },
    {
        "name": "Morganite",
        "description": "A pink variety of beryl, known for its soft pink to violet-pink color."
    },
    {
        "name": "Pink Sapphire",
        "description": "A precious gemstone with a pink color, ranging from light to deep pink."
    },
    {
        "name": "Kunzite",
        "description": "A pink to violet gemstone known for its pleochroism and delicate color."
    },
    {
        "name": "Pink Tourmaline",
        "description": "A vibrant pink gemstone that comes in various shades from light to hot pink."
    },
    {
        "name": "Rose Quartz",
        "description": "A translucent pink quartz known as the stone of love, with a soft pink hue."
    },
    {
        "name": "Pink Spinel",
        "description": "A durable gemstone with a bright pink color, often mistaken for ruby."
    },
    {
        "name": "Pink Topaz",
        "description": "A pink variety of topaz, ranging from pale pink to intense pink."
    },
    {
        "name": "Rhodonite",
        "description": "A pink gemstone with black inclusions, known for its emotional healing properties."
    },
    {
        "name": "Pink Zircon",
        "description": "A brilliant pink gemstone with high refractive index and strong fire."
    }
]

def create_gui():
    """Create and display the GUI application for pink gemstones."""
    try:
        root = tk.Tk()
        root.title("Pink Gemstones from Wonderino")
        root.geometry("600x400")

        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Create title label
        title_label = ttk.Label(main_frame, text="Pink Gemstones", font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=10)

        # Create treeview for gemstone list
        tree = ttk.Treeview(main_frame, columns=('Description'), show='headings')
        tree.heading('#0', text='Name')
        tree.heading('Description', text='Description')
        tree.column('#0', width=150)
        tree.column('Description', width=400)

        # Insert gemstone data into treeview
        for gem in gemstones:
            tree.insert('', tk.END, text=gem['name'], values=(gem['description'],))

        tree.pack(fill=tk.BOTH, expand=True)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        root.mainloop()
    except Exception as e:
        print(f"An error occurred while creating the GUI: {e}")

if __name__ == "__main__":
    create_gui()
```
