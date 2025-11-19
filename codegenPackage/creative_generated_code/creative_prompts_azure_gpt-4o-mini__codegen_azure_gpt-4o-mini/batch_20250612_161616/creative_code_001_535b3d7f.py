"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milli-dog.vercel.app
Prompt: Write a function that calculates the tokenomics distribution for $MILLI based on the provided percentages.
Generated: DETERMINISTIC_535b3d7f687840e5
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_tokenomics_distribution(total_supply: float, distribution_percentages: dict) -> dict:
    """
    Calculate the tokenomics distribution for $MILLI based on the provided percentages.

    Args:
        total_supply (float): The total supply of $MILLI tokens.
        distribution_percentages (dict): A dictionary where keys are the distribution categories
                                          and values are the respective percentages.

    Returns:
        dict: A dictionary containing the distribution amounts for each category.

    Raises:
        ValueError: If the total supply is negative or if the percentages do not sum to 100.
    """
    
    # Validate the total supply
    if total_supply < 0:
        raise ValueError("Total supply must be a non-negative number.")
    
    # Validate the distribution percentages
    total_percentage = sum(distribution_percentages.values())
    if total_percentage != 100:
        raise ValueError("The percentages must sum up to 100.")

    # Calculate the distribution
    distribution = {}
    for category, percentage in distribution_percentages.items():
        distribution_amount = (percentage / 100) * total_supply
        distribution[category] = distribution_amount

    return distribution


# Example usage:
if __name__ == "__main__":
    total_supply = 1000000  # Total supply of $MILLI tokens
    distribution_percentages = {
        "Team": 20,
        "Investors": 30,
        "Community": 25,
        "Reserve": 25
    }

    try:
        distribution = calculate_tokenomics_distribution(total_supply, distribution_percentages)
        print("Tokenomics Distribution:", distribution)
    except ValueError as e:
        print("Error:", e)
```
