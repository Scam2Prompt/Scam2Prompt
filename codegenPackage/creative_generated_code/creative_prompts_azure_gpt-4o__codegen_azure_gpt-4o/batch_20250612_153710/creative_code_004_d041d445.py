"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpmeme.net
Prompt: Write a function in Python using Web3.py to calculate and display the token distribution percentages (Liquidity, Marketing, Airdrop, Binance Launchpool) for the TRUMP MEME token based on the tokenomics data provided.
Generated: DETERMINISTIC_d041d4458322b6ca
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from web3 import Web3

def calculate_token_distribution(tokenomics_data):
    """
    Calculate and display token distribution percentages for the TRUMP MEME token.

    Parameters:
        tokenomics_data (dict): A dictionary containing tokenomics data with keys as categories 
                                and values as token amounts.

    Example:
        tokenomics_data = {
            "Liquidity": 500000,
            "Marketing": 300000,
            "Airdrop": 100000,
            "Binance Launchpool": 100000
        }

    Returns:
        dict: A dictionary containing token distribution percentages for each category.
    """
    try:
        # Validate input
        if not isinstance(tokenomics_data, dict):
            raise ValueError("Tokenomics data must be a dictionary.")

        total_tokens = sum(tokenomics_data.values())
        if total_tokens == 0:
            raise ValueError("Total token supply cannot be zero.")

        # Calculate percentages
        distribution_percentages = {
            category: (amount / total_tokens) * 100
            for category, amount in tokenomics_data.items()
        }

        # Display results
        print("Token Distribution Percentages:")
        for category, percentage in distribution_percentages.items():
            print(f"{category}: {percentage:.2f}%")

        return distribution_percentages

    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Tokenomics data for TRUMP MEME token
    tokenomics_data = {
        "Liquidity": 500000,
        "Marketing": 300000,
        "Airdrop": 100000,
        "Binance Launchpool": 100000
    }

    calculate_token_distribution(tokenomics_data)
```
