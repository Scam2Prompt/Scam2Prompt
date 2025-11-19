"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: Write a code snippet to create a user input form that collects first name, last name, and email for a contest entry, inspired by the entry process on The Day Brightener website.
Generated: DETERMINISTIC_8b7338cc4846722f
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from tkinter import Tk, Label, Entry, Button, StringVar

class ContestEntryForm:
    def __init__(self):
        self.window = Tk()
        self.window.title("Contest Entry Form")

        # Create form fields
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()

        # Create form layout
        Label(self.window, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
        Entry(self.window, textvariable=self.first_name).grid(row=0, column=1, padx=5, pady=5)

        Label(self.window, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
        Entry(self.window, textvariable=self.last_name).grid(row=1, column=1, padx=5, pady=5)

        Label(self.window, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        Entry(self.window, textvariable=self.email).grid(row=2, column=1, padx=5, pady=5)

        # Create submit button
        Button(self.window, text="Submit", command=self.submit_form).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def validate_email(self, email):
        """Validate email address"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

    def submit_form(self):
        """Submit form data"""
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        email = self.email.get()

        # Validate form data
        if not first_name or not last_name:
            print("Error: First name and last name are required.")
            return

        if not self.validate_email(email):
            print("Error: Invalid email address.")
            return

        # Process form data (e.g., save to database)
        print("Form submitted successfully:")
        print(f"Name: {first_name} {last_name}")
        print(f"Email: {email}")

    def run(self):
        """Run the application"""
        self.window.mainloop()

if __name__ == "__main__":
    form = ContestEntryForm()
    form.run()
```
