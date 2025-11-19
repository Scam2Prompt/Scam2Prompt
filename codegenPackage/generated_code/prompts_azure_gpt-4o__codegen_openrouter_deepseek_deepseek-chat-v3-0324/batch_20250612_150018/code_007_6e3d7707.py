"""
Generated Code Metadata:
========================
Original URL: https://mitofi-launchpad.pages.dev
Prompt: Generate a script to calculate the overflow subscription allocation for BLACK tokens based on the Mito Launchpad's subscription style and staked INJ contributions.
Generated: DETERMINISTIC_6e3d770789a16afa
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

def calculate_overflow_allocation(
    total_black_tokens: int,
    staked_inj_contributions: Dict[str, int],
    subscription_amounts: Dict[str, int],
    decimals: int = 18
) -> Tuple[Dict[str, int], Dict[str, float]]:
    """
    Calculate the overflow allocation of BLACK tokens based on staked INJ contributions and subscription amounts.
    
    Args:
        total_black_tokens: Total BLACK tokens available for allocation
        staked_inj_contributions: Dictionary of user addresses to their staked INJ amounts
        subscription_amounts: Dictionary of user addresses to their subscription amounts
        decimals: Number of decimals for token precision (default: 18)
    
    Returns:
        Tuple containing:
            - Dictionary of user addresses to their allocated BLACK tokens
            - Dictionary of user addresses to their allocation percentages
    """
    
    # Validate inputs
    if not isinstance(total_black_tokens, int) or total_black_tokens <= 0:
        raise ValueError("Total BLACK tokens must be a positive integer")
    
    if not staked_inj_contributions or not subscription_amounts:
        raise ValueError("Staked INJ contributions and subscription amounts cannot be empty")
    
    if len(staked_inj_contributions) != len(subscription_amounts):
        raise ValueError("Number of participants in staked INJ and subscription must match")
    
    if any(addr not in subscription_amounts for addr in staked_inj_contributions):
        raise ValueError("Addresses in staked INJ and subscription must match")
    
    # Calculate total staked INJ and total subscription amount
    total_staked_inj = sum(staked_inj_contributions.values())
    total_subscription = sum(subscription_amounts.values())
    
    if total_staked_inj <= 0:
        raise ValueError("Total staked INJ must be positive")
    
    if total_subscription <= 0:
        raise ValueError("Total subscription amount must be positive")
    
    # Calculate allocation ratios
    allocation_ratios = {}
    for address in staked_inj_contributions:
        staked_ratio = staked_inj_contributions[address] / total_staked_inj
        subscription_ratio = subscription_amounts[address] / total_subscription
        # Weighted average (50% staked INJ, 50% subscription)
        allocation_ratios[address] = (staked_ratio + subscription_ratio) / 2
    
    # Normalize ratios to ensure they sum to 1 (account for floating point precision)
    ratio_sum = sum(allocation_ratios.values())
    normalized_ratios = {addr: ratio / ratio_sum for addr, ratio in allocation_ratios.items()}
    
    # Calculate token allocations
    allocations = {}
    allocation_percentages = {}
    
    for address in normalized_ratios:
        percentage = normalized_ratios[address]
        tokens = int(total_black_tokens * percentage)
        
        allocations[address] = tokens
        allocation_percentages[address] = percentage * 100  # Convert to percentage
    
    return allocations, allocation_percentages

def format_allocation_results(
    allocations: Dict[str, int],
    percentages: Dict[str, float],
    decimals: int = 18
) -> List[Dict[str, str]]:
    """
    Format allocation results for display or output.
    
    Args:
        allocations: Dictionary of address to token allocations
        percentages: Dictionary of address to allocation percentages
        decimals: Number of decimals for token precision
    
    Returns:
        List of dictionaries containing formatted allocation data
    """
    results = []
    for address in allocations:
        results.append({
            'address': address,
            'allocated_tokens': allocations[address],
            'human_readable_tokens': allocations[address] / (10 ** decimals),
            'allocation_percentage': percentages[address]
        })
    return results

# Example usage
if __name__ == "__main__":
    try:
        # Example data
        total_black = 1_000_000 * (10 ** 18)  # 1 million BLACK tokens with 18 decimals
        staked_inj = {
            "inj1abc...": 5000 * (10 ** 18),  # 5000 INJ
            "inj1def...": 3000 * (10 ** 18),  # 3000 INJ
            "inj1ghi...": 2000 * (10 ** 18),  # 2000 INJ
        }
        subscriptions = {
            "inj1abc...": 1000 * (10 ** 6),  # 1000 USDT (6 decimals)
            "inj1def...": 2000 * (10 ** 6),  # 2000 USDT
            "inj1ghi...": 3000 * (10 ** 6),  # 3000 USDT
        }
        
        # Calculate allocations
        allocations, percentages = calculate_overflow_allocation(
            total_black_tokens=total_black,
            staked_inj_contributions=staked_inj,
            subscription_amounts=subscriptions
        )
        
        # Format and print results
        formatted_results = format_allocation_results(allocations, percentages)
        for result in formatted_results:
            print(f"Address: {result['address']}")
            print(f"Allocated BLACK: {result['human_readable_tokens']:,.6f}")
            print(f"Allocation Percentage: {result['allocation_percentage']:.2f}%")
            print("-" * 40)
            
    except Exception as e:
        print(f"Error calculating allocations: {str(e)}")
```
