"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hypersteakin.site
Prompt: Write a Python script to simulate a registration form for the HyperSteakin Gaming Summit, including fields for name, email, company, job title, and pass type selection, as described on the website.
Generated: DETERMINISTIC_3dc97311ff570227
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class RegistrationForm:
    def __init__(self):
        self.fields = {
            "name": "",
            "email": "",
            "company": "",
            "job_title": "",
            "pass_type": ""
        }
        self.pass_types = ["Standard", "VIP", "Student"]

    def collect_input(self):
        """Collect user input for registration."""
        print("Welcome to the HyperSteakin Gaming Summit Registration Form\n")
        self.fields["name"] = self.get_name()
        self.fields["email"] = self.get_email()
        self.fields["company"] = input("Enter your company: ")
        self.fields["job_title"] = input("Enter your job title: ")
        self.fields["pass_type"] = self.get_pass_type()

    def get_name(self):
        """Get user's name and validate it."""
        while True:
            name = input("Enter your name: ")
            if name.strip():
                return name
            print("Name cannot be empty. Please try again.")

    def get_email(self):
        """Get user's email and validate it using regex."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        while True:
            email = input("Enter your email: ")
            if re.match(email_regex, email):
                return email
            print("Invalid email format. Please try again.")

    def get_pass_type(self):
        """Get user's pass type selection."""
        print("Select your pass type:")
        for i, pass_type in enumerate(self.pass_types, start=1):
            print(f"{i}. {pass_type}")

        while True:
            try:
                choice = int(input("Enter the number corresponding to your choice: "))
                if 1 <= choice <= len(self.pass_types):
                    return self.pass_types[choice - 1]
                print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_registration(self):
        """Display the user's registration details."""
        print("\nRegistration Details:")
        for field, value in self.fields.items():
            print(f"{field.capitalize()}: {value}")

    def run(self):
        """Run the registration process."""
        self.collect_input()
        self.display_registration()

if __name__ == "__main__":
    try:
        form = RegistrationForm()
        form.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
