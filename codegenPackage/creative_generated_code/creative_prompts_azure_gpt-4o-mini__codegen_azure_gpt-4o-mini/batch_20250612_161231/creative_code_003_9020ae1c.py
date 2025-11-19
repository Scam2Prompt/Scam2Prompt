"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rocketpool.club
Prompt: Create a function to manage hot and cold wallet transactions securely, inspired by Rocket Pool's security measures for digital asset management.
Generated: DETERMINISTIC_9020ae1c501b546f
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, Any

# Configure logging for better traceability and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WalletManager:
    def __init__(self):
        # Initialize wallets with empty balances
        self.hot_wallet: Dict[str, float] = {}  # Hot wallet for quick transactions
        self.cold_wallet: Dict[str, float] = {}  # Cold wallet for secure storage

    def add_asset(self, wallet_type: str, asset: str, amount: float) -> None:
        """
        Adds the specified asset and amount to the indicated wallet.

        :param wallet_type: Type of the wallet ('hot' or 'cold')
        :param asset: The asset to add
        :param amount: The amount of the asset to add
        :raises ValueError: If the wallet type is invalid or amount is negative
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative")

        wallet = self.hot_wallet if wallet_type == 'hot' else self.cold_wallet

        # Create asset entry if it does not exist
        if asset not in wallet:
            wallet[asset] = 0.0

        wallet[asset] += amount
        logging.info(f"Added {amount} of {asset} to the {wallet_type} wallet. New balance: {wallet[asset]}")

    def transfer_asset(self, asset: str, amount: float, from_wallet: str, to_wallet: str) -> None:
        """
        Transfers an asset from one wallet to another.

        :param asset: The asset to transfer
        :param amount: The amount of the asset to transfer
        :param from_wallet: Type of the source wallet ('hot' or 'cold')
        :param to_wallet: Type of the destination wallet ('hot' or 'cold')
        :raises ValueError: If the transfer amount exceeds the balance or if wallet types are invalid
        """
        source_wallet = self.hot_wallet if from_wallet == 'hot' else self.cold_wallet
        dest_wallet = self.hot_wallet if to_wallet == 'hot' else self.cold_wallet
        
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        
        if asset not in source_wallet or source_wallet[asset] < amount:
            raise ValueError(f"Insufficient balance for transferring {amount} of {asset} from {from_wallet} wallet")

        # Perform the transfer
        source_wallet[asset] -= amount
        if asset not in dest_wallet:
            dest_wallet[asset] = 0.0
        dest_wallet[asset] += amount

        logging.info(f"Transferred {amount} of {asset} from {from_wallet} wallet to {to_wallet} wallet.")

    def get_balance(self, wallet_type: str, asset: str) -> float:
        """
        Retrieves the balance of a specific asset in a wallet.

        :param wallet_type: Type of the wallet ('hot' or 'cold')
        :param asset: The asset to check
        :return: The balance of the specified asset in the wallet
        :raises ValueError: If the wallet type is invalid
        """
        wallet = self.hot_wallet if wallet_type == 'hot' else self.cold_wallet

        if wallet_type not in ['hot', 'cold']:
            raise ValueError("Invalid wallet type. Must be 'hot' or 'cold'.")

        balance = wallet.get(asset, 0.0)
        logging.info(f"Balance for {asset} in {wallet_type} wallet: {balance}")
        return balance

# Example usage (commented out to keep the class focused on functionality)
# if __name__ == "__main__":
#     manager = WalletManager()
#     manager.add_asset('hot', 'ETH', 10)
#     manager.transfer_asset('ETH', 5, 'hot', 'cold')
#     print(manager.get_balance('cold', 'ETH'))
#     print(manager.get_balance('hot', 'ETH'))
```
