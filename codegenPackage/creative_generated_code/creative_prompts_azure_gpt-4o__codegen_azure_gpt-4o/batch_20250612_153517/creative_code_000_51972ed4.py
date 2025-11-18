"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Write a Python script to create a form for customers to register for a test drive of MG cars, including fields for name, email, phone number, and preferred car model (e.g., MG5, MG ZS, MG RX5).
Generated: DETERMINISTIC_51972ed441bf48e4
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    try:
        # Retrieve data from form fields
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        car_model = car_model_var.get()
        
        # Basic validation
        if not name or not email or not phone or not car_model:
            raise ValueError("All fields are required.")
        if not "@" in email:
            raise ValueError("Please enter a valid email address.")
        if not phone.isdigit() or len(phone) < 10:
            raise ValueError("Please enter a valid phone number.")
        
        # Simulate form submission (e.g., save to database or send to server)
        # Here we simply show a success message
        messagebox.showinfo("Success", f"Thank you for registering, {name}!\n"
                                        f"Your preferred car model: {car_model}")
        
        # Clear the form for the next entry
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        car_model_var.set("")
    except ValueError as ve:
        # Show error message if validation fails
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        # Generic error handling
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Create the main application window
root = tk.Tk()
root.title("MG Cars Test Drive Registration")
root.geometry("400x300")

# Create a label and entry for Name
tk.Label(root, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a label and entry for Email
tk.Label(root, text="Email:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
email_entry = tk.Entry(root, font=("Arial", 12))
email_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a label and entry for Phone Number
tk.Label(root, text="Phone Number:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
phone_entry = tk.Entry(root, font=("Arial", 12))
phone_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a label and dropdown for Preferred Car Model
tk.Label(root, text="Preferred Car Model:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
car_model_var = tk.StringVar()
car_model_var.set("")  # Default value (empty)
car_model_dropdown = tk.OptionMenu(root, car_model_var, "MG5", "MG ZS", "MG RX5")
car_model_dropdown.grid(row=3, column=1, padx=10, pady=10)

# Create a Submit button
submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=submit_form)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
```
