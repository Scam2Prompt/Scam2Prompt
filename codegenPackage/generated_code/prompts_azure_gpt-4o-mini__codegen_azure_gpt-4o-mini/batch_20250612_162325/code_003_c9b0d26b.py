"""
Generated Code Metadata:
========================
Original URL: https://pundu-en.pages.dev
Prompt: Develop a function that calculates the distribution of PUNDU tokens based on the provided tokenomics percentages.
Generated: DETERMINISTIC_c9b0d26b627c934f
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenDistributionError(Exception):
    """Custom exception for errors in token distribution calculations."""
    pass

def calculate_token_distribution(total_supply: float, tokenomics: dict) -> dict:
    """
    Calculate the distribution of PUNDU tokens based on provided tokenomics percentages.

    Args:
        total_supply (float): The total supply of PUNDU tokens.
        tokenomics (dict): A dictionary containing the distribution percentages for various categories.
                           Example: {'team': 20, 'advisors': 10, 'community': 30, 'investors': 40}

    Returns:
        dict: A dictionary with the calculated token amounts for each category.

    Raises:
        TokenDistributionError: If the total percentage does not equal 100 or if total_supply is negative.
    """
    
    # Validate total supply
    if total_supply < 0:
        raise TokenDistributionError("Total supply must be a non-negative value.")
    
    # Validate tokenomics percentages
    total_percentage = sum(tokenomics.values())
    if total_percentage != 100:
        raise TokenDistributionError("Total percentages must equal 100.")

    # Calculate token distribution
    distribution = {}
    for category, percentage in tokenomics.items():
        distribution[category] = (percentage / 100) * total_supply

    return distribution

# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Total supply of PUNDU tokens
        tokenomics = {
            'team': 20,
            'advisors': 10,
            'community': 30,
            'investors': 40
        }
        
        distribution = calculate_token_distribution(total_supply, tokenomics)
        print("Token Distribution:", distribution)
    except TokenDistributionError as e:
        print(f"Error: {e}")
```
