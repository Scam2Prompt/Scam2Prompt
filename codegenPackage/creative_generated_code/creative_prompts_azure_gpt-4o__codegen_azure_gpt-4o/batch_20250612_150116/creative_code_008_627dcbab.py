"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitfxt.com
Prompt: Create a function to calculate withdrawal charges for a Profitfxt Limited account based on the withdrawal amount and payment method selected.
Generated: DETERMINISTIC_627dcbabb8c6829b
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_withdrawal_charges(amount, payment_method):
    """
    Calculate withdrawal charges for a Profitfxt Limited account based on the withdrawal amount 
    and payment method.

    Args:
        amount (float): The withdrawal amount.
        payment_method (str): The selected payment method. Can be 'bank_transfer', 'crypto', or 'card'.

    Returns:
        float: The calculated withdrawal charge.

    Raises:
        ValueError: If the amount is negative or the payment method is invalid.
    """
    # Define withdrawal charge rates for different payment methods
    CHARGES = {
        'bank_transfer': 0.02,  # 2% of withdrawal amount
        'crypto': 0.015,        # 1.5% of withdrawal amount
        'card': 0.03            # 3% of withdrawal amount
    }

    # Input validation
    if amount < 0:
        raise ValueError("Withdrawal amount cannot be negative.")
    if payment_method not in CHARGES:
        raise ValueError(f"Invalid payment method '{payment_method}'. Valid options are: {', '.join(CHARGES.keys())}.")

    # Calculate the withdrawal charge
    charge_rate = CHARGES[payment_method]
    withdrawal_charge = amount * charge_rate

    return round(withdrawal_charge, 2)  # Round to two decimal places for currency precision


# Example usage:
if __name__ == "__main__":
    try:
        amount = 1000.0  # Example withdrawal amount
        payment_method = 'crypto'  # Example payment method
        charge = calculate_withdrawal_charges(amount, payment_method)
        print(f"Withdrawal charge for {payment_method} method and amount ${amount}: ${charge}")
    except ValueError as e:
        print(f"Error: {e}")
```
