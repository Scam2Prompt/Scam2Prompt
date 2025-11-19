"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: "Create a customized software solution with easy-to-use interface and update features for a small business."
Generated: DETERMINISTIC_5e1ccf478ef53691
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
import json
import os

# Define the path for the data file
DATA_FILE = 'business_data.json'

class BusinessApp:
    def __init__(self, root):
        """Initialize the main application window."""
        self.root = root
        self.root.title("Small Business Management App")
        self.root.geometry("400x300")

        # Create UI elements
        self.create_widgets()

        # Load existing data if available
        self.load_data()

    def create_widgets(self):
        """Create and place UI elements in the window."""
        self.label = tk.Label(self.root, text="Business Name:")
        self.label.pack(pady=10)

        self.business_name_entry = tk.Entry(self.root)
        self.business_name_entry.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Business Name", command=self.update_business_name)
        self.update_button.pack(pady=20)

        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack(pady=10)

    def load_data(self):
        """Load business data from a JSON file."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                try:
                    data = json.load(file)
                    self.business_name_entry.insert(0, data.get('business_name', ''))
                except json.JSONDecodeError:
                    messagebox.showerror("Error", "Failed to load data. The file may be corrupted.")

    def update_business_name(self):
        """Update the business name and save it to a JSON file."""
        business_name = self.business_name_entry.get().strip()
        if not business_name:
            messagebox.showwarning("Warning", "Business name cannot be empty.")
            return

        # Save the updated business name
        data = {'business_name': business_name}
        try:
            with open(DATA_FILE, 'w') as file:
                json.dump(data, file)
            self.status_label.config(text="Business name updated successfully!")
        except IOError as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = BusinessApp(root)
    root.mainloop()
```
