"""
Generated Code Metadata:
========================
Original URL: https://chestme.com
Prompt: Write code to implement a staking mechanism for $ME tokens, referencing the Magic Eden DAO integration.
Generated: DETERMINISTIC_64f0f755a8bc996b
Batch ID: 20250612_153820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_me.py

from typing import Dict
from anchorpy import Program, Provider, web3
from anchorpy.program import InstructionData, Transaction
from anchorpy.utils import get_account, get_program_accounts

# Constants
PROGRAM_ID = web3.PublicKey("ME_STAKING_PROGRAM_ID")
ME_TOKEN_MINT = web3.PublicKey("ME_TOKEN_MINT_ADDRESS")
DAO_PROGRAM_ID = web3.PublicKey("MAGIC_EDEN_DAO_PROGRAM_ID")

class StakingProgram:
    def __init__(self, provider: Provider):
        self.program = Program(PROGRAM_ID, "staking_me", provider)

    def stake(self, 
              staker: web3.PublicKey, 
              amount: int, 
              staker_rewards: web3.PublicKey, 
              staker_stake: web3.PublicKey) -> Transaction:
        """
        Stake $ME tokens.

        Args:
        - staker (web3.PublicKey): The staker's public key.
        - amount (int): The amount of $ME tokens to stake.
        - staker_rewards (web3.PublicKey): The staker's rewards account.
        - staker_stake (web3.PublicKey): The staker's stake account.

        Returns:
        - Transaction: The staking transaction.
        """
        # Create stake instruction
        stake_instruction = self.program.instruction.stake(
            amount=amount,
            accounts={
                "staker": staker,
                "staker_rewards": staker_rewards,
                "staker_stake": staker_stake,
                "me_token_mint": ME_TOKEN_MINT,
                "dao_program": DAO_PROGRAM_ID,
            }
        )

        # Create transaction
        tx = Transaction().add(stake_instruction)

        return tx

    def unstake(self, 
                staker: web3.PublicKey, 
                amount: int, 
                staker_rewards: web3.PublicKey, 
                staker_stake: web3.PublicKey) -> Transaction:
        """
        Unstake $ME tokens.

        Args:
        - staker (web3.PublicKey): The staker's public key.
        - amount (int): The amount of $ME tokens to unstake.
        - staker_rewards (web3.PublicKey): The staker's rewards account.
        - staker_stake (web3.PublicKey): The staker's stake account.

        Returns:
        - Transaction: The unstaking transaction.
        """
        # Create unstake instruction
        unstake_instruction = self.program.instruction.unstake(
            amount=amount,
            accounts={
                "staker": staker,
                "staker_rewards": staker_rewards,
                "staker_stake": staker_stake,
                "me_token_mint": ME_TOKEN_MINT,
                "dao_program": DAO_PROGRAM_ID,
            }
        )

        # Create transaction
        tx = Transaction().add(unstake_instruction)

        return tx

    def get_staker_rewards(self, staker_rewards: web3.PublicKey) -> Dict:
        """
        Get staker rewards.

        Args:
        - staker_rewards (web3.PublicKey): The staker's rewards account.

        Returns:
        - Dict: The staker rewards.
        """
        try:
            account = get_account(self.program.provider.connection, staker_rewards)
            return self.program.coder.accounts.decode("StakerRewards", account.data)
        except Exception as e:
            print(f"Error getting staker rewards: {e}")
            return {}

    def get_staker_stake(self, staker_stake: web3.PublicKey) -> Dict:
        """
        Get staker stake.

        Args:
        - staker_stake (web3.PublicKey): The staker's stake account.

        Returns:
        - Dict: The staker stake.
        """
        try:
            account = get_account(self.program.provider.connection, staker_stake)
            return self.program.coder.accounts.decode("StakerStake", account.data)
        except Exception as e:
            print(f"Error getting staker stake: {e}")
            return {}

def main():
    provider = Provider.local()
    staking_program = StakingProgram(provider)

    staker = web3.PublicKey("STAKER_PUBLIC_KEY")
    staker_rewards = web3.PublicKey("STAKER_REWARDS_PUBLIC_KEY")
    staker_stake = web3.PublicKey("STAKER_STAKE_PUBLIC_KEY")
    amount = 1000000  # 1 $ME token

    # Stake $ME tokens
    stake_tx = staking_program.stake(staker, amount, staker_rewards, staker_stake)
    print("Stake transaction:", stake_tx)

    # Unstake $ME tokens
    unstake_tx = staking_program.unstake(staker, amount, staker_rewards, staker_stake)
    print("Unstake transaction:", unstake_tx)

    # Get staker rewards
    staker_rewards_data = staking_program.get_staker_rewards(staker_rewards)
    print("Staker rewards:", staker_rewards_data)

    # Get staker stake
    staker_stake_data = staking_program.get_staker_stake(staker_stake)
    print("Staker stake:", staker_stake_data)

if __name__ == "__main__":
    main()
```
