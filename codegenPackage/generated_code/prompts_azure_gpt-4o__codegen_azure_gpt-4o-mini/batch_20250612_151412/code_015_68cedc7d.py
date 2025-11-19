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
# cashback_calculator.py

def calculate_cashback(purchases):
    """
    Calculate the total cashback earned based on the purchases made.

    Args:
        purchases (list of float): A list of purchase amounts.

    Returns:
        float: Total cashback earned.
    """
    # Define cashback rates
    cashback_rate = 0.02  # 2% cashback on all purchases

    # Calculate total cashback
    total_cashback = sum(purchase * cashback_rate for purchase in purchases)
    return total_cashback


def get_user_input():
    """
    Get user input for purchases over the year.

    Returns:
        list of float: A list of purchase amounts entered by the user.
    """
    purchases = []
    print("Enter your purchases for the year (type 'done' to finish):")

    while True:
        user_input = input("Enter purchase amount: ")
        if user_input.lower() == 'done':
            break
        try:
            # Convert input to float and add to purchases list
            purchase_amount = float(user_input)
            if purchase_amount < 0:
                raise ValueError("Purchase amount cannot be negative.")
            purchases.append(purchase_amount)
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

    return purchases


def main():
    """
    Main function to execute the cashback calculation.
    """
    # Get user input for purchases
    purchases = get_user_input()

    # Calculate cashback if there are purchases
    if purchases:
        total_cashback = calculate_cashback(purchases)
        print(f"Total cashback earned over the year: ${total_cashback:.2f}")
    else:
        print("No purchases entered. Cashback calculation cannot be performed.")


if __name__ == "__main__":
    main()
```
