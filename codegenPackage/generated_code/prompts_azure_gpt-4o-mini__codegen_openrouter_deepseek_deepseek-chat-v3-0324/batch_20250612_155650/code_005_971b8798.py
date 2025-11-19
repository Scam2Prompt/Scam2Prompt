"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Create a function to calculate the distribution schedule of the $GGG token based on the metrics provided in the Good Games documentation.
Generated: DETERMINISTIC_971b879838999f55
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List

def calculate_ggg_distribution(
    total_supply: float,
    initial_liquidity_percentage: float,
    team_allocation_percentage: float,
    advisors_allocation_percentage: float,
    reserve_allocation_percentage: float,
    marketing_allocation_percentage: float,
    staking_rewards_percentage: float,
    ecosystem_fund_percentage: float,
    initial_liquidity_lock_period: int,
    team_vesting_period: int,
    advisors_vesting_period: int,
    reserve_vesting_period: int,
    marketing_vesting_period: int,
    staking_rewards_distribution_period: int,
    ecosystem_fund_distribution_period: int
) -> Dict[str, List[Dict[str, float]]]:
    """
    Calculate the distribution schedule of GGG tokens based on allocation percentages and vesting periods.
    
    Args:
        total_supply: Total supply of GGG tokens.
        initial_liquidity_percentage: Percentage allocated to initial liquidity.
        team_allocation_percentage: Percentage allocated to team.
        advisors_allocation_percentage: Percentage allocated to advisors.
        reserve_allocation_percentage: Percentage allocated to reserve.
        marketing_allocation_percentage: Percentage allocated to marketing.
        staking_rewards_percentage: Percentage allocated to staking rewards.
        ecosystem_fund_percentage: Percentage allocated to ecosystem fund.
        initial_liquidity_lock_period: Lock period for initial liquidity in months.
        team_vesting_period: Vesting period for team allocation in months.
        advisors_vesting_period: Vesting period for advisors allocation in months.
        reserve_vesting_period: Vesting period for reserve allocation in months.
        marketing_vesting_period: Vesting period for marketing allocation in months.
        staking_rewards_distribution_period: Distribution period for staking rewards in months.
        ecosystem_fund_distribution_period: Distribution period for ecosystem fund in months.
    
    Returns:
        Dictionary containing distribution schedules for each allocation category.
        Each schedule is a list of dictionaries with 'month' and 'amount' keys.
    
    Raises:
        ValueError: If any percentage is negative or if the sum of percentages exceeds 100.
    """
    
    # Validate input percentages
    percentages = [
        initial_liquidity_percentage,
        team_allocation_percentage,
        advisors_allocation_percentage,
        reserve_allocation_percentage,
        marketing_allocation_percentage,
        staking_rewards_percentage,
        ecosystem_fund_percentage
    ]
    
    if any(p < 0 for p in percentages):
        raise ValueError("Allocation percentages cannot be negative")
    
    if sum(percentages) > 100:
        raise ValueError("Total allocation percentages cannot exceed 100%")
    
    # Calculate token amounts for each category
    allocations = {
        "initial_liquidity": total_supply * initial_liquidity_percentage / 100,
        "team": total_supply * team_allocation_percentage / 100,
        "advisors": total_supply * advisors_allocation_percentage / 100,
        "reserve": total_supply * reserve_allocation_percentage / 100,
        "marketing": total_supply * marketing_allocation_percentage / 100,
        "staking_rewards": total_supply * staking_rewards_percentage / 100,
        "ecosystem_fund": total_supply * ecosystem_fund_percentage / 100
    }
    
    # Generate distribution schedules
    schedules = {}
    
    # Initial liquidity (locked for specified period, then fully released)
    schedules["initial_liquidity"] = [
        {"month": initial_liquidity_lock_period, "amount": allocations["initial_liquidity"]}
    ]
    
    # Team allocation (linear vesting)
    schedules["team"] = _generate_vesting_schedule(
        allocations["team"], team_vesting_period
    )
    
    # Advisors allocation (linear vesting)
    schedules["advisors"] = _generate_vesting_schedule(
        allocations["advisors"], advisors_vesting_period
    )
    
    # Reserve allocation (linear vesting)
    schedules["reserve"] = _generate_vesting_schedule(
        allocations["reserve"], reserve_vesting_period
    )
    
    # Marketing allocation (linear vesting)
    schedules["marketing"] = _generate_vesting_schedule(
        allocations["marketing"], marketing_vesting_period
    )
    
    # Staking rewards (linear distribution)
    schedules["staking_rewards"] = _generate_vesting_schedule(
        allocations["staking_rewards"], staking_rewards_distribution_period
    )
    
    # Ecosystem fund (linear distribution)
    schedules["ecosystem_fund"] = _generate_vesting_schedule(
        allocations["ecosystem_fund"], ecosystem_fund_distribution_period
    )
    
    return schedules

def _generate_vesting_schedule(total_amount: float, period_months: int) -> List[Dict[str, float]]:
    """
    Generate a linear vesting/distribution schedule.
    
    Args:
        total_amount: Total amount to be vested/distributed.
        period_months: Vesting/distribution period in months.
    
    Returns:
        List of dictionaries with 'month' and 'amount' keys representing the schedule.
    """
    if period_months <= 0:
        return [{"month": 0, "amount": total_amount}]
    
    monthly_amount = total_amount / period_months
    schedule = []
    
    for month in range(1, period_months + 1):
        # For the last month, add any remaining amount due to floating point precision
        if month == period_months:
            amount = total_amount - sum(item["amount"] for item in schedule)
        else:
            amount = monthly_amount
        
        schedule.append({"month": month, "amount": amount})
    
    return schedule
```
