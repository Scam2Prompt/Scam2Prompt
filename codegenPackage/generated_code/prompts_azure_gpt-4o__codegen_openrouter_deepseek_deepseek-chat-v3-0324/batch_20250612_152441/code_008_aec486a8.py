"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: Create a script to generate a quote for UPVC window and door installation services, including input fields for design selection, service type, and location, as described on the Dexodoor website.
Generated: DETERMINISTIC_aec486a88e839f37
Batch ID: 20250612_152441
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
import json
import os

class QuoteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("UPVC Window & Door Installation Quote Generator")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Load configuration data
        self.load_config()
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Initialize UI
        self.create_widgets()
        
    def load_config(self):
        """Load configuration data from JSON file"""
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        try:
            with open(config_path, "r") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "Configuration file not found!")
            self.root.destroy()
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid configuration file!")
            self.root.destroy()
    
    def create_widgets(self):
        """Create all UI widgets"""
        # Header
        header = ttk.Label(
            self.main_frame,
            text="UPVC Window & Door Installation Quote",
            font=("Helvetica", 16, "bold")
        )
        header.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Customer Information
        customer_frame = ttk.LabelFrame(self.main_frame, text="Customer Information", padding=10)
        customer_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        
        ttk.Label(customer_frame, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(customer_frame, width=30)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=2)
        
        ttk.Label(customer_frame, text="Email:").grid(row=1, column=0, sticky="w")
        self.email_entry = ttk.Entry(customer_frame, width=30)
        self.email_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        
        ttk.Label(customer_frame, text="Phone:").grid(row=2, column=0, sticky="w")
        self.phone_entry = ttk.Entry(customer_frame, width=30)
        self.phone_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        
        ttk.Label(customer_frame, text="Address:").grid(row=3, column=0, sticky="w")
        self.address_entry = ttk.Entry(customer_frame, width=30)
        self.address_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=2)
        
        ttk.Label(customer_frame, text="Postcode:").grid(row=4, column=0, sticky="w")
        self.postcode_entry = ttk.Entry(customer_frame, width=30)
        self.postcode_entry.grid(row=4, column=1, sticky="ew", padx=5, pady=2)
        
        # Product Selection
        product_frame = ttk.LabelFrame(self.main_frame, text="Product Selection", padding=10)
        product_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        
        ttk.Label(product_frame, text="Product Type:").grid(row=0, column=0, sticky="w")
        self.product_type = ttk.Combobox(
            product_frame,
            values=list(self.config["products"].keys()),
            state="readonly"
        )
        self.product_type.grid(row=0, column=1, sticky="ew", padx=5, pady=2)
        self.product_type.bind("<<ComboboxSelected>>", self.update_designs)
        
        ttk.Label(product_frame, text="Design:").grid(row=1, column=0, sticky="w")
        self.design = ttk.Combobox(product_frame, state="readonly")
        self.design.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        self.design.bind("<<ComboboxSelected>>", self.update_price)
        
        ttk.Label(product_frame, text="Color:").grid(row=2, column=0, sticky="w")
        self.color = ttk.Combobox(
            product_frame,
            values=self.config["colors"],
            state="readonly"
        )
        self.color.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        
        ttk.Label(product_frame, text="Quantity:").grid(row=3, column=0, sticky="w")
        self.quantity = ttk.Spinbox(product_frame, from_=1, to=100, width=5)
        self.quantity.grid(row=3, column=1, sticky="w", padx=5, pady=2)
        self.quantity.bind("<KeyRelease>", self.update_price)
        
        # Additional Services
        service_frame = ttk.LabelFrame(self.main_frame, text="Additional Services", padding=10)
        service_frame.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        
        self.services_vars = {}
        for i, service in enumerate(self.config["services"]):
            var = tk.BooleanVar()
            cb = ttk.Checkbutton(
                service_frame,
                text=f"{service} (+£{self.config['services'][service]:.2f})",
                variable=var,
                onvalue=True,
                offvalue=False
            )
            cb.grid(row=i, column=0, sticky="w", padx=5, pady=2)
            self.services_vars[service] = var
        
        # Quote Summary
        summary_frame = ttk.LabelFrame(self.main_frame, text="Quote Summary", padding=10)
        summary_frame.grid(row=1, column=1, rowspan=3, sticky="nsew", padx=5, pady=5)
        
        self.summary_text = tk.Text(
            summary_frame,
            height=15,
            width=40,
            state="disabled",
            wrap="word"
        )
        self.summary_text.pack(fill=tk.BOTH, expand=True)
        
        # Buttons
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(
            button_frame,
            text="Generate Quote",
            command=self.generate_quote
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Reset Form",
            command=self.reset_form
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Exit",
            command=self.root.quit
        ).pack(side=tk.LEFT, padx=5)
        
        # Initialize summary
        self.update_summary()
    
    def update_designs(self, event=None):
        """Update design options based on selected product type"""
        product = self.product_type.get()
        if product in self.config["products"]:
            designs = list(self.config["products"][product].keys())
            self.design["values"] = designs
            if designs:
                self.design.current(0)
                self.update_price()
    
    def update_price(self, event=None):
        """Update price based on current selections"""
        self.update_summary()
    
    def calculate_total(self):
        """Calculate the total price"""
        total = 0.0
        
        # Product price
        product = self.product_type.get()
        design = self.design.get()
        if product and design and product in self.config["products"]:
            if design in self.config["products"][product]:
                try:
                    quantity = int(self.quantity.get())
                    total += self.config["products"][product][design] * quantity
                except ValueError:
                    pass
        
        # Additional services
        for service, var in self.services_vars.items():
            if var.get():
                total += self.config["services"][service]
        
        return total
    
    def update_summary(self):
        """Update the quote summary"""
        self.summary_text.config(state="normal")
        self.summary_text.delete(1.0, tk.END)
        
        # Customer info
        self.summary_text.insert(tk.END, "Customer Information:\n")
        self.summary_text.insert(tk.END, f"Name: {self.name_entry.get()}\n")
        self.summary_text.insert(tk.END, f"Address: {self.address_entry.get()}\n")
        self.summary_text.insert(tk.END, f"Postcode: {self.postcode_entry.get()}\n\n")
        
        # Product info
