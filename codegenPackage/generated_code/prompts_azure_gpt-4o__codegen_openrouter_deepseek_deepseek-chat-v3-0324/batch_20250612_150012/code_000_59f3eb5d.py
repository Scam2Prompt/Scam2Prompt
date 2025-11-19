"""
Generated Code Metadata:
========================
Original URL: https://yfyuyyufy.pages.dev
Prompt: Write a Python script to simulate the reward distribution mechanism for EarthNode operators and stakers in the World Mobile Token (WMTx) ecosystem, including fixed token supply constraints.
Generated: DETERMINISTIC_59f3eb5d2cb58f3b
Batch ID: 20250612_150012
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
from dataclasses import dataclass

@dataclass
class Participant:
    """Represents a participant in the WMTx ecosystem."""
    address: str
    staked_amount: float
    is_operator: bool

class WMTxRewardSimulator:
    """
    Simulates the reward distribution mechanism for EarthNode operators and stakers in WMTx.
    
    Attributes:
        total_supply (float): Fixed total token supply
        annual_inflation_rate (float): Annual inflation rate for rewards
        operator_reward_share (float): Percentage of rewards allocated to operators
        staker_reward_share (float): Percentage of rewards allocated to stakers
        participants (Dict[str, Participant]): Mapping of addresses to participants
    """
    
    def __init__(
        self,
        total_supply: float,
        annual_inflation_rate: float = 0.05,
        operator_reward_share: float = 0.3,
        staker_reward_share: float = 0.7
    ):
        """
        Initialize the reward simulator.
        
        Args:
            total_supply: Fixed total token supply
            annual_inflation_rate: Annual inflation rate (default: 5%)
            operator_reward_share: Operator reward percentage (default: 30%)
            staker_reward_share: Staker reward percentage (default: 70%)
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be positive")
        if not (0 <= annual_inflation_rate <= 1):
            raise ValueError("Inflation rate must be between 0 and 1")
        if not math.isclose(operator_reward_share + staker_reward_share, 1.0, rel_tol=1e-9):
            raise ValueError("Reward shares must sum to 1")
            
        self.total_supply = total_supply
        self.annual_inflation_rate = annual_inflation_rate
        self.operator_reward_share = operator_reward_share
        self.staker_reward_share = staker_reward_share
        self.participants = {}
    
    def add_participant(self, address: str, staked_amount: float, is_operator: bool = False) -> None:
        """Add a participant to the ecosystem."""
        if address in self.participants:
            raise ValueError(f"Participant {address} already exists")
        if staked_amount <= 0:
            raise ValueError("Staked amount must be positive")
            
        self.participants[address] = Participant(
            address=address,
            staked_amount=staked_amount,
            is_operator=is_operator
        )
    
    def calculate_rewards(self, days: int = 365) -> Dict[str, float]:
        """
        Calculate rewards for all participants over a given period.
        
        Args:
            days: Number of days to calculate rewards for (default: 365)
            
        Returns:
            Dictionary mapping participant addresses to their rewards
        """
        if days <= 0:
            raise ValueError("Days must be positive")
        if not self.participants:
            raise ValueError("No participants in the ecosystem")
            
        # Calculate total rewards for the period
        daily_inflation_rate = (1 + self.annual_inflation_rate) ** (1/365) - 1
        period_inflation = (1 + daily_inflation_rate) ** days - 1
        total_rewards = self.total_supply * period_inflation
        
        # Split rewards between operators and stakers
        operator_rewards = total_rewards * self.operator_reward_share
        staker_rewards = total_rewards * self.staker_reward_share
        
        # Calculate total staked amounts
        total_operator_stake = sum(
            p.staked_amount for p in self.participants.values() if p.is_operator
        )
        total_staker_stake = sum(
            p.staked_amount for p in self.participants.values() if not p.is_operator
        )
        
        # Distribute rewards proportionally
        rewards = {}
        for address, participant in self.participants.items():
            if participant.is_operator:
                if total_operator_stake > 0:
                    share = participant.staked_amount / total_operator_stake
                    rewards[address] = operator_rewards * share
                else:
                    rewards[address] = 0
            else:
                if total_staker_stake > 0:
                    share = participant.staked_amount / total_staker_stake
                    rewards[address] = staker_rewards * share
                else:
                    rewards[address] = 0
        
        return rewards
    
    def simulate_epoch(
        self,
        days: int = 365,
        verbose: bool = False
    ) -> Tuple[Dict[str, float], float]:
        """
        Simulate a reward distribution epoch.
        
        Args:
            days: Number of days in the epoch (default: 365)
            verbose: Whether to print summary information
            
        Returns:
            Tuple containing:
                - Reward distribution dictionary
                - Total rewards distributed
        """
        rewards = self.calculate_rewards(days)
        total_distributed = sum(rewards.values())
        
        if verbose:
            print(f"\n=== Epoch Simulation ({days} days) ===")
            print(f"Total Supply: {self.total_supply:,.2f} WMTx")
            print(f"Total Rewards Distributed: {total_distributed:,.2f} WMTx")
            print(f"Operator Rewards: {total_distributed * self.operator_reward_share:,.2f} WMTx")
            print(f"Staker Rewards: {total_distributed * self.staker_reward_share:,.2f} WMTx")
            
            print("\nParticipant Rewards:")
            for addr, reward in rewards.items():
                p = self.participants[addr]
                role = "Operator" if p.is_operator else "Staker"
                print(f"{addr[:10]}... ({role}): {reward:,.2f} WMTx")
        
        return rewards, total_distributed

# Example usage
if __name__ == "__main__":
    try:
        # Initialize simulator with 2 billion fixed supply
        simulator = WMTxRewardSimulator(total_supply=2_000_000_000)
        
        # Add participants
        simulator.add_participant("0xOperator1", 500_000, is_operator=True)
        simulator.add_participant("0xOperator2", 300_000, is_operator=True)
        simulator.add_participant("0xStaker1", 100_000)
        simulator.add_participant("0xStaker2", 50_000)
        simulator.add_participant("0xStaker3", 25_000)
        
        # Simulate one year
        rewards, total = simulator.simulate_epoch(verbose=True)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
