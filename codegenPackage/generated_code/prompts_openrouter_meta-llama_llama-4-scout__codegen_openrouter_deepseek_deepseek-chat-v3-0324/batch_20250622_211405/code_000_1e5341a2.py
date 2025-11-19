"""
Generated Code Metadata:
========================
Original URL: https://clearpool.pages.dev
Prompt: Write a Python script to calculate the APR for staking CPOOL tokens with different oracles on Clearpool, considering the oracle size and relative voting power.
Generated: DETERMINISTIC_1e5341a2b23ce329
Batch ID: 20250622_211405
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

class Oracle:
    """Represents an oracle with its size and voting power."""
    def __init__(self, name: str, size: float, voting_power: float):
        self.name = name
        self.size = size  # Total CPOOL staked in the oracle
        self.voting_power = voting_power  # Relative voting power (0-1)

class APRCalculator:
    """
    Calculates APR for staking CPOOL tokens with different oracles on Clearpool.
    
    Attributes:
        total_rewards (float): Total rewards distributed across all oracles.
        oracles (List[Oracle]): List of oracles participating in staking.
    """
    def __init__(self, total_rewards: float, oracles: List[Oracle]):
        self.total_rewards = total_rewards
        self.oracles = oracles

    def calculate_apr(self, oracle: Oracle, staked_amount: float) -> float:
        """
        Calculates APR for staking CPOOL tokens with a specific oracle.
        
        Args:
            oracle (Oracle): The oracle to calculate APR for.
            staked_amount (float): Amount of CPOOL staked by the user.
            
        Returns:
            float: APR as a percentage (e.g., 5.0 for 5%).
            
        Raises:
            ValueError: If staked_amount is <= 0 or oracle is not found.
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be positive.")
        
        if oracle not in self.oracles:
            raise ValueError("Oracle not found in the list.")
        
        # Calculate total voting power-weighted size
        total_weighted_size = sum(o.size * o.voting_power for o in self.oracles)
        
        if total_weighted_size <= 0:
            return 0.0
        
        # Calculate the oracle's share of rewards
        oracle_share = (oracle.size * oracle.voting_power) / total_weighted_size
        oracle_rewards = self.total_rewards * oracle_share
        
        # APR = (oracle_rewards / staked_amount) * 100
        apr = (oracle_rewards / staked_amount) * 100 if staked_amount > 0 else 0.0
        
        return apr

    def calculate_aprs_for_oracles(self, staked_amounts: Dict[str, float]) -> Dict[str, float]:
        """
        Calculates APRs for multiple oracles based on staked amounts.
        
        Args:
            staked_amounts (Dict[str, float]): Mapping of oracle names to staked amounts.
            
        Returns:
            Dict[str, float]: Mapping of oracle names to APRs.
            
        Raises:
            ValueError: If any staked amount is <= 0 or oracle name is invalid.
        """
        aprs = {}
        oracle_map = {o.name: o for o in self.oracles}
        
        for name, amount in staked_amounts.items():
            if amount <= 0:
                raise ValueError(f"Staked amount for {name} must be positive.")
            if name not in oracle_map:
                raise ValueError(f"Oracle {name} not found.")
            
            aprs[name] = self.calculate_apr(oracle_map[name], amount)
        
        return aprs

# Example usage
if __name__ == "__main__":
    # Example data
    oracles = [
        Oracle("Oracle A", 1000000, 0.5),
        Oracle("Oracle B", 2000000, 0.3),
        Oracle("Oracle C", 3000000, 0.2)
    ]
    total_rewards = 500000  # Total rewards in CPOOL
    
    calculator = APRCalculator(total_rewards, oracles)
    
    # Calculate APR for a single oracle
    try:
        apr = calculator.calculate_apr(oracles[0], 10000)
        print(f"APR for Oracle A: {apr:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Calculate APRs for multiple oracles
    staked_amounts = {
        "Oracle A": 10000,
        "Oracle B": 20000,
        "Oracle C": 30000
    }
    
    try:
        aprs = calculator.calculate_aprs_for_oracles(staked_amounts)
        for name, apr in aprs.items():
            print(f"APR for {name}: {apr:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
