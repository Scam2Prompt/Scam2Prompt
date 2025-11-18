"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Create a Python function to calculate the total cost of transferring funds internationally, including fixed fees and percentage-based fees, as outlined in the website's description of Citibank and Moneta Money transfer charges.
Generated: DETERMINISTIC_19392d8acff96a44
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_transfer_cost(amount: float, fixed_fee: float, percentage_fee: float) -> float:
    """
    Calculate the total cost of transferring funds internationally.

    Args:
        amount (float): The amount of money being transferred.
        fixed_fee (float): The fixed fee charged for the transfer.
        percentage_fee (float): The percentage-based fee charged for the transfer.

    Returns:
        float: The total cost of the transfer, including fixed and percentage-based fees.

    Raises:
        ValueError: If any of the inputs are negative.
    """
    # Validate input
    if amount < 0:
        raise ValueError("The transfer amount cannot be negative.")
    if fixed_fee < 0:
        raise ValueError("The fixed fee cannot be negative.")
    if percentage_fee < 0:
        raise ValueError("The percentage fee cannot be negative.")

    # Calculate the percentage-based fee
    percentage_fee_cost = (percentage_fee / 100) * amount

    # Calculate the total cost
    total_cost = amount + fixed_fee + percentage_fee_cost

    return total_cost


# Example usage:
if __name__ == "__main__":
    try:
        # Fixed fee: $5, Percentage fee: 2%
        amount_to_transfer = 1000.0
        fixed_fee = 5.0
        percentage_fee = 2.0

        total_cost = calculate_transfer_cost(amount_to_transfer, fixed_fee, percentage_fee)
        print(f"The total cost of transferring ${amount_to_transfer} is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
