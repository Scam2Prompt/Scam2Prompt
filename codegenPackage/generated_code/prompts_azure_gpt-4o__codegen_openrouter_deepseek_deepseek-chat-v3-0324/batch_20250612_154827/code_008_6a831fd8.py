"""
Generated Code Metadata:
========================
Original URL: https://suifren.xyz
Prompt: Write a function to calculate the percentage distribution of $FREN tokens across liquidity pool, airdrops, marketing fund, team reserve, and dev/utility fund.
Generated: DETERMINISTIC_6a831fd8c26cef0c
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_token_distribution(
    total_supply: float,
    liquidity_pool_pct: float,
    airdrops_pct: float,
    marketing_fund_pct: float,
    team_reserve_pct: float,
    dev_utility_pct: float
) -> dict:
    """
    Calculate the token distribution across different categories based on given percentages.
    
    Args:
        total_supply: Total supply of $FREN tokens.
        liquidity_pool_pct: Percentage allocated to liquidity pool (0-100).
        airdrops_pct: Percentage allocated to airdrops (0-100).
        marketing_fund_pct: Percentage allocated to marketing fund (0-100).
        team_reserve_pct: Percentage allocated to team reserve (0-100).
        dev_utility_pct: Percentage allocated to dev/utility fund (0-100).
    
    Returns:
        Dictionary containing the token amounts for each category.
    
    Raises:
        ValueError: If percentages don't sum to 100 or any percentage is invalid.
    """
    
    # Validate input percentages
    percentages = [
        liquidity_pool_pct,
        airdrops_pct,
        marketing_fund_pct,
        team_reserve_pct,
        dev_utility_pct
    ]
    
    if not all(0 <= p <= 100 for p in percentages):
        raise ValueError("All percentages must be between 0 and 100")
    
    if sum(percentages) != 100:
        raise ValueError("Percentages must sum to 100")
    
    # Calculate token amounts
    distribution = {
        "liquidity_pool": total_supply * liquidity_pool_pct / 100,
        "airdrops": total_supply * airdrops_pct / 100,
        "marketing_fund": total_supply * marketing_fund_pct / 100,
        "team_reserve": total_supply * team_reserve_pct / 100,
        "dev_utility_fund": total_supply * dev_utility_pct / 100
    }
    
    return distribution
```
