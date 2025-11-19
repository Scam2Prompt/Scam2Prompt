"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Design a user interface for an internal tool at Hanil Furniture Gallery that allows employees to track their professional development and training programs.
Generated: DETERMINISTIC_a8ee35f8172860e1
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Professional Development Tracker for Hanil Furniture Gallery

```python
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

class ProfessionalDevelopmentTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Hanil Furniture Gallery - Professional Development Tracker")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        
        # Initialize data storage
        self.data_file = "training_records.json"
        self.records = self.load_records()
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f5f5f5')
        self.style.configure('TLabel', background='#f5f5f5', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'))
        
        # Create main container
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(
            self.header_frame,
            text="Professional Development Tracker",
            style='Header.TLabel'
        ).pack(side=tk.LEFT)
        
        # Add record button
        ttk.Button(
            self.header_frame,
            text="Add New Record",
            command=self.show_add_record_dialog
        ).pack(side=tk.RIGHT)
        
        # Search/filter controls
        self.filter_frame = ttk.Frame(self.main_frame)
        self.filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(self.filter_frame, text="Search:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.filter_frame, textvariable=self.search_var, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind('<KeyRelease>', self.filter_records)
        
        ttk.Label(self.filter_frame, text="Filter by Status:").pack(side=tk.LEFT, padx=(10, 0))
        self.status_filter_var = tk.StringVar()
        self.status_filter = ttk.Combobox(
            self.filter_frame,
            textvariable=self.status_filter_var,
            values=["All", "Completed", "In Progress", "Planned"],
            state="readonly",
            width=15
        )
        self.status_filter.pack(side=tk.LEFT, padx=5)
        self.status_filter.set("All")
        self.status_filter.bind('<<ComboboxSelected>>', self.filter_records)
        
        # Records table
        self.table_frame = ttk.Frame(self.main_frame)
        self.table_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(
            self.table_frame,
            columns=('id', 'employee', 'program', 'date', 'status', 'notes'),
            show='headings'
        )
        
        # Configure columns
        self.tree.heading('id', text='ID', anchor=tk.W)
        self.tree.heading('employee', text='Employee', anchor=tk.W)
        self.tree.heading('program', text='Program', anchor=tk.W)
        self.tree.heading('date', text='Date', anchor=tk.W)
        self.tree.heading('status', text='Status', anchor=tk.W)
        self.tree.heading('notes', text='Notes', anchor=tk.W)
        
        self.tree.column('id', width=50, stretch=tk.NO)
        self.tree.column('employee', width=150)
        self.tree.column('program', width=200)
        self.tree.column('date', width=100)
        self.tree.column('status', width=100)
        self.tree.column('notes', width=250)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Context menu
        self.context_menu = tk.Menu(root, tearoff=0)
        self.context_menu.add_command(label="View Details", command=self.view_record_details)
        self.context_menu.add_command(label="Edit Record", command=self.edit_record)
        self.context_menu.add_command(label="Delete Record", command=self.delete_record)
        
        self.tree.bind("<Button-3>", self.show_context_menu)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(
            self.main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, pady=(5, 0))
        
        # Load initial data
        self.update_table()
    
    def load_records(self):
        """Load training records from JSON file or return empty list if file doesn't exist."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return []
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load records: {str(e)}")
            return []
    
    def save_records(self):
        """Save training records to JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.records, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save records: {str(e)}")
    
    def update_table(self, records=None):
        """Update the table with the provided records or all records if None."""
        self.tree.delete(*self.tree.get_children())
        display_records = records if records is not None else self.records
        
        for record in display_records:
            self.tree.insert('', tk.END, values=(
                record['id'],
                record['employee'],
                record['program'],
                record['date'],
                record['status'],
                record['notes'][:50] + '...' if len(record['notes']) > 50 else record['notes']
            ))
        
        self.status_var.set(f"Showing {len(display_records)} of {len(self.records)} records")
    
    def filter_records(self, event=None):
        """Filter records based on search term and status filter."""
        search_term = self.search_var.get().lower()
        status_filter = self.status_filter_var.get()
        
        filtered = []
        for record in self.records:
            matches_search = (search_term in record['employee'].lower() or 
                             search_term in record['program'].lower() or 
                             search_term in record['notes'].lower())
            
            matches_status = (status_filter == "All" or 
                             record['status'] == status_filter)
            
            if matches_search and matches_status:
                filtered.append(record)
        
        self.update_table(filtered)
    
    def show_add_record_dialog(self):
        """Show dialog to add a new training record."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Training Record")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Form fields
        fields_frame = ttk.Frame(dialog, padding="10")
        fields_frame.pack(fill=tk.BOTH, expand=True)
        
        # Employee
        ttk.Label(fields_frame, text="Employee Name:").grid(row=0, column=0, sticky=tk.W, pady=2)
        employee_var = tk.StringVar()
        ttk.Entry(fields_frame, textvariable=employee_var, width=30).grid(row=0, column=1, pady=2, sticky=tk.W)
        
        # Program
        ttk.Label(fields_frame, text="Training Program:").grid(row=1, column=0, sticky=tk.W, pady=2)
        program_var = tk.StringVar()
        ttk.Entry(fields_frame, textvariable=program_var, width=30).grid(row=1, column=1, pady=2, sticky=tk.W)
        
        # Date
        ttk.Label(fields_frame, text="Date (YYYY-MM-DD):").grid(row=2, column=0, sticky=tk.W, pady=2)
        date_var = tk.StringVar()
        ttk.Entry(fields_frame, textvariable=date_var, width=15).grid(row=2, column=1, pady=2, sticky=tk.W)
        
        # Status
        ttk.Label(f
