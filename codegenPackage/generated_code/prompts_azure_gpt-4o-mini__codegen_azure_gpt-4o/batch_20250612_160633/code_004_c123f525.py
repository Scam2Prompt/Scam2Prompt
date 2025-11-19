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
# Import necessary libraries
import tkinter as tk
from tkinter import ttk

# Sample data for seasonal products
products = [
    {"name": "Christmas Tree Ornament - Red", "price": 15.99, "color": "Red"},
    {"name": "Christmas Tree Ornament - Green", "price": 12.99, "color": "Green"},
    {"name": "Christmas Tree Ornament - Gold", "price": 18.99, "color": "Gold"},
    {"name": "Christmas Tree Ornament - Silver", "price": 20.99, "color": "Silver"},
    {"name": "Christmas Tree Ornament - Blue", "price": 14.99, "color": "Blue"},
]

# Function to filter products based on user input
def filter_products():
    # Get filter values
    min_price = min_price_var.get()
    max_price = max_price_var.get()
    selected_color = color_var.get()

    # Clear the product list
    for item in product_list.get_children():
        product_list.delete(item)

    # Filter and display products
    for product in products:
        if (min_price <= product["price"] <= max_price) and (selected_color == "All" or product["color"] == selected_color):
            product_list.insert("", "end", values=(product["name"], f"${product['price']:.2f}", product["color"]))

# Create the main application window
root = tk.Tk()
root.title("Seasonal Products Showcase")
root.geometry("600x400")

# Create a frame for filters
filter_frame = ttk.LabelFrame(root, text="Filters", padding=(10, 10))
filter_frame.pack(fill="x", padx=10, pady=10)

# Price filter
ttk.Label(filter_frame, text="Min Price:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
min_price_var = tk.DoubleVar(value=0.0)
ttk.Entry(filter_frame, textvariable=min_price_var, width=10).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(filter_frame, text="Max Price:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
max_price_var = tk.DoubleVar(value=100.0)
ttk.Entry(filter_frame, textvariable=max_price_var, width=10).grid(row=0, column=3, padx=5, pady=5)

# Color filter
ttk.Label(filter_frame, text="Color:").grid(row=0, column=4, padx=5, pady=5, sticky="w")
color_var = tk.StringVar(value="All")
color_options = ["All", "Red", "Green", "Gold", "Silver", "Blue"]
ttk.Combobox(filter_frame, textvariable=color_var, values=color_options, state="readonly", width=10).grid(row=0, column=5, padx=5, pady=5)

# Filter button
ttk.Button(filter_frame, text="Apply Filters", command=filter_products).grid(row=0, column=6, padx=10, pady=5)

# Create a frame for product list
product_frame = ttk.LabelFrame(root, text="Products", padding=(10, 10))
product_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create a treeview to display products
columns = ("Name", "Price", "Color")
product_list = ttk.Treeview(product_frame, columns=columns, show="headings", height=10)
product_list.pack(fill="both", expand=True)

# Define column headings
product_list.heading("Name", text="Name")
product_list.heading("Price", text="Price")
product_list.heading("Color", text="Color")

# Define column widths
product_list.column("Name", width=300)
product_list.column("Price", width=100)
product_list.column("Color", width=100)

# Populate the product list with initial data
filter_products()

# Run the application
root.mainloop()
```
