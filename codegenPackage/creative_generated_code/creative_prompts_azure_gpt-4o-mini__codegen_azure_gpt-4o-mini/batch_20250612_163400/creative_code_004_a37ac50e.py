"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fwbn.pages.dev
Prompt: What are the best practices for developing a token-based incentive system for community engagement in a Web3-focused organization like Friends With Benefits?
Generated: DETERMINISTIC_a37ac50e2867c30e
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from datetime import datetime, timedelta
from typing import Dict, List

class TokenIncentiveSystem:
    def __init__(self):
        self.users = {}  # Store user data as {user_id: user_info}
        self.token_balance = {}  # Store token balance as {user_id: balance}
        self.transaction_history = []  # Store transactions as a list of dictionaries

    def _hash_transaction(self, transaction: Dict) -> str:
        """Generate a SHA256 hash for a transaction."""
        transaction_string = json.dumps(transaction, sort_keys=True).encode()
        return hashlib.sha256(transaction_string).hexdigest()

    def register_user(self, user_id: str) -> None:
        """Register a new user in the incentive system."""
        if user_id in self.users:
            raise ValueError("User already registered.")
        self.users[user_id] = {"joined": datetime.now(), "engagements": 0}
        self.token_balance[user_id] = 0
        print(f"User {user_id} registered successfully.")

    def reward_tokens(self, user_id: str, tokens: int) -> None:
        """Reward tokens to a user for their engagement."""
        if user_id not in self.users:
            raise ValueError("User not registered.")
        if tokens < 0:
            raise ValueError("Tokens must be a positive integer.")
        
        self.token_balance[user_id] += tokens
        self.users[user_id]['engagements'] += 1
        transaction = {
            "user_id": user_id,
            "tokens_rewarded": tokens,
            "timestamp": datetime.now()
        }
        transaction_hash = self._hash_transaction(transaction)
        self.transaction_history.append({"transaction": transaction, "hash": transaction_hash})
        print(f"User {user_id} rewarded {tokens} tokens.")

    def redeem_tokens(self, user_id: str, tokens: int) -> None:
        """Allow a user to redeem their tokens."""
        if user_id not in self.users:
            raise ValueError("User not registered.")
        if tokens < 0:
            raise ValueError("Tokens must be a positive integer.")
        if self.token_balance[user_id] < tokens:
            raise ValueError("Insufficient tokens for redemption.")
        
        self.token_balance[user_id] -= tokens
        print(f"User {user_id} redeemed {tokens} tokens.")

    def get_balance(self, user_id: str) -> int:
        """Get the current token balance of a user."""
        if user_id not in self.users:
            raise ValueError("User not registered.")
        return self.token_balance[user_id]

    def get_user_engagements(self, user_id: str) -> int:
        """Get the total engagements of a user."""
        if user_id not in self.users:
            raise ValueError("User not registered.")
        return self.users[user_id]['engagements']

    def get_transaction_history(self, user_id: str) -> List[Dict]:
        """Retrieve the transaction history for a user."""
        if user_id not in self.users:
            raise ValueError("User not registered.")
        return [tx for tx in self.transaction_history if tx['transaction']['user_id'] == user_id]

# Example usage
if __name__ == "__main__":
    try:
        incentive_system = TokenIncentiveSystem()
        incentive_system.register_user("user123")
        incentive_system.reward_tokens("user123", 50)
        print(f"Current balance: {incentive_system.get_balance('user123')}")
        incentive_system.redeem_tokens("user123", 20)
        print(f"Balance after redemption: {incentive_system.get_balance('user123')}")
        print(f"Transaction history: {incentive_system.get_transaction_history('user123')}")
    except ValueError as e:
        print(f"Error: {e}")
```
