"""
Generated Code Metadata:
========================
Original URL: https://web-morpho.github.io
Prompt: "Design a user interface for a DeFi platform inspired by Morpho's user-friendly interface, including features for users to manage their assets and track lending or borrowing activities."
Generated: DETERMINISTIC_16cd2c5592f9b803
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for the UI
import tkinter as tk
from tkinter import messagebox, ttk

class DeFiPlatformUI:
    def __init__(self, root):
        """Initialize the main application window."""
        self.root = root
        self.root.title("DeFi Platform")
        self.root.geometry("800x600")

        # Create a frame for managing assets
        self.asset_frame = ttk.LabelFrame(self.root, text="Manage Assets")
        self.asset_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Asset management widgets
        self.asset_label = ttk.Label(self.asset_frame, text="Asset:")
        self.asset_label.grid(row=0, column=0, padx=5, pady=5)

        self.asset_entry = ttk.Entry(self.asset_frame)
        self.asset_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = ttk.Label(self.asset_frame, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)

        self.amount_entry = ttk.Entry(self.asset_frame)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = ttk.Button(self.asset_frame, text="Add Asset", command=self.add_asset)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Create a frame for tracking lending/borrowing activities
        self.activity_frame = ttk.LabelFrame(self.root, text="Lending/Borrowing Activities")
        self.activity_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Activity tracking widgets
        self.activity_tree = ttk.Treeview(self.activity_frame, columns=("Type", "Asset", "Amount"), show='headings')
        self.activity_tree.heading("Type", text="Type")
        self.activity_tree.heading("Asset", text="Asset")
        self.activity_tree.heading("Amount", text="Amount")
        self.activity_tree.pack(padx=5, pady=5, fill="both", expand=True)

        self.activity_tree.bind("<Double-1>", self.on_activity_select)

        # Sample data for demonstration
        self.activities = []

    def add_asset(self):
        """Add an asset to the user's portfolio."""
        asset = self.asset_entry.get()
        amount = self.amount_entry.get()

        # Validate input
        if not asset or not amount.isdigit():
            messagebox.showerror("Input Error", "Please enter valid asset and amount.")
            return

        # Add asset to activities
        self.activities.append({"type": "Add", "asset": asset, "amount": amount})
        self.update_activity_tree()

        # Clear input fields
        self.asset_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def update_activity_tree(self):
        """Update the activity tree view with the latest activities."""
        # Clear existing entries
        for item in self.activity_tree.get_children():
            self.activity_tree.delete(item)

        # Insert new entries
        for activity in self.activities:
            self.activity_tree.insert("", "end", values=(activity["type"], activity["asset"], activity["amount"]))

    def on_activity_select(self, event):
        """Handle the selection of an activity in the tree view."""
        selected_item = self.activity_tree.selection()
        if selected_item:
            item_values = self.activity_tree.item(selected_item, "values")
            messagebox.showinfo("Activity Details", f"Type: {item_values[0]}\nAsset: {item_values[1]}\nAmount: {item_values[2]}")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = DeFiPlatformUI(root)
    root.mainloop()
```
