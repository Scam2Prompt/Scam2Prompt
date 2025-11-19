"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gummy.pages.dev
Prompt: Write a code snippet to calculate the tokenomics distribution for $Gummy, including percentages for liquidity, marketing, and team allocations.
Generated: DETERMINISTIC_7d5b1f68dad864bc
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Tokenomics Distribution Calculator for $Gummy

def calculate_tokenomics(total_supply, allocations):
    """
    Calculate the tokenomics distribution based on given allocations.

    Args:
        total_supply (int): Total supply of tokens ($Gummy).
        allocations (dict): Allocation percentages for each category 
                            (keys: category names, values: allocation percentages).

    Returns:
        dict: Token distribution with category names as keys and token amounts as values.
    """
    # Validate inputs
    if total_supply <= 0:
        raise ValueError("Total supply must be a positive number.")
    
    if not isinstance(allocations, dict) or not allocations:
        raise ValueError("Allocations must be a non-empty dictionary.")
    
    if sum(allocations.values()) != 100:
        raise ValueError("The sum of allocation percentages must equal 100.")

    # Compute token allocations
    token_distribution = {}
    for category, percentage in allocations.items():
        if percentage < 0:
            raise ValueError(f"Allocation percentage for '{category}' cannot be negative.")
        token_distribution[category] = (total_supply * percentage) // 100

    return token_distribution


# Example usage
if __name__ == "__main__":
    try:
        # Total supply of $Gummy tokens
        total_supply = 1_000_000  # 1 million tokens

        # Allocations in percentages
        allocations = {
            "Liquidity": 40,   # 40%
            "Marketing": 30,   # 30%
            "Team": 20,        # 20%
            "Reserve": 10      # 10%
        }

        # Calculate and display the token distribution
        token_distribution = calculate_tokenomics(total_supply, allocations)
        print("Tokenomics Distribution for $Gummy:")
        for category, amount in token_distribution.items():
            print(f"{category}: {amount} tokens")

    except ValueError as e:
        print(f"Error: {e}")
```
