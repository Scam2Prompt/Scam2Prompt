"""
Generated Code Metadata:
========================
Original URL: https://umbrella-d96b1.web.app
Prompt: Generate code to implement a user interface for a digital asset management system that allows users to manage their assets on their own terms, similar to Umbrella.
Generated: DETERMINISTIC_698d26b12d213a23
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox, filedialog
import os

class DigitalAssetManager:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("Digital Asset Management System")
        self.master.geometry("600x400")

        # Create a list to hold asset file paths
        self.assets = []

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        """Create and place UI components in the window."""
        # Title label
        self.title_label = tk.Label(self.master, text="Digital Asset Manager", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Asset listbox
        self.asset_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, width=50, height=15)
        self.asset_listbox.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(self.master, text="Add Asset", command=self.add_asset)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(self.master, text="Remove Asset", command=self.remove_asset)
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.view_button = tk.Button(self.master, text="View Asset", command=self.view_asset)
        self.view_button.pack(side=tk.LEFT, padx=10)

    def add_asset(self):
        """Add a new asset to the list."""
        file_path = filedialog.askopenfilename(title="Select Asset File")
        if file_path:
            self.assets.append(file_path)
            self.asset_listbox.insert(tk.END, os.path.basename(file_path))

    def remove_asset(self):
        """Remove the selected asset from the list."""
        try:
            selected_index = self.asset_listbox.curselection()[0]
            self.asset_listbox.delete(selected_index)
            del self.assets[selected_index]
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select an asset to remove.")

    def view_asset(self):
        """View the selected asset."""
        try:
            selected_index = self.asset_listbox.curselection()[0]
            asset_path = self.assets[selected_index]
            os.startfile(asset_path)  # Open the asset file with the default application
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select an asset to view.")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = DigitalAssetManager(root)
    root.mainloop()
```
