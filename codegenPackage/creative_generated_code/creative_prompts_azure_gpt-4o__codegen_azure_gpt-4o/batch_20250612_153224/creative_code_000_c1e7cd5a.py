"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Write a Python script to create a reservation form for horse riding tours, including fields for tour options like "Laguna Ride," "Cowboy Experience," and "Skiing & Riding Experience," as described on the Chile Horse Riding website.
Generated: DETERMINISTIC_c1e7cd5a928f69d8
Batch ID: 20250612_153224
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

# Create the main application window
class ReservationFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Horse Riding Tour Reservation Form")
        self.root.geometry("400x400")

        # Create a label for the form
        tk.Label(root, text="Horse Riding Tour Reservation Form", font=("Arial", 14, "bold")).pack(pady=10)

        # Customer Name input
        tk.Label(root, text="Customer Name:").pack(anchor="w", padx=10)
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack(padx=10, pady=5)

        # Email input
        tk.Label(root, text="Email:").pack(anchor="w", padx=10)
        self.email_entry = tk.Entry(root, width=50)
        self.email_entry.pack(padx=10, pady=5)

        # Phone Number input
        tk.Label(root, text="Phone Number:").pack(anchor="w", padx=10)
        self.phone_entry = tk.Entry(root, width=50)
        self.phone_entry.pack(padx=10, pady=5)

        # Tour options
        tk.Label(root, text="Select Tour:").pack(anchor="w", padx=10)
        self.tour_var = tk.StringVar(value="Laguna Ride")  # Default selection
        tours = ["Laguna Ride", "Cowboy Experience", "Skiing & Riding Experience"]
        for tour in tours:
            tk.Radiobutton(root, text=tour, variable=self.tour_var, value=tour).pack(anchor="w", padx=20)

        # Submit button
        tk.Button(root, text="Submit", command=self.submit_form).pack(pady=20)

    def submit_form(self):
        # Retrieve input values
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        tour = self.tour_var.get()

        # Validate inputs
        if not name or not email or not phone:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Basic email validation
        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid email address!")
            return

        # Success message
        success_message = f"Reservation successful!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nTour: {tour}"
        messagebox.showinfo("Success", success_message)

        # Clear fields after submission
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.tour_var.set("Laguna Ride")

# Main execution point
if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationFormApp(root)
    root.mainloop()
```
