"""
Generated Code Metadata:
========================
Original URL: https://azimutfloor.com
Prompt: Illustrate how to implement a user interface that allows users to explore the unique features of Azimut flooring collections like Antico Filo and Magellano.
Generated: DETERMINISTIC_24348eec6cc60081
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Azimut Flooring Explorer UI

```python
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import json

class AzimutFlooringExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Azimut Flooring Collections Explorer")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        
        # Load collections data
        self.load_collections_data()
        
        # Create UI elements
        self.create_main_frame()
        self.create_navigation_panel()
        self.create_content_area()
        self.create_feature_display()
        
        # Show initial collection
        self.show_collection("Antico Filo")
    
    def load_collections_data(self):
        """Load collections data from JSON file or use default data if not found"""
        try:
            with open('collections_data.json', 'r') as f:
                self.collections = json.load(f)
        except FileNotFoundError:
            # Default data if file not found
            self.collections = {
                "Antico Filo": {
                    "description": "Handcrafted luxury with a vintage appeal.",
                    "features": [
                        "Hand-scraped surface texture",
                        "Multi-width plank design",
                        "Authentic wood grain patterns",
                        "Premium European oak"
                    ],
                    "image_paths": ["antico_filo_1.jpg", "antico_filo_2.jpg"]
                },
                "Magellano": {
                    "description": "Modern elegance with innovative technology.",
                    "features": [
                        "Waterproof construction",
                        "High-definition printing technology",
                        "Enhanced scratch resistance",
                        "Easy click-lock installation"
                    ],
                    "image_paths": ["magellano_1.jpg", "magellano_2.jpg"]
                }
            }
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid collections data file")
            self.root.destroy()
    
    def create_main_frame(self):
        """Create the main container frame"""
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def create_navigation_panel(self):
        """Create the left navigation panel"""
        nav_frame = ttk.LabelFrame(self.main_frame, text="Collections", padding=10)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        for collection in self.collections.keys():
            btn = ttk.Button(
                nav_frame, 
                text=collection, 
                command=lambda c=collection: self.show_collection(c),
                width=20
            )
            btn.pack(pady=5, fill=tk.X)
    
    def create_content_area(self):
        """Create the main content area"""
        content_frame = ttk.Frame(self.main_frame)
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Collection description
        self.desc_frame = ttk.LabelFrame(content_frame, text="Collection Description", padding=10)
        self.desc_frame.pack(fill=tk.X, pady=5)
        
        self.desc_text = tk.Text(
            self.desc_frame, 
            height=4, 
            wrap=tk.WORD, 
            font=('Arial', 10)
        )
        self.desc_text.pack(fill=tk.X)
        self.desc_text.config(state=tk.DISABLED)
        
        # Image gallery
        self.gallery_frame = ttk.LabelFrame(content_frame, text="Gallery", padding=10)
        self.gallery_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.image_canvas = tk.Canvas(self.gallery_frame)
        self.scrollbar = ttk.Scrollbar(
            self.gallery_frame, 
            orient=tk.HORIZONTAL, 
            command=self.image_canvas.xview
        )
        self.image_canvas.configure(xscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.image_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.image_frame = ttk.Frame(self.image_canvas)
        self.image_canvas.create_window((0, 0), window=self.image_frame, anchor=tk.NW)
        
        self.image_frame.bind(
            "<Configure>",
            lambda e: self.image_canvas.configure(scrollregion=self.image_canvas.bbox("all"))
        )
    
    def create_feature_display(self):
        """Create the features display area"""
        feature_frame = ttk.LabelFrame(self.main_frame, text="Key Features", padding=10)
        feature_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=5, pady=5)
        
        self.feature_text = tk.Text(
            feature_frame, 
            height=6, 
            wrap=tk.WORD, 
            font=('Arial', 10)
        )
        self.feature_text.pack(fill=tk.BOTH, expand=True)
        self.feature_text.config(state=tk.DISABLED)
    
    def show_collection(self, collection_name):
        """Display the selected collection's details"""
        collection = self.collections.get(collection_name)
        if not collection:
            messagebox.showerror("Error", f"Collection '{collection_name}' not found")
            return
        
        # Update description
        self.desc_text.config(state=tk.NORMAL)
        self.desc_text.delete(1.0, tk.END)
        self.desc_text.insert(tk.END, collection["description"])
        self.desc_text.config(state=tk.DISABLED)
        
        # Update features
        self.feature_text.config(state=tk.NORMAL)
        self.feature_text.delete(1.0, tk.END)
        for feature in collection["features"]:
            self.feature_text.insert(tk.END, f"• {feature}\n")
        self.feature_text.config(state=tk.DISABLED)
        
        # Update images
        for widget in self.image_frame.winfo_children():
            widget.destroy()
        
        row = 0
        col = 0
        max_width = 300
        
        for img_path in collection["image_paths"]:
            try:
                img = Image.open(img_path)
                img.thumbnail((max_width, max_width))
                photo = ImageTk.PhotoImage(img)
                
                label = ttk.Label(self.image_frame, image=photo)
                label.image = photo  # Keep reference
                label.grid(row=row, column=col, padx=5, pady=5)
                
                col += 1
                if col > 2:  # 3 images per row
                    col = 0
                    row += 1
            except FileNotFoundError:
                placeholder = ttk.Label(
                    self.image_frame, 
                    text=f"Image not found: {img_path}", 
                    foreground="red"
                )
                placeholder.grid(row=row, column=col, padx=5, pady=5)
                col += 1
                if col > 2:
                    col = 0
                    row += 1

def main():
    root = tk.Tk()
    app = AzimutFlooringExplorer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```
