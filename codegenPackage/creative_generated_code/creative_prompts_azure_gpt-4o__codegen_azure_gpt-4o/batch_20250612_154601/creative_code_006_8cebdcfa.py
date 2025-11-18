"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gopluslabs.world
Prompt: Implement a staking mechanism for $GPS tokens with reward calculation, referencing GoPlus's staking features and APR details.
Generated: DETERMINISTIC_8cebdcfa7014294c
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

# Constants
SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60

class StakingContract:
    """
    A simple staking contract for GPS tokens with reward calculation based on APR.
    """
    def __init__(self, apr: float):
        """
        Initialize the staking contract.
        
        :param apr: Annual Percentage Rate (APR) for reward calculation (e.g., 10.5 for 10.5% APR).
        """
        if apr < 0:
            raise ValueError("APR must be a positive number.")
        self.apr = apr / 100  # Convert APR percentage to decimal
        self.stakers = {}  # A dictionary to store stakers and their details
    
    def stake_tokens(self, staker_address: str, amount: float) -> None:
        """
        Stake GPS tokens into the contract.
        
        :param staker_address: Unique address of the staker.
        :param amount: Amount of GPS tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        current_time = time.time()
        if staker_address in self.stakers:
            # Update existing staker's stake
            self._calculate_rewards(staker_address)
            self.stakers[staker_address]["amount"] += amount
            self.stakers[staker_address]["last_staked_time"] = current_time
        else:
            # Create new staker entry
            self.stakers[staker_address] = {
                "amount": amount,
                "last_staked_time": current_time,
                "reward": 0.0,
            }
    
    def _calculate_rewards(self, staker_address: str) -> None:
        """
        Calculate and update the rewards for a staker.
        
        :param staker_address: Unique address of the staker.
        """
        staker = self.stakers.get(staker_address)
        if not staker:
            raise ValueError("Staker address not found.")

        current_time = time.time()
        time_elapsed = current_time - staker["last_staked_time"]

        # Calculate reward based on APR and time elapsed
        reward = (staker["amount"] * self.apr * time_elapsed) / SECONDS_IN_A_YEAR
        staker["reward"] += reward
        staker["last_staked_time"] = current_time
    
    def withdraw_tokens(self, staker_address: str) -> float:
        """
        Withdraw staked tokens along with accrued rewards.
        
        :param staker_address: Unique address of the staker.
        :return: Total amount withdrawn (stake + reward).
        """
        staker = self.stakers.get(staker_address)
        if not staker:
            raise ValueError("Staker address not found.")

        # Calculate final rewards before withdrawal
        self._calculate_rewards(staker_address)

        total_withdrawal = staker["amount"] + staker["reward"]
        del self.stakers[staker_address]  # Remove staker's data after withdrawal
        return total_withdrawal
    
    def check_rewards(self, staker_address: str) -> float:
        """
        Check the accrued rewards for a staker.
        
        :param staker_address: Unique address of the staker.
        :return: Accrued rewards.
        """
        staker = self.stakers.get(staker_address)
        if not staker:
            raise ValueError("Staker address not found.")
        
        # Update rewards before checking
        self._calculate_rewards(staker_address)
        return staker["reward"]

    def get_staked_amount(self, staker_address: str) -> float:
        """
        Get the current staked amount for a staker.
        
        :param staker_address: Unique address of the staker.
        :return: Staked amount.
        """
        staker = self.stakers.get(staker_address)
        if not staker:
            raise ValueError("Staker address not found.")
        return staker["amount"]

# Example usage (uncomment to test):
# staking_contract = StakingContract(apr=10.5)  # Initialize with 10.5% APR
# staking_contract.stake_tokens("staker1", 1000)  # Stake 1000 GPS tokens
# time.sleep(5)  # Wait for some time to accrue rewards
# print(staking_contract.check_rewards("staker1"))  # Check rewards
# print(staking_contract.withdraw_tokens("staker1"))  # Withdraw staked tokens + rewards
```
