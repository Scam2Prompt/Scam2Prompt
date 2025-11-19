"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Construct a user interface component that displays the available leather cases for Emanuelson Reels, ensuring it includes options for customization as mentioned on the website.
Generated: DETERMINISTIC_38bab8a97c09d963
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Emanuelson Reels Leather Case UI Component

import tkinter as tk
from tkinter import ttk

class EmanuelsonReelsLeatherCaseUI:
    def __init__(self, root):
        """
        Initialize the Emanuelson Reels Leather Case UI component.

        Args:
            root (tkinter.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Emanuelson Reels Leather Cases")

        # Create a notebook to hold the different customization options
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Create frames for each customization option
        self.case_selection_frame = tk.Frame(self.notebook)
        self.customization_frame = tk.Frame(self.notebook)
        self.summary_frame = tk.Frame(self.notebook)

        # Add frames to the notebook
        self.notebook.add(self.case_selection_frame, text="Case Selection")
        self.notebook.add(self.customization_frame, text="Customization")
        self.notebook.add(self.summary_frame, text="Summary")

        # Case selection frame
        self.case_selection_label = tk.Label(self.case_selection_frame, text="Select a leather case:")
        self.case_selection_label.pack()

        # List of available leather cases
        self.leather_cases = [
            "Brown Leather",
            "Black Leather",
            "Tan Leather",
            "Custom Leather"
        ]

        # Variable to hold the selected case
        self.selected_case = tk.StringVar()
        self.selected_case.set(self.leather_cases[0])  # default value

        # Create a dropdown menu for case selection
        self.case_selection_dropdown = tk.OptionMenu(self.case_selection_frame, self.selected_case, *self.leather_cases)
        self.case_selection_dropdown.pack()

        # Customization frame
        self.customization_label = tk.Label(self.customization_frame, text="Customize your leather case:")
        self.customization_label.pack()

        # Customization options
        self.customization_options = {
            "Monogram": tk.BooleanVar(),
            "Special Message": tk.BooleanVar()
        }

        # Create checkboxes for customization options
        self.monogram_checkbox = tk.Checkbutton(self.customization_frame, text="Monogram", variable=self.customization_options["Monogram"])
        self.monogram_checkbox.pack(anchor=tk.W)

        self.special_message_checkbox = tk.Checkbutton(self.customization_frame, text="Special Message", variable=self.customization_options["Special Message"])
        self.special_message_checkbox.pack(anchor=tk.W)

        # Summary frame
        self.summary_label = tk.Label(self.summary_frame, text="Summary:")
        self.summary_label.pack()

        # Create a button to generate a summary
        self.summary_button = tk.Button(self.summary_frame, text="Generate Summary", command=self.generate_summary)
        self.summary_button.pack()

        # Create a label to display the summary
        self.summary_text = tk.Text(self.summary_frame, height=5, width=40)
        self.summary_text.pack()

    def generate_summary(self):
        """
        Generate a summary of the selected leather case and customization options.
        """
        try:
            selected_case = self.selected_case.get()
            customization_options = {option: var.get() for option, var in self.customization_options.items()}

            summary = f"Leather Case: {selected_case}\n"
            summary += "Customization Options:\n"
            for option, value in customization_options.items():
                summary += f"- {option}: {value}\n"

            self.summary_text.delete(1.0, tk.END)
            self.summary_text.insert(tk.END, summary)
        except Exception as e:
            print(f"Error generating summary: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmanuelsonReelsLeatherCaseUI(root)
    root.mainloop()
```
