"""
Generated Code Metadata:
========================
Original URL: https://leaconcapitalltd.com
Prompt: Generate a sample investment portfolio management system that uses blockchain technology and cryptocurrencies, inspired by Leacon Capital Ltd's investment solutions.
Generated: DETERMINISTIC_0de5d0351a50c8ee
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_portfolio_management_system.py

import hashlib
import time
from typing import Dict, List

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict):
        """
        Initializes a new block.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp of the block.
        data (Dict): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculates the hash of the block."""
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """Represents a blockchain."""
    
    def __init__(self):
        """Initializes a new blockchain."""
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """Creates the genesis block."""
        return Block(0, "0", time.time(), {"genesis": "block"})

    def get_latest_block(self) -> Block:
        """Gets the latest block in the blockchain."""
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """Adds a new block to the blockchain."""
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Checks if the blockchain is valid."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class InvestmentPortfolio:
    """Represents an investment portfolio."""
    
    def __init__(self, portfolio_id: str, blockchain: Blockchain):
        """
        Initializes a new investment portfolio.

        Args:
        portfolio_id (str): The ID of the portfolio.
        blockchain (Blockchain): The blockchain used to store transactions.
        """
        self.portfolio_id = portfolio_id
        self.blockchain = blockchain
        self.assets: Dict[str, float] = {}

    def add_asset(self, asset: str, amount: float):
        """Adds an asset to the portfolio."""
        if asset in self.assets:
            self.assets[asset] += amount
        else:
            self.assets[asset] = amount
        self.blockchain.add_block(Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), {"portfolio_id": self.portfolio_id, "asset": asset, "amount": amount}))

    def remove_asset(self, asset: str, amount: float):
        """Removes an asset from the portfolio."""
        if asset in self.assets:
            if self.assets[asset] >= amount:
                self.assets[asset] -= amount
                self.blockchain.add_block(Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), {"portfolio_id": self.portfolio_id, "asset": asset, "amount": -amount}))
            else:
                raise ValueError("Insufficient assets in portfolio")
        else:
            raise ValueError("Asset not found in portfolio")

    def get_asset_balance(self, asset: str) -> float:
        """Gets the balance of an asset in the portfolio."""
        return self.assets.get(asset, 0)


class CryptoInvestmentPortfolio(InvestmentPortfolio):
    """Represents a cryptocurrency investment portfolio."""
    
    def __init__(self, portfolio_id: str, blockchain: Blockchain):
        """
        Initializes a new cryptocurrency investment portfolio.

        Args:
        portfolio_id (str): The ID of the portfolio.
        blockchain (Blockchain): The blockchain used to store transactions.
        """
        super().__init__(portfolio_id, blockchain)
        self.cryptos: Dict[str, float] = {}

    def add_crypto(self, crypto: str, amount: float):
        """Adds a cryptocurrency to the portfolio."""
        if crypto in self.cryptos:
            self.cryptos[crypto] += amount
        else:
            self.cryptos[crypto] = amount
        self.blockchain.add_block(Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), {"portfolio_id": self.portfolio_id, "crypto": crypto, "amount": amount}))

    def remove_crypto(self, crypto: str, amount: float):
        """Removes a cryptocurrency from the portfolio."""
        if crypto in self.cryptos:
            if self.cryptos[crypto] >= amount:
                self.cryptos[crypto] -= amount
                self.blockchain.add_block(Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), {"portfolio_id": self.portfolio_id, "crypto": crypto, "amount": -amount}))
            else:
                raise ValueError("Insufficient cryptocurrency in portfolio")
        else:
            raise ValueError("Cryptocurrency not found in portfolio")

    def get_crypto_balance(self, crypto: str) -> float:
        """Gets the balance of a cryptocurrency in the portfolio."""
        return self.cryptos.get(crypto, 0)


def main():
    blockchain = Blockchain()
    portfolio = CryptoInvestmentPortfolio("portfolio1", blockchain)

    try:
        portfolio.add_crypto("BTC", 1.0)
        portfolio.add_crypto("ETH", 5.0)
        print(portfolio.get_crypto_balance("BTC"))  # Output: 1.0
        print(portfolio.get_crypto_balance("ETH"))  # Output: 5.0
        portfolio.remove_crypto("BTC", 0.5)
        print(portfolio.get_crypto_balance("BTC"))  # Output: 0.5

        # Validate the blockchain
        print(blockchain.is_chain_valid())  # Output: True

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
