"""
Generated Code Metadata:
========================
Original URL: https://pulsedapp.pages.dev
Prompt: Generate a code example for calculating the estimated completion time of a transaction on the PulseChain Bridge, assuming a 30-minute completion time.
Generated: DETERMINISTIC_ed034ed29592dbbb
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

class PulseChainBridgeETC:
    """
    A class to calculate and manage the estimated completion time for transactions
    on the PulseChain Bridge with a fixed 30-minute completion time.
    """

    def __init__(self):
        """Initialize the PulseChainBridgeETC class."""
        self.default_completion_time = 30  # minutes

    def calculate_etc(self, start_time=None):
        """
        Calculate the estimated completion time for a transaction.
        
        Args:
            start_time (datetime, optional): The start time of the transaction.
                If None, current time will be used.
                
        Returns:
            dict: A dictionary containing:
                - 'start_time': The transaction start time
                - 'estimated_completion': The estimated completion time
                - 'completion_duration': The duration in minutes
                - 'current_time': The time when calculation was made
        """
        try:
            if start_time is None:
                start_time = datetime.now()
            
            if not isinstance(start_time, datetime):
                raise ValueError("start_time must be a datetime object")
                
            completion_time = start_time + timedelta(minutes=self.default_completion_time)
            
            return {
                'start_time': start_time,
                'estimated_completion': completion_time,
                'completion_duration': self.default_completion_time,
                'current_time': datetime.now()
            }
            
        except Exception as e:
            return {
                'error': str(e),
                'current_time': datetime.now()
            }

    def get_remaining_time(self, start_time):
        """
        Calculate remaining time for a transaction to complete.
        
        Args:
            start_time (datetime): The start time of the transaction.
                
        Returns:
            dict: A dictionary containing:
                - 'remaining_minutes': Remaining time in minutes
                - 'is_completed': Boolean indicating if transaction is complete
                - 'current_time': The time when calculation was made
        """
        try:
            if not isinstance(start_time, datetime):
                raise ValueError("start_time must be a datetime object")
                
            now = datetime.now()
            completion_time = start_time + timedelta(minutes=self.default_completion_time)
            remaining = (completion_time - now).total_seconds() / 60
            
            if remaining <= 0:
                return {
                    'remaining_minutes': 0,
                    'is_completed': True,
                    'current_time': now
                }
            else:
                return {
                    'remaining_minutes': round(remaining, 2),
                    'is_completed': False,
                    'current_time': now
                }
                
        except Exception as e:
            return {
                'error': str(e),
                'current_time': datetime.now()
            }

# Example usage
if __name__ == "__main__":
    bridge = PulseChainBridgeETC()
    
    # Calculate ETC for a new transaction
    etc_result = bridge.calculate_etc()
    print("Estimated Completion:", etc_result['estimated_completion'])
    
    # Check remaining time (using the start_time from previous calculation)
    time.sleep(5)  # Simulate time passing
    remaining_result = bridge.get_remaining_time(etc_result['start_time'])
    print("Remaining Minutes:", remaining_result['remaining_minutes'])
```
