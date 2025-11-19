"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Design a user interface component that showcases seasonal products like enfeites de árvore de Natal, as featured on the Camicado website, with options to filter by price and color.
Generated: DETERMINISTIC_c123f52577c373b2
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# seasonal_products.py

import tkinter as tk
from tkinter import ttk

class SeasonalProduct:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

class SeasonalProductUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Seasonal Products")
        self.products = [
            SeasonalProduct("Enfeite 1", 10.99, "Red"),
            SeasonalProduct("Enfeite 2", 9.99, "Green"),
            SeasonalProduct("Enfeite 3", 12.99, "Blue"),
            SeasonalProduct("Enfeite 4", 8.99, "Red"),
            SeasonalProduct("Enfeite 5", 11.99, "Green"),
        ]

        # Create filter frame
        self.filter_frame = ttk.Frame(self.root)
        self.filter_frame.pack(fill="x")

        # Create price filter
        self.price_label = ttk.Label(self.filter_frame, text="Price:")
        self.price_label.pack(side="left")
        self.price_var = tk.StringVar()
        self.price_var.set("All")
        self.price_option = ttk.Combobox(self.filter_frame, textvariable=self.price_var)
        self.price_option['values'] = ['All', 'Under 10', '10-20', 'Over 20']
        self.price_option.pack(side="left")

        # Create color filter
        self.color_label = ttk.Label(self.filter_frame, text="Color:")
        self.color_label.pack(side="left")
        self.color_var = tk.StringVar()
        self.color_var.set("All")
        self.color_option = ttk.Combobox(self.filter_frame, textvariable=self.color_var)
        self.color_option['values'] = ['All', 'Red', 'Green', 'Blue']
        self.color_option.pack(side="left")

        # Create filter button
        self.filter_button = ttk.Button(self.filter_frame, text="Filter", command=self.filter_products)
        self.filter_button.pack(side="left")

        # Create product frame
        self.product_frame = ttk.Frame(self.root)
        self.product_frame.pack(fill="both", expand=True)

        # Display products
        self.display_products()

    def display_products(self, filtered_products=None):
        for widget in self.product_frame.winfo_children():
            widget.destroy()

        if filtered_products is None:
            products = self.products
        else:
            products = filtered_products

        for product in products:
            product_card = ttk.Frame(self.product_frame)
            product_card.pack(fill="x")

            name_label = ttk.Label(product_card, text=product.name)
            name_label.pack(side="left")

            price_label = ttk.Label(product_card, text=f"${product.price:.2f}")
            price_label.pack(side="left")

            color_label = ttk.Label(product_card, text=product.color)
            color_label.pack(side="left")

    def filter_products(self):
        price_range = self.price_var.get()
        color = self.color_var.get()

        filtered_products = self.products.copy()

        if price_range != "All":
            if price_range == "Under 10":
                filtered_products = [p for p in filtered_products if p.price < 10]
            elif price_range == "10-20":
                filtered_products = [p for p in filtered_products if 10 <= p.price <= 20]
            elif price_range == "Over 20":
                filtered_products = [p for p in filtered_products if p.price > 20]

        if color != "All":
            filtered_products = [p for p in filtered_products if p.color == color]

        self.display_products(filtered_products)

if __name__ == "__main__":
    root = tk.Tk()
    app = SeasonalProductUI(root)
    root.mainloop()
```
