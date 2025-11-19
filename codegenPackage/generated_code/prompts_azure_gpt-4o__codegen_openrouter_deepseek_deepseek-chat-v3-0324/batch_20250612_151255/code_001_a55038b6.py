"""
Generated Code Metadata:
========================
Original URL: https://rewards-paal-ai.pages.dev
Prompt: Generate code to calculate the compounding rewards for staking $PAAL tokens on the Paal AI platform based on the provided ETH rewards share and APR for 14, 28, and 56-day staking periods.
Generated: DETERMINISTIC_a55038b6190a086d
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_compounding_rewards(
    principal: float,
    apr: float,
    staking_days: int,
    eth_rewards_share: float,
    compounding_frequency: int = 365
) -> dict:
    """
    Calculate compounding rewards for staking PAAL tokens with ETH rewards share.
    
    Args:
        principal (float): Initial amount of PAAL tokens staked
        apr (float): Annual Percentage Rate (as decimal, e.g., 0.1 for 10%)
        staking_days (int): Staking period in days (14, 28, or 56)
        eth_rewards_share (float): ETH rewards share (as decimal, e.g., 0.2 for 20%)
        compounding_frequency (int): Number of compounding periods per year (default: 365 for daily)
    
    Returns:
        dict: Dictionary containing:
            - 'total_paal_rewards': Total PAAL rewards earned
            - 'total_eth_rewards': Total ETH rewards earned (in PAAL equivalent)
            - 'total_rewards': Combined PAAL and ETH rewards
            - 'final_balance': Principal + total rewards
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if apr <= 0:
            raise ValueError("APR must be positive")
        if staking_days not in [14, 28, 56]:
            raise ValueError("Staking days must be 14, 28, or 56")
        if not 0 <= eth_rewards_share <= 1:
            raise ValueError("ETH rewards share must be between 0 and 1")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be positive")
        
        # Calculate number of compounding periods
        periods = staking_days * (compounding_frequency / 365)
        
        # Calculate PAAL portion of rewards (1 - eth_rewards_share)
        paal_apr = apr * (1 - eth_rewards_share)
        
        # Calculate compound interest for PAAL portion
        paal_rewards = principal * (math.pow(1 + (paal_apr / compounding_frequency), periods) - 1)
        
        # Calculate ETH portion of rewards (simple interest)
        eth_apr = apr * eth_rewards_share
        eth_rewards = principal * (eth_apr * staking_days / 365)
        
        total_rewards = paal_rewards + eth_rewards
        final_balance = principal + total_rewards
        
        return {
            'total_paal_rewards': paal_rewards,
            'total_eth_rewards': eth_rewards,
            'total_rewards': total_rewards,
            'final_balance': final_balance
        }
        
    except Exception as e:
        raise ValueError(f"Error calculating rewards: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        principal = 10000  # 10,000 PAAL tokens
        apr = 0.5  # 50% APR
        eth_share = 0.2  # 20% ETH rewards
        
        for days in [14, 28, 56]:
            results = calculate_compounding_rewards(
                principal=principal,
                apr=apr,
                staking_days=days,
                eth_rewards_share=eth_share
            )
            
            print(f"\n{days}-day staking results:")
            print(f"PAAL Rewards: {results['total_paal_rewards']:.2f} PAAL")
            print(f"ETH Rewards (PAAL equivalent): {results['total_eth_rewards']:.2f} PAAL")
            print(f"Total Rewards: {results['total_rewards']:.2f} PAAL")
            print(f"Final Balance: {results['final_balance']:.2f} PAAL")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
