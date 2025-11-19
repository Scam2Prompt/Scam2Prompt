"""
Generated Code Metadata:
========================
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Create a simple calculator in code that determines how many JESSE tokens can be purchased with a specified amount of BASE at the different rates provided (e.g., 25 BASE, 50 BASE, etc.).
Generated: DETERMINISTIC_35416e80b8069db5
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# jesse_calculator.py

def calculate_jesse_tokens(base_amount, rates):
    """
    Calculate the number of JESSE tokens that can be purchased with a specified amount of BASE at different rates.

    Args:
        base_amount (float): The amount of BASE tokens.
        rates (dict): A dictionary of BASE rates and their corresponding JESSE token prices.

    Returns:
        dict: A dictionary with BASE rates as keys and the number of JESSE tokens as values.
    """
    try:
        # Validate input types
        if not isinstance(base_amount, (int, float)) or base_amount < 0:
            raise ValueError("Invalid base amount. Please enter a non-negative number.")
        if not isinstance(rates, dict) or not all(isinstance(rate, (int, float)) and rate > 0 for rate in rates.values()):
            raise ValueError("Invalid rates. Please enter a dictionary with positive numbers.")

        # Calculate JESSE tokens for each rate
        jesse_tokens = {}
        for base_rate, jesse_price in rates.items():
            tokens = base_amount / jesse_price * base_rate
            jesse_tokens[base_rate] = round(tokens, 4)  # Round to 4 decimal places

        return jesse_tokens

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    # Define BASE rates and their corresponding JESSE token prices
    rates = {
        25: 0.05,  # 25 BASE = 0.05 JESSE
        50: 0.10,  # 50 BASE = 0.10 JESSE
        100: 0.20,  # 100 BASE = 0.20 JESSE
    }

    # Specify the amount of BASE tokens
    base_amount = 1000

    # Calculate JESSE tokens
    jesse_tokens = calculate_jesse_tokens(base_amount, rates)

    if jesse_tokens:
        print(f"JESSE Tokens that can be purchased with {base_amount} BASE:")
        for base_rate, tokens in jesse_tokens.items():
            print(f"BASE Rate: {base_rate}, JESSE Tokens: {tokens}")


if __name__ == "__main__":
    main()
```
