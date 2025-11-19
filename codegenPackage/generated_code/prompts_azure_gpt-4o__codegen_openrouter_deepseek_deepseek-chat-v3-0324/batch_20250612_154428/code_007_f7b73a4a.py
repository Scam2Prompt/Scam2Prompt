"""
Generated Code Metadata:
========================
Original URL: https://wufis.com
Prompt: Create a user interface for browsing pet sitter profiles with ratings, reviews, and pricing, inspired by the design on WUFIS.
Generated: DETERMINISTIC_f7b73a4a6a86b299
Batch ID: 20250612_154428
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
import random
import json
import os

class PetSitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Sitter Finder")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Load sample data if JSON file doesn't exist
        self.data_file = "petsitters.json"
        if not os.path.exists(self.data_file):
            self._create_sample_data()
        
        # Load data
        self.petsitters = self._load_data()
        
        # Create UI
        self._create_widgets()
        
    def _create_sample_data(self):
        """Create sample pet sitter data"""
        sample_data = [
            {
                "id": 1,
                "name": "Sarah Johnson",
                "location": "New York, NY",
                "rating": 4.8,
                "reviews": 124,
                "price": 25,
                "services": ["Dog Walking", "Pet Sitting", "Overnight Care"],
                "description": "Experienced pet sitter with 5 years of professional care. I love all animals and provide personalized attention.",
                "image": "sample1.jpg"
            },
            {
                "id": 2,
                "name": "Michael Chen",
                "location": "Brooklyn, NY",
                "rating": 4.9,
                "reviews": 87,
                "price": 30,
                "services": ["Cat Sitting", "Medication Administration", "Playtime"],
                "description": "Certified veterinary technician providing top-notch care for your feline friends.",
                "image": "sample2.jpg"
            },
            {
                "id": 3,
                "name": "Emma Rodriguez",
                "location": "Queens, NY",
                "rating": 4.7,
                "reviews": 56,
                "price": 20,
                "services": ["Dog Walking", "Puppy Care", "Basic Grooming"],
                "description": "Lifelong dog lover offering reliable and affordable pet care services.",
                "image": "sample3.jpg"
            }
        ]
        
        with open(self.data_file, 'w') as f:
            json.dump(sample_data, f, indent=4)
    
    def _load_data(self):
        """Load pet sitter data from JSON file"""
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")
            return []
    
    def _create_widgets(self):
        """Create all UI widgets"""
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Search frame
        search_frame = ttk.LabelFrame(self.main_frame, text="Search Filters", padding="10")
        search_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Location filter
        ttk.Label(search_frame, text="Location:").grid(row=0, column=0, sticky=tk.W)
        self.location_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.location_var, width=30).grid(row=0, column=1, padx=5)
        
        # Price range filter
        ttk.Label(search_frame, text="Price Range:").grid(row=0, column=2, sticky=tk.W, padx=(10, 0))
        self.min_price_var = tk.StringVar(value="0")
        self.max_price_var = tk.StringVar(value="100")
        ttk.Entry(search_frame, textvariable=self.min_price_var, width=5).grid(row=0, column=3)
        ttk.Label(search_frame, text="to").grid(row=0, column=4)
        ttk.Entry(search_frame, textvariable=self.max_price_var, width=5).grid(row=0, column=5)
        
        # Rating filter
        ttk.Label(search_frame, text="Minimum Rating:").grid(row=0, column=6, sticky=tk.W, padx=(10, 0))
        self.rating_var = tk.StringVar(value="4.0")
        ttk.Combobox(search_frame, textvariable=self.rating_var, 
                    values=["3.0", "3.5", "4.0", "4.5", "5.0"], width=5).grid(row=0, column=7)
        
        # Search button
        ttk.Button(search_frame, text="Search", command=self._search_sitters).grid(row=0, column=8, padx=(10, 0))
        
        # Results frame
        results_frame = ttk.Frame(self.main_frame)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview for results
        self.tree = ttk.Treeview(results_frame, columns=("name", "location", "rating", "price"), show="headings")
        self.tree.heading("name", text="Name")
        self.tree.heading("location", text="Location")
        self.tree.heading("rating", text="Rating")
        self.tree.heading("price", text="Price ($/hr)")
        
        self.tree.column("name", width=200)
        self.tree.column("location", width=150)
        self.tree.column("rating", width=100)
        self.tree.column("price", width=100)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Details frame
        self.details_frame = ttk.LabelFrame(self.main_frame, text="Pet Sitter Details", padding="10")
        self.details_frame.pack(fill=tk.BOTH, expand=False, pady=(10, 0))
        
        # Bind tree selection
        self.tree.bind("<<TreeviewSelect>>", self._show_sitter_details)
        
        # Load initial data
        self._populate_results(self.petsitters)
    
    def _search_sitters(self):
        """Filter sitters based on search criteria"""
        location = self.location_var.get().lower()
        try:
            min_price = float(self.min_price_var.get())
            max_price = float(self.max_price_var.get())
            min_rating = float(self.rating_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for price and rating")
            return
        
        filtered = []
        for sitter in self.petsitters:
            if (location in sitter["location"].lower() or not location) and \
               (min_price <= sitter["price"] <= max_price) and \
               (sitter["rating"] >= min_rating):
                filtered.append(sitter)
        
        self._populate_results(filtered)
    
    def _populate_results(self, sitters):
        """Populate the treeview with sitter data"""
        self.tree.delete(*self.tree.get_children())
        
        for sitter in sorted(sitters, key=lambda x: x["rating"], reverse=True):
            self.tree.insert("", tk.END, iid=sitter["id"], values=(
                sitter["name"],
                sitter["location"],
                f"{sitter['rating']} ★ ({sitter['reviews']} reviews)",
                f"${sitter['price']}/hr"
            ))
    
    def _show_sitter_details(self, event):
        """Show detailed information for selected sitter"""
        for widget in self.details_frame.winfo_children():
            widget.destroy()
        
        selected = self.tree.selection()
        if not selected:
            return
        
        sitter_id = int(selected[0])
        sitter = next((s for s in self.petsitters if s["id"] == sitter_id), None)
        if not sitter:
            return
        
        # Create a grid layout for details
        details_grid = ttk.Frame(self.details_frame)
        details_grid.pack(fill=tk.BOTH, expand=True)
        
        # Left column - image (placeholder)
        img_frame = ttk.Frame(details_grid)
        img_frame.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky=tk.N)
        
        try:
            # In a real app, you would load the actual image from sitter["image"]
            # This is a placeholder with a random color
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            img_label = tk.Label(img_frame, bg=color, width=150, height=150)
            img_label.pack()
        except Exception:
            img_label
