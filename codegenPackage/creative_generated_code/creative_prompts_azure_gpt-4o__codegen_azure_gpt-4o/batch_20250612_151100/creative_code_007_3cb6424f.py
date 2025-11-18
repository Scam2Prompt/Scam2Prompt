"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theoldcastle.pages.dev
Prompt: Generate code for a decentralized leaderboard system that tracks and displays $FOMO Points earned by users after each game, similar to the distribution model described on The Old Castle Defense.
Generated: DETERMINISTIC_3cb6424f3dd84f4f
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: decentralized_leaderboard.py

import hashlib
import json
import time
from typing import Dict, List

# Class: Blockchain
# This class represents a simple blockchain for decentralized leaderboard tracking.
class Blockchain:
    def __init__(self):
        self.chain = []  # List to store the blockchain
        self.pending_transactions = []  # List to store transactions waiting to be added to the chain
        self.create_block(previous_hash="0")  # Genesis block

    def create_block(self, previous_hash: str) -> Dict:
        """
        Creates a new block in the blockchain.
        :param previous_hash: Hash of the previous block.
        :return: Newly created block.
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "transactions": self.pending_transactions,
            "previous_hash": previous_hash,
        }
        block["hash"] = self.hash(block)
        self.pending_transactions = []  # Clear pending transactions
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block: Dict) -> str:
        """
        Creates a hash for a block.
        :param block: Block to hash.
        :return: SHA-256 hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, user: str, points: int):
        """
        Adds a transaction to the pending transactions list.
        :param user: Username earning points.
        :param points: Points earned.
        """
        transaction = {"user": user, "points": points}
        self.pending_transactions.append(transaction)

    def get_leaderboard(self) -> List[Dict]:
        """
        Computes the leaderboard based on the blockchain data.
        :return: Leaderboard sorted by points in descending order.
        """
        leaderboard = {}
        for block in self.chain:
            for transaction in block["transactions"]:
                user = transaction["user"]
                points = transaction["points"]
                leaderboard[user] = leaderboard.get(user, 0) + points

        sorted_leaderboard = [{"user": user, "points": points} for user, points in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)]
        return sorted_leaderboard


# Class: DecentralizedLeaderboardSystem
# A wrapper class to interact with the blockchain and manage the leaderboard system.
class DecentralizedLeaderboardSystem:
    def __init__(self):
        self.blockchain = Blockchain()

    def record_game_results(self, game_results: Dict[str, int]):
        """
        Records game results into the blockchain.
        :param game_results: Dictionary mapping usernames to points earned.
        """
        if not isinstance(game_results, dict):
            raise ValueError("Game results must be a dictionary mapping usernames to points.")

        for user, points in game_results.items():
            if not isinstance(user, str) or not isinstance(points, int):
                raise ValueError("Invalid data format: Usernames must be strings and points integers.")

            self.blockchain.add_transaction(user, points)

        # Commit transactions to a new block
        last_block = self.blockchain.chain[-1]
        self.blockchain.create_block(previous_hash=last_block["hash"])

    def display_leaderboard(self):
        """
        Displays the current leaderboard.
        """
        leaderboard = self.blockchain.get_leaderboard()
        print("Leaderboard:")
        print("-" * 30)
        for rank, entry in enumerate(leaderboard, start=1):
            print(f"{rank}. {entry['user']} - {entry['points']} points")


# Example usage
if __name__ == "__main__":
    leaderboard_system = DecentralizedLeaderboardSystem()

    # Simulate game results
    game_results_1 = {"Alice": 50, "Bob": 120, "Charlie": 75}
    game_results_2 = {"Alice": 30, "Charlie": 55, "Dave": 100}

    # Record and display results
    leaderboard_system.record_game_results(game_results_1)
    leaderboard_system.record_game_results(game_results_2)
    leaderboard_system.display_leaderboard()
```
