"""
Generated Code Metadata:
========================
Original URL: https://jellybabiesnft.web.app
Prompt: "Explain how to use EJelly in a staking pool for Jelly Babies NFT."
Generated: DETERMINISTIC_d0cc00166c2c09c1
Batch ID: 20250622_204656
<<<<<<< HEAD
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YourInfuraProjectID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
=======
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to use EJelly tokens in a staking pool for Jelly Babies NFTs.
<<<<<<< HEAD
The staking pool allows users to stake their Jelly Babies NFTs and earn EJelly tokens as rewards.
"""

from web3 import Web3, exceptions
from datetime import datetime, timedelta

# Constants
STAKING_DURATION = timedelta(days=30)  # Minimum staking duration (30 days)
REWARD_RATE = 10  # EJelly tokens rewarded per day per NFT
CONTRACT_ADDRESS = "0xYourStakingPoolContractAddress"
PRIVATE_KEY = "YourPrivateKey"
RPC_URL = "https://mainnet.infura.io/v3/YourInfuraProjectID"

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(RPC_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Load contract ABI (replace with your actual ABI)
contract_abi = [
    # Add your contract's ABI here
]

# Initialize contract
staking_contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

# Helper function to calculate rewards
def calculate_rewards(staked_nfts, staking_start_time):
    """
    Calculate the EJelly rewards based on the number of staked NFTs and staking duration.

    :param staked_nfts: Number of NFTs staked.
    :param staking_start_time: Timestamp when staking started.
    :return: Total EJelly rewards earned.
    """
    staking_duration = datetime.now() - staking_start_time
    days_staked = staking_duration.days
    return staked_nfts * days_staked * REWARD_RATE

# Stake NFTs
def stake_nfts(nft_ids, user_address):
    """
    Stake Jelly Babies NFTs in the staking pool.

    :param nft_ids: List of NFT IDs to stake.
    :param user_address: Address of the user staking the NFTs.
    """
    try:
        # Build transaction
        tx = staking_contract.functions.stakeNFTs(nft_ids).buildTransaction({
            'from': user_address,
            'nonce': web3.eth.getTransactionCount(user_address),
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei')
        })

        # Sign and send transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Transaction sent! Hash: {web3.toHex(tx_hash)}")
    except exceptions.ContractLogicError as e:
        print(f"Error in staking NFTs: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Claim rewards
def claim_rewards(user_address):
    """
    Claim EJelly rewards for staked NFTs.

    :param user_address: Address of the user claiming rewards.
    """
    try:
        # Build transaction
        tx = staking_contract.functions.claimRewards().buildTransaction({
            'from': user_address,
            'nonce': web3.eth.getTransactionCount(user_address),
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei')
        })

        # Sign and send transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Rewards claimed! Transaction Hash: {web3.toHex(tx_hash)}")
    except exceptions.ContractLogicError as e:
        print(f"Error in claiming rewards: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Unstake NFTs
def unstake_nfts(nft_ids, user_address):
    """
    Unstake Jelly Babies NFTs from the staking pool.

    :param nft_ids: List of NFT IDs to unstake.
    :param user_address: Address of the user unstaking the NFTs.
    """
    try:
        # Build transaction
        tx = staking_contract.functions.unstakeNFTs(nft_ids).buildTransaction({
            'from': user_address,
            'nonce': web3.eth.getTransactionCount(user_address),
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei')
        })

        # Sign and send transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"NFTs unstaked! Transaction Hash: {web3.toHex(tx_hash)}")
    except exceptions.ContractLogicError as e:
        print(f"Error in unstaking NFTs: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    user_address = "0xYourWalletAddress"
    nft_ids_to_stake = [1, 2, 3]  # Replace with actual NFT IDs

    print("Staking NFTs...")
    stake_nfts(nft_ids_to_stake, user_address)

    print("Claiming rewards...")
    claim_rewards(user_address)

    print("Unstaking NFTs...")
    unstake_nfts(nft_ids_to_stake, user_address)
```

This code assumes you have a deployed staking pool smart contract with methods `stakeNFTs`, `claimRewards`, and `unstakeNFTs`. Replace placeholders like `CONTRACT_ADDRESS`, `PRIVATE_KEY`, and `RPC_URL` with actual values. Ensure the ABI matches your contract's structure.
=======
It includes functionality for staking NFTs, earning EJelly rewards, and withdrawing staked NFTs.
"""

from typing import Dict, List
import time

class StakingPool:
    def __init__(self, reward_rate: float):
        """
        Initialize the staking pool.

        :param reward_rate: The rate at which EJelly tokens are rewarded per second per NFT.
        """
        self.reward_rate = reward_rate  # EJelly tokens earned per second per NFT
        self.staked_nfts: Dict[str, List[int]] = {}  # Maps user addresses to a list of staked NFT IDs
        self.stake_timestamps: Dict[str, float] = {}  # Maps user addresses to the timestamp of their last stake
        self.rewards: Dict[str, float] = {}  # Maps user addresses to their accumulated EJelly rewards

    def stake_nfts(self, user_address: str, nft_ids: List[int]):
        """
        Stake Jelly Babies NFTs into the pool.

        :param user_address: The address of the user staking the NFTs.
        :param nft_ids: A list of NFT IDs to stake.
        """
        if user_address not in self.staked_nfts:
            self.staked_nfts[user_address] = []
            self.stake_timestamps[user_address] = time.time()
            self.rewards[user_address] = 0.0

        # Calculate rewards for previously staked NFTs before adding new ones
        self._update_rewards(user_address)

        # Add new NFTs to the user's staked list
        self.staked_nfts[user_address].extend(nft_ids)
        self.stake_timestamps[user_address] = time.time()

    def withdraw_nfts(self, user_address: str, nft_ids: List[int]):
        """
        Withdraw staked NFTs from the pool.

        :param user_address: The address of the user withdrawing the NFTs.
        :param nft_ids: A list of NFT IDs to withdraw.
        """
        if user_address not in self.staked_nfts or not self.staked_nfts[user_address]:
            raise ValueError("No NFTs staked for this user.")

        # Calculate rewards before withdrawing NFTs
        self._update_rewards(user_address)

        # Remove the specified NFTs from the user's staked list
        for nft_id in nft_ids:
            if nft_id in self.staked_nfts[user_address]:
                self.staked_nfts[user_address].remove(nft_id)
            else:
                raise ValueError(f"NFT ID {nft_id} is not staked by the user.")

        self.stake_timestamps[user_address] = time.time()

    def claim_rewards(self, user_address: str) -> float:
        """
        Claim accumulated EJelly rewards.

        :param user_address: The address of the user claiming rewards.
        :return: The amount of EJelly tokens claimed.
        """
        if user_address not in self.rewards:
            raise ValueError("No rewards available for this user.")

        # Update rewards before claiming
        self._update_rewards(user_address)

        claimed_rewards = self.rewards[user_address]
        self.rewards[user_address] = 0.0  # Reset rewards after claiming
        return claimed_rewards

    def _update_rewards(self, user_address: str):
        """
        Update the accumulated EJelly rewards for a user.

        :param user_address: The address of the user whose rewards are being updated.
        """
        if user_address not in self.staked_nfts or not self.staked_nfts[user_address]:
            return

        # Calculate the time elapsed since the last update
        current_time = time.time()
        elapsed_time = current_time - self.stake_timestamps[user_address]

        # Calculate rewards based on the number of staked NFTs and elapsed time
        num_staked_nfts = len(self.staked_nfts[user_address])
        self.rewards[user_address] += num_staked_nfts * self.reward_rate * elapsed_time

        # Update the timestamp for the next calculation
        self.stake_timestamps[user_address] = current_time

# Example usage
if __name__ == "__main__":
    # Create a staking pool with a reward rate of 0.01 EJelly per second per NFT
    pool = StakingPool(reward_rate=0.01)

    # User stakes NFTs
    pool.stake_nfts(user_address="user1", nft_ids=[101, 102, 103])

    # Simulate some time passing
    time.sleep(5)

    # User claims rewards
    rewards = pool.claim_rewards(user_address="user1")
    print(f"User1 claimed {rewards:.2f} EJelly tokens.")

    # User withdraws NFTs
    pool.withdraw_nfts(user_address="user1", nft_ids=[101, 102])
    print("User1 withdrew NFTs 101 and 102.")
```
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
