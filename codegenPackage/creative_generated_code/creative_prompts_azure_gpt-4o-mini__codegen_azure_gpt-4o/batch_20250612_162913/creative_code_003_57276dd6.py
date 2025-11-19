"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://expressfinsbk.com
Prompt: Provide an example of how to implement a loan application form that collects valid information, based on the loan plans offered by Express Finance Banking.
Generated: DETERMINISTIC_57276dd6d5ba805e
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_email(email):
    """Validate email format using regular expressions."""
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_pattern, email) is not None

def validate_phone(phone):
    """Ensure phone number contains only digits and is 10 characters long."""
    return phone.isdigit() and len(phone) == 10

def validate_loan_amount(amount):
    """Ensure loan amount is a positive number."""
    return amount > 0

def get_loan_plans():
    """Return the loan plans offered by Express Finance Banking."""
    return {
        1: {"type": "Personal Loan", "min_amount": 5000, "max_amount": 50000},
        2: {"type": "Home Loan", "min_amount": 20000, "max_amount": 500000},
        3: {"type": "Car Loan", "min_amount": 10000, "max_amount": 100000},
    }

def display_loan_plans(plans):
    """Display the loan plans in a user-friendly format."""
    print("Available Loan Plans:")
    for plan_id, plan in plans.items():
        print(f"{plan_id}. {plan['type']} - Min: ${plan['min_amount']} Max: ${plan['max_amount']}")

def collect_loan_application():
    """Collect valid loan application information from the user."""
    print("Welcome to Express Finance Banking Loan Application Form")

    # Collect and validate name
    name = input("Enter your full name: ").strip()
    if not name:
        raise ValueError("Name cannot be empty.")

    # Collect and validate email
    email = input("Enter your email address: ").strip()
    if not validate_email(email):
        raise ValueError("Invalid email format.")

    # Collect and validate phone number
    phone = input("Enter your phone number (10 digits): ").strip()
    if not validate_phone(phone):
        raise ValueError("Phone number must be 10 digits.")

    # Display loan plans and collect loan type
    loan_plans = get_loan_plans()
    display_loan_plans(loan_plans)
    loan_type = int(input("Select a loan plan by entering the corresponding number: ").strip())
    if loan_type not in loan_plans:
        raise ValueError("Invalid loan plan selected.")

    # Collect and validate loan amount
    loan_amount = float(input(f"Enter the loan amount (min ${loan_plans[loan_type]['min_amount']} max ${loan_plans[loan_type]['max_amount']}): ").strip())
    if not validate_loan_amount(loan_amount) or not (loan_plans[loan_type]['min_amount'] <= loan_amount <= loan_plans[loan_type]['max_amount']):
        raise ValueError("Loan amount is out of the allowed range.")

    # Return collected data
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "loan_type": loan_plans[loan_type]["type"],
        "loan_amount": loan_amount,
    }

def main():
    """Main function to handle the loan application process."""
    try:
        application = collect_loan_application()
        print("Loan application submitted successfully!")
        print("Application Details:")
        for key, value in application.items():
            print(f"{key.replace('_', ' ').capitalize()}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
