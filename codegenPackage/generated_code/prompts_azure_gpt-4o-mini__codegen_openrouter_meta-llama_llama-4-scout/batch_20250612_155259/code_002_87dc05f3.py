"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: Write a code snippet to create a registration form for the short courses offered at SMA Rizvi Textile Institute, including fields for name, course selection, and contact information.
Generated: DETERMINISTIC_87dc05f359d819bb
Batch ID: 20250612_155259
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

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Short Course Registration Form")
        self.root.geometry("500x300")

        # Create main form frame
        self.form_frame = ttk.Frame(self.root, padding="10")
        self.form_frame.pack(fill="both", expand=True)

        # Create form fields
        self.name_label = ttk.Label(self.form_frame, text="Name:")
        self.name_label.grid(column=0, row=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.form_frame, width=30)
        self.name_entry.grid(column=1, row=0, padx=5, pady=5)

        self.course_label = ttk.Label(self.form_frame, text="Course:")
        self.course_label.grid(column=0, row=1, padx=5, pady=5)
        self.course_var = tk.StringVar()
        self.course_option = ttk.Combobox(self.form_frame, textvariable=self.course_var)
        self.course_option['values'] = (
            "Textile Design",
            "Fashion Design",
            "Apparel Manufacturing",
            "Textile Testing and Quality Control",
            "Other (please specify)"
        )
        self.course_option.grid(column=1, row=1, padx=5, pady=5)
        self.course_other = ttk.Entry(self.form_frame, width=20)
        self.course_other.grid(column=2, row=1, padx=5, pady=5)

        self.email_label = ttk.Label(self.form_frame, text="Email:")
        self.email_label.grid(column=0, row=2, padx=5, pady=5)
        self.email_entry = ttk.Entry(self.form_frame, width=30)
        self.email_entry.grid(column=1, row=2, padx=5, pady=5)

        self.phone_label = ttk.Label(self.form_frame, text="Phone:")
        self.phone_label.grid(column=0, row=3, padx=5, pady=5)
        self.phone_entry = ttk.Entry(self.form_frame, width=30)
        self.phone_entry.grid(column=1, row=3, padx=5, pady=5)

        # Create submit button
        self.submit_button = ttk.Button(self.form_frame, text="Submit", command=self.submit_form)
        self.submit_button.grid(column=1, row=4, padx=5, pady=5)

    def submit_form(self):
        name = self.name_entry.get()
        course = self.course_var.get()
        if course == "Other (please specify)":
            course = self.course_other.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not name or not course or not email or not phone:
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        try:
            # Here you would put your code to save the data to a database or file
            # For now, just print the data
            print("Name:", name)
            print("Course:", course)
            print("Email:", email)
            print("Phone:", phone)
            messagebox.showinfo("Success", "Form submitted successfully.")
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.course_var.set("")
        self.course_other.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
```
