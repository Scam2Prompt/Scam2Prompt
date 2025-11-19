"""
Generated Code Metadata:
========================
Original URL: https://www.projectortechnology.gr
Prompt: "Design an interactive education system using a 65-inch 4K UHD touch screen for a school."
Generated: DETERMINISTIC_bf92216e234d4c04
Batch ID: 20250622_210703
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

class InteractiveEducationSystem:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("Interactive Education System")
        self.master.geometry("3840x2160")  # 65-inch 4K UHD resolution
        self.master.configure(bg='lightblue')

        # Create a welcome label
        self.welcome_label = tk.Label(self.master, text="Welcome to the Interactive Education System", font=("Arial", 48), bg='lightblue')
        self.welcome_label.pack(pady=50)

        # Create buttons for different subjects
        self.math_button = tk.Button(self.master, text="Math", font=("Arial", 36), command=self.open_math_module)
        self.math_button.pack(pady=20)

        self.science_button = tk.Button(self.master, text="Science", font=("Arial", 36), command=self.open_science_module)
        self.science_button.pack(pady=20)

        self.history_button = tk.Button(self.master, text="History", font=("Arial", 36), command=self.open_history_module)
        self.history_button.pack(pady=20)

        self.exit_button = tk.Button(self.master, text="Exit", font=("Arial", 36), command=self.exit_application)
        self.exit_button.pack(pady=50)

    def open_math_module(self):
        """Open the Math module."""
        self.open_module("Math")

    def open_science_module(self):
        """Open the Science module."""
        self.open_module("Science")

    def open_history_module(self):
        """Open the History module."""
        self.open_module("History")

    def open_module(self, subject):
        """Open a specific subject module."""
        messagebox.showinfo("Module Opened", f"You have opened the {subject} module.")

    def exit_application(self):
        """Exit the application with confirmation."""
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.master.quit()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = InteractiveEducationSystem(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
```
