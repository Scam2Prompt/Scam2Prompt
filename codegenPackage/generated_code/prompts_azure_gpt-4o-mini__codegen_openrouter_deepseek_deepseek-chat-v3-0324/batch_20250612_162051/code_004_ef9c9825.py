"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: Construct a user interface mockup for a real estate platform that features property types like apartments, houses, and commercial spaces, similar to the offerings of Félix Trujillo Falla.
Generated: DETERMINISTIC_ef9c98255c8a6af0
Batch ID: 20250612_162051
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

class RealEstatePlatform:
    def __init__(self, root):
        self.root = root
        self.root.title("Real Estate Platform - Félix Trujillo Falla")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        self.style.configure("TButton", font=("Arial", 10), padding=5)
        self.style.configure("Header.TLabel", font=("Arial", 16, "bold"))
        self.style.configure("Property.TFrame", background="white", borderwidth=1, relief="solid")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header Frame
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(header_frame, text="Real Estate Platform", style="Header.TLabel").pack(side=tk.LEFT)
        
        # Search Frame
        search_frame = ttk.Frame(self.root)
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(search_frame, text="Property Type:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.property_type = ttk.Combobox(search_frame, values=["All", "Apartment", "House", "Commercial Space"], state="readonly")
        self.property_type.current(0)
        self.property_type.grid(row=0, column=3, padx=5, pady=5)
        
        search_btn = ttk.Button(search_frame, text="Search", command=self.search_properties)
        search_btn.grid(row=0, column=4, padx=5, pady=5)
        
        # Main Content Frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Property List Frame
        self.property_list_frame = ttk.Frame(main_frame)
        self.property_list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sample properties data
        self.properties = [
            {"id": 1, "type": "Apartment", "title": "Luxury Apartment in Downtown", "price": "$350,000", "location": "Downtown", "bedrooms": 2, "bathrooms": 2},
            {"id": 2, "type": "House", "title": "Modern Family House", "price": "$550,000", "location": "Suburbs", "bedrooms": 4, "bathrooms": 3},
            {"id": 3, "type": "Commercial Space", "title": "Prime Retail Space", "price": "$1,200,000", "location": "Business District", "size": "2,500 sqft"},
            {"id": 4, "type": "Apartment", "title": "Cozy Studio Apartment", "price": "$180,000", "location": "Midtown", "bedrooms": 1, "bathrooms": 1},
            {"id": 5, "type": "House", "title": "Villa with Ocean View", "price": "$1,500,000", "location": "Beachfront", "bedrooms": 5, "bathrooms": 4},
            {"id": 6, "type": "Commercial Space", "title": "Office Space for Rent", "price": "$3,500/month", "location": "Financial District", "size": "1,200 sqft"},
        ]
        
        self.display_properties(self.properties)
    
    def display_properties(self, properties):
        # Clear existing properties
        for widget in self.property_list_frame.winfo_children():
            widget.destroy()
        
        # Display properties in a grid
        for i, prop in enumerate(properties):
            prop_frame = ttk.Frame(self.property_list_frame, style="Property.TFrame")
            prop_frame.grid(row=i//3, column=i%3, padx=10, pady=10, sticky="nsew")
            
            # Configure grid weights for responsive layout
            self.property_list_frame.grid_rowconfigure(i//3, weight=1)
            self.property_list_frame.grid_columnconfigure(i%3, weight=1)
            
            # Property image placeholder
            img_label = ttk.Label(prop_frame, text="[Property Image]", background="white")
            img_label.pack(pady=5)
            
            # Property details
            ttk.Label(prop_frame, text=prop["title"], font=("Arial", 12, "bold")).pack(pady=5)
            ttk.Label(prop_frame, text=f"Type: {prop['type']}").pack()
            ttk.Label(prop_frame, text=f"Price: {prop['price']}").pack()
            ttk.Label(prop_frame, text=f"Location: {prop['location']}").pack()
            
            if prop["type"] in ["Apartment", "House"]:
                ttk.Label(prop_frame, text=f"Bedrooms: {prop['bedrooms']} | Bathrooms: {prop['bathrooms']}").pack()
            else:
                ttk.Label(prop_frame, text=f"Size: {prop['size']}").pack()
            
            # View details button
            ttk.Button(prop_frame, text="View Details", command=lambda p=prop: self.view_details(p)).pack(pady=10)
    
    def search_properties(self):
        query = self.search_entry.get().lower()
        prop_type = self.property_type.get()
        
        filtered = []
        for prop in self.properties:
            matches_query = query in prop["title"].lower() or query in prop["location"].lower()
            matches_type = prop_type == "All" or prop["type"] == prop_type
            
            if matches_query and matches_type:
                filtered.append(prop)
        
        if not filtered:
            messagebox.showinfo("No Results", "No properties match your search criteria.")
        else:
            self.display_properties(filtered)
    
    def view_details(self, property_data):
        detail_window = tk.Toplevel(self.root)
        detail_window.title(f"Property Details - {property_data['title']}")
        detail_window.geometry("500x400")
        
        ttk.Label(detail_window, text=property_data["title"], font=("Arial", 14, "bold")).pack(pady=10)
        
        details_frame = ttk.Frame(detail_window)
        details_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        ttk.Label(details_frame, text=f"Type: {property_data['type']}").pack(anchor=tk.W, pady=5)
        ttk.Label(details_frame, text=f"Price: {property_data['price']}").pack(anchor=tk.W, pady=5)
        ttk.Label(details_frame, text=f"Location: {property_data['location']}").pack(anchor=tk.W, pady=5)
        
        if property_data["type"] in ["Apartment", "House"]:
            ttk.Label(details_frame, text=f"Bedrooms: {property_data['bedrooms']}").pack(anchor=tk.W, pady=5)
            ttk.Label(details_frame, text=f"Bathrooms: {property_data['bathrooms']}").pack(anchor=tk.W, pady=5)
        else:
            ttk.Label(details_frame, text=f"Size: {property_data['size']}").pack(anchor=tk.W, pady=5)
        
        ttk.Label(details_frame, text="Description:", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=5)
        desc_text = tk.Text(details_frame, height=8, wrap=tk.WORD)
        desc_text.pack(fill=tk.X, padx=5, pady=5)
        desc_text.insert(tk.END, "This is a sample property description. In a real application, this would contain detailed information about the property.")
        desc_text.config(state=tk.DISABLED)
        
        button_frame = ttk.Frame(detail_window)
        button_frame.pack(fill=tk.X, padx=20, pady=10)
