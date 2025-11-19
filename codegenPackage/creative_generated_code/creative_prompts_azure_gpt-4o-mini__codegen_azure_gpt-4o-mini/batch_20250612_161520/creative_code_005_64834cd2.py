"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://publichealth-care.com
Prompt: How can I build a user-friendly interface for tracking mental wellness, drawing from the expert insights shared on Public Health Care?
Generated: DETERMINISTIC_64834cd21fbe1297
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import os

# Define the main application class
class MentalWellnessTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Wellness Tracker")

        # Set up the interface elements
        self.create_widgets()
        self.data_file = "wellness_data.json"
        self.load_data()

    def create_widgets(self):
        """Create the user interface widgets."""
        # Create a label for the title
        title_label = tk.Label(self.root, text="Mental Wellness Tracker", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Create a text area for user input
        self.entry = tk.Text(self.root, height=10, width=50)
        self.entry.pack(pady=10)

        # Create a button to submit the entry
        submit_button = tk.Button(self.root, text="Submit Entry", command=self.submit_entry)
        submit_button.pack(pady=5)

        # Create a button to view history
        history_button = tk.Button(self.root, text="View History", command=self.view_history)
        history_button.pack(pady=5)

    def submit_entry(self):
        """Handle the submission of a new entry."""
        entry_text = self.entry.get("1.0", tk.END).strip()
        if not entry_text:
            messagebox.showwarning("Warning", "Entry cannot be empty!")
            return

        # Create a new entry dictionary
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "text": entry_text
        }

        # Save the entry to a file
        self.save_entry(entry)

        # Clear the text area after submission
        self.entry.delete("1.0", tk.END)
        messagebox.showinfo("Success", "Entry submitted successfully!")

    def save_entry(self, entry):
        """Save the new entry to a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                data = json.load(file)
        else:
            data = []

        data.append(entry)

        # Write the updated data back to the file
        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        """Load existing data from the JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                self.history_data = json.load(file)
        else:
            self.history_data = []

    def view_history(self):
        """Display the history of entries in a message box."""
        if not self.history_data:
            messagebox.showinfo("History", "No entries found.")
            return

        history_text = "\n".join([f"{entry['date']}: {entry['text']}" for entry in self.history_data])
        messagebox.showinfo("Entry History", history_text)

# Entry point of the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MentalWellnessTracker(root)
    root.mainloop()
```
