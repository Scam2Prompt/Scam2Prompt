"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: How can I create a user-friendly interface for a film production service that allows users to request armourer services and uniform hires?
Generated: DETERMINISTIC_67a79d0189388edc
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Film Production Armourer and Uniform Hire Service

```python
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import json
import os

class FilmProductionServiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Film Production Service Portal")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        
        # Initialize data storage
        self.data_file = "production_requests.json"
        self.requests = self.load_requests()
        
        # Create main notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_request_tab()
        self.create_view_requests_tab()
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        
    def load_requests(self):
        """Load existing requests from JSON file or return empty list if file doesn't exist"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                messagebox.showerror("Error", f"Failed to load requests: {str(e)}")
                return []
        return []
    
    def save_requests(self):
        """Save requests to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.requests, f, indent=2)
        except IOError as e:
            messagebox.showerror("Error", f"Failed to save requests: {str(e)}")
    
    def create_request_tab(self):
        """Create the request submission tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="New Request")
        
        # Header
        header = ttk.Label(tab, text="Armourer Services & Uniform Hire Request", style='Header.TLabel')
        header.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Client Information
        client_frame = ttk.LabelFrame(tab, text="Client Information")
        client_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        ttk.Label(client_frame, text="Production Name:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        self.production_name = ttk.Entry(client_frame, width=30)
        self.production_name.grid(row=0, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(client_frame, text="Contact Person:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.contact_person = ttk.Entry(client_frame, width=30)
        self.contact_person.grid(row=1, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(client_frame, text="Email:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
        self.email = ttk.Entry(client_frame, width=30)
        self.email.grid(row=2, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(client_frame, text="Phone:").grid(row=3, column=0, sticky="e", padx=5, pady=2)
        self.phone = ttk.Entry(client_frame, width=30)
        self.phone.grid(row=3, column=1, sticky="w", padx=5, pady=2)
        
        # Service Selection
        service_frame = ttk.LabelFrame(tab, text="Service Selection")
        service_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        
        self.service_type = tk.StringVar(value="uniform")
        ttk.Radiobutton(service_frame, text="Uniform Hire", variable=self.service_type, value="uniform").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        ttk.Radiobutton(service_frame, text="Armourer Services", variable=self.service_type, value="armourer").grid(row=0, column=1, sticky="w", padx=5, pady=2)
        
        # Uniform Details
        self.uniform_frame = ttk.LabelFrame(tab, text="Uniform Details")
        self.uniform_frame.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        
        ttk.Label(self.uniform_frame, text="Uniform Type:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        self.uniform_type = ttk.Entry(self.uniform_frame, width=30)
        self.uniform_type.grid(row=0, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(self.uniform_frame, text="Quantity:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.quantity = ttk.Spinbox(self.uniform_frame, from_=1, to=1000, width=10)
        self.quantity.grid(row=1, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(self.uniform_frame, text="Size Range:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
        self.size_range = ttk.Entry(self.uniform_frame, width=30)
        self.size_range.grid(row=2, column=1, sticky="w", padx=5, pady=2)
        
        # Armourer Details
        self.armourer_frame = ttk.LabelFrame(tab, text="Armourer Services Details")
        self.armourer_frame.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        self.armourer_frame.grid_remove()  # Hide initially
        
        ttk.Label(self.armourer_frame, text="Weapon Types:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        self.weapon_types = ttk.Entry(self.armourer_frame, width=30)
        self.weapon_types.grid(row=0, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(self.armourer_frame, text="Number of Weapons:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.num_weapons = ttk.Spinbox(self.armourer_frame, from_=1, to=1000, width=10)
        self.num_weapons.grid(row=1, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(self.armourer_frame, text="Special Requirements:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
        self.special_reqs = tk.Text(self.armourer_frame, width=30, height=4)
        self.special_reqs.grid(row=2, column=1, sticky="w", padx=5, pady=2)
        
        # Dates
        date_frame = ttk.LabelFrame(tab, text="Dates")
        date_frame.grid(row=5, column=0, padx=10, pady=5, sticky="ew")
        
        ttk.Label(date_frame, text="Start Date:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        self.start_date = ttk.Entry(date_frame, width=15)
        self.start_date.grid(row=0, column=1, sticky="w", padx=5, pady=2)
        self.start_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        
        ttk.Label(date_frame, text="End Date:").grid(row=0, column=2, sticky="e", padx=5, pady=2)
        self.end_date = ttk.Entry(date_frame, width=15)
        self.end_date.grid(row=0, column=3, sticky="w", padx=5, pady=2)
        self.end_date.insert(0, (datetime.now() + timedelta(days=7)).strftime("%
