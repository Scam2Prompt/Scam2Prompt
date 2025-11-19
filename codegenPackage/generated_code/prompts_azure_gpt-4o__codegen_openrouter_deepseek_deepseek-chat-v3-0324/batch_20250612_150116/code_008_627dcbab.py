"""
Generated Code Metadata:
========================
Original URL: https://profitfxt.com
Prompt: Create a function to calculate withdrawal charges for a Profitfxt Limited account based on the withdrawal amount and payment method selected.
Generated: DETERMINISTIC_627dcbabb8c6829b
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_withdrawal_charges(withdrawal_amount: float, payment_method: str) -> float:
    """
    Calculate withdrawal charges for a Profitfxt Limited account based on the withdrawal amount and payment method.

    Args:
        withdrawal_amount (float): The amount to be withdrawn.
        payment_method (str): The payment method selected. Options: 'bank', 'credit_card', 'ewallet', 'crypto'.

    Returns:
        float: The calculated withdrawal charge.

    Raises:
        ValueError: If withdrawal_amount is negative or payment_method is invalid.
    """
    # Validate input parameters
    if withdrawal_amount < 0:
        raise ValueError("Withdrawal amount cannot be negative.")
    
    payment_method = payment_method.lower()
    valid_methods = ['bank', 'credit_card', 'ewallet', 'crypto']
    if payment_method not in valid_methods:
        raise ValueError(f"Invalid payment method. Must be one of: {valid_methods}")

    # Define charge structure based on payment method
    charges = {
        'bank': {
            'flat_fee': 10.0,
            'percentage_fee': 0.02,  # 2%
            'min_fee': 5.0,
            'max_fee': 50.0
        },
        'credit_card': {
            'flat_fee': 15.0,
            'percentage_fee': 0.03,  # 3%
            'min_fee': 10.0,
            'max_fee': 75.0
        },
        'ewallet': {
            'flat_fee': 5.0,
            'percentage_fee': 0.01,  # 1%
            'min_fee': 2.0,
            'max_fee': 30.0
        },
        'crypto': {
            'flat_fee': 3.0,
            'percentage_fee': 0.005,  # 0.5%
            'min_fee': 1.0,
            'max_fee': 20.0
        }
    }

    # Calculate the charge
    method_charges = charges[payment_method]
    percentage_charge = withdrawal_amount * method_charges['percentage_fee']
    total_charge = method_charges['flat_fee'] + percentage_charge

    # Apply min and max limits
    total_charge = max(total_charge, method_charges['min_fee'])
    total_charge = min(total_charge, method_charges['max_fee'])

    return round(total_charge, 2)
```
