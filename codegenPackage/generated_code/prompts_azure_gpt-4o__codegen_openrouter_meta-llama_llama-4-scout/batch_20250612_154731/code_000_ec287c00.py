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
# Import required libraries
import tkinter as tk
from tkinter import ttk, messagebox

class BookingForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Balaji Tours & Travels Booking Form")

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(padx=10, pady=10)

        # Create form fields
        self.name_label = tk.Label(self.main_frame, text="Name:", font=("Arial", 12))
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.mobile_label = tk.Label(self.main_frame, text="Mobile Number:", font=("Arial", 12))
        self.mobile_label.grid(row=1, column=0, padx=5, pady=5)
        self.mobile_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 12))
        self.mobile_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.main_frame, text="Email:", font=("Arial", 12))
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 12))
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.tour_package_label = tk.Label(self.main_frame, text="Tour Package:", font=("Arial", 12))
        self.tour_package_label.grid(row=3, column=0, padx=5, pady=5)
        self.tour_package = tk.StringVar()
        self.tour_package.set("Select Package")  # default value
        self.tour_package_menu = ttk.Combobox(self.main_frame, textvariable=self.tour_package)
        self.tour_package_menu['values'] = ("Tirupathi", "Kerala", "Munnar")
        self.tour_package_menu.grid(row=3, column=1, padx=5, pady=5)

        # Create submit button
        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_form, font=("Arial", 12))
        self.submit_button.grid(row=4, column=1, padx=5, pady=5)

    def submit_form(self):
        name = self.name_entry.get()
        mobile = self.mobile_entry.get()
        email = self.email_entry.get()
        package = self.tour_package.get()

        if not name or not mobile or not email or package == "Select Package":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        try:
            # Validate mobile number
            int(mobile)
        except ValueError:
            messagebox.showerror("Error", "Invalid mobile number")
            return

        # Validate email
        if "@" not in email:
            messagebox.showerror("Error", "Invalid email")
            return

        # Save or send data (for demonstration purposes, just print)
        print("Booking Form Data:")
        print(f"Name: {name}")
        print(f"Mobile: {mobile}")
        print(f"Email: {email}")
        print(f"Package: {package}")

        # Clear form fields
        self.name_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.tour_package.set("Select Package")

        messagebox.showinfo("Success", "Form submitted successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookingForm(root)
    root.mainloop()
```
