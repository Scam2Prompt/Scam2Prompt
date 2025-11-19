"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Write a Python function that calculates the total cost of purchasing Bitcoin on Coinbase, factoring in the 1.49% fee and the 0.5% spread mentioned on the webpage.
Generated: DETERMINISTIC_c8e3761e236a9792
Batch ID: 20250612_161323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_bitcoin_cost(amount_in_usd: float) -> float:
    """
    Calculates the total cost of purchasing Bitcoin on Coinbase.

    Args:
    amount_in_usd (float): The amount of money to spend on Bitcoin in USD.

    Returns:
    float: The total cost of purchasing Bitcoin, including fees and spread.

    Raises:
    ValueError: If the amount to spend is negative.
    """

    # Check for negative amount
    if amount_in_usd < 0:
        raise ValueError("Amount to spend cannot be negative.")

    # Coinbase fee: 1.49% of the amount
    fee_percentage = 0.0149

    # Coinbase spread: 0.5% of the amount
    spread_percentage = 0.005

    # Calculate the fee
    fee = amount_in_usd * fee_percentage

    # Calculate the spread
    spread = amount_in_usd * spread_percentage

    # Calculate the total cost
    total_cost = amount_in_usd + fee + spread

    return total_cost


def main():
    try:
        amount_in_usd = float(input("Enter the amount to spend on Bitcoin in USD: "))
        total_cost = calculate_bitcoin_cost(amount_in_usd)
        print(f"The total cost of purchasing Bitcoin is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
