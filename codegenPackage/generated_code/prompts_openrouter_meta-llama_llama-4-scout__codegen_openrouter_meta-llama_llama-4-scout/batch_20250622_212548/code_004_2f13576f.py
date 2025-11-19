"""
Generated Code Metadata:
========================
Original URL: https://worldlibertyfinanciallabs.com
Prompt: Design a high-level architecture for a decentralized finance (DeFi) platform, incorporating key features such as community-owned governance, token swapping, and secure token transfer, as described on the World Liberty Financial website.
Generated: DETERMINISTIC_2f13576fdacc40e3
Batch ID: 20250622_212548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
import hashlib
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define custom exceptions
class InsufficientBalanceError(Exception):
    """Raised when a user has insufficient balance for a transaction"""
    pass

class InvalidTransactionError(Exception):
    """Raised when a transaction is invalid"""
    pass

# Define an enum for transaction types
class TransactionType(Enum):
    """Enum for transaction types"""
    TOKEN_SWAP = 1
    TOKEN_TRANSFER = 2

# Define a data class for transactions
@dataclass
class Transaction:
    """Data class for transactions"""
    sender: str
    recipient: str
    amount: float
    transaction_type: TransactionType

# Define a data class for tokens
@dataclass
class Token:
    """Data class for tokens"""
    name: str
    symbol: str
    supply: float

# Define a class for the DeFi platform
class DeFiPlatform:
    """Class for the DeFi platform"""
    def __init__(self):
        self.tokens: Dict[str, Token] = {}
        self.user_balances: Dict[str, Dict[str, float]] = {}
        self.governance_votes: Dict[str, Dict[str, bool]] = {}

    def add_token(self, token: Token):
        """Add a token to the platform"""
        self.tokens[token.symbol] = token
        logger.info(f"Token {token.symbol} added")

    def register_user(self, user: str):
        """Register a user on the platform"""
        if user not in self.user_balances:
            self.user_balances[user] = {}
            logger.info(f"User {user} registered")
        else:
            logger.info(f"User {user} already registered")

    def deposit_tokens(self, user: str, token_symbol: str, amount: float):
        """Deposit tokens into a user's account"""
        if token_symbol in self.tokens:
            if user not in self.user_balances:
                self.register_user(user)
            if token_symbol not in self.user_balances[user]:
                self.user_balances[user][token_symbol] = 0
            self.user_balances[user][token_symbol] += amount
            logger.info(f"User {user} deposited {amount} {token_symbol} tokens")
        else:
            logger.error(f"Token {token_symbol} does not exist")

    def token_swap(self, user: str, token_symbol_in: str, token_symbol_out: str, amount: float):
        """Swap tokens"""
        try:
            # Check if tokens exist
            if token_symbol_in not in self.tokens or token_symbol_out not in self.tokens:
                raise InvalidTransactionError("One or both tokens do not exist")

            # Check if user has sufficient balance
            if token_symbol_in not in self.user_balances.get(user, {}) or self.user_balances[user][token_symbol_in] < amount:
                raise InsufficientBalanceError("Insufficient balance")

            # Perform token swap
            self.user_balances[user][token_symbol_in] -= amount
            if token_symbol_out not in self.user_balances[user]:
                self.user_balances[user][token_symbol_out] = 0
            self.user_balances[user][token_symbol_out] += amount

            # Create a transaction
            transaction = Transaction(user, user, amount, TransactionType.TOKEN_SWAP)

            logger.info(f"User {user} swapped {amount} {token_symbol_in} tokens for {token_symbol_out} tokens")
        except Exception as e:
            logger.error(f"Error during token swap: {e}")

    def token_transfer(self, sender: str, recipient: str, token_symbol: str, amount: float):
        """Transfer tokens"""
        try:
            # Check if token exists
            if token_symbol not in self.tokens:
                raise InvalidTransactionError("Token does not exist")

            # Check if sender has sufficient balance
            if token_symbol not in self.user_balances.get(sender, {}) or self.user_balances[sender][token_symbol] < amount:
                raise InsufficientBalanceError("Insufficient balance")

            # Perform token transfer
            self.user_balances[sender][token_symbol] -= amount
            if token_symbol not in self.user_balances.get(recipient, {}):
                self.user_balances[recipient] = {token_symbol: 0}
            self.user_balances[recipient][token_symbol] = self.user_balances[recipient].get(token_symbol, 0) + amount

            # Create a transaction
            transaction = Transaction(sender, recipient, amount, TransactionType.TOKEN_TRANSFER)

            logger.info(f"User {sender} transferred {amount} {token_symbol} tokens to user {recipient}")
        except Exception as e:
            logger.error(f"Error during token transfer: {e}")

    def vote(self, user: str, proposal: str, vote: bool):
        """Cast a vote on a governance proposal"""
        if user not in self.governance_votes:
            self.governance_votes[user] = {}
        self.governance_votes[user][proposal] = vote
        logger.info(f"User {user} voted on proposal {proposal}")

def main():
    # Create a DeFi platform
    defi_platform = DeFiPlatform()

    # Add tokens
    token1 = Token("Token 1", "T1", 1000)
    token2 = Token("Token 2", "T2", 1000)
    defi_platform.add_token(token1)
    defi_platform.add_token(token2)

    # Register users
    defi_platform.register_user("User1")
    defi_platform.register_user("User2")

    # Deposit tokens
    defi_platform.deposit_tokens("User1", "T1", 100)
    defi_platform.deposit_tokens("User2", "T2", 100)

    # Swap tokens
    defi_platform.token_swap("User1", "T1", "T2", 50)

    # Transfer tokens
    defi_platform.token_transfer("User2", "User1", "T2", 20)

    # Vote on a proposal
    defi_platform.vote("User1", "Proposal1", True)

if __name__ == "__main__":
    main()
```
