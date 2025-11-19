"""
Generated Code Metadata:
========================
Original URL: https://prominsac.com
Prompt: How can I use the Prominsac library to create a menu interface with icons for different items?
Generated: DETERMINISTIC_26508d4b0e73a41c
Batch ID: 20250612_162106
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
from PIL import Image, ImageTk

class MenuItem:
    """Represents a menu item with an icon."""
    
    def __init__(self, name, icon_path, command):
        """
        Initializes a MenuItem.

        Args:
            name (str): The name of the menu item.
            icon_path (str): The path to the icon image.
            command (function): The function to call when the item is selected.
        """
        self.name = name
        self.icon_path = icon_path
        self.command = command

class MenuInterface:
    """A menu interface with icons for different items."""
    
    def __init__(self, root):
        """
        Initializes a MenuInterface.

        Args:
            root (tkinter.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Menu Interface")
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.items = []

    def add_item(self, item):
        """
        Adds a menu item to the interface.

        Args:
            item (MenuItem): The item to add.
        """
        self.items.append(item)
        self._create_item(item)

    def _create_item(self, item):
        """Creates a button for a menu item."""
        item_frame = tk.Frame(self.frame)
        item_frame.pack(fill="x", pady=10)

        try:
            icon = Image.open(item.icon_path)
            icon = icon.resize((24, 24))  # Resize the icon to 24x24
            icon = ImageTk.PhotoImage(icon)
            button = tk.Button(item_frame, image=icon, command=item.command)
            button.image = icon  # Keep a reference to prevent garbage collection
            button.pack(side="left")

            label = tk.Label(item_frame, text=item.name)
            label.pack(side="left", padx=10)
        except Exception as e:
            print(f"Error creating item: {e}")

    def run(self):
        """Runs the application."""
        self.root.mainloop()

def example_command():
    print("Example command executed")

if __name__ == "__main__":
    root = tk.Tk()

    menu = MenuInterface(root)

    item1 = MenuItem("Item 1", "icon1.png", example_command)
    item2 = MenuItem("Item 2", "icon2.png", example_command)

    menu.add_item(item1)
    menu.add_item(item2)

    menu.run()
```
