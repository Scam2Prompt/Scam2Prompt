"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone.cx
Prompt: Generate code to calculate the distribution of $INIT tokens across different categories (Community Reserve, Investors, Treasury, etc.) based on the tokenomics provided on the Initia website.
Generated: DETERMINISTIC_a987ecbdb837dbbd
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the distribution of $INIT tokens across different categories
# based on tokenomics provided. This script assumes tokenomics data is provided in a dictionary.

def calculate_token_distribution(total_supply, tokenomics):
    """
    Calculates the distribution of tokens across different categories.

    Parameters:
        total_supply (int): Total number of tokens available.
        tokenomics (dict): Tokenomics data specifying percentage allocation for each category.

    Returns:
        dict: A dictionary containing the allocation of tokens for each category.
    """
    try:
        # Validate inputs
        if not isinstance(total_supply, (int, float)) or total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        if not isinstance(tokenomics, dict) or not tokenomics:
            raise ValueError("Tokenomics must be a non-empty dictionary.")

        # Ensure percentages in tokenomics add up to 100%
        total_percentage = sum(tokenomics.values())
        if total_percentage != 100:
            raise ValueError("Tokenomics percentages must add up to 100%. Current total: {:.2f}".format(total_percentage))

        # Calculate the distribution
        distribution = {}
        for category, percentage in tokenomics.items():
            allocation = total_supply * (percentage / 100)
            distribution[category] = round(allocation, 2)  # Round to 2 decimal places for readability

        return distribution

    except Exception as e:
        print(f"Error calculating token distribution: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    # Define total supply and tokenomics percentages
    total_supply = 100000000  # Example: 100 million tokens
    tokenomics = {
        "Community Reserve": 40,  # 40% allocation
        "Investors": 30,         # 30% allocation
        "Treasury": 20,          # 20% allocation
        "Team": 10               # 10% allocation
    }

    # Calculate the distribution
    distribution = calculate_token_distribution(total_supply, tokenomics)

    if distribution:
        print("Token Distribution:")
        for category, amount in distribution.items():
            print(f"{category}: {amount} tokens")
```
