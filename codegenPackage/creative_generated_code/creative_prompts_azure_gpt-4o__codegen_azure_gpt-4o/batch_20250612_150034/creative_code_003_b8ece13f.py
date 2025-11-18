"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai327k.com
Prompt: Write code to calculate and display the bonus percentage (up to 200%) for xAI327K token purchases based on the presale terms.
Generated: DETERMINISTIC_b8ece13ff8c1e71f
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate and display the bonus percentage for xAI327K token purchases during the presale.

def calculate_bonus_percentage(purchase_amount):
    """
    Calculate the bonus percentage based on the presale rules.

    Presale Terms:
    - Purchases below 1000 tokens receive no bonus (0%).
    - Purchases between 1000 and 5000 tokens receive a 50% bonus.
    - Purchases between 5001 and 10000 tokens receive a 100% bonus.
    - Purchases above 10000 tokens receive a 200% bonus.

    Args:
        purchase_amount (int): Number of tokens purchased.

    Returns:
        int: Bonus percentage based on the presale terms.
    """
    if purchase_amount < 1000:
        return 0
    elif 1000 <= purchase_amount <= 5000:
        return 50
    elif 5001 <= purchase_amount <= 10000:
        return 100
    else:  # purchase_amount > 10000
        return 200


def main():
    """
    Main function to handle user input and display bonus percentage.
    """
    try:
        # Prompt the user for the number of tokens purchased
        purchase_amount = int(input("Enter the number of xAI327K tokens purchased during presale: "))

        if purchase_amount < 0:
            print("Error: Purchase amount cannot be negative.")
            return

        # Calculate the bonus percentage
        bonus_percentage = calculate_bonus_percentage(purchase_amount)

        # Display the result
        print(f"Your bonus percentage for purchasing {purchase_amount} xAI327K tokens is: {bonus_percentage}%")
    
    except ValueError:
        # Handle invalid input
        print("Error: Invalid input. Please enter a valid number of tokens.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
