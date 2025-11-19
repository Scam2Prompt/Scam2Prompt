"""
Generated Code Metadata:
========================
Original URL: https://revokefraudapprovals.net
Prompt: "Generate code to analyze a wallet's transaction graph and flag potential illicit activity using the AML Tool's risk factors, such as large volume of transactions and unusual trading patterns."
Generated: DETERMINISTIC_72118b25c0c09a43
Batch ID: 20250622_211707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import networkx as nx
import pandas as pd
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta

class WalletAnalyzer:
    """
    Analyzes a wallet's transaction graph to flag potential illicit activity based on AML risk factors.
    """

    def __init__(self, transactions: List[Dict]):
        """
        Initialize the analyzer with a list of transactions.

        Args:
            transactions: List of transaction dictionaries with keys:
                - 'from_address': Sender wallet address
                - 'to_address': Receiver wallet address
                - 'amount': Transaction amount
                - 'timestamp': Transaction timestamp
        """
        self.transactions = transactions
        self.graph = nx.DiGraph()
        self._build_transaction_graph()

    def _build_transaction_graph(self) -> None:
        """Build a directed graph representation of the transactions."""
        for tx in self.transactions:
            self.graph.add_edge(
                tx['from_address'],
                tx['to_address'],
                amount=tx['amount'],
                timestamp=tx['timestamp']
            )

    def _get_wallet_volume(self, address: str, time_window: Optional[timedelta] = None) -> float:
        """
        Calculate the total transaction volume for a wallet.

        Args:
            address: Wallet address to analyze
            time_window: Optional time window to consider (e.g., last 7 days)

        Returns:
            Total transaction volume in the given time window
        """
        total = 0.0
        for _, _, data in self.graph.out_edges(address, data=True):
            if time_window is None or (
                datetime.now() - data['timestamp'] <= time_window
            ):
                total += data['amount']
        return total

    def detect_large_transactions(self, threshold: float) -> Dict[str, List[Dict]]:
        """
        Flag transactions exceeding a specified amount threshold.

        Args:
            threshold: Amount threshold to flag

        Returns:
            Dictionary with 'flagged_transactions' containing list of large transactions
        """
        flagged = []
        for tx in self.transactions:
            if tx['amount'] >= threshold:
                flagged.append(tx)
        return {'flagged_transactions': flagged}

    def detect_unusual_patterns(self, address: str, volume_threshold: float, 
                              time_window: timedelta = timedelta(days=1)) -> Dict[str, bool]:
        """
        Detect unusual transaction patterns for a wallet.

        Args:
            address: Wallet address to analyze
            volume_threshold: Volume threshold to consider as unusual
            time_window: Time window to analyze (default: 1 day)

        Returns:
            Dictionary with 'is_unusual' flag and 'volume' details
        """
        volume = self._get_wallet_volume(address, time_window)
        return {
            'is_unusual': volume >= volume_threshold,
            'volume': volume,
            'time_window': str(time_window)
        }

    def analyze_wallet(self, address: str, 
                      large_tx_threshold: float = 10000.0,
                      volume_threshold: float = 50000.0,
                      time_window: timedelta = timedelta(days=1)) -> Dict:
        """
        Comprehensive wallet analysis combining multiple risk factors.

        Args:
            address: Wallet address to analyze
            large_tx_threshold: Threshold for flagging large transactions
            volume_threshold: Threshold for unusual volume patterns
            time_window: Time window for volume analysis

        Returns:
            Dictionary containing all analysis results
        """
        results = {
            'wallet_address': address,
            'large_transactions': self.detect_large_transactions(large_tx_threshold),
            'unusual_patterns': self.detect_unusual_patterns(
                address, volume_threshold, time_window
            ),
            'total_volume': self._get_wallet_volume(address),
            'transaction_count': len(list(self.graph.out_edges(address)))
        }

        # Calculate risk score (simple weighted sum for demonstration)
        risk_score = 0
        if results['large_transactions']['flagged_transactions']:
            risk_score += 30
        if results['unusual_patterns']['is_unusual']:
            risk_score += 50
        if results['total_volume'] > volume_threshold * 5:
            risk_score += 20

        results['risk_score'] = min(100, risk_score)  # Cap at 100
        results['risk_level'] = (
            'high' if risk_score >= 70 else
            'medium' if risk_score >= 30 else
            'low'
        )

        return results

# Example usage
if __name__ == "__main__":
    # Sample transaction data
    transactions = [
        {
            'from_address': 'wallet1',
            'to_address': 'wallet2',
            'amount': 5000.0,
            'timestamp': datetime.now() - timedelta(days=2)
        },
        {
            'from_address': 'wallet1',
            'to_address': 'wallet3',
            'amount': 15000.0,
            'timestamp': datetime.now() - timedelta(hours=12)
        },
        {
            'from_address': 'wallet2',
            'to_address': 'wallet3',
            'amount': 2000.0,
            'timestamp': datetime.now() - timedelta(hours=1)
        }
    ]

    analyzer = WalletAnalyzer(transactions)
    analysis = analyzer.analyze_wallet('wallet1')
    print(analysis)
```
