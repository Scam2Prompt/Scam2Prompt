"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Design a user interface for an internal tool at Hanil Furniture Gallery that allows employees to track their professional development and training programs.
Generated: DETERMINISTIC_a8ee35f8172860e1
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# Define the path for the data file
DATA_FILE = 'employee_training_data.json'

# Function to load existing training data from a JSON file
def load_training_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save training data to a JSON file
def save_training_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Main application class
class TrainingTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Training Tracker")
        
        # Load existing training data
        self.training_data = load_training_data()
        
        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Frame for input fields
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

        # Employee Name Label and Entry
        ttk.Label(input_frame, text="Employee Name:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = ttk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1)

        # Training Program Label and Entry
        ttk.Label(input_frame, text="Training Program:").grid(row=1, column=0, sticky=tk.W)
        self.program_entry = ttk.Entry(input_frame, width=30)
        self.program_entry.grid(row=1, column=1)

        # Add Training Button
        self.add_button = ttk.Button(input_frame, text="Add Training", command=self.add_training)
        self.add_button.grid(row=2, columnspan=2)

        # Treeview for displaying training records
        self.tree = ttk.Treeview(self.root, columns=("Name", "Program"), show='headings')
        self.tree.heading("Name", text="Employee Name")
        self.tree.heading("Program", text="Training Program")
        self.tree.grid(row=1, column=0, sticky=(tk.W, tk.E))

        # Load existing records into the treeview
        self.load_records()

    def load_records(self):
        """Load training records into the treeview."""
        for name, programs in self.training_data.items():
            for program in programs:
                self.tree.insert("", tk.END, values=(name, program))

    def add_training(self):
        """Add a new training record for the employee."""
        name = self.name_entry.get().strip()
        program = self.program_entry.get().strip()

        if not name or not program:
            messagebox.showerror("Input Error", "Both fields must be filled out.")
            return

        # Add training record to the data structure
        if name in self.training_data:
            self.training_data[name].append(program)
        else:
            self.training_data[name] = [program]

        # Save updated data to file
        save_training_data(self.training_data)

        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.program_entry.delete(0, tk.END)

        # Refresh the treeview
        self.tree.delete(*self.tree.get_children())
        self.load_records()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = TrainingTrackerApp(root)
    root.mainloop()
```
