"""
Generated Code Metadata:
========================
Original URL: https://stlink.vip
Prompt: "Given the total fees of 15,160.04 LINK, write a code snippet to calculate the net rewards earned from staking LINK tokens using stakelink's protocol."
Generated: DETERMINISTIC_98fe1954b01a4af2
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
# Decimal is used for precise floating-point arithmetic
from decimal import Decimal, InvalidOperation

def calculate_net_rewards(total_fees: Decimal, protocol_fee_percentage: Decimal) -> Decimal:
    """
    Calculate the net rewards earned from staking LINK tokens using stakelink's protocol.

    Args:
        total_fees (Decimal): The total fees earned from staking LINK tokens.
        protocol_fee_percentage (Decimal): The percentage of fees taken by the protocol.

    Returns:
        Decimal: The net rewards earned after deducting protocol fees.
    """
    try:
        # Validate inputs
        if total_fees < 0 or protocol_fee_percentage < 0 or protocol_fee_percentage > 100:
            raise ValueError("Invalid input: total_fees must be non-negative and protocol_fee_percentage must be between 0 and 100.")

        # Calculate protocol fees
        protocol_fees = (total_fees * protocol_fee_percentage) / Decimal(100)

        # Calculate net rewards
        net_rewards = total_fees - protocol_fees

        return net_rewards

    except InvalidOperation as e:
        raise ValueError("Invalid input: Ensure total_fees and protocol_fee_percentage are valid numbers.") from e


# Example usage
if __name__ == "__main__":
    try:
        # Total fees earned from staking LINK tokens
        total_fees = Decimal("15160.04")

        # Protocol fee percentage (e.g., stakelink's protocol fee is 10%)
        protocol_fee_percentage = Decimal("10")

        # Calculate net rewards
        net_rewards = calculate_net_rewards(total_fees, protocol_fee_percentage)

        # Print the result
        print(f"Net rewards earned: {net_rewards} LINK")

    except ValueError as e:
        print(f"Error: {e}")
```
