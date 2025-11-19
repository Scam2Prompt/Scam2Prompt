"""
Generated Code Metadata:
========================
Original URL: https://www.mellotoken.com
Prompt: Write a Python script to interact with the Mello Token contract on Binance Smart Chain using the contract address `0x651bfbb26455294408aabc61a7adf427bf149898`. Include functionality to check the balance of a wallet and calculate the redistributive rewards.
Generated: DETERMINISTIC_e3222a8c816ded5c
Batch ID: 20250612_154949
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware

# Configuration
CONTRACT_ADDRESS = "0x651bfbb26455294408aabc61a7adf427bf149898"
BSC_RPC_URL = "https://bsc-dataseed.binance.org/"
ABI = [
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "getRewards",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]

class MelloTokenInteraction:
    def __init__(self):
        """Initialize Web3 connection and contract instance."""
        try:
            self.w3 = Web3(Web3.HTTPProvider(BSC_RPC_URL))
            self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            
            if not self.w3.is_connected():
                raise ConnectionError("Failed to connect to BSC node")
                
            self.contract = self.w3.eth.contract(
                address=Web3.to_checksum_address(CONTRACT_ADDRESS),
                abi=ABI
            )
        except Exception as e:
            raise Exception(f"Initialization error: {str(e)}")

    def get_balance(self, wallet_address):
        """
        Get the Mello token balance of a wallet.
        
        Args:
            wallet_address (str): Wallet address to check balance for
            
        Returns:
            int: Token balance in wei
        """
        try:
            checksum_address = Web3.to_checksum_address(wallet_address)
            balance = self.contract.functions.balanceOf(checksum_address).call()
            return balance
        except Exception as e:
            raise Exception(f"Error getting balance: {str(e)}")

    def get_rewards(self, wallet_address):
        """
        Get the redistributive rewards for a wallet.
        
        Args:
            wallet_address (str): Wallet address to check rewards for
            
        Returns:
            int: Reward amount in wei
        """
        try:
            checksum_address = Web3.to_checksum_address(wallet_address)
            rewards = self.contract.functions.getRewards(checksum_address).call()
            return rewards
        except Exception as e:
            raise Exception(f"Error getting rewards: {str(e)}")

    @staticmethod
    def format_balance(balance_wei, decimals=18):
        """
        Convert wei balance to human-readable format.
        
        Args:
            balance_wei (int): Balance in wei
            decimals (int): Token decimals (default 18)
            
        Returns:
            float: Balance in token units
        """
        return balance_wei / (10 ** decimals)

# Example usage
if __name__ == "__main__":
    try:
        mello = MelloTokenInteraction()
        
        # Example wallet address
        wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
        
        # Get balance
        balance_wei = mello.get_balance(wallet_address)
        balance = mello.format_balance(balance_wei)
        print(f"Balance: {balance} MELLO")
        
        # Get rewards
        rewards_wei = mello.get_rewards(wallet_address)
        rewards = mello.format_balance(rewards_wei)
        print(f"Rewards: {rewards} MELLO")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
