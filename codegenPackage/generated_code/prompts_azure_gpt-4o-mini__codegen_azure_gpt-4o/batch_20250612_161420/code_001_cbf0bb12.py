"""
Generated Code Metadata:
========================
Original URL: https://ghozali-den.pages.dev
Prompt: Write a script to calculate the total supply of $GHOZALI tokens and distribute them among holders.
Generated: DETERMINISTIC_cbf0bb12e8d0afeb
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class TokenDistributionError(Exception):
    """Custom exception for token distribution errors."""
    pass

def calculate_total_supply(token_data):
    """
    Calculate the total supply of tokens.

    Args:
        token_data (list of dict): List of token data where each dict contains 'holder' and 'balance'.

    Returns:
        int: Total supply of tokens.
    """
    try:
        total_supply = sum(holder['balance'] for holder in token_data)
        return total_supply
    except KeyError as e:
        raise TokenDistributionError(f"Invalid token data format: Missing key {e}")
    except TypeError as e:
        raise TokenDistributionError(f"Invalid token data format: {e}")

def distribute_tokens(token_data, total_supply):
    """
    Distribute tokens among holders based on their current balance.

    Args:
        token_data (list of dict): List of token data where each dict contains 'holder' and 'balance'.
        total_supply (int): Total supply of tokens.

    Returns:
        dict: Distribution of tokens among holders.
    """
    try:
        distribution = {}
        for holder in token_data:
            address = holder['holder']
            balance = holder['balance']
            # Calculate the percentage share of the total supply
            distribution[address] = (balance / total_supply) * total_supply
        return distribution
    except ZeroDivisionError:
        raise TokenDistributionError("Total supply cannot be zero.")
    except KeyError as e:
        raise TokenDistributionError(f"Invalid token data format: Missing key {e}")
    except TypeError as e:
        raise TokenDistributionError(f"Invalid token data format: {e}")

def main():
    """
    Main function to calculate total supply and distribute tokens.
    """
    # Example token data
    token_data = [
        {'holder': '0x123', 'balance': 100},
        {'holder': '0x456', 'balance': 200},
        {'holder': '0x789', 'balance': 300},
    ]

    try:
        # Calculate total supply
        total_supply = calculate_total_supply(token_data)
        print(f"Total Supply of $GHOZALI Tokens: {total_supply}")

        # Distribute tokens among holders
        distribution = distribute_tokens(token_data, total_supply)
        print("Token Distribution:")
        for holder, tokens in distribution.items():
            print(f"Holder: {holder}, Tokens: {tokens:.2f}")
    except TokenDistributionError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
