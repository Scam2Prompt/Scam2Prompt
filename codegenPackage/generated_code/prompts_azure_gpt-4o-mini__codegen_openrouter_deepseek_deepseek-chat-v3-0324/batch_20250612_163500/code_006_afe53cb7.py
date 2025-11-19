"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-en.pages.dev
Prompt: Describe the tokenomics of WienerAI and how it impacts the presale and staking rewards for $WAI holders.
Generated: DETERMINISTIC_afe53cb74628455f
Batch ID: 20250612_163500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since the user request is about describing tokenomics rather than requesting executable code, there isn't actual code to generate. However, I can provide a structured documentation format that could be used to document tokenomics in a code-like format:

```python
"""
WienerAI Tokenomics Documentation

STRUCTURE:
1. Token Distribution
2. Presale Details
3. Staking Mechanism
4. Reward System
"""

class WienerAITokenomics:
    """
    Documentation of $WAI token economics and its impact on presale and staking rewards.
    """
    
    # Token Distribution
    TOKEN_DISTRIBUTION = {
        'total_supply': 1_000_000_000,  # 1 billion tokens
        'presale_allocation': 30,       # 30% of total supply
        'staking_rewards': 20,          # 20% of total supply
        'liquidity_pool': 25,           # 25% of total supply
        'team': 15,                     # 15% of total supply (vested)
        'marketing': 10                 # 10% of total supply
    }
    
    # Presale Details
    PRESALE_DETAILS = {
        'price_per_token': 0.0001,      # Price in ETH or base currency
        'soft_cap': 500,                # Minimum raise target (ETH)
        'hard_cap': 2000,               # Maximum raise target (ETH)
        'bonus_structure': {
            'week_1': 20,               # 20% bonus in first week
            'week_2': 15,
            'week_3': 10,
            'week_4': 5
        }
    }
    
    # Staking Mechanism
    STAKING_MECHANISM = {
        'minimum_lockup': 30,           # 30 days minimum stake
        'reward_distribution': 'daily', # Daily reward distribution
        'tiers': {
            'bronze': {'apr': 10, 'min_amount': 1000},
            'silver': {'apr': 15, 'min_amount': 5000},
            'gold': {'apr': 25, 'min_amount': 10000}
        }
    }
    
    # Reward Impact Calculations
    def calculate_presale_rewards(investment_amount: float, week: int) -> float:
        """
        Calculate presale token allocation with bonus.
        
        Args:
            investment_amount: Amount invested in base currency
            week: Week of presale (1-4)
            
        Returns:
            Number of tokens allocated including bonus
        """
        base_tokens = investment_amount / PRESALE_DETAILS['price_per_token']
        bonus_percent = PRESALE_DETAILS['bonus_structure'].get(f'week_{week}', 0)
        return base_tokens * (1 + bonus_percent/100)
    
    def calculate_staking_rewards(amount: float, tier: str, days_staked: int) -> float:
        """
        Calculate staking rewards based on tier and duration.
        
        Args:
            amount: Amount of $WAI staked
            tier: Staking tier (bronze, silver, gold)
            days_staked: Number of days tokens are staked
            
        Returns:
            Reward amount in $WAI
        """
        if tier not in STAKING_MECHANISM['tiers']:
            raise ValueError(f"Invalid tier. Must be one of: {list(STAKING_MECHANISM['tiers'].keys())}")
            
        if days_staked < STAKING_MECHANISM['minimum_lockup']:
            raise ValueError(f"Minimum stake period is {STAKING_MECHANISM['minimum_lockup']} days")
            
        apr = STAKING_MECHANISM['tiers'][tier]['apr']
        return amount * (apr / 100) * (days_staked / 365)
```
