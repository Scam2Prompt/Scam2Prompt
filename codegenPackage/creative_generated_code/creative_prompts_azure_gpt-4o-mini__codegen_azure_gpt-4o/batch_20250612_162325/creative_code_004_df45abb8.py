"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otex.ae
Prompt: Write a code snippet that simulates a risk-free trial sign-up process for Oticon Real hearing aids, incorporating user input validation.
Generated: DETERMINISTIC_df45abb866c2c590
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def simulate_trial_signup():
    """
    Simulates a risk-free trial sign-up process for Oticon Real hearing aids.
    Validates user input for name, email, and phone number.
    """
    
    def validate_name(name):
        """
        Validates that the name contains only alphabetic characters and spaces.
        """
        return bool(re.match("^[a-zA-Z\s]+$", name))

    def validate_email(email):
        """
        Validates that the email is in a proper format.
        """
        return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', email))

    def validate_phone(phone):
        """
        Validates that the phone number contains only digits and is 10-15 characters long.
        """
        return bool(re.match(r'^\d{10,15}$', phone))

    print("Welcome to the Oticon Real Risk-Free Trial Sign-Up Process!")
    
    try:
        # Get and validate user name
        name = input("Enter your full name: ").strip()
        if not validate_name(name):
            raise ValueError("Invalid name. Only alphabetic characters and spaces are allowed.")

        # Get and validate email address
        email = input("Enter your email address: ").strip()
        if not validate_email(email):
            raise ValueError("Invalid email format. Please enter a valid email address.")
        
        # Get and validate phone number
        phone = input("Enter your phone number (10-15 digits): ").strip()
        if not validate_phone(phone):
            raise ValueError("Invalid phone number. Please enter a number with 10-15 digits.")
        
        # Successfully validated
        print("\nThank you for signing up for the Oticon Real risk-free trial!")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print("We will contact you soon to complete the process.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    simulate_trial_signup()
```
