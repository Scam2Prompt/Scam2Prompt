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
def calculate_bonus_and_wagering(deposit_amount, bonus_percentage=400, wagering_multiplier=10):
    """
    Calculate the total bonus amount and wagering requirements for a casino bonus.

    Parameters:
    deposit_amount (float): The amount deposited by the player.
    bonus_percentage (int): The percentage of the bonus (default is 400%).
    wagering_multiplier (int): The multiplier for wagering requirements (default is 10).

    Returns:
    tuple: A tuple containing the total bonus amount and the total wagering requirement.
    """
    # Validate input
    if deposit_amount < 0:
        raise ValueError("Deposit amount must be a non-negative value.")
    
    if not isinstance(bonus_percentage, (int, float)) or not isinstance(wagering_multiplier, (int, float)):
        raise TypeError("Bonus percentage and wagering multiplier must be numeric values.")

    # Calculate the total bonus amount
    bonus_amount = deposit_amount * (bonus_percentage / 100)

    # Calculate the total wagering requirement
    total_wagering_requirement = (deposit_amount + bonus_amount) * wagering_multiplier

    return bonus_amount, total_wagering_requirement

def main():
    """
    Main function to execute the bonus calculation.
    """
    try:
        # Input: Deposit amount from the user
        deposit_amount = float(input("Enter the deposit amount: "))
        
        # Calculate bonus and wagering requirements
        bonus, wagering = calculate_bonus_and_wagering(deposit_amount)
        
        # Output the results
        print(f"Total Bonus Amount: ${bonus:.2f}")
        print(f"Total Wagering Requirement: ${wagering:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except TypeError as te:
        print(f"Type error: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
