"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: Write a Python script to create a simple sweepstakes entry form that collects first name, last name, address, city, state, zip, and email.
Generated: DETERMINISTIC_405a688e93e80089
Batch ID: 20250622_205236
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

class SweepstakesEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Sweepstakes Entry Form")
        self.root.geometry("400x500")
        
        # Create form fields
        self.create_widgets()
        
    def create_widgets(self):
        # Form title
        tk.Label(self.root, text="Sweepstakes Entry Form", font=("Arial", 16)).pack(pady=10)
        
        # Frame for form fields
        form_frame = tk.Frame(self.root)
        form_frame.pack(padx=20, pady=10)
        
        # First Name
        tk.Label(form_frame, text="First Name:").grid(row=0, column=0, sticky="w", pady=2)
        self.first_name = tk.Entry(form_frame, width=30)
        self.first_name.grid(row=0, column=1, pady=2)
        
        # Last Name
        tk.Label(form_frame, text="Last Name:").grid(row=1, column=0, sticky="w", pady=2)
        self.last_name = tk.Entry(form_frame, width=30)
        self.last_name.grid(row=1, column=1, pady=2)
        
        # Address
        tk.Label(form_frame, text="Address:").grid(row=2, column=0, sticky="w", pady=2)
        self.address = tk.Entry(form_frame, width=30)
        self.address.grid(row=2, column=1, pady=2)
        
        # City
        tk.Label(form_frame, text="City:").grid(row=3, column=0, sticky="w", pady=2)
        self.city = tk.Entry(form_frame, width=30)
        self.city.grid(row=3, column=1, pady=2)
        
        # State
        tk.Label(form_frame, text="State:").grid(row=4, column=0, sticky="w", pady=2)
        self.state = tk.Entry(form_frame, width=30)
        self.state.grid(row=4, column=1, pady=2)
        
        # Zip Code
        tk.Label(form_frame, text="Zip Code:").grid(row=5, column=0, sticky="w", pady=2)
        self.zip_code = tk.Entry(form_frame, width=30)
        self.zip_code.grid(row=5, column=1, pady=2)
        
        # Email
        tk.Label(form_frame, text="Email:").grid(row=6, column=0, sticky="w", pady=2)
        self.email = tk.Entry(form_frame, width=30)
        self.email.grid(row=6, column=1, pady=2)
        
        # Submit Button
        submit_btn = tk.Button(self.root, text="Submit Entry", command=self.validate_and_submit)
        submit_btn.pack(pady=20)
        
    def validate_and_submit(self):
        # Get field values
        first_name = self.first_name.get().strip()
        last_name = self.last_name.get().strip()
        address = self.address.get().strip()
        city = self.city.get().strip()
        state = self.state.get().strip()
        zip_code = self.zip_code.get().strip()
        email = self.email.get().strip()
        
        # Validate required fields
        if not all([first_name, last_name, address, city, state, zip_code, email]):
            messagebox.showerror("Error", "All fields are required!")
            return
            
        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Please enter a valid email address!")
            return
            
        # Validate zip code format (basic check for 5 digits)
        if not re.match(r"^\d{5}(-\d{4})?$", zip_code):
            messagebox.showerror("Error", "Please enter a valid zip code!")
            return
            
        # If all validations pass, show success message
        messagebox.showinfo("Success", "Your entry has been submitted successfully!")
        
        # Clear form (optional)
        self.clear_form()
        
    def clear_form(self):
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.city.delete(0, tk.END)
        self.state.delete(0, tk.END)
        self.zip_code.delete(0, tk.END)
        self.email.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SweepstakesEntryForm(root)
    root.mainloop()
```
