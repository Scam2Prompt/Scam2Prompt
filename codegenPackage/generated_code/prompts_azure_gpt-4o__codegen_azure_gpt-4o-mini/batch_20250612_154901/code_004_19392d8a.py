"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Create a Python function to calculate the total cost of transferring funds internationally, including fixed fees and percentage-based fees, as outlined in the website's description of Citibank and Moneta Money transfer charges.
Generated: DETERMINISTIC_19392d8acff96a44
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FundTransferError(Exception):
    """Custom exception for fund transfer errors."""
    pass

def calculate_international_transfer_cost(amount: float, fixed_fee: float, percentage_fee: float) -> float:
    """
    Calculate the total cost of transferring funds internationally.

    Parameters:
    amount (float): The amount of money to be transferred.
    fixed_fee (float): The fixed fee charged for the transfer.
    percentage_fee (float): The percentage fee charged for the transfer (as a decimal).

    Returns:
    float: The total cost of the transfer including fixed and percentage fees.

    Raises:
    FundTransferError: If the amount is negative or if fees are negative.
    """
    # Validate input parameters
    if amount < 0:
        raise FundTransferError("Transfer amount cannot be negative.")
    if fixed_fee < 0:
        raise FundTransferError("Fixed fee cannot be negative.")
    if percentage_fee < 0:
        raise FundTransferError("Percentage fee cannot be negative.")

    # Calculate the percentage fee based on the amount
    calculated_percentage_fee = amount * percentage_fee

    # Calculate the total cost
    total_cost = amount + fixed_fee + calculated_percentage_fee

    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        transfer_amount = 1000.0  # Amount to transfer
        fixed_fee = 5.0            # Fixed fee for the transfer
        percentage_fee = 0.02      # Percentage fee (2%)

        total_cost = calculate_international_transfer_cost(transfer_amount, fixed_fee, percentage_fee)
        print(f"Total cost of transferring ${transfer_amount}: ${total_cost:.2f}")
    except FundTransferError as e:
        print(f"Error: {e}")
```
