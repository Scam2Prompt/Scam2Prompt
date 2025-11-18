"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancake-ifo.pages.dev
Prompt: Write a function that calculates the participation fee for a PancakeSwap Public Sale based on the "Cliff" model, using the percentage of overflow from the sale.
Generated: DETERMINISTIC_159e6714320251f7
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_participation_fee(total_contribution, user_contribution, sale_allocation, max_allocation, overflow_percentage):
    """
    Calculate the participation fee for a PancakeSwap Public Sale using the "Cliff" model.

    Args:
        total_contribution (float): Total amount of contributions to the public sale.
        user_contribution (float): Amount contributed by the user.
        sale_allocation (float): Allocation received by the user from the sale.
        max_allocation (float): Maximum allocation allowed for the user.
        overflow_percentage (float): Percentage of overflow from the sale.

    Returns:
        float: Participation fee to be paid by the user.
    """
    try:
        # Input validation
        if total_contribution <= 0:
            raise ValueError("Total contribution must be greater than zero.")
        if user_contribution <= 0:
            raise ValueError("User contribution must be greater than zero.")
        if sale_allocation < 0 or max_allocation <= 0:
            raise ValueError("Sale allocation and max allocation must be non-negative numbers.")
        if not (0 <= overflow_percentage <= 100):
            raise ValueError("Overflow percentage must be between 0 and 100.")

        # Calculate user's participation ratio
        participation_ratio = user_contribution / total_contribution

        # Calculate the user's adjusted allocation based on the overflow percentage
        adjusted_allocation = sale_allocation + (sale_allocation * (overflow_percentage / 100))

        # Ensure that the adjusted allocation does not exceed the maximum allocation
        if adjusted_allocation > max_allocation:
            adjusted_allocation = max_allocation

        # Participation fee is calculated as the difference between user's contribution and allocated value
        participation_fee = user_contribution - adjusted_allocation

        # Ensure that the fee is non-negative
        participation_fee = max(0, participation_fee)
        return participation_fee

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    total_contrib = 100000  # Total contribution in the sale
    user_contrib = 5000     # User's contribution
    sale_alloc = 4500       # Allocation received by the user
    max_alloc = 5000        # Maximum allocation allowed
    overflow_pct = 20       # Overflow percentage

    fee = calculate_participation_fee(total_contrib, user_contrib, sale_alloc, max_alloc, overflow_pct)
    if fee is not None:
        print(f"Participation fee: {fee}")
```
