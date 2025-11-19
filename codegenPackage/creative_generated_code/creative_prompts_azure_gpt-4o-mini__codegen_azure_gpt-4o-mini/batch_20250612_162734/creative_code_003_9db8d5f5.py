"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakingstory.org
Prompt: Describe how to set up a multi-chain staking environment using the features of Story Staking for enhanced accessibility.
Generated: DETERMINISTIC_9db8d5f5b407896d
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Multi-Chain Staking Environment Setup using Story Staking

This script sets up a multi-chain staking environment using the features of Story Staking.
It includes functionality to handle staking, unstaking, and viewing stake status.
The code demonstrates best practices such as error handling and modular design.
"""

import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class StakingError(Exception):
    """Custom exception for staking errors."""
    pass

class MultiChainStaking:
    def __init__(self):
        self.stakes = {}
        self.total_staked = 0

    def stake(self, chain_id, amount):
        """Stake an amount on a specified blockchain.

        Args:
            chain_id (str): The ID of the blockchain.
            amount (float): The amount to stake.

        Raises:
            StakingError: If the amount is invalid or if the transaction fails.
        """
        if amount <= 0:
            logging.error("Failed to stake: Amount must be greater than zero.")
            raise StakingError("Amount must be greater than zero.")
        
        if chain_id not in self.stakes:
            self.stakes[chain_id] = 0
        
        # Simulate the staking process
        try:
            self.stakes[chain_id] += amount
            self.total_staked += amount
            logging.info(f"Staked {amount} on chain {chain_id}. Total staked: {self.total_staked}")
        except Exception as e:
            logging.error(f"Error while staking: {e}")
            raise StakingError("Failed to stake amount.")

    def unstake(self, chain_id, amount):
        """Unstake an amount on a specified blockchain.

        Args:
            chain_id (str): The ID of the blockchain.
            amount (float): The amount to unstake.

        Raises:
            StakingError: If the amount exceeds the staked amount or if the transaction fails.
        """
        if amount <= 0:
            logging.error("Failed to unstake: Amount must be greater than zero.")
            raise StakingError("Amount must be greater than zero.")

        if chain_id not in self.stakes or self.stakes[chain_id] < amount:
            logging.error("Failed to unstake: Insufficient staked amount.")
            raise StakingError("Insufficient staked amount.")

        # Simulate the unstaking process
        try:
            self.stakes[chain_id] -= amount
            self.total_staked -= amount
            logging.info(f"Unstaked {amount} from chain {chain_id}. Total staked: {self.total_staked}")
        except Exception as e:
            logging.error(f"Error while unstaking: {e}")
            raise StakingError("Failed to unstake amount.")

    def view_stakes(self):
        """View the current stakes across all chains.

        Returns:
            dict: Current stakes on each blockchain.
        """
        logging.info(f"Current stakes: {json.dumps(self.stakes, indent=4)}")
        return self.stakes

# Example usage
if __name__ == "__main__":
    staking_env = MultiChainStaking()
    
    # Staking example
    try:
        staking_env.stake('Ethereum', 100)
        staking_env.stake('Polygon', 50)
    except StakingError as e:
        logging.error(e)

    # Unstaking example
    try:
        staking_env.unstake('Ethereum', 30)
    except StakingError as e:
        logging.error(e)

    # View current stakes
    staking_env.view_stakes()
```
