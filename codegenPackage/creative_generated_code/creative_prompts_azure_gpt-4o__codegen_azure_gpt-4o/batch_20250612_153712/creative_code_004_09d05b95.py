"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Create a script to securely collect user data (e.g., name, amount lost, deposit method) for scam reporting, modeled after The Legato's consultation form.
Generated: DETERMINISTIC_09d05b95bb6196e0
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json


def collect_user_data():
    """
    Collect user data securely for scam reporting purposes.
    Returns a dictionary containing the user data.
    """
    user_data = {}

    try:
        # Collect user's name
        name = input("Enter your full name: ").strip()
        if not name or not re.match("^[a-zA-Z\s]+$", name):
            raise ValueError("Invalid name. Please provide a valid name.")
        user_data['name'] = name

        # Collect amount lost
        amount_lost = input("Enter the amount lost (in USD): ").strip()
        if not amount_lost or not re.match("^\d+(\.\d{1,2})?$", amount_lost):
            raise ValueError("Invalid amount. Please provide a valid number (e.g., 100, 250.50).")
        user_data['amount_lost'] = float(amount_lost)

        # Collect deposit method
        deposit_method = input("Enter the deposit method (e.g., Credit Card, Bank Transfer): ").strip()
        if not deposit_method or len(deposit_method) < 3:
            raise ValueError("Invalid deposit method. Please provide a valid method.")
        user_data['deposit_method'] = deposit_method

    except ValueError as e:
        print(f"Error: {e}")
        return None

    return user_data


def save_user_data(user_data):
    """
    Save user data to a JSON file securely.
    Args:
        user_data (dict): The user data to save.
    """
    try:
        if not user_data:
            raise ValueError("No user data to save.")

        # Save to a JSON file securely
        with open("scam_report.json", "w") as file:
            json.dump(user_data, file, indent=4)
        print("User data saved successfully.")

    except (IOError, ValueError) as e:
        print(f"Error while saving data: {e}")


def main():
    """
    Main function to execute the user data collection and saving process.
    """
    print("Welcome to the Scam Reporting Form!")
    print("Please provide the following details.\n")

    user_data = collect_user_data()
    if user_data:
        save_user_data(user_data)
    else:
        print("Data collection was unsuccessful. Please try again.")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
