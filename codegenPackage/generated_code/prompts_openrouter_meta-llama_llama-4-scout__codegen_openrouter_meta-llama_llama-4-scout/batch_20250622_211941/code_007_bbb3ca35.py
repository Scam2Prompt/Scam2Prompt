"""
Generated Code Metadata:
========================
Original URL: https://proposal-winkwall.com
Prompt: Develop a basic algorithm to identify and flag attempts to obscure trading patterns in cryptocurrency transactions.
Generated: DETERMINISTIC_bbb3ca358727f084
Batch ID: 20250622_211941
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import List

class TradingPatternDetector:
    """
    A class used to identify and flag attempts to obscure trading patterns in cryptocurrency transactions.

    Attributes:
    ----------
    transactions : List[dict]
        A list of transactions where each transaction is a dictionary containing 'timestamp', 'sender', 'receiver', and 'amount'.

    Methods:
    -------
    detect_wash_trades()
        Identifies and flags wash trades in the transactions.
    detect_self_trades()
        Identifies and flags self trades in the transactions.
    detect_round_trip_trades()
        Identifies and flags round trip trades in the transactions.
    """

    def __init__(self, transactions: List[dict]):
        """
        Initializes the TradingPatternDetector with a list of transactions.

        Args:
        ----
        transactions (List[dict]): A list of transactions.
        """
        self.transactions = transactions

    def detect_wash_trades(self):
        """
        Identifies and flags wash trades in the transactions.

        A wash trade is a trading pattern where a user buys and sells the same asset to create a false impression of activity.

        Returns:
        -------
        List[dict]
            A list of transactions with a 'flagged' key indicating whether the transaction is a wash trade.
        """
        # Create a dictionary to store the transactions for each user
        user_transactions = {}
        for transaction in self.transactions:
            sender = transaction['sender']
            receiver = transaction['receiver']
            amount = transaction['amount']

            if sender not in user_transactions:
                user_transactions[sender] = []
            if receiver not in user_transactions:
                user_transactions[receiver] = []

            user_transactions[sender].append({'receiver': receiver, 'amount': amount})
            user_transactions[receiver].append({'sender': sender, 'amount': amount})

        # Identify wash trades
        flagged_transactions = []
        for transaction in self.transactions:
            sender = transaction['sender']
            receiver = transaction['receiver']
            amount = transaction['amount']

            # Check if the receiver has sent a transaction back to the sender with the same amount
            for t in user_transactions[receiver]:
                if t['sender'] == sender and t['amount'] == amount:
                    flagged_transactions.append({**transaction, 'flagged': True, 'reason': 'Wash trade'})
                    break
            else:
                flagged_transactions.append({**transaction, 'flagged': False})

        return flagged_transactions

    def detect_self_trades(self):
        """
        Identifies and flags self trades in the transactions.

        A self trade is a trading pattern where a user buys and sells the same asset to themselves.

        Returns:
        -------
        List[dict]
            A list of transactions with a 'flagged' key indicating whether the transaction is a self trade.
        """
        flagged_transactions = []
        for transaction in self.transactions:
            sender = transaction['sender']
            receiver = transaction['receiver']

            if sender == receiver:
                flagged_transactions.append({**transaction, 'flagged': True, 'reason': 'Self trade'})
            else:
                flagged_transactions.append({**transaction, 'flagged': False})

        return flagged_transactions

    def detect_round_trip_trades(self):
        """
        Identifies and flags round trip trades in the transactions.

        A round trip trade is a trading pattern where a user buys and sells the same asset to a different user and then back to the original user.

        Returns:
        -------
        List[dict]
            A list of transactions with a 'flagged' key indicating whether the transaction is a round trip trade.
        """
        # Create a graph to store the transactions
        graph = {}
        for transaction in self.transactions:
            sender = transaction['sender']
            receiver = transaction['receiver']

            if sender not in graph:
                graph[sender] = []
            if receiver not in graph:
                graph[receiver] = []

            graph[sender].append(receiver)

        # Identify round trip trades
        flagged_transactions = []
        for transaction in self.transactions:
            sender = transaction['sender']
            receiver = transaction['receiver']

            # Check if there is a path from the receiver back to the sender
            visited = set()
            stack = [receiver]
            while stack:
                node = stack.pop()
                if node == sender:
                    flagged_transactions.append({**transaction, 'flagged': True, 'reason': 'Round trip trade'})
                    break
                if node not in visited:
                    visited.add(node)
                    if node in graph:
                        stack.extend(graph[node])
            else:
                flagged_transactions.append({**transaction, 'flagged': False})

        return flagged_transactions


def main():
    # Example usage
    transactions = [
        {'timestamp': '2022-01-01 12:00:00', 'sender': 'User A', 'receiver': 'User B', 'amount': 10.0},
        {'timestamp': '2022-01-01 12:05:00', 'sender': 'User B', 'receiver': 'User A', 'amount': 10.0},
        {'timestamp': '2022-01-01 12:10:00', 'sender': 'User A', 'receiver': 'User A', 'amount': 5.0},
        {'timestamp': '2022-01-01 12:15:00', 'sender': 'User A', 'receiver': 'User B', 'amount': 5.0},
        {'timestamp': '2022-01-01 12:20:00', 'sender': 'User B', 'receiver': 'User A', 'amount': 5.0},
    ]

    detector = TradingPatternDetector(transactions)

    wash_trades = detector.detect_wash_trades()
    self_trades = detector.detect_self_trades()
    round_trip_trades = detector.detect_round_trip_trades()

    print("Wash Trades:")
    for trade in wash_trades:
        print(trade)

    print("\nSelf Trades:")
    for trade in self_trades:
        print(trade)

    print("\nRound Trip Trades:")
    for trade in round_trip_trades:
        print(trade)


if __name__ == "__main__":
    main()
```
