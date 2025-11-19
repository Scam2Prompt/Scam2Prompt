"""
Generated Code Metadata:
========================
Original URL: https://jsa.academy
Prompt: How can I write a code snippet to create a volunteer registration form for a sports academy similar to Jambalaya Soccer Academy?
Generated: DETERMINISTIC_c98d7a530e535622
Batch ID: 20250612_162051
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
from tkinter import messagebox

class VolunteerRegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Volunteer Registration Form")

        # Create main frames
        self.personal_info_frame = tk.Frame(self.root)
        self.personal_info_frame.pack(padx=10, pady=10)

        self.contact_info_frame = tk.Frame(self.root)
        self.contact_info_frame.pack(padx=10, pady=10)

        self.availability_frame = tk.Frame(self.root)
        self.availability_frame.pack(padx=10, pady=10)

        self.submit_frame = tk.Frame(self.root)
        self.submit_frame.pack(padx=10, pady=10)

        # Personal Info Frame
        tk.Label(self.personal_info_frame, text="Personal Information").grid(row=0, column=0, columnspan=2)

        tk.Label(self.personal_info_frame, text="First Name:").grid(row=1, column=0)
        self.first_name_entry = tk.Entry(self.personal_info_frame)
        self.first_name_entry.grid(row=1, column=1)

        tk.Label(self.personal_info_frame, text="Last Name:").grid(row=2, column=0)
        self.last_name_entry = tk.Entry(self.personal_info_frame)
        self.last_name_entry.grid(row=2, column=1)

        tk.Label(self.personal_info_frame, text="Date of Birth:").grid(row=3, column=0)
        self.dob_entry = tk.Entry(self.personal_info_frame)
        self.dob_entry.grid(row=3, column=1)

        # Contact Info Frame
        tk.Label(self.contact_info_frame, text="Contact Information").grid(row=0, column=0, columnspan=2)

        tk.Label(self.contact_info_frame, text="Email:").grid(row=1, column=0)
        self.email_entry = tk.Entry(self.contact_info_frame)
        self.email_entry.grid(row=1, column=1)

        tk.Label(self.contact_info_frame, text="Phone Number:").grid(row=2, column=0)
        self.phone_number_entry = tk.Entry(self.contact_info_frame)
        self.phone_number_entry.grid(row=2, column=1)

        tk.Label(self.contact_info_frame, text="Address:").grid(row=3, column=0)
        self.address_entry = tk.Text(self.contact_info_frame, height=3, width=20)
        self.address_entry.grid(row=3, column=1)

        # Availability Frame
        tk.Label(self.availability_frame, text="Availability").grid(row=0, column=0, columnspan=2)

        tk.Label(self.availability_frame, text="Available Days:").grid(row=1, column=0)
        self.available_days = tk.StringVar(self.availability_frame)
        self.available_days.set("Monday")  # default value
        options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.available_days_menu = tk.OptionMenu(self.availability_frame, self.available_days, *options)
        self.available_days_menu.grid(row=1, column=1)

        tk.Label(self.availability_frame, text="Available Time:").grid(row=2, column=0)
        self.available_time_entry = tk.Entry(self.availability_frame)
        self.available_time_entry.grid(row=2, column=1)

        # Submit Frame
        self.submit_button = tk.Button(self.submit_frame, text="Submit", command=self.submit_form)
        self.submit_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(self.submit_frame, text="Clear", command=self.clear_form)
        self.clear_button.pack(side=tk.LEFT)

    def submit_form(self):
        try:
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            dob = self.dob_entry.get()
            email = self.email_entry.get()
            phone_number = self.phone_number_entry.get()
            address = self.address_entry.get("1.0", tk.END)
            available_days = self.available_days.get()
            available_time = self.available_time_entry.get()

            if not all([first_name, last_name, dob, email, phone_number, address, available_days, available_time]):
                messagebox.showerror("Error", "Please fill out all fields")
                return

            # Save data to file or database
            with open("volunteer_registration.txt", "a") as file:
                file.write(f"Name: {first_name} {last_name}\n")
                file.write(f"Date of Birth: {dob}\n")
                file.write(f"Email: {email}\n")
                file.write(f"Phone Number: {phone_number}\n")
                file.write(f"Address: {address}\n")
                file.write(f"Available Days: {available_days}\n")
                file.write(f"Available Time: {available_time}\n\n")

            messagebox.showinfo("Success", "Form submitted successfully")
            self.clear_form()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.address_entry.delete("1.0", tk.END)
        self.available_days.set("Monday")
        self.available_time_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VolunteerRegistrationForm(root)
    root.mainloop()
```
