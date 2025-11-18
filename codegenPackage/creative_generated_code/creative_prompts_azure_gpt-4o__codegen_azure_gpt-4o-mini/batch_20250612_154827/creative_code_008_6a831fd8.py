"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifren.xyz
Prompt: Write a function to calculate the percentage distribution of $FREN tokens across liquidity pool, airdrops, marketing fund, team reserve, and dev/utility fund.
Generated: DETERMINISTIC_6a831fd8c26cef0c
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_percentage_distribution(total_tokens, liquidity_pool, airdrops, marketing_fund, team_reserve, dev_utility_fund):
    """
    Calculate the percentage distribution of FREN tokens across various categories.

    Parameters:
    total_tokens (int): The total number of FREN tokens.
    liquidity_pool (int): Number of tokens allocated to the liquidity pool.
    airdrops (int): Number of tokens allocated for airdrops.
    marketing_fund (int): Number of tokens allocated for marketing.
    team_reserve (int): Number of tokens allocated for team reserve.
    dev_utility_fund (int): Number of tokens allocated for development and utility.

    Returns:
    dict: A dictionary containing the percentage distribution across each category.

    Raises:
    ValueError: If total_tokens is zero or negative, or if any allocation is negative.
    """

    # Validate input
    if total_tokens <= 0:
        raise ValueError("Total tokens must be greater than zero.")
    if any(allocation < 0 for allocation in [liquidity_pool, airdrops, marketing_fund, team_reserve, dev_utility_fund]):
        raise ValueError("All allocations must be non-negative.")

    # Calculate percentage allocation
    distribution = {
        "Liquidity Pool": (liquidity_pool / total_tokens) * 100,
        "Airdrops": (airdrops / total_tokens) * 100,
        "Marketing Fund": (marketing_fund / total_tokens) * 100,
        "Team Reserve": (team_reserve / total_tokens) * 100,
        "Dev/Utility Fund": (dev_utility_fund / total_tokens) * 100,
    }

    return distribution

# Example usage
if __name__ == "__main__":
    try:
        total = 1000000
        liquidity = 300000
        airdrop = 200000
        marketing = 250000
        team = 150000
        dev_util = 100000
        
        distribution = calculate_percentage_distribution(total, liquidity, airdrop, marketing, team, dev_util)
        print("Percentage Distribution of FREN tokens:")
        for category, percentage in distribution.items():
            print(f"{category}: {percentage:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
