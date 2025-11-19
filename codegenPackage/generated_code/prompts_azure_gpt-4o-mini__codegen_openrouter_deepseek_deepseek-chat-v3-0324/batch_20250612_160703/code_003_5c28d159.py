"""
Generated Code Metadata:
========================
Original URL: https://medex.trakmd.dev
Prompt: Generate a sample patient portal interface that allows users to connect with doctors online, inspired by trakMD’s features.
Generated: DETERMINISTIC_5c28d159044b46a4
Batch ID: 20250612_160703
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
import json
import os

class PatientPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Portal")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Initialize data storage
        self.patients_file = "patients.json"
        self.doctors_file = "doctors.json"
        self.appointments_file = "appointments.json"
        self.current_user = None
        
        # Create files if they don't exist
        self._initialize_data_files()
        
        # Create UI
        self._create_login_frame()
        
    def _initialize_data_files(self):
        """Initialize data files with empty structures if they don't exist"""
        default_data = {
            "patients": [],
            "doctors": [
                {"id": 1, "name": "Dr. Smith", "specialty": "Cardiology", "available": True},
                {"id": 2, "name": "Dr. Johnson", "specialty": "Pediatrics", "available": True},
                {"id": 3, "name": "Dr. Williams", "specialty": "Neurology", "available": False}
            ],
            "appointments": []
        }
        
        for file, key in [(self.patients_file, "patients"), 
                         (self.doctors_file, "doctors"),
                         (self.appointments_file, "appointments")]:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    json.dump({key: default_data[key]}, f, indent=4)
    
    def _load_data(self, file):
        """Load data from JSON file"""
        try:
            with open(file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {file.split('.')[0]: []}
    
    def _save_data(self, file, data):
        """Save data to JSON file"""
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)
    
    def _create_login_frame(self):
        """Create the login/registration frame"""
        self.clear_frame()
        
        self.login_frame = ttk.Frame(self.root, padding="20")
        self.login_frame.pack(expand=True)
        
        # Login Section
        ttk.Label(self.login_frame, text="Patient Login", font=('Helvetica', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.login_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.login_email = ttk.Entry(self.login_frame, width=30)
        self.login_email.grid(row=1, column=1, pady=5)
        
        ttk.Label(self.login_frame, text="Password:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.login_password = ttk.Entry(self.login_frame, width=30, show="*")
        self.login_password.grid(row=2, column=1, pady=5)
        
        ttk.Button(self.login_frame, text="Login", command=self._handle_login).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Registration Section
        ttk.Label(self.login_frame, text="New Patient Registration", font=('Helvetica', 14, 'bold')).grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.login_frame, text="Full Name:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.reg_name = ttk.Entry(self.login_frame, width=30)
        self.reg_name.grid(row=5, column=1, pady=5)
        
        ttk.Label(self.login_frame, text="Email:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.reg_email = ttk.Entry(self.login_frame, width=30)
        self.reg_email.grid(row=6, column=1, pady=5)
        
        ttk.Label(self.login_frame, text="Password:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.reg_password = ttk.Entry(self.login_frame, width=30, show="*")
        self.reg_password.grid(row=7, column=1, pady=5)
        
        ttk.Label(self.login_frame, text="Date of Birth (YYYY-MM-DD):").grid(row=8, column=0, sticky=tk.W, pady=5)
        self.reg_dob = ttk.Entry(self.login_frame, width=30)
        self.reg_dob.grid(row=8, column=1, pady=5)
        
        ttk.Button(self.login_frame, text="Register", command=self._handle_registration).grid(row=9, column=0, columnspan=2, pady=10)
    
    def _handle_login(self):
        """Handle patient login"""
        email = self.login_email.get()
        password = self.login_password.get()
        
        if not email or not password:
            messagebox.showerror("Error", "Please enter both email and password")
            return
        
        patients = self._load_data(self.patients_file)["patients"]
        for patient in patients:
            if patient["email"] == email and patient["password"] == password:
                self.current_user = patient
                self._create_dashboard()
                return
        
        messagebox.showerror("Error", "Invalid email or password")
    
    def _handle_registration(self):
        """Handle new patient registration"""
        name = self.reg_name.get()
        email = self.reg_email.get()
        password = self.reg_password.get()
        dob = self.reg_dob.get()
        
        if not all([name, email, password, dob]):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        try:
            datetime.strptime(dob, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD")
            return
        
        patients_data = self._load_data(self.patients_file)
        patients = patients_data["patients"]
        
        # Check if email already exists
        if any(p["email"] == email for p in patients):
            messagebox.showerror("Error", "Email already registered")
            return
        
        # Create new patient
        new_patient = {
            "id": len(patients) + 1,
            "name": name,
            "email": email,
            "password": password,
            "dob": dob,
            "medical_history": []
        }
        
        patients.append(new_patient)
        patients_data["patients"] = patients
        self._save_data(self.patients_file, patients_data)
        
        messagebox.showinfo("Success", "Registration successful! Please login.")
        self.login_email.delete(0, tk.END)
        self.login_password.delete(0, tk.END)
        self.login_email.insert(0, email)
        self.login_password.focus()
    
    def _create_dashboard(self):
        """Create the main dashboard after login"""
        self.clear_frame()
        
        self.dashboard_frame = ttk.Frame(self.root, padding="20")
        self.dashboard_frame.pack(expand=True, fill=tk.BOTH)
        
        # Header
        header_frame = ttk.Frame(self.dashboard_frame)
        header_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(header_frame, text=f"Welcome, {self.current_user['name']}", font=('Helvetica', 16, 'bold')).pack(side=tk.LEFT)
        ttk.Button(header_frame, text="Logout", command=self._create_login_frame).pack(side=tk.RIGHT)
        
        # Navigation
        nav_frame = ttk.Frame(self.dashboard_frame)
        nav_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(nav_frame, text="Book Appointment", command=self._show_book_appointment).pack(side=tk.LEFT, padx=5)
        ttk.Button(nav_frame, text="My Appointments", command=self._show_my_appointments).pack(side=tk.LEFT, padx=5)
        ttk.Button(nav_frame, text="Medical History", command=self._show_medical_history).pack(side=tk.LEFT, padx=5)
        ttk.Button(nav_frame, text="Profile", command=self._show_profile).pack(side=tk.LEFT, padx=5)
        
        # Main content area
        self.content_frame = ttk.Frame(self.dashboard_frame)
        self.content_frame.pack(expand=True, fill=tk.BOTH)
        
        # Show default view
        self._show_welcome_message()
    
    def _show_welcome_message(self):
        """Show welcome message in content area
