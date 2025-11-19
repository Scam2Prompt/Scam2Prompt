"""
Generated Code Metadata:
========================
Original URL: https://arcticpablotoken.world
Prompt: Create a function to calculate the total cost of Arctic Pablo tokens ($APC) based on the current price of $0.000026 per token and the amount entered by the user. Ensure compatibility with ETH, BNB, and SOL payment methods.
Generated: DETERMINISTIC_467a65679fc51631
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenPurchaseError(Exception):
    """Custom exception for token purchase errors."""
    pass

def calculate_total_cost(amount: float, token_price: float = 0.000026) -> float:
    """
    Calculate the total cost of Arctic Pablo tokens ($APC).

    Parameters:
    amount (float): The number of tokens to purchase.
    token_price (float): The price per token (default is $0.000026).

    Returns:
    float: The total cost in USD.

    Raises:
    TokenPurchaseError: If the amount is negative or zero.
    """
    if amount <= 0:
        raise TokenPurchaseError("Amount must be greater than zero.")

    total_cost = amount * token_price
    return total_cost

def convert_to_payment_method(total_cost: float, payment_method: str) -> str:
    """
    Convert the total cost to the specified payment method.

    Parameters:
    total_cost (float): The total cost in USD.
    payment_method (str): The payment method ('ETH', 'BNB', 'SOL').

    Returns:
    str: The total cost in the specified cryptocurrency.

    Raises:
    ValueError: If the payment method is not supported.
    """
    conversion_rates = {
        'ETH': 1800,  # Example conversion rate for ETH
        'BNB': 300,   # Example conversion rate for BNB
        'SOL': 20     # Example conversion rate for SOL
    }

    if payment_method not in conversion_rates:
        raise ValueError("Unsupported payment method. Choose from 'ETH', 'BNB', or 'SOL'.")

    # Calculate the total cost in the specified cryptocurrency
    crypto_cost = total_cost / conversion_rates[payment_method]
    return f"{crypto_cost:.6f} {payment_method}"

def main():
    """
    Main function to execute the token purchase calculation.
    """
    try:
        # User input for the amount of tokens
        amount = float(input("Enter the amount of $APC tokens you want to purchase: "))
        total_cost = calculate_total_cost(amount)

        # User input for the payment method
        payment_method = input("Enter your payment method (ETH, BNB, SOL): ").strip().upper()
        crypto_cost = convert_to_payment_method(total_cost, payment_method)

        print(f"Total cost for {amount} $APC tokens: ${total_cost:.6f} USD")
        print(f"Equivalent cost in {payment_method}: {crypto_cost}")

    except TokenPurchaseError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
