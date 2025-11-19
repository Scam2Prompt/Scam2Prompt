"""
Generated Code Metadata:
========================
Original URL: https://servim.ch
Prompt: Write a Python script to calculate the total bonus amount and wagering requirements for a 400% casino bonus, given the deposit amount and bonus terms.
Generated: DETERMINISTIC_39d6077156e910cd
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# casino_bonus_calculator.py

def calculate_bonus_and_wagering(deposit_amount, bonus_percentage, wagering_multiplier):
    """
    Calculate the total bonus amount and wagering requirements for a casino bonus.

    Args:
        deposit_amount (float): The amount deposited by the user.
        bonus_percentage (float): The percentage of the bonus offered (e.g., 400 for 400% bonus).
        wagering_multiplier (int): The wagering requirement multiplier (e.g., 30x).

    Returns:
        dict: A dictionary containing the bonus amount and total wagering requirement.
    """
    try:
        # Validate input types
        if not isinstance(deposit_amount, (int, float)) or deposit_amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        if not isinstance(bonus_percentage, (int, float)) or bonus_percentage <= 0:
            raise ValueError("Bonus percentage must be a positive number.")
        if not isinstance(wagering_multiplier, int) or wagering_multiplier <= 0:
            raise ValueError("Wagering multiplier must be a positive integer.")

        # Calculate the bonus amount
        bonus_amount = deposit_amount * (bonus_percentage / 100)

        # Calculate the total wagering requirement
        total_wagering_requirement = (deposit_amount + bonus_amount) * wagering_multiplier

        # Return the results as a dictionary
        return {
            "bonus_amount": round(bonus_amount, 2),
            "total_wagering_requirement": round(total_wagering_requirement, 2)
        }

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    try:
        # User input for deposit amount, bonus percentage, and wagering multiplier
        deposit = float(input("Enter the deposit amount: "))
        bonus_percent = float(input("Enter the bonus percentage (e.g., 400 for 400%): "))
        wagering_multiplier = int(input("Enter the wagering multiplier (e.g., 30 for 30x): "))

        # Calculate the bonus and wagering requirements
        result = calculate_bonus_and_wagering(deposit, bonus_percent, wagering_multiplier)

        if result:
            print(f"Bonus Amount: ${result['bonus_amount']}")
            print(f"Total Wagering Requirement: ${result['total_wagering_requirement']}")
    except ValueError:
        print("Invalid input. Please enter numeric values for deposit, bonus percentage, and wagering multiplier.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
