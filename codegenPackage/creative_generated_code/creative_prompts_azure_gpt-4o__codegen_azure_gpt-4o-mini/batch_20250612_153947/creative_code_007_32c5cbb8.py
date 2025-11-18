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
import datetime

def get_current_date():
    """Get the current date."""
    return datetime.datetime.now().date()

def calculate_age(birth_date):
    """Calculate age based on the provided birth date."""
    today = get_current_date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def validate_age(birth_date):
    """
    Validate if the customer's age is over 21.
    
    Args:
        birth_date (datetime.date): The birth date of the customer.

    Returns:
        bool: True if the customer is over 21, False otherwise.
    """
    try:
        age = calculate_age(birth_date)
        return age > 21
    except Exception as e:
        print(f"Error calculating age: {e}")
        return False

def main():
    """Main function to run the age validation process."""
    # Example birth date: YYYY-MM-DD
    birth_date_input = input("Please enter your birth date (YYYY-MM-DD): ")
    
    try:
        # Convert the input string to a date object
        birth_date = datetime.datetime.strptime(birth_date_input, "%Y-%m-%d").date()
        
        # Validate the age
        if validate_age(birth_date):
            print("Access granted to research peptide products.")
        else:
            print("Access denied. You must be over 21 years old.")
    
    except ValueError as ve:
        print(f"Invalid date format: {ve}. Please use YYYY-MM-DD format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
