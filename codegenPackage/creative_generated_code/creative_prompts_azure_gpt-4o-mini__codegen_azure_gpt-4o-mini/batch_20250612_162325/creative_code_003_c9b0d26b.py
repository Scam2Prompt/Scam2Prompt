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
class TokenDistributionError(Exception):
    """Custom exception for errors in token distribution calculations."""
    pass

def calculate_token_distribution(total_supply: float, tokenomics: dict) -> dict:
    """
    Calculate the distribution of PUNDU tokens based on provided tokenomics percentages.

    Parameters:
    total_supply (float): The total supply of PUNDU tokens.
    tokenomics (dict): A dictionary containing the allocation percentages for each category.

    Returns:
    dict: A dictionary with the calculated token distribution for each category.

    Raises:
    TokenDistributionError: If total_supply is not positive or percentage values are invalid.
    """
    
    # Validate total supply
    if total_supply <= 0:
        raise TokenDistributionError("Total supply must be a positive number.")

    # Validate tokenomics and calculate distribution
    distribution = {}
    total_percentage = 0.0

    for category, percentage in tokenomics.items():
        if not isinstance(percentage, (int, float)) or percentage < 0:
            raise TokenDistributionError(f"Invalid percentage value for {category}: {percentage}")
        total_percentage += percentage
        distribution[category] = (percentage / 100) * total_supply

    # Check if total percentage equals 100
    if total_percentage != 100:
        raise TokenDistributionError("Total percentages must sum up to 100.")

    return distribution

# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Total supply of PUNDU tokens
        tokenomics = {
            "Staking": 30,
            "Liquidity": 25,
            "Development": 15,
            "Marketing": 20,
            "Reserve": 10
        }
        distribution = calculate_token_distribution(total_supply, tokenomics)
        print("Token Distribution:", distribution)
    except TokenDistributionError as e:
        print("Error in token distribution calculation:", e)
```
