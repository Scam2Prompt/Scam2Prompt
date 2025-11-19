"""
Generated Code Metadata:
========================
Original URL: https://pansos4dmax.site
Prompt: Develop a program to track and display the average deposit and withdrawal times (1 minute and 3 minutes, respectively) as mentioned on the PANSOS4D website.
Generated: DETERMINISTIC_e4ce2c6a3da2d0e2
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from collections import defaultdict
from typing import Dict, Tuple, List
import statistics

class TransactionTracker:
    """
    A class to track and display average deposit and withdrawal times.
    """
    
    def __init__(self):
        """
        Initialize the transaction tracker with default deposit and withdrawal times.
        """
        self.deposit_time = 1 * 60  # 1 minute in seconds
        self.withdrawal_time = 3 * 60  # 3 minutes in seconds
        self.transactions: Dict[str, List[Tuple[float, str]]] = defaultdict(list)
    
    def start_transaction(self, transaction_type: str) -> None:
        """
        Start tracking a transaction.
        
        Args:
            transaction_type: Type of transaction ('deposit' or 'withdrawal')
        """
        if transaction_type not in ['deposit', 'withdrawal']:
            raise ValueError("Transaction type must be 'deposit' or 'withdrawal'")
        
        start_time = time.time()
        self.transactions[transaction_type].append((start_time, 'start'))
    
    def end_transaction(self, transaction_type: str) -> None:
        """
        End tracking a transaction.
        
        Args:
            transaction_type: Type of transaction ('deposit' or 'withdrawal')
        """
        if transaction_type not in ['deposit', 'withdrawal']:
            raise ValueError("Transaction type must be 'deposit' or 'withdrawal'")
        
        end_time = time.time()
        self.transactions[transaction_type].append((end_time, 'end'))
    
    def _calculate_durations(self, transaction_type: str) -> List[float]:
        """
        Calculate durations for completed transactions of a given type.
        
        Args:
            transaction_type: Type of transaction ('deposit' or 'withdrawal')
            
        Returns:
            List of durations in seconds for completed transactions
        """
        transactions = self.transactions.get(transaction_type, [])
        starts = [t[0] for t in transactions if t[1] == 'start']
        ends = [t[0] for t in transactions if t[1] == 'end']
        
        if len(starts) != len(ends):
            raise ValueError("Mismatch between start and end transaction counts")
            
        return [end - start for start, end in zip(starts, ends)]
    
    def get_average_times(self) -> Dict[str, float]:
        """
        Calculate and return average times for deposits and withdrawals.
        
        Returns:
            Dictionary with average times in seconds for 'deposit' and 'withdrawal'
        """
        result = {}
        
        try:
            deposit_durations = self._calculate_durations('deposit')
            result['deposit'] = statistics.mean(deposit_durations) if deposit_durations else self.deposit_time
        except (ValueError, statistics.StatisticsError):
            result['deposit'] = self.deposit_time
            
        try:
            withdrawal_durations = self._calculate_durations('withdrawal')
            result['withdrawal'] = statistics.mean(withdrawal_durations) if withdrawal_durations else self.withdrawal_time
        except (ValueError, statistics.StatisticsError):
            result['withdrawal'] = self.withdrawal_time
            
        return result
    
    def display_average_times(self) -> None:
        """
        Display the average deposit and withdrawal times in minutes.
        """
        averages = self.get_average_times()
        print(f"Average Deposit Time: {averages['deposit'] / 60:.2f} minutes")
        print(f"Average Withdrawal Time: {averages['withdrawal'] / 60:.2f} minutes")


# Example usage
if __name__ == "__main__":
    tracker = TransactionTracker()
    
    # Simulate some transactions
    tracker.start_transaction('deposit')
    time.sleep(65)  # Simulate 1 minute 5 seconds
    tracker.end_transaction('deposit')
    
    tracker.start_transaction('withdrawal')
    time.sleep(185)  # Simulate 3 minutes 5 seconds
    tracker.end_transaction('withdrawal')
    
    # Display averages
    tracker.display_average_times()
```
