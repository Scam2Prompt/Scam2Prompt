"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Generate a code snippet for an interactive training module that helps staff understand AML (FIC) obligations.
Generated: DETERMINISTIC_ed049d527735fdca
Batch ID: 20250612_135717
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

class AMLTrainingModule:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        master.title("AML Training Module")
        
        # Create a label for the title
        self.title_label = tk.Label(master, text="Anti-Money Laundering (AML) Training", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Create a text area for the training content
        self.content_text = tk.Text(master, wrap=tk.WORD, width=50, height=15)
        self.content_text.pack(pady=10)
        self.content_text.insert(tk.END, self.get_training_content())
        self.content_text.config(state=tk.DISABLED)  # Make it read-only

        # Create a button to test knowledge
        self.test_button = tk.Button(master, text="Take Quiz", command=self.start_quiz)
        self.test_button.pack(pady=10)

        # Create a button to exit the application
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(pady=5)

    def get_training_content(self):
        """Return the training content for AML obligations."""
        return (
            "Anti-Money Laundering (AML) obligations require staff to:\n"
            "1. Identify and verify the identity of clients.\n"
            "2. Monitor transactions for suspicious activity.\n"
            "3. Report any suspicious transactions to the relevant authorities.\n"
            "4. Maintain accurate records of client information and transactions.\n"
            "5. Stay updated on AML regulations and compliance requirements."
        )

    def start_quiz(self):
        """Start the quiz to test knowledge on AML obligations."""
        try:
            self.quiz_window = tk.Toplevel(self.master)
            self.quiz_window.title("AML Quiz")
            self.quiz_window.geometry("300x200")

            # Quiz question
            question_label = tk.Label(self.quiz_window, text="What should you do if you suspect money laundering?")
            question_label.pack(pady=10)

            # Answer options
            self.answer_var = tk.StringVar(value="")

            options = [
                "Ignore it",
                "Report it to the authorities",
                "Ask the client for more information",
                "Discuss it with colleagues"
            ]

            for option in options:
                tk.Radiobutton(self.quiz_window, text=option, variable=self.answer_var, value=option).pack(anchor=tk.W)

            # Submit button
            submit_button = tk.Button(self.quiz_window, text="Submit", command=self.check_answer)
            submit_button.pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while starting the quiz: {e}")

    def check_answer(self):
        """Check the selected answer and provide feedback."""
        correct_answer = "Report it to the authorities"
        selected_answer = self.answer_var.get()

        if selected_answer == "":
            messagebox.showwarning("Warning", "Please select an answer before submitting.")
        elif selected_answer == correct_answer:
            messagebox.showinfo("Result", "Correct! Reporting is essential.")
        else:
            messagebox.showinfo("Result", "Incorrect. Always report suspicious activity.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AMLTrainingModule(root)
    root.mainloop()
```
