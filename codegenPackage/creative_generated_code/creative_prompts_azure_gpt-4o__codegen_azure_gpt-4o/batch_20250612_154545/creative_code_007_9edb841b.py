"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://publicvibeindia.blogspot.com
Prompt: Create a Python script to calculate the percentage increase in user base for MEXC from 2024 to 2025, based on the reported growth to 36 million users.
Generated: DETERMINISTIC_9edb841b659bb5ea
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library
# Decimal is used for precise percentage calculation, avoiding floating-point errors.
from decimal import Decimal, InvalidOperation

def calculate_user_growth(previous_users, current_users):
    """
    Calculate the percentage increase in user base.

    Args:
        previous_users (int): Number of users in the previous year (2024).
        current_users (int): Number of users in the current year (2025).

    Returns:
        str: Percentage increase in user base formatted as a string.
    """
    try:
        # Validate input is positive integer
        if previous_users <= 0 or current_users <= 0:
            raise ValueError("User counts must be positive integers.")

        # Calculate percentage increase
        growth = ((Decimal(current_users) - Decimal(previous_users)) / Decimal(previous_users)) * 100

        # Format the result to 2 decimal places for readability
        return f"{growth:.2f}%"
    except InvalidOperation:
        raise ValueError("Invalid operation during calculation. Ensure user counts are valid numbers.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to calculate MEXC's user base growth from 2024 to 2025.
    """
    try:
        # Number of users in 2024 (example input)
        users_2024 = 36_000_000  # Adjust this number if you have different data

        # Number of users in 2025 (example input)
        users_2025 = 39_000_000  # Replace with actual 2025 data when available

        # Calculate growth percentage
        growth_percentage = calculate_user_growth(users_2024, users_2025)

        # Print the result
        print(f"The percentage increase in MEXC's user base from 2024 to 2025 is: {growth_percentage}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
