"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Design a user interface for a property management system that allows owners and renters to access their accounts, make payments, and view property information, inspired by Inmobiliaria Nueva Ciudad's online services.
Generated: DETERMINISTIC_78f8a161603ca460
Batch ID: 20250622_210655
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
import sqlite3
from datetime import datetime

class PropertyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Property Management System")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Database connection
        self.conn = sqlite3.connect('property_management.db')
        self.create_tables()
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'))
        
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Login screen
        self.show_login_screen()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                user_type TEXT NOT NULL,
                full_name TEXT NOT NULL
            )
        ''')
        
        # Properties table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS properties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner_id INTEGER NOT NULL,
                address TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                zip_code TEXT NOT NULL,
                rent_amount REAL NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (owner_id) REFERENCES users (id)
            )
        ''')
        
        # Payments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                property_id INTEGER NOT NULL,
                tenant_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                payment_date TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (property_id) REFERENCES properties (id),
                FOREIGN KEY (tenant_id) REFERENCES users (id)
            )
        ''')
        
        # Contracts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contracts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                property_id INTEGER NOT NULL,
                tenant_id INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                monthly_rent REAL NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (property_id) REFERENCES properties (id),
                FOREIGN KEY (tenant_id) REFERENCES users (id)
            )
        ''')
        
        self.conn.commit()
    
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        self.clear_frame()
        
        # Header
        header = ttk.Label(self.main_frame, text="Property Management System", style='Header.TLabel')
        header.pack(pady=20)
        
        # Login form
        login_frame = ttk.Frame(self.main_frame)
        login_frame.pack(pady=20)
        
        ttk.Label(login_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.username_entry = ttk.Entry(login_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(login_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.password_entry = ttk.Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        
        login_btn = ttk.Button(login_frame, text="Login", command=self.login)
        login_btn.grid(row=2, column=1, pady=10, sticky=tk.E)
        
        register_btn = ttk.Button(self.main_frame, text="Register New Account", command=self.show_registration_screen)
        register_btn.pack(pady=10)
    
    def show_registration_screen(self):
        self.clear_frame()
        
        # Header
        header = ttk.Label(self.main_frame, text="Register New Account", style='Header.TLabel')
        header.pack(pady=20)
        
        # Registration form
        reg_frame = ttk.Frame(self.main_frame)
        reg_frame.pack(pady=20)
        
        ttk.Label(reg_frame, text="Full Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.reg_fullname = ttk.Entry(reg_frame)
        self.reg_fullname.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(reg_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.reg_email = ttk.Entry(reg_frame)
        self.reg_email.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(reg_frame, text="Username:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.reg_username = ttk.Entry(reg_frame)
        self.reg_username.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(reg_frame, text="Password:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.reg_password = ttk.Entry(reg_frame, show="*")
        self.reg_password.grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Label(reg_frame, text="Confirm Password:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.reg_confirm_password = ttk.Entry(reg_frame, show="*")
        self.reg_confirm_password.grid(row=4, column=1, padx=5, pady=5)
        
        ttk.Label(reg_frame, text="Account Type:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.user_type = tk.StringVar()
        self.user_type.set("tenant")
        ttk.Radiobutton(reg_frame, text="Tenant", variable=self.user_type, value="tenant").grid(row=5, column=1, sticky=tk.W)
        ttk.Radiobutton(reg_frame, text="Owner", variable=self.user_type, value="owner").grid(row=6, column=1, sticky=tk.W)
        
        register_btn = ttk.Button(reg_frame, text="Register", command=self.register)
        register_btn.grid(row=7, column=1, pady=10, sticky=tk.E)
        
        back_btn = ttk.Button(self.main_frame, text="Back to Login", command=self.show_login_screen)
        back_btn.pack(pady=10)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, user_type, full_name FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        
        if user:
            self.current_user = {
                'id': user[0],
                'user_type': user[1],
                'full_name': user[2]
            }
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def register(self):
        fullname = self.reg_fullname.get()
        email = self.reg_email.get()
        username = self.reg_username.get()
        password = self.reg_password.get()
        confirm_password = self.reg_confirm_password.get()
        user_type = self.user_type.get()
        
        if not all([fullname, email, username, password, confirm_password]):
            messagebox.showerror("Error", "All fields are required")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password, email, user_type, full_name) VALUES (?, ?, ?, ?, ?)",
                (username, password, email, user_type, fullname)
            )
            self.conn.commit()
