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
# Import required libraries
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class PropertyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Property Management System")
        self.root.geometry("800x600")

        # Create database connection
        self.conn = sqlite3.connect("property_management.db")
        self.cursor = self.conn.cursor()

        # Create tables if not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS properties
            (id INTEGER PRIMARY KEY, address TEXT, owner_id INTEGER)
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS payments
            (id INTEGER PRIMARY KEY, property_id INTEGER, amount REAL, date TEXT)
        """)
        self.conn.commit()

        # Create notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Create frames
        self.login_frame = tk.Frame(self.notebook)
        self.owner_frame = tk.Frame(self.notebook)
        self.renter_frame = tk.Frame(self.notebook)

        # Add frames to notebook
        self.notebook.add(self.login_frame, text="Login")
        self.notebook.add(self.owner_frame, text="Owner")
        self.notebook.add(self.renter_frame, text="Renter")

        # Login frame
        self.login_username_label = tk.Label(self.login_frame, text="Username:")
        self.login_username_label.pack()
        self.login_username_entry = tk.Entry(self.login_frame)
        self.login_username_entry.pack()
        self.login_password_label = tk.Label(self.login_frame, text="Password:")
        self.login_password_label.pack()
        self.login_password_entry = tk.Entry(self.login_frame, show="*")
        self.login_password_entry.pack()
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack()

        # Owner frame
        self.owner_properties_label = tk.Label(self.owner_frame, text="Properties:")
        self.owner_properties_label.pack()
        self.owner_properties_listbox = tk.Listbox(self.owner_frame)
        self.owner_properties_listbox.pack()
        self.owner_make_payment_button = tk.Button(self.owner_frame, text="Make Payment", command=self.owner_make_payment)
        self.owner_make_payment_button.pack()
        self.owner_view_property_info_button = tk.Button(self.owner_frame, text="View Property Info", command=self.owner_view_property_info)
        self.owner_view_property_info_button.pack()

        # Renter frame
        self.renter_properties_label = tk.Label(self.renter_frame, text="Properties:")
        self.renter_properties_label.pack()
        self.renter_properties_listbox = tk.Listbox(self.renter_frame)
        self.renter_properties_listbox.pack()
        self.renter_make_payment_button = tk.Button(self.renter_frame, text="Make Payment", command=self.renter_make_payment)
        self.renter_make_payment_button.pack()
        self.renter_view_property_info_button = tk.Button(self.renter_frame, text="View Property Info", command=self.renter_view_property_info)
        self.renter_view_property_info_button.pack()

    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()
        if user:
            if user[3] == "owner":
                self.owner_frame.tkraise()
                self.update_owner_properties_listbox()
            elif user[3] == "renter":
                self.renter_frame.tkraise()
                self.update_renter_properties_listbox()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def update_owner_properties_listbox(self):
        self.owner_properties_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM properties WHERE owner_id=?", (1,))
        properties = self.cursor.fetchall()
        for property in properties:
            self.owner_properties_listbox.insert(tk.END, property[1])

    def owner_make_payment(self):
        try:
            property_index = self.owner_properties_listbox.curselection()[0]
            property_address = self.owner_properties_listbox.get(property_index)
            self.cursor.execute("SELECT * FROM properties WHERE address=?", (property_address,))
            property = self.cursor.fetchone()
            payment_amount = float(input("Enter payment amount: "))
            self.cursor.execute("INSERT INTO payments (property_id, amount, date) VALUES (?, ?, date('now'))", (property[0], payment_amount))
            self.conn.commit()
            messagebox.showinfo("Success", "Payment made successfully")
        except:
            messagebox.showerror("Error", "Error making payment")

    def owner_view_property_info(self):
        try:
            property_index = self.owner_properties_listbox.curselection()[0]
            property_address = self.owner_properties_listbox.get(property_index)
            self.cursor.execute("SELECT * FROM properties WHERE address=?", (property_address,))
            property = self.cursor.fetchone()
            messagebox.showinfo("Property Info", f"Address: {property[1]}\nOwner ID: {property[2]}")
        except:
            messagebox.showerror("Error", "Error viewing property info")

    def update_renter_properties_listbox(self):
        self.renter_properties_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM properties")
        properties = self.cursor.fetchall()
        for property in properties:
            self.renter_properties_listbox.insert(tk.END, property[1])

    def renter_make_payment(self):
        try:
            property_index = self.renter_properties_listbox.curselection()[0]
            property_address = self.renter_properties_listbox.get(property_index)
            self.cursor.execute("SELECT * FROM properties WHERE address=?", (property_address,))
            property = self.cursor.fetchone()
            payment_amount = float(input("Enter payment amount: "))
            self.cursor.execute("INSERT INTO payments (property_id, amount, date) VALUES (?, ?, date('now'))", (property[0], payment_amount))
            self.conn.commit()
            messagebox.showinfo("Success", "Payment made successfully")
        except:
            messagebox.showerror("Error", "Error making payment")

    def renter_view_property_info(self):
        try:
            property_index = self.renter_properties_listbox.curselection()[0]
            property_address = self.renter_properties_listbox.get(property_index)
            self.cursor.execute("SELECT * FROM properties WHERE address=?", (property_address,))
            property = self.cursor.fetchone()
            messagebox.showinfo("Property Info", f"Address: {property[1]}\nOwner ID: {property[2]}")
        except:
            messagebox.showerror("Error", "Error viewing property info")

if __name__ == "__main__":
    root = tk.Tk()
    app = PropertyManagementSystem(root)
    root.mainloop()
```
