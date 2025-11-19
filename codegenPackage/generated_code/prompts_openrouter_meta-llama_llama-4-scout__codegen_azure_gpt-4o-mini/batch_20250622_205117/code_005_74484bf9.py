"""
Generated Code Metadata:
========================
Original URL: https://buildonbeam-7h0.pages.dev
Prompt: Design a user interface for the Beam Market, BeamOS's native marketplace.
Generated: DETERMINISTIC_74484bf9239fb7f4
Batch ID: 20250622_205117
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

class BeamMarketApp:
    def __init__(self, root):
        """Initialize the main application window."""
        self.root = root
        self.root.title("Beam Market")
        self.root.geometry("600x400")

        # Create a frame for the marketplace
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title label
        self.title_label = ttk.Label(self.frame, text="Welcome to Beam Market", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Product list
        self.product_list = ttk.Treeview(self.frame, columns=("Name", "Price"), show='headings')
        self.product_list.heading("Name", text="Product Name")
        self.product_list.heading("Price", text="Price")
        self.product_list.pack(fill=tk.BOTH, expand=True)

        # Sample products
        self.load_products()

        # Buy button
        self.buy_button = ttk.Button(self.frame, text="Buy Selected Product", command=self.buy_product)
        self.buy_button.pack(pady=10)

    def load_products(self):
        """Load sample products into the product list."""
        products = [
            ("Beam Widget", "$10.00"),
            ("Beam Gadget", "$15.00"),
            ("Beam Tool", "$20.00"),
        ]
        for product in products:
            self.product_list.insert("", tk.END, values=product)

    def buy_product(self):
        """Handle the purchase of the selected product."""
        selected_item = self.product_list.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a product to buy.")
            return

        product_name = self.product_list.item(selected_item, 'values')[0]
        messagebox.showinfo("Purchase Successful", f"You have purchased {product_name}!")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = BeamMarketApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Application Error", f"An error occurred: {str(e)}")
```
