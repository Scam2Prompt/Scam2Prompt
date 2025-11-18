"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Develop a Python-based dashboard for tracking Agile certifications and course progress, as outlined in CrestAgile's offerings.
Generated: DETERMINISTIC_33b75eadc7b49409
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# Constants for file management
DATA_FILE = 'agile_certifications.json'

# Ensure data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Load existing certifications from JSON file
def load_certifications():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save certifications to JSON file
def save_certifications(certifications):
    with open(DATA_FILE, 'w') as f:
        json.dump(certifications, f, indent=4)

# Main application class
class AgileCertDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Agile Certifications Tracker")
        
        # Initialize data
        self.certifications = load_certifications()
        
        # Set up UI components
        self.setup_ui()

    def setup_ui(self):
        # Frame for adding certifications
        frame_add = ttk.Frame(self.root)
        frame_add.pack(padx=10, pady=10)

        # Input fields for certification name and progress
        ttk.Label(frame_add, text="Certification Name:").grid(column=0, row=0)
        self.cert_name_entry = ttk.Entry(frame_add)
        self.cert_name_entry.grid(column=1, row=0)

        ttk.Label(frame_add, text="Progress (%):").grid(column=0, row=1)
        self.progress_entry = ttk.Entry(frame_add)
        self.progress_entry.grid(column=1, row=1)

        # Button to add certification
        self.add_button = ttk.Button(frame_add, text="Add Certification", command=self.add_certification)
        self.add_button.grid(columnspan=2, pady=5)

        # Treeview for displaying certifications
        self.cert_tree = ttk.Treeview(self.root, columns=("Name", "Progress"), show='headings')
        self.cert_tree.heading("Name", text="Certification Name")
        self.cert_tree.heading("Progress", text="Progress (%)")
        self.cert_tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Load existing certifications into the treeview
        self.load_certifications_into_tree()

    def load_certifications_into_tree(self):
        """Load certifications into the Treeview widget."""
        for cert in self.certifications:
            self.cert_tree.insert("", tk.END, values=(cert['name'], cert['progress']))

    def add_certification(self):
        """Add a new certification to the list and save it."""
        name = self.cert_name_entry.get().strip()
        progress = self.progress_entry.get().strip()

        # Basic validation
        if not name or not progress.isdigit() or not (0 <= int(progress) <= 100):
            messagebox.showerror("Input Error", "Please provide a valid certification name and progress percentage (0-100).")
            return

        # Create a new certification entry
        certification = {
            'name': name,
            'progress': int(progress)
        }
        self.certifications.append(certification)
        self.save_certifications(self.certifications)
        
        # Clear input fields
        self.cert_name_entry.delete(0, tk.END)
        self.progress_entry.delete(0, tk.END)

        # Refresh the Treeview
        self.cert_tree.insert("", tk.END, values=(certification['name'], certification['progress']))

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AgileCertDashboard(root)
    root.mainloop()
```
