"""
Generated Code Metadata:
========================
Original URL: https://stader.pages.dev
Prompt: Create a function that calculates the ETHx exchange rate (1 ETHx = 1.029570 ETH) and simulates the staking rewards based on the annualized rate of 2.72%.
Generated: DETERMINISTIC_0ff37a4cc6c50ec3
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_ethx_exchange_rate(eth_amount: float) -> float:
    """
    Calculate the equivalent ETHx amount based on the given ETH amount.
    
    Args:
        eth_amount (float): Amount of ETH to convert to ETHx.
        
    Returns:
        float: Equivalent ETHx amount.
    """
    if eth_amount < 0:
        raise ValueError("ETH amount cannot be negative")
    return eth_amount / 1.029570


def calculate_staking_rewards(
    principal: float,
    annual_rate: float = 2.72,
    days_staked: int = 365
) -> float:
    """
    Calculate staking rewards based on annualized rate and staking period.
    
    Args:
        principal (float): Initial amount of ETHx staked.
        annual_rate (float, optional): Annualized reward rate in percentage. Defaults to 2.72.
        days_staked (int, optional): Number of days staked. Defaults to 365.
        
    Returns:
        float: Total rewards earned in ETHx.
        
    Raises:
        ValueError: If any input is invalid.
    """
    if principal < 0:
        raise ValueError("Principal cannot be negative")
    if annual_rate < 0:
        raise ValueError("Annual rate cannot be negative")
    if days_staked < 0:
        raise ValueError("Days staked cannot be negative")
        
    daily_rate = annual_rate / 100 / 365
    return principal * daily_rate * days_staked


def simulate_staking(
    eth_amount: float,
    annual_rate: float = 2.72,
    days_staked: int = 365
) -> dict:
    """
    Simulate ETH to ETHx conversion and staking rewards.
    
    Args:
        eth_amount (float): Amount of ETH to convert and stake.
        annual_rate (float, optional): Annualized reward rate in percentage. Defaults to 2.72.
        days_staked (int, optional): Number of days staked. Defaults to 365.
        
    Returns:
        dict: Dictionary containing:
            - eth_amount: Original ETH amount
            - ethx_amount: Converted ETHx amount
            - rewards: Earned rewards in ETHx
            - total: Total ETHx after rewards
    """
    try:
        ethx_amount = calculate_ethx_exchange_rate(eth_amount)
        rewards = calculate_staking_rewards(ethx_amount, annual_rate, days_staked)
        
        return {
            "eth_amount": eth_amount,
            "ethx_amount": ethx_amount,
            "rewards": rewards,
            "total": ethx_amount + rewards
        }
    except ValueError as e:
        raise ValueError(f"Invalid input: {str(e)}")
```
