"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-onchain.pages.dev
Prompt: Generate code for a blockchain-based game that uses Chain Links as in-game currency, allowing players to spend them on boosters and improvements.
Generated: DETERMINISTIC_ac763beddb91041c
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Blockchain-based game with Chain Links as in-game currency.

This script implements a simple blockchain-based game mechanism using Python.
Players can earn, spend, and check their balance of Chain Links.
They can use these Chain Links to purchase boosters and improvements.
"""

import hashlib
import json
import time


class Blockchain:
    """Class to manage the blockchain structure for the game."""

    def __init__(self):
        self.chain = []  # The main blockchain
        self.transactions = []  # Pending transactions
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash):
        """
        Create a new block and add it to the chain.
        :param proof: Proof of work
        :param previous_hash: Hash of the previous block
        :return: The newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.transactions = []  # Clear pending transactions after block is added
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """Return the last block of the chain."""
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        Proof of Work algorithm to generate valid proof.
        :param previous_proof: Proof from the previous block
        :return: Valid proof for the current block
        """
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:4] == '0000':  # Leading zeros indicate valid proof
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        """
        Generate a hash for a block.
        :param block: Block to be hashed
        :return: Hash value
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        """
        Validate the blockchain.
        :return: True if valid, False otherwise
        """
        previous_block = self.chain[0]
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
        return True

    def add_transaction(self, player_id, amount, transaction_type):
        """
        Add a transaction to the blockchain.
        :param player_id: Player's unique identifier
        :param amount: Amount of Chain Links spent or earned
        :param transaction_type: Type of transaction ('earn' or 'spend')
        :return: Index of the block where the transaction will be added
        """
        self.transactions.append({
            'player_id': player_id,
            'amount': amount,
            'transaction_type': transaction_type,
        })
        return self.get_previous_block()['index'] + 1


class Game:
    """Class to manage the game logic."""

    def __init__(self):
        self.blockchain = Blockchain()
        self.player_balances = {}  # Store player balances

    def earn_chain_links(self, player_id, amount):
        """
        Increase player's balance by earning Chain Links.
        :param player_id: Player's unique identifier
        :param amount: Amount of Chain Links earned
        """
        if player_id not in self.player_balances:
            self.player_balances[player_id] = 0
        self.player_balances[player_id] += amount
        self.blockchain.add_transaction(player_id, amount, 'earn')
        print(f"Player {player_id} earned {amount} Chain Links.")

    def spend_chain_links(self, player_id, amount):
        """
        Decrease player's balance by spending Chain Links.
        :param player_id: Player's unique identifier
        :param amount: Amount of Chain Links spent
        """
        if player_id not in self.player_balances or self.player_balances[player_id] < amount:
            print(f"Player {player_id} does not have enough Chain Links.")
            return False
        self.player_balances[player_id] -= amount
        self.blockchain.add_transaction(player_id, amount, 'spend')
        print(f"Player {player_id} spent {amount} Chain Links.")
        return True

    def get_balance(self, player_id):
        """
        Get the balance of a player.
        :param player_id: Player's unique identifier
        :return: Balance amount
        """
        return self.player_balances.get(player_id, 0)

    def purchase_booster(self, player_id):
        """
        Allow players to purchase boosters using Chain Links.
        :param player_id: Player's unique identifier
        """
        booster_cost = 10
        if self.spend_chain_links(player_id, booster_cost):
            print(f"Player {player_id} purchased a booster for {booster_cost} Chain Links.")

    def purchase_improvement(self, player_id):
        """
        Allow players to purchase improvements using Chain Links.
        :param player_id: Player's unique identifier
        """
        improvement_cost = 20
        if self.spend_chain_links(player_id, improvement_cost):
            print(f"Player {player_id} purchased an improvement for {improvement_cost} Chain Links.")


# Example usage:
if __name__ == "__main__":
    # Instantiate the game
    game = Game()

    # Player interactions
    game.earn_chain_links("player1", 50)
    print(f"Player1's balance: {game.get_balance('player1')} Chain Links")
    game.purchase_booster("player1")
    print(f"Player1's balance after buying booster: {game.get_balance('player1')} Chain Links")
    game.purchase_improvement("player1")
    print(f"Player1's balance after buying improvement: {game.get_balance('player1')} Chain Links")

    # Blockchain validation check
    print("Is blockchain valid:", game.blockchain.is_chain_valid())
```
