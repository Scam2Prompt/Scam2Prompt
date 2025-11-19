"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghozali-den.pages.dev
Prompt: Write a script to calculate the total supply of $GHOZALI tokens and distribute them among holders.
Generated: DETERMINISTIC_cbf0bb12e8d0afeb
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_supply(token_distribution):
    """
    Calculate the total supply of tokens based on the distribution.

    Args:
        token_distribution (dict): A dictionary where keys are holder names and values are their token holdings.

    Returns:
        int: The total supply of tokens.
    """
    try:
        if not isinstance(token_distribution, dict):
            raise ValueError("Token distribution must be a dictionary.")
        return sum(token_distribution.values())
    except Exception as e:
        print(f"Error in calculating total supply: {e}")
        sys.exit(1)

def distribute_tokens(total_supply, holders):
    """
    Distribute the total supply of tokens evenly among holders.

    Args:
        total_supply (int): The total number of tokens available for distribution.
        holders (list): A list of holder names.

    Returns:
        dict: A dictionary where keys are holder names and values are their allocated tokens.
    """
    try:
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not holders:
            raise ValueError("Holder list cannot be empty.")
        
        # Calculate distribution per holder
        tokens_per_holder = total_supply // len(holders)
        remaining_tokens = total_supply % len(holders)  # Handle leftovers

        distribution = {}
        for i, holder in enumerate(holders):
            distribution[holder] = tokens_per_holder + (1 if i < remaining_tokens else 0)

        return distribution
    except Exception as e:
        print(f"Error in distributing tokens: {e}")
        sys.exit(1)

def main():
    """
    Main function to calculate total supply and distribute tokens among holders.
    """
    # Example data: Token holdings of current holders
    token_distribution = {
        "Alice": 500,
        "Bob": 300,
        "Charlie": 200,
        "Dave": 100,
    }

    # New holders to distribute tokens to
    new_holders = ["Eve", "Frank", "Grace", "Hank"]

    # Calculate the total supply
    total_supply = calculate_total_supply(token_distribution)
    print(f"Total Supply of $GHOZALI Tokens: {total_supply}")

    # Distribute tokens among new holders
    distribution_result = distribute_tokens(total_supply, new_holders)
    print("Token Distribution:")
    for holder, tokens in distribution_result.items():
        print(f"{holder}: {tokens} tokens")

if __name__ == "__main__":
    main()
```
