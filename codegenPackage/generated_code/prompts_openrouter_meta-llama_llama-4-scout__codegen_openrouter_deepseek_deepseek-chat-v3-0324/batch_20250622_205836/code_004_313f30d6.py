"""
Generated Code Metadata:
========================
Original URL: https://pinknotyellowsale.pages.dev
Prompt: "Create a function to calculate the maximum approved RPL balance for v1 rETH, given the current ETH staking amount across multiple node operators."
Generated: DETERMINISTIC_313f30d6e784aa55
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_max_rpl_balance(
    eth_staking_amounts: list[float], 
    rpl_staked_per_node: list[float], 
    min_rpl_stake_per_eth: float = 0.1,
    max_rpl_stake_per_eth: float = 1.5
) -> float:
    """
    Calculate the maximum approved RPL balance for v1 rETH given ETH staking amounts.
    
    Args:
        eth_staking_amounts: List of ETH amounts staked by each node operator
        rpl_staked_per_node: List of RPL amounts staked by each node operator
        min_rpl_stake_per_eth: Minimum RPL required per ETH staked (default 0.1)
        max_rpl_stake_per_eth: Maximum RPL allowed per ETH staked (default 1.5)
    
    Returns:
        float: The maximum approved RPL balance
    
    Raises:
        ValueError: If input lists are empty or lengths don't match
    """
    # Validate inputs
    if not eth_staking_amounts or not rpl_staked_per_node:
        raise ValueError("ETH staking amounts and RPL staked lists cannot be empty")
    if len(eth_staking_amounts) != len(rpl_staked_per_node):
        raise ValueError("ETH staking amounts and RPL staked lists must be same length")
    
    total_eth_staked = sum(eth_staking_amounts)
    total_rpl_staked = sum(rpl_staked_per_node)
    
    # Calculate min and max RPL bounds based on ETH staked
    min_rpl_required = total_eth_staked * min_rpl_stake_per_eth
    max_rpl_allowed = total_eth_staked * max_rpl_stake_per_eth
    
    # Ensure current RPL staked meets minimum requirement
    if total_rpl_staked < min_rpl_required:
        raise ValueError(f"Total RPL staked ({total_rpl_staked}) is below minimum requirement ({min_rpl_required})")
    
    # Return the minimum of current RPL staked and max allowed
    return min(total_rpl_staked, max_rpl_allowed)
```
