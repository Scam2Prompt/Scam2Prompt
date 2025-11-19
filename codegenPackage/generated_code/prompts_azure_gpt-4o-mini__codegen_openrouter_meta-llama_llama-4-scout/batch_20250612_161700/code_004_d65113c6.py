"""
Generated Code Metadata:
========================
Original URL: https://utterlybaked.com
Prompt: Design a user interface mockup for a bakery's online ordering system that highlights special promotions, similar to what is offered on utterlybaked.com.
Generated: DETERMINISTIC_d65113c646f60118
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bakery_online_ordering_system.py

import tkinter as tk
from tkinter import ttk, messagebox

class BakeryOrderingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bakery Online Ordering System")

        # Create notebook with tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Create frames for each tab
        self.promotions_frame = tk.Frame(self.notebook)
        self.order_frame = tk.Frame(self.notebook)
        self.about_frame = tk.Frame(self.notebook)

        # Add frames to notebook
        self.notebook.add(self.promotions_frame, text="Promotions")
        self.notebook.add(self.order_frame, text="Order")
        self.notebook.add(self.about_frame, text="About")

        # Promotions tab
        self.promotions_tab()

        # Order tab
        self.order_tab()

        # About tab
        self.about_tab()

    def promotions_tab(self):
        # Create promotions label and text box
        tk.Label(self.promotions_frame, text="Special Promotions:", font=("Arial", 18)).pack(pady=10)
        self.promotions_text = tk.Text(self.promotions_frame, height=10, width=40)
        self.promotions_text.pack(pady=10)

        # Sample promotions
        promotions = [
            "Buy one dozen cupcakes, get one free!",
            "10% off all cake orders over $100",
            "Free delivery on orders over $50"
        ]

        # Insert promotions into text box
        for promotion in promotions:
            self.promotions_text.insert(tk.END, promotion + "\n")

        # Make text box read-only
        self.promotions_text.config(state="disabled")

    def order_tab(self):
        # Create order form
        tk.Label(self.order_frame, text="Place Your Order:", font=("Arial", 18)).pack(pady=10)

        # Item label and entry
        tk.Label(self.order_frame, text="Item:").grid(row=0, column=0, padx=5, pady=5)
        self.item_entry = tk.Entry(self.order_frame, width=30)
        self.item_entry.grid(row=0, column=1, padx=5, pady=5)

        # Quantity label and entry
        tk.Label(self.order_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(self.order_frame, width=30)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        # Order button
        self.order_button = tk.Button(self.order_frame, text="Place Order", command=self.place_order)
        self.order_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def about_tab(self):
        # Create about label and text box
        tk.Label(self.about_frame, text="About Us:", font=("Arial", 18)).pack(pady=10)
        self.about_text = tk.Text(self.about_frame, height=10, width=40)
        self.about_text.pack(pady=10)

        # Sample about text
        about_text = "Welcome to our bakery! We offer a wide variety of delicious treats, including cakes, cupcakes, and pastries. Our goal is to provide the best customer service and make your ordering experience as easy and enjoyable as possible."

        # Insert about text into text box
        self.about_text.insert(tk.END, about_text)

        # Make text box read-only
        self.about_text.config(state="disabled")

    def place_order(self):
        try:
            item = self.item_entry.get()
            quantity = int(self.quantity_entry.get())

            if item and quantity > 0:
                messagebox.showinfo("Order Confirmation", f"Thank you for ordering {quantity} {item}(s)!")
                self.item_entry.delete(0, tk.END)
                self.quantity_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Invalid Order", "Please enter a valid item and quantity.")
        except ValueError:
            messagebox.showerror("Invalid Quantity", "Please enter a valid quantity.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BakeryOrderingSystem(root)
    root.mainloop()
```
