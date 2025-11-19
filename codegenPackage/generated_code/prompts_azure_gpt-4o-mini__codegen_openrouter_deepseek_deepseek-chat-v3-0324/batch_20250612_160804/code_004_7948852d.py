"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Design a user interface layout for a car service app that includes features like service inquiry, car pickup scheduling, and repair tracking, based on the process described by Mechanics.ae.
Generated: DETERMINISTIC_7948852d3ff6018d
Batch ID: 20250612_160804
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
from datetime import datetime

class CarServiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mechanics.ae - Car Service App")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TNotebook.Tab', font=('Arial', 10, 'bold'))
        
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.logo_label = ttk.Label(
            self.header_frame, 
            text="Mechanics.ae", 
            style='Header.TLabel'
        )
        self.logo_label.pack(side=tk.LEFT)
        
        self.user_label = ttk.Label(
            self.header_frame, 
            text="Welcome, User", 
            style='Header.TLabel'
        )
        self.user_label.pack(side=tk.RIGHT)
        
        # Tab control
        self.tab_control = ttk.Notebook(self.main_frame)
        
        # Service Inquiry Tab
        self.service_tab = ttk.Frame(self.tab_control)
        self._setup_service_tab()
        
        # Pickup Scheduling Tab
        self.pickup_tab = ttk.Frame(self.tab_control)
        self._setup_pickup_tab()
        
        # Repair Tracking Tab
        self.tracking_tab = ttk.Frame(self.tab_control)
        self._setup_tracking_tab()
        
        self.tab_control.add(self.service_tab, text='Service Inquiry')
        self.tab_control.add(self.pickup_tab, text='Schedule Pickup')
        self.tab_control.add(self.tracking_tab, text='Repair Tracking')
        self.tab_control.pack(fill=tk.BOTH, expand=True)
        
    def _setup_service_tab(self):
        # Service Inquiry Form
        form_frame = ttk.Frame(self.service_tab)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Car Details
        car_frame = ttk.LabelFrame(form_frame, text="Car Details")
        car_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(car_frame, text="Make:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.make_entry = ttk.Entry(car_frame, width=30)
        self.make_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(car_frame, text="Model:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.model_entry = ttk.Entry(car_frame, width=30)
        self.model_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(car_frame, text="Year:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.year_entry = ttk.Entry(car_frame, width=30)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Service Details
        service_frame = ttk.LabelFrame(form_frame, text="Service Details")
        service_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(service_frame, text="Service Type:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.service_type = ttk.Combobox(service_frame, values=[
            "Oil Change", "Tire Rotation", "Brake Inspection", 
            "Engine Check", "Full Service", "Other"
        ], width=27)
        self.service_type.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(service_frame, text="Additional Notes:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.notes_text = tk.Text(service_frame, width=40, height=5)
        self.notes_text.grid(row=1, column=1, padx=5, pady=5)
        
        # Submit Button
        submit_btn = ttk.Button(
            form_frame, 
            text="Submit Inquiry", 
            command=self._submit_inquiry
        )
        submit_btn.pack(pady=10)
        
    def _setup_pickup_tab(self):
        # Pickup Scheduling Form
        form_frame = ttk.Frame(self.pickup_tab)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Pickup Details
        pickup_frame = ttk.LabelFrame(form_frame, text="Pickup Details")
        pickup_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(pickup_frame, text="Pickup Date:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.pickup_date = ttk.Entry(pickup_frame, width=30)
        self.pickup_date.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(pickup_frame, text="Pickup Time:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.pickup_time = ttk.Combobox(pickup_frame, values=[
            "08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM",
            "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM",
            "04:00 PM", "05:00 PM"
        ], width=27)
        self.pickup_time.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(pickup_frame, text="Pickup Address:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.pickup_address = tk.Text(pickup_frame, width=40, height=3)
        self.pickup_address.grid(row=2, column=1, padx=5, pady=5)
        
        # Contact Details
        contact_frame = ttk.LabelFrame(form_frame, text="Contact Details")
        contact_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(contact_frame, text="Contact Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.contact_name = ttk.Entry(contact_frame, width=30)
        self.contact_name.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(contact_frame, text="Phone Number:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.contact_phone = ttk.Entry(contact_frame, width=30)
        self.contact_phone.grid(row=1, column=1, padx=5, pady=5)
        
        # Submit Button
        submit_btn = ttk.Button(
            form_frame, 
            text="Schedule Pickup", 
            command=self._schedule_pickup
        )
        submit_btn.pack(pady=10)
        
    def _setup_tracking_tab(self):
        # Repair Tracking Form
        form_frame = ttk.Frame(self.tracking_tab)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Search Frame
        search_frame = ttk.Frame(form_frame)
        search_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(search_frame, text="Service ID:").pack(side=tk.LEFT, padx=5)
        self.service_id_entry = ttk.Entry(search_frame, width=20)
