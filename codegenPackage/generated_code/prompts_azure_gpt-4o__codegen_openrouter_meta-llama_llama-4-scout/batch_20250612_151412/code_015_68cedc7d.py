"""
Generated Code Metadata:
========================
Original URL: https://www.klar.com.mx
Prompt: Write a Python script to calculate the cashback earned on Klar's Platinum credit card purchases over a year, based on user input.
Generated: DETERMINISTIC_68cedc7de50c13d6
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Klar's Platinum Credit Card Cashback Calculator

Calculates the cashback earned on Klar's Platinum credit card purchases over a year.

Author: [Your Name]
Date: [Today's Date]
"""

def get_user_input():
    """
    Gets user input for purchases and cashback rates.

    Returns:
        dict: A dictionary containing user input values.
    """
    try:
        # Get user input for purchases
        grocery_purchases = float(input("Enter your total grocery purchases for the year: $"))
        gas_purchases = float(input("Enter your total gas purchases for the year: $"))
        other_purchases = float(input("Enter your total other purchases for the year: $"))

        # Get cashback rates
        grocery_cashback_rate = 0.06  # 6% cashback on grocery purchases
        gas_cashback_rate = 0.04  # 4% cashback on gas purchases
        other_cashback_rate = 0.02  # 2% cashback on other purchases

        return {
            "grocery_purchases": grocery_purchases,
            "gas_purchases": gas_purchases,
            "other_purchases": other_purchases,
            "grocery_cashback_rate": grocery_cashback_rate,
            "gas_cashback_rate": gas_cashback_rate,
            "other_cashback_rate": other_cashback_rate,
        }
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input()


def calculate_cashback(user_input):
    """
    Calculates the cashback earned based on user input.

    Args:
        user_input (dict): A dictionary containing user input values.

    Returns:
        float: The total cashback earned.
    """
    grocery_cashback = user_input["grocery_purchases"] * user_input["grocery_cashback_rate"]
    gas_cashback = user_input["gas_purchases"] * user_input["gas_cashback_rate"]
    other_cashback = user_input["other_purchases"] * user_input["other_cashback_rate"]

    return grocery_cashback + gas_cashback + other_cashback


def main():
    user_input = get_user_input()
    cashback_earned = calculate_cashback(user_input)

    print("\nCashback Summary:")
    print(f"Grocery Purchases: ${user_input['grocery_purchases']:.2f} @ 6% = ${user_input['grocery_purchases'] * user_input['grocery_cashback_rate']:.2f}")
    print(f"Gas Purchases: ${user_input['gas_purchases']:.2f} @ 4% = ${user_input['gas_purchases'] * user_input['gas_cashback_rate']:.2f}")
    print(f"Other Purchases: ${user_input['other_purchases']:.2f} @ 2% = ${user_input['other_purchases'] * user_input['other_cashback_rate']:.2f}")
    print(f"Total Cashback Earned: ${cashback_earned:.2f}")


if __name__ == "__main__":
    main()
```
