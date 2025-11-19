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
import hashlib
import json
from datetime import datetime
from typing import List, Dict, Optional

class Blockchain:
    """
    A simple blockchain implementation for investment portfolio management.
    """
    
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        
        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof: int, previous_hash: Optional[str] = None) -> Dict:
        """
        Create a new block in the blockchain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []
        
        self.chain.append(block)
        return block

    def new_transaction(self, sender: str, recipient: str, amount: float, asset: str) -> int:
        """
        Creates a new transaction to go into the next mined block.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'asset': asset,
            'timestamp': str(datetime.now())
        })
        
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block: Dict) -> str:
        """
        Creates a SHA-256 hash of a block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self) -> Dict:
        """
        Returns the last block in the chain.
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work algorithm.
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validates the Proof of Work.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def register_node(self, address: str) -> None:
        """
        Add a new node to the list of nodes.
        """
        self.nodes.add(address)

    def valid_chain(self, chain: List[Dict]) -> bool:
        """
        Determine if a given blockchain is valid.
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True


class Portfolio:
    """
    Investment portfolio management system.
    """
    
    def __init__(self, blockchain: Blockchain):
        self.blockchain = blockchain
        self.assets = {}  # Tracks asset balances for all users
        
    def add_asset(self, user_id: str, asset: str, amount: float) -> bool:
        """
        Add an asset to a user's portfolio.
        """
        if user_id not in self.assets:
            self.assets[user_id] = {}
            
        if asset not in self.assets[user_id]:
            self.assets[user_id][asset] = 0.0
            
        self.assets[user_id][asset] += amount
        return True
    
    def transfer_asset(self, sender: str, recipient: str, asset: str, amount: float) -> bool:
        """
        Transfer assets between users and record on blockchain.
        """
        # Check sender has sufficient balance
        if sender not in self.assets or asset not in self.assets[sender] or self.assets[sender][asset] < amount:
            return False
            
        # Create blockchain transaction
        self.blockchain.new_transaction(sender, recipient, amount, asset)
        
        # Update balances
        self.assets[sender][asset] -= amount
        
        if recipient not in self.assets:
            self.assets[recipient] = {}
        if asset not in self.assets[recipient]:
            self.assets[recipient][asset] = 0.0
            
        self.assets[recipient][asset] += amount
        return True
    
    def get_balance(self, user_id: str, asset: str) -> float:
        """
        Get a user's balance for a specific asset.
        """
        if user_id not in self.assets or asset not in self.assets[user_id]:
            return 0.0
        return self.assets[user_id][asset]
    
    def get_portfolio(self, user_id: str) -> Dict[str, float]:
        """
        Get a user's entire portfolio.
        """
        return self.assets.get(user_id, {})


class InvestmentAPI:
    """
    API layer for investment portfolio management.
    """
    
    def __init__(self):
        self.blockchain = Blockchain()
        self.portfolio = Portfolio(self.blockchain)
        
    def create_investment(self, user_id: str, asset: str, amount: float) -> Dict:
        """
        Create a new investment for a user.
        """
        if amount <= 0:
            return {'status': 'error', 'message': 'Amount must be positive'}
            
        self.portfolio.add_asset(user_id, asset, amount)
        return {'status': 'success', 'message': 'Investment created'}
    
    def transfer_investment(self, sender: str, recipient: str, asset: str, amount: float) -> Dict:
        """
        Transfer investment between users.
        """
        if amount <= 0:
            return {'status': 'error', 'message': 'Amount must be positive'}
            
        success = self.portfolio.transfer_asset(sender, recipient, asset, amount)
        if not success:
            return {'status': 'error', 'message': 'Transfer failed - insufficient balance'}
            
        return {'status': 'success', 'message': 'Transfer completed'}
    
    def get_investment_balance(self, user_id: str, asset: str) -> Dict:
        """
        Get a user's investment balance for a specific asset.
        """
        balance = self.portfolio.get_balance(user_id, asset)
        return {'status': 'success', 'balance': balance}
    
    def get_full_portfolio(self, user_id: str) -> Dict:
        """
        Get a user's complete investment portfolio.
        """
        portfolio = self.portfolio.get_portfolio(user_id)
        return {'status': 'success', 'portfolio': portfolio}
    
    def mine_block(self) -> Dict:
        """
        Mine a new block (for demo purposes).
        """
        last_block = self.blockchain.last_block
        last_proof = last_block['proof']
        proof = self.blockchain.proof_of_work(last_proof)
        
        # Reward the miner (for demo purposes)
        self.blockchain.new_transaction(
            sender="0",  # Represents the blockchain
            recipient="miner_address",
            amount=1.0,
            asset="BTC"
        )
        
        previous_hash = self.blockchain.hash(last_block)
        block = self.blockchain.new_block(proof, previous_hash)
        
        return {
            'status': 'success',
            'message': 'New block mined',
            'block': block
        }


# Example usage
if __name__ == '__main__':
    api = InvestmentAPI()
    
    # Create investments
    api.create_investment("user1", "BTC", 5.0)
    api.create_investment("user1", "ETH", 10.0)
    api.create_investment("user2", "BTC", 3.0)
    
    # Transfer between users
    api.transfer_investment("user1", "user2", "BTC", 1.0)
    
    # Get balances
    print(api.get_investment_balance("user1", "BTC"))
    print(api.get_full_portfolio("user1"))
    
    # Mine a block
    print(api.mine_block())
```
