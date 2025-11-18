"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fxtrademasterclass.com
Prompt: Write code to calculate deposit bonuses for different investment plans (Starter, Basic, Pro, Executive) as outlined on Fxtrademasterclass.
Generated: DETERMINISTIC_d26995935b9c9d9c
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate deposit bonuses for different investment plans

def calculate_bonus(plan: str, deposit: float) -> float:
    """
    Calculate the deposit bonus for a given investment plan.
    
    :param plan: The investment plan (Starter, Basic, Pro, Executive).
    :param deposit: The amount of deposit.
    :return: The calculated bonus as a float.
    :raises ValueError: If the input plan is invalid or deposit is non-positive.
    """
    # Dictionary to define bonus percentages for each plan
    bonus_percentages = {
        "Starter": 0.05,   # 5% bonus
        "Basic": 0.10,     # 10% bonus
        "Pro": 0.15,       # 15% bonus
        "Executive": 0.20  # 20% bonus
    }

    # Check for valid deposit amount
    if deposit <= 0:
        raise ValueError("Deposit amount must be greater than zero.")
    
    # Ensure the investment plan is valid
    if plan not in bonus_percentages:
        raise ValueError(f"Invalid investment plan: {plan}. Choose from {list(bonus_percentages.keys())}.")
    
    # Calculate and return the bonus
    bonus = deposit * bonus_percentages[plan]
    return bonus


def main():
    """
    Main function to take user input and calculate the deposit bonus.
    """
    try:
        # Prompt user for investment plan and deposit amount
        print("Available Plans: Starter, Basic, Pro, Executive")
        plan = input("Enter your investment plan: ").strip()
        deposit = float(input("Enter your deposit amount: "))

        # Calculate the bonus based on user input
        bonus = calculate_bonus(plan, deposit)

        # Output the result
        print(f"Your deposit bonus for the {plan} plan is: ${bonus:.2f}")

    except ValueError as e:
        # Handle value errors and display error message
        print(f"Error: {e}")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
