"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Write a code for an educational program that teaches children about the importance of respect and empathy in coexistence, similar to the "Vivir es Convivir" program.
Generated: DETERMINISTIC_1b9ed3eaab605644
Batch ID: 20250622_210655
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

class EducationalProgram:
    def __init__(self, master):
        """Initialize the main window and set up the program."""
        self.master = master
        master.title("Respect and Empathy Program")
        
        # Create a welcome label
        self.welcome_label = tk.Label(master, text="Welcome to the Respect and Empathy Program!")
        self.welcome_label.pack(pady=10)

        # Create a button to start the lesson
        self.start_button = tk.Button(master, text="Start Lesson", command=self.start_lesson)
        self.start_button.pack(pady=5)

        # Create a button to exit the program
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(pady=5)

    def start_lesson(self):
        """Start the lesson on respect and empathy."""
        lesson_text = (
            "Lesson: The Importance of Respect and Empathy\n\n"
            "1. Respect means treating others the way you want to be treated.\n"
            "2. Empathy is understanding and sharing the feelings of others.\n"
            "3. Together, respect and empathy help us coexist peacefully.\n\n"
            "Let's practice these values in our daily lives!"
        )
        messagebox.showinfo("Lesson", lesson_text)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        program = EducationalProgram(root)
        root.mainloop()
    except Exception as e:
        # Handle any unexpected errors gracefully
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
```
