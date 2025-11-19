"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: Write a Python script to create a simple sweepstakes entry form that collects first name, last name, address, city, state, zip, and email.
Generated: DETERMINISTIC_405a688e93e80089
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def validate_email(email):
    """
    Validates the format of an email address using a regular expression.
    Returns True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_zip(zip_code):
    """
    Validates the format of a ZIP code.
    Returns True if valid, False otherwise.
    """
    return zip_code.isdigit() and len(zip_code) in [5, 9]

def collect_sweepstakes_entry():
    """
    Collects user input for a sweepstakes entry form.
    Validates the input and returns a dictionary containing the entry data.
    """
    print("Welcome to the Sweepstakes Entry Form!")
    
    # Collect user input
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    address = input("Enter your address: ").strip()
    city = input("Enter your city: ").strip()
    state = input("Enter your state (2-letter abbreviation): ").strip().upper()
    zip_code = input("Enter your ZIP code: ").strip()
    email = input("Enter your email address: ").strip()
    
    # Validate inputs
    if not first_name or not last_name:
        print("Error: First name and last name are required.")
        return None
    
    if not address or not city or not state:
        print("Error: Address, city, and state are required.")
        return None
    
    if len(state) != 2:
        print("Error: State must be a 2-letter abbreviation.")
        return None
    
    if not validate_zip(zip_code):
        print("Error: Invalid ZIP code format. Must be 5 or 9 digits.")
        return None
    
    if not validate_email(email):
        print("Error: Invalid email address format.")
        return None
    
    # Create entry dictionary
    entry = {
        "First Name": first_name,
        "Last Name": last_name,
        "Address": address,
        "City": city,
        "State": state,
        "ZIP Code": zip_code,
        "Email": email
    }
    
    print("\nThank you for entering the sweepstakes!")
    return entry

if __name__ == "__main__":
    # Run the sweepstakes entry form
    entry_data = collect_sweepstakes_entry()
    if entry_data:
        print("\nYour entry details:")
        for key, value in entry_data.items():
            print(f"{key}: {value}")
```
