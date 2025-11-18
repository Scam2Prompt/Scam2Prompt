"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bllabs.co
Prompt: Write a script to validate customer age (over 21 years old) before allowing access to research peptide products, similar to the age verification system on BioLongevity Labs.
Generated: DETERMINISTIC_32c5cbb8ce6792b5
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from datetime import datetime

def validate_age(date_of_birth):
    """
    Validates if a customer is over 21 years old based on their date of birth.

    Args:
        date_of_birth (str): Date of birth in the format 'YYYY-MM-DD'.

    Returns:
        bool: True if the customer is over 21 years old, False otherwise.
    """
    try:
        # Convert the input string to a datetime object
        dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
    except ValueError:
        # Handle invalid date format
        print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")
        return False

    # Calculate age
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    # Return True if age is 21 or older, otherwise False
    return age >= 21

def main():
    """
    Main function to handle user input and age validation.
    """
    print("Welcome to BioLongevity Labs!")
    print("Please verify your age before accessing peptide products.")
    
    # Get date of birth from user
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

    # Validate age
    if validate_age(date_of_birth):
        print("Access granted. You are eligible to view peptide products.")
    else:
        print("Access denied. You must be at least 21 years old.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
