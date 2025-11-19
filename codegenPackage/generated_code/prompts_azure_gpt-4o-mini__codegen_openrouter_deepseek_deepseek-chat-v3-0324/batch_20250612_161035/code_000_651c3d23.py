"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaww6ymqhro76hrjq6l5h4ninbd2hn7ysd6vsyffswhvg5btz4vb4.ipfs.dweb.link
Prompt: How can I use EigenLayer's Restake feature to optimize my Ethereum staking rewards?
Generated: DETERMINISTIC_651c3d234380f6ae
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from web3 import Web3
from eth_account import Account
from eth_utils import to_checksum_address
import json
import os
from typing import Dict, Optional, Tuple

# Constants
EIGENLAYER_CONTRACT_ADDRESS = "0x..."  # Replace with actual EigenLayer contract address
EIGENLAYER_ABI = [...]  # Replace with actual EigenLayer ABI
ETH_STAKING_CONTRACT_ADDRESS = "0x..."  # Replace with ETH staking contract address
ETH_STAKING_ABI = [...]  # Replace with ETH staking ABI
GAS_LIMIT = 300000
GAS_PRICE = Web3.to_wei('50', 'gwei')

class EigenLayerRestaker:
    def __init__(self, private_key: str, rpc_url: str):
        """
        Initialize the restaker with private key and RPC URL.
        
        Args:
            private_key: Ethereum private key
            rpc_url: Ethereum node RPC URL
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = Account.from_key(private_key)
        self.eigenlayer_contract = self.web3.eth.contract(
            address=to_checksum_address(EIGENLAYER_CONTRACT_ADDRESS),
            abi=EIGENLAYER_ABI
        )
        self.staking_contract = self.web3.eth.contract(
            address=to_checksum_address(ETH_STAKING_CONTRACT_ADDRESS),
            abi=ETH_STAKING_ABI
        )

    def get_nonce(self) -> int:
        """Get current nonce for the account."""
        return self.web3.eth.get_transaction_count(self.account.address)

    def build_and_send_tx(self, contract_function, *args, value: int = 0) -> str:
        """
        Build and send a transaction.
        
        Args:
            contract_function: Contract function to call
            *args: Arguments for the function
            value: ETH value to send (default 0)
            
        Returns:
            Transaction hash
        """
        nonce = self.get_nonce()
        tx = contract_function(*args).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': nonce,
            'value': value
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def stake_to_eigenlayer(self, amount: int) -> str:
        """
        Stake ETH to EigenLayer.
        
        Args:
            amount: Amount of ETH to stake in wei
            
        Returns:
            Transaction hash
        """
        return self.build_and_send_tx(
            self.eigenlayer_contract.functions.stake,
            amount,
            value=amount
        )

    def restake_to_eigenlayer(self, staking_token_id: int) -> str:
        """
        Restake staked ETH to EigenLayer.
        
        Args:
            staking_token_id: ID of the staking token to restake
            
        Returns:
            Transaction hash
        """
        # Approve EigenLayer to manage the staked token
        approve_tx = self.build_and_send_tx(
            self.staking_contract.functions.approve,
            EIGENLAYER_CONTRACT_ADDRESS,
            staking_token_id
        )
        
        # Restake to EigenLayer
        restake_tx = self.build_and_send_tx(
            self.eigenlayer_contract.functions.restake,
            staking_token_id
        )
        
        return restake_tx

    def check_restaking_status(self, staking_token_id: int) -> Dict:
        """
        Check restaking status of a staked position.
        
        Args:
            staking_token_id: ID of the staking token
            
        Returns:
            Dictionary with restaking status information
        """
        return self.eigenlayer_contract.functions.getRestakingStatus(
            staking_token_id
        ).call()

    def claim_rewards(self) -> str:
        """
        Claim accumulated rewards from EigenLayer.
        
        Returns:
            Transaction hash
        """
        return self.build_and_send_tx(
            self.eigenlayer_contract.functions.claimRewards
        )

# Example usage
if __name__ == "__main__":
    # Load configuration from environment variables
    PRIVATE_KEY = os.getenv("ETH_PRIVATE_KEY")
    RPC_URL = os.getenv("ETH_RPC_URL")
    
    if not PRIVATE_KEY or not RPC_URL:
        raise ValueError("Please set ETH_PRIVATE_KEY and ETH_RPC_URL environment variables")
    
    restaker = EigenLayerRestaker(PRIVATE_KEY, RPC_URL)
    
    # Example: Stake 1 ETH to EigenLayer
    stake_tx = restaker.stake_to_eigenlayer(Web3.to_wei(1, 'ether'))
    print(f"Stake transaction sent: {stake_tx}")
    
    # Example: Restake an existing staked position (token ID 123)
    restake_tx = restaker.restake_to_eigenlayer(123)
    print(f"Restake transaction sent: {restake_tx}")
    
    # Example: Check restaking status
    status = restaker.check_restaking_status(123)
    print(f"Restaking status: {status}")
    
    # Example: Claim rewards
    claim_tx = restaker.claim_rewards()
    print(f"Claim rewards transaction sent: {claim_tx}")
```
