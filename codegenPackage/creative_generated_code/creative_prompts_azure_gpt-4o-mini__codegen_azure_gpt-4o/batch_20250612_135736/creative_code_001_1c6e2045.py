"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaptimizer.com
Prompt: Write a Python script to automate the registration process for new members on an online gambling site, ensuring it includes bonus calculations as described by HOLYWIN69.
Generated: DETERMINISTIC_1c6e2045d1667867
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class RegistrationError(Exception):
    """Custom exception for registration errors."""
    pass


def validate_email(email):
    """
    Validates the given email address using a regular expression.
    :param email: str, email address to validate
    :return: bool, True if valid, otherwise False
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))


def calculate_bonus(initial_deposit):
    """
    Calculates the bonus based on the initial deposit.
    :param initial_deposit: float, the first deposit made by the user
    :return: float, the calculated bonus
    """
    if initial_deposit <= 0:
        raise ValueError("Initial deposit must be greater than zero.")
    
    # Bonus calculation logic (as per HOLYWIN69 rules)
    if initial_deposit < 100:
        bonus = initial_deposit * 0.10  # 10% bonus for deposits < $100
    elif initial_deposit <= 500:
        bonus = initial_deposit * 0.20  # 20% bonus for deposits between $100 and $500
    else:
        bonus = initial_deposit * 0.30  # 30% bonus for deposits > $500

    return bonus


def register_user(username, email, initial_deposit):
    """
    Simulates the registration process for a new member.
    :param username: str, the username chosen by the user
    :param email: str, the user's email address
    :param initial_deposit: float, the amount of the user's initial deposit
    :return: dict, success message and bonus details
    """
    # Validate inputs
    if not username or len(username) < 3:
        raise RegistrationError("Username must be at least 3 characters long.")
    if not validate_email(email):
        raise RegistrationError("Invalid email address provided.")
    if initial_deposit <= 0:
        raise RegistrationError("Initial deposit must be greater than zero.")

    # Calculate bonus
    bonus = calculate_bonus(initial_deposit)

    # Return success message and bonus details
    return {
        "message": "Registration successful!",
        "username": username,
        "email": email,
        "initial_deposit": initial_deposit,
        "bonus": bonus
    }


def main():
    """
    Main function to simulate user input and registration process.
    """
    print("Welcome to HOLYWIN69 Online Gambling Site!")
    
    try:
        # Simulate user input (replace with actual input gathering in production)
        username = input("Enter your username: ").strip()
        email = input("Enter your email address: ").strip()
        initial_deposit = float(input("Enter your initial deposit amount: ").strip())

        # Register user
        result = register_user(username, email, initial_deposit)

        # Display result
        print("\n--- Registration Summary ---")
        print(f"Message: {result['message']}")
        print(f"Username: {result['username']}")
        print(f"Email: {result['email']}")
        print(f"Initial Deposit: ${result['initial_deposit']:.2f}")
        print(f"Bonus: ${result['bonus']:.2f}")

    except RegistrationError as e:
        print(f"Registration failed: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
