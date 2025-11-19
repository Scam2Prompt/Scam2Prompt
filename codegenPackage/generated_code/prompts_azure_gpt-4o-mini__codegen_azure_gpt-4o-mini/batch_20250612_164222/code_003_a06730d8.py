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
from tkinter import messagebox, ttk

class CarRentalBookingManager:
    def __init__(self, root):
        """Initialize the main application window and components."""
        self.root = root
        self.root.title("Car Rental Booking Manager")
        self.root.geometry("600x400")

        # Create a frame for the booking management
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Booking details
        self.create_widgets()

    def create_widgets(self):
        """Create and layout the UI components."""
        # Label for booking ID
        ttk.Label(self.frame, text="Booking ID:").grid(column=0, row=0, sticky=tk.W)
        self.booking_id_entry = ttk.Entry(self.frame)
        self.booking_id_entry.grid(column=1, row=0, sticky=tk.W)

        # Label for car type
        ttk.Label(self.frame, text="Car Type:").grid(column=0, row=1, sticky=tk.W)
        self.car_type_entry = ttk.Entry(self.frame)
        self.car_type_entry.grid(column=1, row=1, sticky=tk.W)

        # Label for rental date
        ttk.Label(self.frame, text="Rental Date:").grid(column=0, row=2, sticky=tk.W)
        self.rental_date_entry = ttk.Entry(self.frame)
        self.rental_date_entry.grid(column=1, row=2, sticky=tk.W)

        # Buttons for managing bookings
        self.add_button = ttk.Button(self.frame, text="Add Booking", command=self.add_booking)
        self.add_button.grid(column=0, row=3, sticky=tk.W)

        self.update_button = ttk.Button(self.frame, text="Update Booking", command=self.update_booking)
        self.update_button.grid(column=1, row=3, sticky=tk.W)

        self.delete_button = ttk.Button(self.frame, text="Delete Booking", command=self.delete_booking)
        self.delete_button.grid(column=2, row=3, sticky=tk.W)

        # Treeview for displaying bookings
        self.booking_tree = ttk.Treeview(self.frame, columns=("Booking ID", "Car Type", "Rental Date"), show='headings')
        self.booking_tree.heading("Booking ID", text="Booking ID")
        self.booking_tree.heading("Car Type", text="Car Type")
        self.booking_tree.heading("Rental Date", text="Rental Date")
        self.booking_tree.grid(column=0, row=4, columnspan=3, sticky=tk.W + tk.E)

    def add_booking(self):
        """Add a new booking to the list."""
        booking_id = self.booking_id_entry.get()
        car_type = self.car_type_entry.get()
        rental_date = self.rental_date_entry.get()

        if not booking_id or not car_type or not rental_date:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        self.booking_tree.insert("", "end", values=(booking_id, car_type, rental_date))
        self.clear_entries()

    def update_booking(self):
        """Update the selected booking."""
        selected_item = self.booking_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a booking to update.")
            return

        booking_id = self.booking_id_entry.get()
        car_type = self.car_type_entry.get()
        rental_date = self.rental_date_entry.get()

        if not booking_id or not car_type or not rental_date:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        self.booking_tree.item(selected_item, values=(booking_id, car_type, rental_date))
        self.clear_entries()

    def delete_booking(self):
        """Delete the selected booking."""
        selected_item = self.booking_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a booking to delete.")
            return

        self.booking_tree.delete(selected_item)

    def clear_entries(self):
        """Clear the input fields."""
        self.booking_id_entry.delete(0, tk.END)
        self.car_type_entry.delete(0, tk.END)
        self.rental_date_entry.delete(0, tk.END)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = CarRentalBookingManager(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Application Error", f"An error occurred: {str(e)}")
```
