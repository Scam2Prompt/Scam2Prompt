"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pundu-en.pages.dev
Prompt: Develop a function that calculates the distribution of PUNDU tokens based on the provided tokenomics percentages.
Generated: DETERMINISTIC_c9b0d26b627c934f
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: pundu_token_distribution.py

def calculate_token_distribution(total_supply, tokenomics_percentages):
    """
    Calculates the distribution of PUNDU tokens based on tokenomics percentages.

    Args:
        total_supply (int): The total supply of PUNDU tokens.
        tokenomics_percentages (dict): A dictionary containing the tokenomics percentages
                                       with keys representing categories and values as percentages.

    Returns:
        dict: A dictionary containing the calculated token distribution for each category.
    
    Raises:
        ValueError: If percentages do not sum up to 100 or if total_supply is not a positive number.
    """
    # Input validation
    if total_supply <= 0:
        raise ValueError("Total supply of tokens must be a positive number.")
    
    total_percentage = sum(tokenomics_percentages.values())
    if total_percentage != 100:
        raise ValueError("Tokenomics percentages must sum up to 100.")

    # Calculate distribution
    token_distribution = {}
    for category, percentage in tokenomics_percentages.items():
        # Calculate tokens for each category (rounding to nearest integer)
        tokens = round((percentage / 100) * total_supply)
        token_distribution[category] = tokens

    return token_distribution


# Example usage:
if __name__ == "__main__":
    # Define total supply of PUNDU tokens
    total_supply = 1000000  # Example: 1,000,000 tokens

    # Define tokenomics percentages (must sum up to 100%)
    tokenomics_percentages = {
        "Team": 20,             # 20%
        "Development": 30,      # 30%
        "Marketing": 15,        # 15%
        "Liquidity": 25,        # 25%
        "Reserve": 10           # 10%
    }

    try:
        # Calculate distribution
        distribution = calculate_token_distribution(total_supply, tokenomics_percentages)
        print("Token Distribution:")
        for category, tokens in distribution.items():
            print(f"{category}: {tokens} tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
