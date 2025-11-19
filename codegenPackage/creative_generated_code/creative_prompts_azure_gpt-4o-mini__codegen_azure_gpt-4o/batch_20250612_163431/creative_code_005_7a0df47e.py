"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retiksupport.pages.dev
Prompt: Create a function to calculate the tokenomics distribution for the RETIK token based on the provided data.
Generated: DETERMINISTIC_7a0df47eb0819435
Batch ID: 20250612_163431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate tokenomics distribution for the RETIK token.

def calculate_tokenomics_distribution(total_supply, distributions):
    """
    Calculate the tokenomics distribution for the RETIK token.

    Parameters:
        total_supply (int): The total supply of tokens.
        distributions (dict): A dictionary containing token distribution categories as keys and
                              their percentage (0-100) as values.

    Returns:
        dict: A dictionary with the token distribution breakdown in terms of token count.
    """
    # Validate input
    if not isinstance(total_supply, (int, float)) or total_supply <= 0:
        raise ValueError("Total supply must be a positive number.")

    if not isinstance(distributions, dict) or not distributions:
        raise ValueError("Distributions must be a non-empty dictionary.")

    if sum(distributions.values()) != 100:
        raise ValueError("The sum of all percentages in distributions must equal 100.")

    # Calculate the distribution of tokens for each category
    distribution_result = {}
    for category, percentage in distributions.items():
        if not isinstance(percentage, (int, float)) or percentage < 0:
            raise ValueError(f"Percentage for '{category}' must be a non-negative number.")
        distribution_result[category] = round((percentage / 100) * total_supply)

    return distribution_result


# Example usage:
if __name__ == "__main__":
    try:
        # Tokenomics data
        total_supply = 1_000_000  # Total supply of RETIK tokens
        distributions = {
            "Founders": 20,        # 20% for founders
            "Development": 30,     # 30% for development
            "Marketing": 25,       # 25% for marketing
            "Community Rewards": 15, # 15% for community rewards
            "Reserve": 10          # 10% for reserve
        }

        # Calculate and display the tokenomics distribution
        result = calculate_tokenomics_distribution(total_supply, distributions)
        print("Tokenomics Distribution:")
        for category, tokens in result.items():
            print(f"{category}: {tokens} tokens")
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
```
