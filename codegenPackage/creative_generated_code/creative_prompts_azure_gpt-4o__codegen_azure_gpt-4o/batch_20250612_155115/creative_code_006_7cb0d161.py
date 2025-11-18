"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solanalaunchtool.com
Prompt: Write code to calculate the estimated market cap of a Solana token after launch, using examples like $BONK, $BRETT, and $SHIB mentioned on Solanalaunchtool.com.
Generated: DETERMINISTIC_7cb0d1617ba02f51
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_market_cap(token_name, price_per_token, total_supply):
    """
    Calculate the estimated market capitalization of a Solana token.
    
    Parameters:
        token_name (str): The name of the token.
        price_per_token (float): The price of one token in dollars.
        total_supply (int): The total supply of tokens.

    Returns:
        float: Estimated market capitalization in dollars.
    """
    try:
        # Validate input parameters
        if not isinstance(token_name, str) or not token_name:
            raise ValueError("Token name must be a non-empty string.")
        if not isinstance(price_per_token, (float, int)) or price_per_token <= 0:
            raise ValueError("Price per token must be a positive number.")
        if not isinstance(total_supply, int) or total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        
        # Calculate market cap
        market_cap = price_per_token * total_supply
        
        return market_cap

    except TypeError as e:
        print(f"TypeError: {e}", file=sys.stderr)
        raise
    except ValueError as e:
        print(f"ValueError: {e}", file=sys.stderr)
        raise


def main():
    """
    Main function to demonstrate market cap calculation for example tokens.
    """
    # Example tokens with dummy data (token name, price per token, total supply)
    tokens = [
        {"token_name": "BONK", "price_per_token": 0.0001, "total_supply": 100_000_000_000},
        {"token_name": "BRETT", "price_per_token": 0.0015, "total_supply": 10_000_000_000},
        {"token_name": "SHIB", "price_per_token": 0.00002, "total_supply": 500_000_000_000},
    ]

    print("Estimated Market Caps for Solana Tokens:")
    print("----------------------------------------")
    
    # Loop through tokens and calculate market cap
    for token in tokens:
        try:
            market_cap = calculate_market_cap(
                token_name=token["token_name"],
                price_per_token=token["price_per_token"],
                total_supply=token["total_supply"]
            )
            print(f"Token: {token['token_name']} | Market Cap: ${market_cap:,.2f}")
        except Exception as e:
            print(f"Failed to calculate market cap for {token['token_name']}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
