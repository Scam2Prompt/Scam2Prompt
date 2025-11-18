"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://currency-connect.com
Prompt: Create a script to automate the process of registering a law firm for a currency exchange service like Currency Connect, including input validation for firm details.
Generated: DETERMINISTIC_5d9a6cf3b35e8679
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def register_law_firm():
    """
    Automates the process of registering a law firm for a currency exchange service.
    Collects and validates law firm details before registering.
    """
    
    print("Welcome to the Law Firm Registration Process for Currency Exchange Service")

    # Function to validate the firm name
    def validate_firm_name(name):
        if len(name) < 3:
            raise ValueError("Firm name must be at least 3 characters long.")
        return name

    # Function to validate the email address
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email address format.")
        return email

    # Function to validate the phone number (basic validation for digits and length)
    def validate_phone(phone):
        if len(phone) < 10 or not phone.isdigit():
            raise ValueError("Phone number must be at least 10 digits and contain only numbers.")
        return phone

    # Function to validate the firm's registration number
    def validate_registration_number(reg_number):
        if len(reg_number) < 5:
            raise ValueError("Registration number must be at least 5 characters long.")
        return reg_number

    # Collect firm information
    try:
        firm_name = input("Enter the firm's name: ").strip()
        firm_name = validate_firm_name(firm_name)

        firm_email = input("Enter the firm's email address: ").strip()
        firm_email = validate_email(firm_email)

        firm_phone = input("Enter the firm's phone number: ").strip()
        firm_phone = validate_phone(firm_phone)

        firm_registration_number = input("Enter the firm's registration number: ").strip()
        firm_registration_number = validate_registration_number(firm_registration_number)

        # Confirm registration details
        print("\nRegistration Details:")
        print(f"Firm Name: {firm_name}")
        print(f"Email Address: {firm_email}")
        print(f"Phone Number: {firm_phone}")
        print(f"Registration Number: {firm_registration_number}")

        confirmation = input("\nConfirm registration? (yes/no): ").strip().lower()
        if confirmation != 'yes':
            print("Registration process aborted.")
            return

        # Simulate successful registration
        print("\nRegistering law firm...")
        # In a production environment, here is where you would call the API or save the details to the database.
        print("Law firm registered successfully!")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    register_law_firm()
```
