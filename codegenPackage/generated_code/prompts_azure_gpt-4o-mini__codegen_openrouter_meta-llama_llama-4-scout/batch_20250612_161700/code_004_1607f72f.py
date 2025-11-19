"""
Generated Code Metadata:
========================
Original URL: https://crop-6qi.pages.dev
Prompt: Create a function to calculate the maximum allocation for purchasing $BLOCK tokens based on ETH or BNB contributions on Seedify.
Generated: DETERMINISTIC_1607f72fc8b9574f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_max_allocation(contribution_amount, contribution_type, block_price, max_allocation_percentage):
    """
    Calculate the maximum allocation for purchasing $BLOCK tokens based on ETH or BNB contributions on Seedify.

    Args:
        contribution_amount (float): The amount of ETH or BNB contributed.
        contribution_type (str): The type of contribution, either 'ETH' or 'BNB'.
        block_price (float): The price of one $BLOCK token.
        max_allocation_percentage (float): The maximum percentage of the contribution amount that can be allocated to $BLOCK tokens.

    Returns:
        float: The maximum allocation amount for purchasing $BLOCK tokens.

    Raises:
        ValueError: If the contribution type is not 'ETH' or 'BNB'.
        ValueError: If the contribution amount, block price, or max allocation percentage is not a positive number.
    """

    # Validate contribution type
    if contribution_type.upper() not in ['ETH', 'BNB']:
        raise ValueError("Invalid contribution type. Must be 'ETH' or 'BNB'.")

    # Validate input values
    if contribution_amount <= 0 or block_price <= 0 or max_allocation_percentage <= 0:
        raise ValueError("Contribution amount, block price, and max allocation percentage must be positive numbers.")

    # Calculate maximum allocation amount
    max_allocation_amount = (contribution_amount * max_allocation_percentage / 100) / block_price

    return max_allocation_amount


def main():
    try:
        # Example usage:
        contribution_amount = 1.0  # 1 ETH or BNB
        contribution_type = 'ETH'
        block_price = 0.1  # $0.10 per $BLOCK token
        max_allocation_percentage = 20.0  # 20% of contribution amount

        max_allocation = calculate_max_allocation(contribution_amount, contribution_type, block_price, max_allocation_percentage)
        print(f"Maximum allocation for purchasing $BLOCK tokens: {max_allocation:.2f} $BLOCK tokens")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
