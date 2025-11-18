"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balloon-gomble-io.pages.dev
Prompt: Write code to display and update the count of "Mystery Marbles" collected during a balloon-lifting game in real time.
Generated: DETERMINISTIC_a63d51fa2bbb9dce
Batch ID: 20250612_153517
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

class MarbleCounterApp:
    def __init__(self, root):
        """
        Initialize the MarbleCounterApp with a Tkinter root window.
        """
        self.root = root
        self.root.title("Mystery Marble Counter")
        self.mystery_marbles = 0  # Initialize marble count to 0

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        """
        Create and configure UI components.
        """
        # Display label for marble count
        self.label = tk.Label(self.root, text=f"Mystery Marbles: {self.mystery_marbles}", font=("Arial", 16))
        self.label.pack(pady=10)

        # Button to increase marble count
        self.increment_button = tk.Button(self.root, text="Add Marble", font=("Arial", 14), command=self.add_marble)
        self.increment_button.pack(pady=5)

        # Button to reset marble count
        self.reset_button = tk.Button(self.root, text="Reset Count", font=("Arial", 14), command=self.reset_count)
        self.reset_button.pack(pady=5)

    def add_marble(self):
        """
        Increment the marble count and update the display label.
        """
        try:
            self.mystery_marbles += 1
            self.label.config(text=f"Mystery Marbles: {self.mystery_marbles}")  # Update label text
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while adding a marble: {e}")

    def reset_count(self):
        """
        Reset the marble count to zero and update the display label.
        """
        try:
            self.mystery_marbles = 0
            self.label.config(text=f"Mystery Marbles: {self.mystery_marbles}")  # Update label text
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while resetting the count: {e}")

# Main application entry point
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MarbleCounterApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Fatal Error", f"An error occurred while starting the application: {e}")
```
