"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dmax.site
Prompt: Develop a program to track and display the average deposit and withdrawal times (1 minute and 3 minutes, respectively) as mentioned on the PANSOS4D website.
Generated: DETERMINISTIC_e4ce2c6a3da2d0e2
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import statistics

class TransactionTracker:
    """A class to track deposit and withdrawal times."""
    
    def __init__(self):
        """Initialize the tracker with lists to store transaction times."""
        self.deposit_times = []
        self.withdrawal_times = []

    def record_deposit(self):
        """Simulate recording a deposit transaction time."""
        start_time = time.time()
        # Simulating a deposit operation taking 1 minute
        time.sleep(60)  # Note: In a real application, you'd handle this differently
        end_time = time.time()
        deposit_duration = end_time - start_time
        self.deposit_times.append(deposit_duration)
        print(f"Recorded deposit time: {deposit_duration:.2f} seconds")

    def record_withdrawal(self):
        """Simulate recording a withdrawal transaction time."""
        start_time = time.time()
        # Simulating a withdrawal operation taking 3 minutes
        time.sleep(180)  # Note: In a real application, you'd handle this differently
        end_time = time.time()
        withdrawal_duration = end_time - start_time
        self.withdrawal_times.append(withdrawal_duration)
        print(f"Recorded withdrawal time: {withdrawal_duration:.2f} seconds")

    def get_average_deposit_time(self):
        """Return the average deposit time."""
        if not self.deposit_times:
            raise ValueError("No deposit times recorded.")
        return statistics.mean(self.deposit_times)

    def get_average_withdrawal_time(self):
        """Return the average withdrawal time."""
        if not self.withdrawal_times:
            raise ValueError("No withdrawal times recorded.")
        return statistics.mean(self.withdrawal_times)

    def display_average_times(self):
        """Display the average deposit and withdrawal times."""
        try:
            avg_deposit = self.get_average_deposit_time()
            avg_withdrawal = self.get_average_withdrawal_time()
            print(f"Average Deposit Time: {avg_deposit:.2f} seconds")
            print(f"Average Withdrawal Time: {avg_withdrawal:.2f} seconds")
        except ValueError as e:
            print(f"Error: {e}")

# Main execution block
if __name__ == "__main__":
    tracker = TransactionTracker()

    # Simulate recording transactions
    try:
        for _ in range(2):  # Record two deposits
            tracker.record_deposit()
        
        for _ in range(2):  # Record two withdrawals
            tracker.record_withdrawal()
        
        # Display average times
        tracker.display_average_times()
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
