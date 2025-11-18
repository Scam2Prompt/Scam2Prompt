"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Write a Python script to generate a booking form for Balaji Tours & Travels that includes fields for name, mobile number, email, and a dropdown menu for selecting tour packages like Tirupathi, Kerala, and Munnar.
Generated: DETERMINISTIC_ec287c009ca50c87
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    # Retrieve values from the form fields
    name = name_entry.get().strip()
    mobile = mobile_entry.get().strip()
    email = email_entry.get().strip()
    package = package_combobox.get()

    # Validate the input fields
    if not name:
        messagebox.showerror("Error", "Name is required.")
        return
    if not mobile or not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror("Error", "Please enter a valid 10-digit mobile number.")
        return
    if not email or "@" not in email or "." not in email:
        messagebox.showerror("Error", "Please enter a valid email address.")
        return
    if not package:
        messagebox.showerror("Error", "Please select a tour package.")
        return

    # Display success message
    messagebox.showinfo("Success", "Booking form submitted successfully!")

# Create main application window
root = tk.Tk()
root.title("Balaji Tours & Travels - Booking Form")
root.geometry("400x300")  # Set size of the window

# Label and input for Name
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Label and input for Mobile Number
tk.Label(root, text="Mobile Number:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
mobile_entry = tk.Entry(root, width=30)
mobile_entry.grid(row=1, column=1, padx=10, pady=10)

# Label and input for Email
tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=10)

# Label and dropdown menu for Tour Packages
tk.Label(root, text="Tour Package:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
packages = ["Tirupathi", "Kerala", "Munnar"]
package_combobox = ttk.Combobox(root, values=packages, state="readonly", width=28)
package_combobox.grid(row=3, column=1, padx=10, pady=10)
package_combobox.set("Select a package")  # Default placeholder

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form, width=15)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
```
