"""
Generated Code Metadata:
========================
Original URL: https://agodarentacar.com
Prompt: Develop a user interface component that allows users to manage their car rental bookings, inspired by the booking management system on Agoda RentACar.
Generated: DETERMINISTIC_a06730d87ce00270
Batch ID: 20250612_164222
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
from typing import List, Dict, Optional

class CarRentalBookingManager:
    """Main class for managing car rental bookings."""
    
    def __init__(self, root: tk.Tk):
        """Initialize the booking manager UI."""
        self.root = root
        self.root.title("Car Rental Booking Manager")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        
        # Sample data - in production, this would come from a database
        self.bookings: List[Dict] = [
            {
                "id": 1,
                "car_model": "Toyota Corolla",
                "pickup_date": "2023-12-15",
                "return_date": "2023-12-20",
                "location": "Los Angeles Airport",
                "price": 250.00,
                "status": "Confirmed"
            },
            {
                "id": 2,
                "car_model": "Honda Civic",
                "pickup_date": "2023-12-10",
                "return_date": "2023-12-12",
                "location": "New York JFK",
                "price": 180.00,
                "status": "Completed"
            }
        ]
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup all UI components."""
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header = ttk.Label(
            self.main_frame,
            text="Your Car Rental Bookings",
            font=("Helvetica", 16, "bold")
        )
        header.pack(pady=(0, 10))
        
        # Filter controls
        self._setup_filters()
        
        # Bookings table
        self._setup_bookings_table()
        
        # Action buttons
        self._setup_action_buttons()
    
    def _setup_filters(self):
        """Setup filter controls."""
        filter_frame = ttk.LabelFrame(self.main_frame, text="Filter Bookings", padding="10")
        filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Status filter
        ttk.Label(filter_frame, text="Status:").grid(row=0, column=0, padx=5, sticky=tk.W)
        self.status_var = tk.StringVar()
        self.status_combobox = ttk.Combobox(
            filter_frame,
            textvariable=self.status_var,
            values=["All", "Confirmed", "Completed", "Cancelled"],
            state="readonly"
        )
        self.status_combobox.set("All")
        self.status_combobox.grid(row=0, column=1, padx=5, sticky=tk.W)
        self.status_combobox.bind("<<ComboboxSelected>>", self._apply_filters)
        
        # Date range filter
        ttk.Label(filter_frame, text="From:").grid(row=0, column=2, padx=5, sticky=tk.W)
        self.from_date_var = tk.StringVar()
        self.from_date_entry = ttk.Entry(filter_frame, textvariable=self.from_date_var, width=10)
        self.from_date_entry.grid(row=0, column=3, padx=5, sticky=tk.W)
        
        ttk.Label(filter_frame, text="To:").grid(row=0, column=4, padx=5, sticky=tk.W)
        self.to_date_var = tk.StringVar()
        self.to_date_entry = ttk.Entry(filter_frame, textvariable=self.to_date_var, width=10)
        self.to_date_entry.grid(row=0, column=5, padx=5, sticky=tk.W)
        
        filter_button = ttk.Button(
            filter_frame,
            text="Apply Filters",
            command=self._apply_filters
        )
        filter_button.grid(row=0, column=6, padx=10)
    
    def _setup_bookings_table(self):
        """Setup the bookings table."""
        # Container for table and scrollbar
        table_container = ttk.Frame(self.main_frame)
        table_container.pack(fill=tk.BOTH, expand=True)
        
        # Treeview widget
        columns = ("id", "car_model", "pickup_date", "return_date", "location", "price", "status")
        self.bookings_table = ttk.Treeview(
            table_container,
            columns=columns,
            show="headings",
            selectmode="browse"
        )
        
        # Configure columns
        self.bookings_table.heading("id", text="ID")
        self.bookings_table.heading("car_model", text="Car Model")
        self.bookings_table.heading("pickup_date", text="Pickup Date")
        self.bookings_table.heading("return_date", text="Return Date")
        self.bookings_table.heading("location", text="Location")
        self.bookings_table.heading("price", text="Price ($)")
        self.bookings_table.heading("status", text="Status")
        
        self.bookings_table.column("id", width=50, anchor=tk.CENTER)
        self.bookings_table.column("car_model", width=150)
        self.bookings_table.column("pickup_date", width=100, anchor=tk.CENTER)
        self.bookings_table.column("return_date", width=100, anchor=tk.CENTER)
        self.bookings_table.column("location", width=150)
        self.bookings_table.column("price", width=100, anchor=tk.CENTER)
        self.bookings_table.column("status", width=100, anchor=tk.CENTER)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_container, orient=tk.VERTICAL, command=self.bookings_table.yview)
        self.bookings_table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.bookings_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Load initial data
        self._load_bookings()
    
    def _setup_action_buttons(self):
        """Setup action buttons."""
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(
            button_frame,
            text="View Details",
            command=self._view_details
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Cancel Booking",
            command=self._cancel_booking
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Modify Booking",
            command=self._modify_booking
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Print Voucher",
            command=self._print_voucher
        ).pack(side=tk.LEFT, padx=5)
    
    def _load_bookings(self, filtered_bookings: Optional[List[Dict]] = None):
        """Load bookings into the table."""
        # Clear existing data
        for item in self.bookings_table.get_children():
            self.bookings_table.delete(item)
        
        # Load new data
        bookings_to_load = filtered_bookings if filtered_bookings else self.bookings
        for booking in bookings_to_load:
            self.bookings_table.insert("", tk.END, values=(
                booking["id"],
                booking["car_model"],
                booking["pickup_date"],
                booking["return_date"],
                booking["location"],
                f"{booking['price']:.2f}",
                booking["status"]
            ))
    
    def _apply_filters(self, event=None):
        """Apply filters to the bookings."""
        status_filter = self.status_var.get()
        from_date = self.from_date_var.get()
        to_date = self.to_date_var.get()
        
        filtered = self.bookings
        
        # Apply status filter
        if status_filter != "All":
            filtered = [b for b in filtered if b["status"] == status_filter]
        
        # Apply date range filter
        try:
            if from_date:
                from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
                filtered = [b for b in filtered if datetime.strptime(b["pickup_date"], "%Y-%m-%d").date() >= from_date]
            
            if to_date:
                to_date = datetime.strptime(to_date, "%Y-%m-%d").date()
                filtered = [b for b in filtered if datetime.strptime(b["return_date"], "%Y-%m-%d").date() <= to_date]
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter dates in YYYY-MM-DD format")
            return
        
        self._load_bookings(filtered)
    
    def _view_details(self):
        """View details of selected booking."""
        selected = self.bookings_table.selection()
        if not selected:
            messagebox.showwarning("No Selection", "
