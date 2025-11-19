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
# car_rental_booking_ui.py

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class CarRentalBookingUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Rental Booking Management")
        self.bookings = {}

        # Create tabs
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(expand=1, fill="both")

        self.booking_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.booking_tab, text="Bookings")

        self.make_booking_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.make_booking_tab, text="Make a Booking")

        self.cancel_booking_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.cancel_booking_tab, text="Cancel a Booking")

        # Booking tab
        self.booking_tree = ttk.Treeview(self.booking_tab)

        self.booking_tree["columns"] = ("pickup", "dropoff", "car_type")

        self.booking_tree.column("#0", width=0, stretch=tk.NO)
        self.booking_tree.column("pickup", anchor=tk.W, width=100)
        self.booking_tree.column("dropoff", anchor=tk.W, width=100)
        self.booking_tree.column("car_type", anchor=tk.W, width=100)

        self.booking_tree.heading("#0", text="", anchor=tk.W)
        self.booking_tree.heading("pickup", text="Pickup Date", anchor=tk.W)
        self.booking_tree.heading("dropoff", text="Dropoff Date", anchor=tk.W)
        self.booking_tree.heading("car_type", text="Car Type", anchor=tk.W)

        self.booking_tree.pack(fill="both", expand=True)

        # Make booking tab
        self.make_booking_form()

        # Cancel booking tab
        self.cancel_booking_form()

    def make_booking_form(self):
        # Create form fields
        tk.Label(self.make_booking_tab, text="Pickup Date").grid(row=0, column=0, padx=5, pady=5)
        self.pickup_date_entry = tk.Entry(self.make_booking_tab)
        self.pickup_date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.make_booking_tab, text="Dropoff Date").grid(row=1, column=0, padx=5, pady=5)
        self.dropoff_date_entry = tk.Entry(self.make_booking_tab)
        self.dropoff_date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.make_booking_tab, text="Car Type").grid(row=2, column=0, padx=5, pady=5)
        self.car_type_var = tk.StringVar()
        self.car_type_menu = ttk.Combobox(self.make_booking_tab, textvariable=self.car_type_var)
        self.car_type_menu["values"] = ("Sedan", "SUV", "Truck")
        self.car_type_menu.grid(row=2, column=1, padx=5, pady=5)

        # Create submit button
        self.make_booking_button = tk.Button(self.make_booking_tab, text="Make Booking", command=self.make_booking)
        self.make_booking_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def cancel_booking_form(self):
        # Create form fields
        tk.Label(self.cancel_booking_tab, text="Booking ID").grid(row=0, column=0, padx=5, pady=5)
        self.booking_id_entry = tk.Entry(self.cancel_booking_tab)
        self.booking_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create submit button
        self.cancel_booking_button = tk.Button(self.cancel_booking_tab, text="Cancel Booking", command=self.cancel_booking)
        self.cancel_booking_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def make_booking(self):
        try:
            pickup_date = datetime.strptime(self.pickup_date_entry.get(), "%Y-%m-%d").date()
            dropoff_date = datetime.strptime(self.dropoff_date_entry.get(), "%Y-%m-%d").date()
            car_type = self.car_type_var.get()

            if pickup_date >= dropoff_date:
                messagebox.showerror("Invalid Dates", "Pickup date must be before dropoff date")
                return

            booking_id = len(self.bookings) + 1
            self.bookings[booking_id] = {
                "pickup": pickup_date,
                "dropoff": dropoff_date,
                "car_type": car_type
            }

            self.booking_tree.insert("", "end", values=(pickup_date, dropoff_date, car_type))
            messagebox.showinfo("Booking Created", f"Booking {booking_id} created successfully")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please fill in all fields")

    def cancel_booking(self):
        try:
            booking_id = int(self.booking_id_entry.get())
            if booking_id in self.bookings:
                del self.bookings[booking_id]
                for row in self.booking_tree.get_children():
                    if self.booking_tree.item(row)["values"][0] == str(self.bookings[booking_id]["pickup"]):
                        self.booking_tree.delete(row)
                messagebox.showinfo("Booking Cancelled", f"Booking {booking_id} cancelled successfully")
            else:
                messagebox.showerror("Invalid Booking ID", "Booking ID not found")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid booking ID")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarRentalBookingUI(root)
    root.mainloop()
```
