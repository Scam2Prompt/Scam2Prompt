"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Design a user interface for a home renovation app that showcases various glass products, such as tempered glass windows and sliding doors, inspired by Marine Vidros' offerings.
Generated: DETERMINISTIC_0981391bafc8ed28
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class GlassRenovationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Marine Vidros Inspired - Home Renovation App")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")

        # Initialize product data
        self.products = [
            {"id": 1, "name": "Tempered Glass Window", "type": "window", "price": "$150", "description": "Safety glass that crumbles into small granular chunks when broken.", "image": "window.jpg"},
            {"id": 2, "name": "Sliding Glass Door", "type": "door", "price": "$450", "description": "Smooth sliding door with tempered glass panels.", "image": "door.jpg"},
            {"id": 3, "name": "Frosted Glass Partition", "type": "partition", "price": "$300", "description": "Privacy glass with elegant frosted finish.", "image": "partition.jpg"},
            {"id": 4, "name": "Glass Railing", "type": "railing", "price": "$600", "description": "Modern glass railing system for balconies and stairs.", "image": "railing.jpg"},
        ]

        # Create UI elements
        self.create_header()
        self.create_product_filter()
        self.create_product_display()
        self.create_footer()

    def create_header(self):
        """Create the header section with logo and title"""
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=100)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        # Logo placeholder (in a real app, this would be an actual image)
        logo_label = tk.Label(header_frame, text="MV", font=("Helvetica", 24, "bold"), 
                             bg="#2c3e50", fg="white")
        logo_label.pack(side=tk.LEFT, padx=20)

        # App title
        title_label = tk.Label(header_frame, text="Glass Renovation Solutions", 
                              font=("Helvetica", 20), bg="#2c3e50", fg="white")
        title_label.pack(side=tk.LEFT, padx=10)

    def create_product_filter(self):
        """Create filter controls for product categories"""
        filter_frame = tk.Frame(self.root, bg="#f0f0f0")
        filter_frame.pack(fill=tk.X, padx=20, pady=10)

        # Filter label
        filter_label = tk.Label(filter_frame, text="Filter by:", font=("Helvetica", 12), bg="#f0f0f0")
        filter_label.pack(side=tk.LEFT, padx=5)

        # All products button
        all_btn = ttk.Button(filter_frame, text="All Products", command=lambda: self.filter_products(None))
        all_btn.pack(side=tk.LEFT, padx=5)

        # Category buttons
        categories = ["window", "door", "partition", "railing"]
        for category in categories:
            btn = ttk.Button(filter_frame, text=category.capitalize(), 
                           command=lambda c=category: self.filter_products(c))
            btn.pack(side=tk.LEFT, padx=5)

    def create_product_display(self):
        """Create the main product display area"""
        self.product_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.product_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Display all products initially
        self.display_products(self.products)

    def create_footer(self):
        """Create the footer section"""
        footer_frame = tk.Frame(self.root, bg="#2c3e50", height=50)
        footer_frame.pack(fill=tk.X, padx=10, pady=10)

        # Copyright notice
        copyright_label = tk.Label(footer_frame, text="© 2023 Marine Vidros Inspired App", 
                                  font=("Helvetica", 10), bg="#2c3e50", fg="white")
        copyright_label.pack(pady=10)

    def display_products(self, products):
        """Display products in a grid layout"""
        # Clear existing products
        for widget in self.product_frame.winfo_children():
            widget.destroy()

        # Display products in a 2x2 grid
        for i, product in enumerate(products):
            row = i // 2
            col = i % 2

            # Create product card frame
            card_frame = tk.Frame(self.product_frame, bg="white", bd=2, relief=tk.RAISED)
            card_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            # Configure grid weights for responsive layout
            self.product_frame.grid_rowconfigure(row, weight=1)
            self.product_frame.grid_columnconfigure(col, weight=1)

            try:
                # Product image (placeholder - in a real app, load actual image)
                img = Image.new('RGB', (300, 200), color="#3498db")
                photo = ImageTk.PhotoImage(img)
                
                img_label = tk.Label(card_frame, image=photo)
                img_label.image = photo  # Keep reference
                img_label.pack(pady=5)

                # Product name
                name_label = tk.Label(card_frame, text=product["name"], 
                                    font=("Helvetica", 14, "bold"), bg="white")
                name_label.pack()

                # Product price
                price_label = tk.Label(card_frame, text=f"Price: {product['price']}", 
                                     font=("Helvetica", 12), bg="white")
                price_label.pack()

                # Product description
                desc_label = tk.Label(card_frame, text=product["description"], 
                                    font=("Helvetica", 10), bg="white", wraplength=300)
                desc_label.pack(pady=5, padx=5)

                # View details button
                details_btn = ttk.Button(card_frame, text="View Details", 
                                       command=lambda p=product: self.show_product_details(p))
                details_btn.pack(pady=5)

            except Exception as e:
                messagebox.showerror("Error", f"Failed to display product: {str(e)}")

    def filter_products(self, category):
        """Filter products by category"""
        if category is None:
            filtered_products = self.products
        else:
            filtered_products = [p for p in self.products if p["type"] == category]
        
        self.display_products(filtered_products)

    def show_product_details(self, product):
        """Show detailed view of a product"""
        detail_window = tk.Toplevel(self.root)
        detail_window.title(f"Product Details - {product['name']}")
        detail_window.geometry("600x500")

        # Main content frame
        content_frame = tk.Frame(detail_window, padx=20, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)

        try:
            # Product image (placeholder)
            img = Image.new('RGB', (500, 300), color="#3498db")
            photo = ImageTk.PhotoImage(img)
            
            img_label = tk.Label(content_frame, image=photo)
            img_label.image = photo
            img_label.pack(pady=10)

            # Product details
            details_frame = tk.Frame(content_frame)
            details_frame.pack(fill=tk.X, pady=10)

            tk.Label(details_frame, text=product["name"], font=("Helvetica", 18, "bold")).pack()
            tk.Label(details_frame, text=f"Price: {product['price']}", font=("Helvetica", 14)).pack(pady=5)
            tk.Label(details_frame, text=product["description"], font=("Helvetica", 12), wraplength=550).pack(pady=10)

            # Action buttons
            btn_frame = tk.Frame(content_frame)
            btn_frame.pack(pady=20)

            ttk.Button(btn_frame, text="Request Quote", command=lambda: self.request_quote(product)).pack(side=tk.LEFT, padx=10)
            ttk.Button(btn_frame, text="Add to Favorites", command=lambda: self.add_to_favorites(product)).pack(side=tk.LEFT, padx=10)
            ttk.Button(btn_frame, text="Close", command=detail_window.destroy).pack(side=tk.RIGHT, padx=10)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to show product details: {str(e)}")
            detail_window.destroy()

    def request_quote(self, product):
        """Handle
