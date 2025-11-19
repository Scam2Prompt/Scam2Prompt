"""
Generated Code Metadata:
========================
Original URL: https://to-ousd.pages.dev
Prompt: Write a code snippet in Python to calculate the redemption value of OUSD, considering the 0.25% fee charged when redeeming or burning OUSD on the OUSD dapp.
Generated: DETERMINISTIC_56dd012c809f245e
Batch ID: 20250622_211131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_redemption_value(ousd_amount: float) -> float:
    """
    Calculate the redemption value of OUSD considering the 0.25% fee.

    Args:
    ousd_amount (float): The amount of OUSD to redeem.

    Returns:
    float: The redemption value after deducting the fee.

    Raises:
    ValueError: If the OUSD amount is negative.
    """

    # Check if the OUSD amount is valid (non-negative)
    if ousd_amount < 0:
        raise ValueError("OUSD amount cannot be negative.")

    # Define the fee percentage as a decimal
    fee_percentage = 0.0025  # 0.25%

    # Calculate the fee amount
    fee_amount = ousd_amount * fee_percentage

    # Calculate the redemption value by subtracting the fee amount
    redemption_value = ousd_amount - fee_amount

    return redemption_value


def main():
    try:
        # Example usage
        ousd_amount = 1000.0
        redemption_value = calculate_redemption_value(ousd_amount)
        print(f"Redemption value for {ousd_amount} OUSD: {redemption_value:.2f} OUSD")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
