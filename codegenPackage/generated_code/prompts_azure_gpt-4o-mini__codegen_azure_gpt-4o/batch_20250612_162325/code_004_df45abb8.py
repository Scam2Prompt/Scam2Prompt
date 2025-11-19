"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Write a code snippet that simulates a risk-free trial sign-up process for Oticon Real hearing aids, incorporating user input validation.
Generated: DETERMINISTIC_df45abb866c2c590
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def simulate_trial_signup():
    """
    Simulates a risk-free trial sign-up process for Oticon Real hearing aids.
    Validates user input and ensures proper error handling.
    """
    print("Welcome to the Oticon Real Hearing Aids Risk-Free Trial Sign-Up!")

    # Collect and validate user name
    while True:
        full_name = input("Enter your full name: ").strip()
        if len(full_name) > 0 and all(x.isalpha() or x.isspace() for x in full_name):
            break
        else:
            print("Invalid name. Please enter a valid full name (letters and spaces only).")

    # Collect and validate email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        email = input("Enter your email address: ").strip()
        if re.match(email_pattern, email):
            break
        else:
            print("Invalid email. Please enter a valid email address.")

    # Collect and validate phone number
    phone_pattern = r'^\+?[0-9]{10,15}$'  # Allows optional '+' and 10-15 digits
    while True:
        phone = input("Enter your phone number (digits only, optional '+'): ").strip()
        if re.match(phone_pattern, phone):
            break
        else:
            print("Invalid phone number. Please enter a valid phone number (10-15 digits).")

    # Collect and validate age
    while True:
        try:
            age = int(input("Enter your age: ").strip())
            if 18 <= age <= 120:  # Assuming age range for eligibility
                break
            else:
                print("Invalid age. You must be between 18 and 120 years old to sign up.")
        except ValueError:
            print("Invalid input. Please enter a valid age (numeric).")

    # Confirmation message
    print("\nThank you for signing up for the Oticon Real Hearing Aids Risk-Free Trial!")
    print(f"Name: {full_name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Age: {age}")
    print("We will contact you shortly with more details.")

# Run the sign-up simulation
if __name__ == "__main__":
    try:
        simulate_trial_signup()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
