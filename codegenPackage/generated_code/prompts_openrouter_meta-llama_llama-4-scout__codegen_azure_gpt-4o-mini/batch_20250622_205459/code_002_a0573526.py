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
from tkinter import messagebox

# List of pink gemstones with their descriptions
PINK_GEMSTONES = [
    ("Rose Quartz", "A crystal known for its gentle pink essence, promoting love and peace."),
    ("Pink Sapphire", "A precious gemstone that symbolizes wisdom, loyalty, and nobility."),
    ("Morganite", "A beautiful pink beryl that represents compassion and promise."),
    ("Pink Tourmaline", "A versatile stone that is believed to inspire creativity and compassion."),
    ("Pink Diamond", "One of the rarest gemstones, symbolizing love and commitment."),
    ("Rhodonite", "A stone of compassion that helps in emotional healing."),
    ("Pink Opal", "A soothing stone that promotes emotional balance and healing."),
    ("Kunsite", "A pink spodumene that encourages love and emotional healing."),
    ("Pink Spinel", "A vibrant gemstone that symbolizes hope and revitalization."),
    ("Pink Topaz", "A gemstone that represents love and affection, often used in jewelry.")
]

def create_gemstone_list():
    """Creates a formatted string of gemstone names and descriptions."""
    gemstone_list = ""
    for name, description in PINK_GEMSTONES:
        gemstone_list += f"{name}: {description}\n"
    return gemstone_list.strip()

def show_gemstone_info():
    """Displays the list of pink gemstones in a message box."""
    gemstone_info = create_gemstone_list()
    messagebox.showinfo("Pink Gemstones", gemstone_info)

def create_gui():
    """Creates the main GUI application window."""
    # Initialize the main window
    root = tk.Tk()
    root.title("Pink Gemstones")

    # Create a button to show gemstone information
    info_button = tk.Button(root, text="Show Pink Gemstones", command=show_gemstone_info)
    info_button.pack(pady=20)

    # Set the window size and start the main loop
    root.geometry("300x150")
    root.mainloop()

if __name__ == "__main__":
    try:
        create_gui()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
```
