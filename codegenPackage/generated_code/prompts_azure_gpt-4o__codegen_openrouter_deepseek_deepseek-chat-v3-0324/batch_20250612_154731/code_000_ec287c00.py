"""
Generated Code Metadata:
========================
Original URL: https://balajitravelsonline.com
Prompt: Write a Python script to generate a booking form for Balaji Tours & Travels that includes fields for name, mobile number, email, and a dropdown menu for selecting tour packages like Tirupathi, Kerala, and Munnar.
Generated: DETERMINISTIC_ec287c009ca50c87
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox
import re

class BookingForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Balaji Tours & Travels - Booking Form")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        
        # Configure styles
        self.root.configure(bg="#f0f0f0")
        label_font = ("Arial", 10)
        entry_font = ("Arial", 10)
        button_font = ("Arial", 10, "bold")
        
        # Header
        header = tk.Label(
            self.root, 
            text="Balaji Tours & Travels", 
            font=("Arial", 16, "bold"), 
            bg="#f0f0f0", 
            fg="#333333"
        )
        header.pack(pady=10)
        
        # Form Frame
        form_frame = tk.Frame(self.root, bg="#f0f0f0")
        form_frame.pack(pady=10, padx=20, fill="both")
        
        # Name Field
        tk.Label(
            form_frame, 
            text="Full Name:", 
            font=label_font, 
            bg="#f0f0f0"
        ).grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(
            form_frame, 
            font=entry_font, 
            width=30
        )
        self.name_entry.grid(row=0, column=1, pady=5, padx=5)
        
        # Mobile Field
        tk.Label(
            form_frame, 
            text="Mobile Number:", 
            font=label_font, 
            bg="#f0f0f0"
        ).grid(row=1, column=0, sticky="w", pady=5)
        self.mobile_entry = tk.Entry(
            form_frame, 
            font=entry_font, 
            width=30
        )
        self.mobile_entry.grid(row=1, column=1, pady=5, padx=5)
        
        # Email Field
        tk.Label(
            form_frame, 
            text="Email:", 
            font=label_font, 
            bg="#f0f0f0"
        ).grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = tk.Entry(
            form_frame, 
            font=entry_font, 
            width=30
        )
        self.email_entry.grid(row=2, column=1, pady=5, padx=5)
        
        # Tour Package Dropdown
        tk.Label(
            form_frame, 
            text="Tour Package:", 
            font=label_font, 
            bg="#f0f0f0"
        ).grid(row=3, column=0, sticky="w", pady=5)
        
        self.package_var = tk.StringVar()
        self.package_var.set("Select Package")  # default value
        packages = ["Tirupathi", "Kerala", "Munnar"]
        self.package_menu = tk.OptionMenu(
            form_frame, 
            self.package_var, 
            *packages
        )
        self.package_menu.config(font=entry_font, width=25)
        self.package_menu.grid(row=3, column=1, pady=5, padx=5)
        
        # Submit Button
        submit_btn = tk.Button(
            self.root, 
            text="Submit Booking", 
            font=button_font, 
            bg="#4CAF50", 
            fg="white", 
            command=self.validate_form
        )
        submit_btn.pack(pady=20)
        
    def validate_form(self):
        name = self.name_entry.get().strip()
        mobile = self.mobile_entry.get().strip()
        email = self.email_entry.get().strip()
        package = self.package_var.get()
        
        # Validation checks
        if not name:
            messagebox.showerror("Error", "Please enter your name")
            return
        
        if not re.match(r'^[0-9]{10}$', mobile):
            messagebox.showerror("Error", "Please enter a valid 10-digit mobile number")
            return
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messagebox.showerror("Error", "Please enter a valid email address")
            return
        
        if package == "Select Package":
            messagebox.showerror("Error", "Please select a tour package")
            return
        
        # If all validations pass
        self.submit_booking(name, mobile, email, package)
    
    def submit_booking(self, name, mobile, email, package):
        # In a real application, this would save to a database
        messagebox.showinfo(
            "Booking Successful", 
            f"Thank you, {name}!\n\n"
            f"Your booking for {package} package has been received.\n"
            f"We'll contact you at {mobile} or {email} shortly."
        )
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookingForm(root)
    root.mainloop()
```
