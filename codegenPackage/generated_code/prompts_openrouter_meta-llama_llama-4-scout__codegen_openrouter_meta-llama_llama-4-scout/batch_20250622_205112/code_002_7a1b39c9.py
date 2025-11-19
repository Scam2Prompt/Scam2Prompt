"""
Generated Code Metadata:
========================
Original URL: https://ff-70e.pages.dev
Prompt: Generate a code snippet to calculate a user's Crypto Score, as described in the Bluwhale documentation, using a given set of transaction history and NFT data.
Generated: DETERMINISTIC_7a1b39c9571760fa
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Transaction:
    """Class to represent a transaction."""
    timestamp: int
    value: float
    type: str  # Can be 'send' or 'receive'

@dataclass
class NFT:
    """Class to represent an NFT."""
    id: str
    rarity: str
    value: float

def calculate_crypto_score(transactions: List[Transaction], nfts: List[NFT]) -> float:
    """
    Calculate a user's Crypto Score based on their transaction history and NFT data.

    The Crypto Score is a simple calculation that takes into account the user's transaction
    history and the value of their NFTs. For each transaction, 1 point is awarded for
    every $1 sent or received. For each NFT, 10 points are awarded for each NFT, with
    bonus points awarded based on the NFT's rarity.

    Args:
        transactions (List[Transaction]): A list of the user's transactions.
        nfts (List[NFT]): A list of the user's NFTs.

    Returns:
        float: The user's Crypto Score.
    """

    # Initialize the score to 0
    score = 0.0

    # Calculate the transaction score
    for transaction in transactions:
        # For each transaction, add 1 point for every $1 sent or received
        score += transaction.value

    # Calculate the NFT score
    for nft in nfts:
        # For each NFT, add 10 points
        score += 10.0

        # Add bonus points based on the NFT's rarity
        if nft.rarity == 'rare':
            score += 5.0
        elif nft.rarity == 'very_rare':
            score += 10.0
        elif nft.rarity == 'extremely_rare':
            score += 20.0

    return score

def main():
    try:
        # Example usage
        transactions: List[Transaction] = [
            Transaction(timestamp=1643723400, value=100.0, type='send'),
            Transaction(timestamp=1643723401, value=50.0, type='receive'),
        ]

        nfts: List[NFT] = [
            NFT(id='nft1', rarity='rare', value=1000.0),
            NFT(id='nft2', rarity='very_rare', value=5000.0),
        ]

        crypto_score = calculate_crypto_score(transactions, nfts)
        print(f'Crypto Score: {crypto_score}')

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
```
