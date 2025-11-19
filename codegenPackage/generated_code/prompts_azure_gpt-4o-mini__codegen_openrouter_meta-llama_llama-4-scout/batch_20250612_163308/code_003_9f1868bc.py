"""
Generated Code Metadata:
========================
Original URL: https://shoppiday.site
Prompt: Generate code to create a user interface for displaying cashback offers and discounts, inspired by Shoppiday's features.
Generated: DETERMINISTIC_9f1868bc7098db25
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cashback_ui.py

import tkinter as tk
from tkinter import ttk

class CashbackUI:
    def __init__(self, root):
        """
        Initialize the cashback UI.

        Args:
            root (tkinter.Tk): The root window.
        """
        self.root = root
        self.root.title("Cashback Offers and Discounts")

        # Create a notebook with tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Create frames for each tab
        self.offers_frame = tk.Frame(self.notebook)
        self.discounts_frame = tk.Frame(self.notebook)
        self.expired_frame = tk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.offers_frame, text="Cashback Offers")
        self.notebook.add(self.discounts_frame, text="Discounts")
        self.notebook.add(self.expired_frame, text="Expired Offers")

        # Create a treeview for displaying offers
        self.offers_tree = ttk.Treeview(self.offers_frame)

        # Define columns
        self.offers_tree['columns'] = ('Offer', 'Discount', 'Expiry Date')

        # Format columns
        self.offers_tree.column("#0", width=0, stretch=tk.NO)
        self.offers_tree.column("Offer", anchor=tk.W, width=200)
        self.offers_tree.column("Discount", anchor=tk.W, width=100)
        self.offers_tree.column("Expiry Date", anchor=tk.W, width=100)

        # Create headings
        self.offers_tree.heading("#0", text='', anchor=tk.W)
        self.offers_tree.heading('Offer', text='Offer', anchor=tk.W)
        self.offers_tree.heading('Discount', text='Discount', anchor=tk.W)
        self.offers_tree.heading('Expiry Date', text='Expiry Date', anchor=tk.W)

        # Pack the treeview
        self.offers_tree.pack(fill=tk.BOTH, expand=True)

        # Create a similar treeview for discounts
        self.discounts_tree = ttk.Treeview(self.discounts_frame)

        # Define columns
        self.discounts_tree['columns'] = ('Discount', 'Code', 'Expiry Date')

        # Format columns
        self.discounts_tree.column("#0", width=0, stretch=tk.NO)
        self.discounts_tree.column("Discount", anchor=tk.W, width=200)
        self.discounts_tree.column("Code", anchor=tk.W, width=100)
        self.discounts_tree.column("Expiry Date", anchor=tk.W, width=100)

        # Create headings
        self.discounts_tree.heading("#0", text='', anchor=tk.W)
        self.discounts_tree.heading('Discount', text='Discount', anchor=tk.W)
        self.discounts_tree.heading('Code', text='Code', anchor=tk.W)
        self.discounts_tree.heading('Expiry Date', text='Expiry Date', anchor=tk.W)

        # Pack the treeview
        self.discounts_tree.pack(fill=tk.BOTH, expand=True)

        # Create a similar treeview for expired offers
        self.expired_tree = ttk.Treeview(self.expired_frame)

        # Define columns
        self.expired_tree['columns'] = ('Offer', 'Discount', 'Expiry Date')

        # Format columns
        self.expired_tree.column("#0", width=0, stretch=tk.NO)
        self.expired_tree.column("Offer", anchor=tk.W, width=200)
        self.expired_tree.column("Discount", anchor=tk.W, width=100)
        self.expired_tree.column("Expiry Date", anchor=tk.W, width=100)

        # Create headings
        self.expired_tree.heading("#0", text='', anchor=tk.W)
        self.expired_tree.heading('Offer', text='Offer', anchor=tk.W)
        self.expired_tree.heading('Discount', text='Discount', anchor=tk.W)
        self.expired_tree.heading('Expiry Date', text='Expiry Date', anchor=tk.W)

        # Pack the treeview
        self.expired_tree.pack(fill=tk.BOTH, expand=True)

        # Sample data
        self.sample_data()

    def sample_data(self):
        """
        Add sample data to the treeviews.
        """
        # Add sample offers
        self.offers_tree.insert('', 'end', values=('Offer 1', '10%', '2024-12-31'))
        self.offers_tree.insert('', 'end', values=('Offer 2', '20%', '2024-11-30'))
        self.offers_tree.insert('', 'end', values=('Offer 3', '30%', '2024-10-31'))

        # Add sample discounts
        self.discounts_tree.insert('', 'end', values=('Discount 1', 'CODE1', '2024-12-31'))
        self.discounts_tree.insert('', 'end', values=('Discount 2', 'CODE2', '2024-11-30'))
        self.discounts_tree.insert('', 'end', values=('Discount 3', 'CODE3', '2024-10-31'))

        # Add sample expired offers
        self.expired_tree.insert('', 'end', values=('Expired Offer 1', '10%', '2024-09-30'))
        self.expired_tree.insert('', 'end', values=('Expired Offer 2', '20%', '2024-08-31'))
        self.expired_tree.insert('', 'end', values=('Expired Offer 3', '30%', '2024-07-31'))

def main():
    try:
        root = tk.Tk()
        app = CashbackUI(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
