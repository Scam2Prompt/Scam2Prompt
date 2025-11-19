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
def calculate_transfer_cost(amount: float, 
                           fixed_fee: float, 
                           percentage_fee: float, 
                           min_percentage_fee: float = 0.0) -> float:
    """
    Calculate the total cost of transferring funds internationally.

    Args:
    - amount (float): The amount to be transferred.
    - fixed_fee (float): The fixed fee for the transfer.
    - percentage_fee (float): The percentage-based fee for the transfer.
    - min_percentage_fee (float): The minimum percentage-based fee. Defaults to 0.0.

    Returns:
    - float: The total cost of the transfer.

    Raises:
    - ValueError: If the amount, fixed fee, or percentage fee is negative.
    """

    # Validate input values
    if amount < 0:
        raise ValueError("Transfer amount cannot be negative.")
    if fixed_fee < 0:
        raise ValueError("Fixed fee cannot be negative.")
    if percentage_fee < 0:
        raise ValueError("Percentage fee cannot be negative.")
    if min_percentage_fee < 0:
        raise ValueError("Minimum percentage fee cannot be negative.")

    # Calculate percentage-based fee
    percentage_based_fee = max(amount * (percentage_fee / 100), min_percentage_fee)

    # Calculate total cost
    total_cost = fixed_fee + percentage_based_fee

    return total_cost


def citibank_transfer_cost(amount: float, 
                           fixed_fee: float = 10.0, 
                           percentage_fee: float = 0.5, 
                           min_percentage_fee: float = 5.0) -> float:
    """
    Calculate the total cost of transferring funds internationally with Citibank.

    Args:
    - amount (float): The amount to be transferred.
    - fixed_fee (float): The fixed fee for the transfer. Defaults to $10.00.
    - percentage_fee (float): The percentage-based fee for the transfer. Defaults to 0.5%.
    - min_percentage_fee (float): The minimum percentage-based fee. Defaults to $5.00.

    Returns:
    - float: The total cost of the transfer.
    """

    return calculate_transfer_cost(amount, fixed_fee, percentage_fee, min_percentage_fee)


def moneta_money_transfer_cost(amount: float, 
                              fixed_fee: float = 5.0, 
                              percentage_fee: float = 1.0, 
                              min_percentage_fee: float = 10.0) -> float:
    """
    Calculate the total cost of transferring funds internationally with Moneta Money.

    Args:
    - amount (float): The amount to be transferred.
    - fixed_fee (float): The fixed fee for the transfer. Defaults to $5.00.
    - percentage_fee (float): The percentage-based fee for the transfer. Defaults to 1.0%.
    - min_percentage_fee (float): The minimum percentage-based fee. Defaults to $10.00.

    Returns:
    - float: The total cost of the transfer.
    """

    return calculate_transfer_cost(amount, fixed_fee, percentage_fee, min_percentage_fee)


# Example usage:
if __name__ == "__main__":
    try:
        amount = 1000.0
        citibank_cost = citibank_transfer_cost(amount)
        moneta_money_cost = moneta_money_transfer_cost(amount)

        print(f"Citibank transfer cost for ${amount:.2f}: ${citibank_cost:.2f}")
        print(f"Moneta Money transfer cost for ${amount:.2f}: ${moneta_money_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
