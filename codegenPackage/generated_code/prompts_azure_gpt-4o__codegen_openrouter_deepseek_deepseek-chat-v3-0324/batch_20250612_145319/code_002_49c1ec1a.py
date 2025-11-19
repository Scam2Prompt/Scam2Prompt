"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: Generate code to simulate a user interface for selecting bold and timeless home decor items, incorporating Zirciulit Design Firm's philosophy of making excellent design accessible.
Generated: DETERMINISTIC_49c1ec1a95e776e9
Batch ID: 20250612_145319
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

class ZirciulitHomeDecorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zirciulit Design Firm - Home Decor Selector")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        # Design philosophy
        self.philosophy = (
            "Zirciulit Design Firm believes excellent design should be accessible to all.\n"
            "Our bold, timeless home decor items combine quality craftsmanship\n"
            "with affordable luxury to elevate everyday living."
        )

        # Sample decor items
        self.decor_items = [
            {"name": "Minimalist Ceramic Vase", "style": "Modern", "price": "$89", "bold": True, "timeless": True},
            {"name": "Industrial Wooden Shelf", "style": "Industrial", "price": "$149", "bold": True, "timeless": True},
            {"name": "Mid-Century Armchair", "style": "Mid-Century", "price": "$299", "bold": False, "timeless": True},
            {"name": "Abstract Wall Art", "style": "Contemporary", "price": "$129", "bold": True, "timeless": False},
            {"name": "Classic Persian Rug", "style": "Traditional", "price": "$399", "bold": False, "timeless": True},
            {"name": "Geometric Coffee Table", "style": "Modern", "price": "$249", "bold": True, "timeless": True},
        ]

        self.create_widgets()
        self.load_images()

    def load_images(self):
        """Load placeholder images for decor items"""
        self.item_images = []
        try:
            for i in range(len(self.decor_items)):
                # In a real app, you would load actual product images
                # This is a placeholder using a solid color
                img = Image.new('RGB', (150, 150), color=(200, 200, 200))
                photo = ImageTk.PhotoImage(img)
                self.item_images.append(photo)
        except Exception as e:
            messagebox.showerror("Image Error", f"Could not load images: {str(e)}")

    def create_widgets(self):
        """Create all UI components"""
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(
            header_frame,
            text="Zirciulit Design Firm",
            font=("Helvetica", 20, "bold"),
            fg="white",
            bg="#2c3e50"
        )
        title_label.pack(pady=20)

        # Philosophy label
        philosophy_label = tk.Label(
            self.root,
            text=self.philosophy,
            font=("Helvetica", 10),
            bg="#f5f5f5",
            justify=tk.CENTER
        )
        philosophy_label.pack(pady=10)

        # Filter controls
        filter_frame = tk.Frame(self.root, bg="#f5f5f5")
        filter_frame.pack(pady=10)

        bold_var = tk.BooleanVar()
        timeless_var = tk.BooleanVar()

        bold_check = ttk.Checkbutton(
            filter_frame,
            text="Bold Designs Only",
            variable=bold_var,
            command=lambda: self.filter_items(bold_var.get(), timeless_var.get())
        )
        bold_check.pack(side=tk.LEFT, padx=10)

        timeless_check = ttk.Checkbutton(
            filter_frame,
            text="Timeless Designs Only",
            variable=timeless_var,
            command=lambda: self.filter_items(bold_var.get(), timeless_var.get())
        )
        timeless_check.pack(side=tk.LEFT, padx=10)

        # Items display
        self.items_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.items_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Create initial items display
        self.display_items(self.decor_items)

    def display_items(self, items):
        """Display decor items in a grid layout"""
        # Clear existing items
        for widget in self.items_frame.winfo_children():
            widget.destroy()

        # Display new items
        for i, item in enumerate(items):
            item_frame = tk.Frame(
                self.items_frame,
                bg="white",
                bd=2,
                relief=tk.RAISED,
                padx=10,
                pady=10
            )
            item_frame.grid(
                row=i // 3,
                column=i % 3,
                padx=10,
                pady=10,
                sticky="nsew"
            )

            # Configure grid weights for responsive layout
            self.items_frame.grid_rowconfigure(i // 3, weight=1)
            self.items_frame.grid_columnconfigure(i % 3, weight=1)

            # Item image
            if i < len(self.item_images):
                img_label = tk.Label(item_frame, image=self.item_images[i], bg="white")
                img_label.pack()

            # Item details
            name_label = tk.Label(
                item_frame,
                text=item["name"],
                font=("Helvetica", 12, "bold"),
                bg="white"
            )
            name_label.pack()

            style_label = tk.Label(
                item_frame,
                text=f"Style: {item['style']}",
                font=("Helvetica", 10),
                bg="white"
            )
            style_label.pack()

            price_label = tk.Label(
                item_frame,
                text=f"Price: {item['price']}",
                font=("Helvetica", 10),
                bg="white"
            )
            price_label.pack()

            # Add to cart button
            cart_button = ttk.Button(
                item_frame,
                text="Add to Cart",
                command=lambda i=item: self.add_to_cart(i)
            )
            cart_button.pack(pady=5)

    def filter_items(self, bold_only, timeless_only):
        """Filter items based on selected criteria"""
        filtered_items = []
        for item in self.decor_items:
            matches = True
            if bold_only and not item["bold"]:
                matches = False
            if timeless_only and not item["timeless"]:
                matches = False
            if matches:
                filtered_items.append(item)
        
        self.display_items(filtered_items)

    def add_to_cart(self, item):
        """Handle adding item to cart"""
        messagebox.showinfo(
            "Added to Cart",
            f"Added {item['name']} to your cart!"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = ZirciulitHomeDecorApp(root)
    root.mainloop()
```
