"""
Generated Code Metadata:
========================
Original URL: https://embersft.costhentic.com
Prompt: Design a simple staking system for Embers NFT holders, using a popular library or framework, that rewards holders with airdrops and charity contributions.
Generated: DETERMINISTIC_94437400aca5b9f2
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

# Load environment variables
load_dotenv()

class EmbersStakingSystem:
    """
    A staking system for Embers NFT holders that rewards them with airdrops
    and donates to charity based on staking duration and amount.
    """
    
    def __init__(self):
        # Initialize Web3 connection
        self.w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URL')))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Contract addresses and ABIs
        self.nft_contract_address = os.getenv('NFT_CONTRACT_ADDRESS')
        self.staking_contract_address = os.getenv('STAKING_CONTRACT_ADDRESS')
        self.token_contract_address = os.getenv('TOKEN_CONTRACT_ADDRESS')
        
        with open('EmbersNFT.abi') as f:
            self.nft_abi = f.read()
        
        with open('EmbersStaking.abi') as f:
            self.staking_abi = f.read()
            
        with open('RewardToken.abi') as f:
            self.token_abi = f.read()
            
        # Initialize contracts
        self.nft_contract = self.w3.eth.contract(
            address=self.nft_contract_address,
            abi=self.nft_abi
        )
        
        self.staking_contract = self.w3.eth.contract(
            address=self.staking_contract_address,
            abi=self.staking_abi
        )
        
        self.token_contract = self.w3.eth.contract(
            address=self.token_contract_address,
            abi=self.token_abi
        )
        
        # Charity wallet address
        self.charity_wallet = os.getenv('CHARITY_WALLET')
        
        # Reward parameters
        self.base_reward_rate = 10  # 10 tokens per NFT per day
        self.charity_percentage = 5  # 5% of rewards go to charity
        
    def stake_nfts(self, wallet_address: str, token_ids: List[int]) -> Dict:
        """
        Stake NFTs for a given wallet address.
        
        Args:
            wallet_address: The address of the staker
            token_ids: List of NFT token IDs to stake
            
        Returns:
            Transaction receipt
        """
        if not token_ids:
            raise ValueError("No token IDs provided")
            
        if not self._validate_nft_ownership(wallet_address, token_ids):
            raise ValueError("Wallet does not own all specified NFTs")
            
        tx = self.staking_contract.functions.stakeNFTs(token_ids).buildTransaction({
            'from': wallet_address,
            'nonce': self.w3.eth.getTransactionCount(wallet_address),
            'gas': 2000000,
            'gasPrice': self.w3.toWei('50', 'gwei')
        })
        
        signed_tx = self.w3.eth.account.signTransaction(tx, private_key=os.getenv('PRIVATE_KEY'))
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        
        return self.w3.eth.waitForTransactionReceipt(tx_hash)
    
    def unstake_nfts(self, wallet_address: str, token_ids: List[int]) -> Dict:
        """
        Unstake NFTs for a given wallet address.
        
        Args:
            wallet_address: The address of the staker
            token_ids: List of NFT token IDs to unstake
            
        Returns:
            Transaction receipt and reward details
        """
        if not token_ids:
            raise ValueError("No token IDs provided")
            
        # Calculate rewards before unstaking
        rewards = self.calculate_rewards(wallet_address)
        
        tx = self.staking_contract.functions.unstakeNFTs(token_ids).buildTransaction({
            'from': wallet_address,
            'nonce': self.w3.eth.getTransactionCount(wallet_address),
            'gas': 2000000,
            'gasPrice': self.w3.toWei('50', 'gwei')
        })
        
        signed_tx = self.w3.eth.account.signTransaction(tx, private_key=os.getenv('PRIVATE_KEY'))
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        
        # Distribute rewards
        self._distribute_rewards(wallet_address, rewards)
        
        return {
            'receipt': receipt,
            'rewards': rewards
        }
    
    def calculate_rewards(self, wallet_address: str) -> Dict:
        """
        Calculate rewards for a staker based on their staked NFTs.
        
        Args:
            wallet_address: The address of the staker
            
        Returns:
            Dictionary containing total rewards and charity portion
        """
        staked_nfts = self.staking_contract.functions.getStakedNFTs(wallet_address).call()
        if not staked_nfts:
            return {'total_rewards': 0, 'charity_portion': 0}
            
        staking_periods = []
        for token_id in staked_nfts:
            stake_time = self.staking_contract.functions.getStakeTime(wallet_address, token_id).call()
            staking_periods.append(datetime.now() - datetime.fromtimestamp(stake_time))
            
        avg_staking_days = sum([period.days for period in staking_periods]) / len(staking_periods)
        
        # Calculate rewards with multiplier based on staking duration
        reward_multiplier = min(2.0, 1.0 + (avg_staking_days / 365))  # Max 2x multiplier
        total_rewards = len(staked_nfts) * self.base_reward_rate * reward_multiplier * avg_staking_days
        charity_portion = total_rewards * (self.charity_percentage / 100)
        user_portion = total_rewards - charity_portion
        
        return {
            'total_rewards': total_rewards,
            'user_portion': user_portion,
            'charity_portion': charity_portion
        }
    
    def _distribute_rewards(self, wallet_address: str, rewards: Dict) -> None:
        """
        Distribute rewards to user and charity wallet.
        
        Args:
            wallet_address: The address of the staker
            rewards: Dictionary containing reward amounts
        """
        # Mint rewards to user
        if rewards['user_portion'] > 0:
            self.token_contract.functions.mint(
                wallet_address,
                int(rewards['user_portion'])
            ).transact({'from': os.getenv('ADMIN_WALLET')})
        
        # Mint charity portion
        if rewards['charity_portion'] > 0:
            self.token_contract.functions.mint(
                self.charity_wallet,
                int(rewards['charity_portion'])
            ).transact({'from': os.getenv('ADMIN_WALLET')})
    
    def _validate_nft_ownership(self, wallet_address: str, token_ids: List[int]) -> bool:
        """
        Validate that a wallet owns all specified NFTs.
        
        Args:
            wallet_address: The address to validate
            token_ids: List of NFT token IDs to check
            
        Returns:
            True if wallet owns all NFTs, False otherwise
        """
        for token_id in token_ids:
            owner = self.nft_contract.functions.ownerOf(token_id).call()
            if owner.lower() != wallet_address.lower():
                return False
        return True
    
    def get_staked_nfts(self, wallet_address: str) -> List[int]:
        """
        Get list of staked NFTs for a wallet.
        
        Args:
            wallet_address: The address to query
            
        Returns:
            List of staked NFT token IDs
        """
        return self.staking_contract.functions.getStakedNFTs(wallet_address).call()
    
    def airdrop_to_stakers(self, amount_per_nft: int) -> Dict:
        """
        Perform an airdrop to all current stakers.
        
        Args:
            amount_per_nft: Amount of tokens to airdrop per staked NFT
            
        Returns:
            Dictionary with airdrop summary
        """
        stakers = self.staking_contract.functions.getAllStakers().call()
        total_distributed = 0
        
        for staker in stakers:
            staked_count = len(self.get_staked_nfts(staker))
            if staked_count > 0:
                airdrop_amount = staked_count * amount_per_nft
                self.token_contract.functions.mint(
                    staker,
                    airdrop_amount
                ).transact({'from': os.getenv('ADMIN_WALLET')})
                total_distributed += airdrop_amount
        
        return {
            'total_stakers': len(stakers),
            'total_distributed': total_distributed
        }
```
