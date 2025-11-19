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
def calculate_bonus_and_wagering(deposit_amount, bonus_percentage, wagering_requirement):
    """
    Calculate the total bonus amount and wagering requirements for a casino bonus.

    Args:
        deposit_amount (float): The amount deposited by the user.
        bonus_percentage (float): The percentage of the bonus.
        wagering_requirement (int): The number of times the bonus must be wagered.

    Returns:
        tuple: A tuple containing the total bonus amount and wagering requirements.
    """
    # Check for valid input
    if deposit_amount <= 0:
        raise ValueError("Deposit amount must be greater than zero.")
    if bonus_percentage <= 0:
        raise ValueError("Bonus percentage must be greater than zero.")
    if wagering_requirement <= 0:
        raise ValueError("Wagering requirement must be greater than zero.")

    # Calculate the bonus amount
    bonus_amount = deposit_amount * (bonus_percentage / 100)

    # Calculate the total wagering requirements
    total_wagering_requirements = (deposit_amount + bonus_amount) * wagering_requirement

    return bonus_amount, total_wagering_requirements


def main():
    try:
        # Define the bonus terms
        deposit_amount = 100.0  # example deposit amount
        bonus_percentage = 400.0  # 400% bonus
        wagering_requirement = 30  # 30x wagering requirement

        # Calculate the bonus and wagering requirements
        bonus_amount, total_wagering_requirements = calculate_bonus_and_wagering(deposit_amount, bonus_percentage, wagering_requirement)

        # Print the results
        print(f"Bonus Amount: ${bonus_amount:.2f}")
        print(f"Total Wagering Requirements: ${total_wagering_requirements:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
