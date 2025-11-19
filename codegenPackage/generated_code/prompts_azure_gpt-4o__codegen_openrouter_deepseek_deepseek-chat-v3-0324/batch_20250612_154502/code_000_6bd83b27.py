"""
Generated Code Metadata:
========================
Original URL: https://www.traveloagency.com
Prompt: Write a Python script to simulate a flight search widget similar to the one described on Traveloagency, allowing users to input origin, destination, travel dates, and passenger details.
Generated: DETERMINISTIC_6bd83b27ab294fb1
Batch ID: 20250612_154502
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
from datetime import datetime, timedelta
import json
import os

class FlightSearchWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Search Widget")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Load cities data
        self.cities = self.load_cities()
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create widgets
        self.create_widgets()
        
    def load_cities(self):
        """Load cities data from JSON file or return default list if file not found."""
        try:
            if os.path.exists("cities.json"):
                with open("cities.json", "r") as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading cities data: {e}")
        
        # Default cities if file not found
        return [
            "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
            "London", "Paris", "Tokyo", "Dubai", "Singapore",
            "Sydney", "Toronto", "Berlin", "Mumbai", "Hong Kong"
        ]
    
    def create_widgets(self):
        """Create all widgets for the flight search form."""
        # Title
        title_label = ttk.Label(
            self.main_frame, 
            text="Find Your Perfect Flight",
            font=("Helvetica", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Origin
        ttk.Label(self.main_frame, text="From:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.origin_var = tk.StringVar()
        self.origin_cb = ttk.Combobox(
            self.main_frame, 
            textvariable=self.origin_var,
            values=self.cities,
            state="normal"
        )
        self.origin_cb.grid(row=1, column=1, sticky=tk.EW, pady=5, padx=(0, 10))
        
        # Destination
        ttk.Label(self.main_frame, text="To:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.dest_var = tk.StringVar()
        self.dest_cb = ttk.Combobox(
            self.main_frame, 
            textvariable=self.dest_var,
            values=self.cities,
            state="normal"
        )
        self.dest_cb.grid(row=2, column=1, sticky=tk.EW, pady=5, padx=(0, 10))
        
        # Departure Date
        ttk.Label(self.main_frame, text="Departure:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.departure_var = tk.StringVar()
        self.departure_entry = ttk.Entry(self.main_frame, textvariable=self.departure_var)
        self.departure_entry.grid(row=3, column=1, sticky=tk.EW, pady=5, padx=(0, 10))
        self.departure_entry.insert(0, (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"))
        
        # Return Date
        ttk.Label(self.main_frame, text="Return:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.return_var = tk.StringVar()
        self.return_entry = ttk.Entry(self.main_frame, textvariable=self.return_var)
        self.return_entry.grid(row=4, column=1, sticky=tk.EW, pady=5, padx=(0, 10))
        self.return_entry.insert(0, (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d"))
        
        # Passengers
        ttk.Label(self.main_frame, text="Passengers:").grid(row=5, column=0, sticky=tk.W, pady=5)
        
        self.passenger_frame = ttk.Frame(self.main_frame)
        self.passenger_frame.grid(row=5, column=1, sticky=tk.EW, pady=5)
        
        # Adults
        ttk.Label(self.passenger_frame, text="Adults:").grid(row=0, column=0, padx=(0, 5))
        self.adults_var = tk.IntVar(value=1)
        self.adults_spin = ttk.Spinbox(
            self.passenger_frame, 
            from_=1, 
            to=10, 
            textvariable=self.adults_var,
            width=3
        )
        self.adults_spin.grid(row=0, column=1, padx=(0, 10))
        
        # Children
        ttk.Label(self.passenger_frame, text="Children:").grid(row=0, column=2, padx=(0, 5))
        self.children_var = tk.IntVar(value=0)
        self.children_spin = ttk.Spinbox(
            self.passenger_frame, 
            from_=0, 
            to=10, 
            textvariable=self.children_var,
            width=3
        )
        self.children_spin.grid(row=0, column=3, padx=(0, 10))
        
        # Infants
        ttk.Label(self.passenger_frame, text="Infants:").grid(row=0, column=4, padx=(0, 5))
        self.infants_var = tk.IntVar(value=0)
        self.infants_spin = ttk.Spinbox(
            self.passenger_frame, 
            from_=0, 
            to=10, 
            textvariable=self.infants_var,
            width=3
        )
        self.infants_spin.grid(row=0, column=5)
        
        # Cabin Class
        ttk.Label(self.main_frame, text="Cabin Class:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.class_var = tk.StringVar(value="Economy")
        self.class_cb = ttk.Combobox(
            self.main_frame,
            textvariable=self.class_var,
            values=["Economy", "Premium Economy", "Business", "First Class"],
            state="readonly"
        )
        self.class_cb.grid(row=6, column=1, sticky=tk.EW, pady=5, padx=(0, 10))
        
        # Search Button
        self.search_btn = ttk.Button(
            self.main_frame,
            text="Search Flights",
            command=self.search_flights
        )
        self.search_btn.grid(row=7, column=0, columnspan=2, pady=20)
        
        # Configure grid weights
        self.main_frame.columnconfigure(1, weight=1)
    
    def validate_inputs(self):
        """Validate all form inputs before searching."""
        origin = self.origin_var.get().strip()
        destination = self.dest_var.get().strip()
        departure = self.departure_var.get().strip()
        return_date = self.return_var.get().strip()
        
        if not origin:
            messagebox.showerror("Error", "Please select origin city")
            return False
        
        if not destination:
            messagebox.showerror("Error", "Please select destination city")
            return False
            
        if origin == destination:
            messagebox.showerror("Error", "Origin and destination cannot be the same")
            return False
            
        try:
            dep_date = datetime.strptime(departure, "%Y-%m-%d")
            ret_date = datetime.strptime(return_date, "%Y-%m-%d")
            
            if dep_date < datetime.now():
                messagebox.showerror("Error", "Departure date cannot be in the past")
                return False
                
            if ret_date < dep_date:
                messagebox.showerror("Error", "Return date must be after departure date")
                return False
                
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD")
            return False
            
        total_passengers = self.adults_var.get() + self.children_var.get() + self.infants_var.get()
        if total_passengers <= 0:
            messagebox.showerror("Error", "At least one passenger is required")
            return False
            
        if self.infants_var.get() > self.adults_var.get():
            messagebox.showerror("Error", "Number of infants cannot exceed number of adults")
            return False
            
        return True
    
    def search_flights(self):
        """Handle flight search button click."""
        if not self.validate_inputs():
            return
            
        search_data = {
            "origin": self.origin_var.get(),
            "destination": self.dest_var.get(),
            "departure_date": self.departure_var.get(),
            "return_date": self
