"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autodigitaltrade.com.easyprofitabletrading.com
Prompt: Create a script to analyze and display withdrawal statuses (confirmed/pending) for a trading platform, inspired by the withdrawal tracking system on Autodigitaltrade.
Generated: DETERMINISTIC_bc4d0ca2dc5c8e27
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime


class WithdrawalTracker:
    """
    A class to track and analyze withdrawal statuses for a trading platform.
    """

    def __init__(self, data_file):
        """
        Initializes the WithdrawalTracker with a file containing withdrawal data.

        :param data_file: Path to the JSON file containing withdrawal data.
        """
        self.data_file = data_file
        self.withdrawals = []

    def load_data(self):
        """
        Loads withdrawal data from the specified JSON file.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(self.data_file, 'r') as file:
                self.withdrawals = json.load(file)
        except FileNotFoundError:
            print(f"ERROR: The file '{self.data_file}' was not found.")
            raise
        except json.JSONDecodeError:
            print(f"ERROR: Failed to decode JSON from '{self.data_file}'.")
            raise

    def analyze_statuses(self):
        """
        Analyzes withdrawal statuses and returns a summary.

        :return: A dictionary with counts of confirmed and pending withdrawals.
        """
        summary = {"confirmed": 0, "pending": 0}

        for withdrawal in self.withdrawals:
            status = withdrawal.get("status")
            if status == "confirmed":
                summary["confirmed"] += 1
            elif status == "pending":
                summary["pending"] += 1
            else:
                print(f"WARNING: Unknown status '{status}' in withdrawal id {withdrawal.get('id')}.")

        return summary

    def display_summary(self):
        """
        Displays a summary of withdrawal statuses.
        """
        summary = self.analyze_statuses()
        print("Withdrawal Status Summary:")
        print(f"  Confirmed Withdrawals: {summary['confirmed']}")
        print(f"  Pending Withdrawals: {summary['pending']}")

    def display_details(self):
        """
        Displays details of each withdrawal including status and timestamp.
        """
        print("Withdrawal Details:")
        for withdrawal in self.withdrawals:
            withdrawal_id = withdrawal.get("id", "Unknown ID")
            status = withdrawal.get("status", "Unknown Status")
            timestamp = withdrawal.get("timestamp", "Unknown Timestamp")
            try:
                # Attempt to format the timestamp for better readability
                formatted_time = datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %H:%M:%S")
            except (ValueError, TypeError):
                formatted_time = timestamp  # Fallback to raw timestamp if formatting fails
            
            print(f"  ID: {withdrawal_id} | Status: {status} | Timestamp: {formatted_time}")


# Example usage
if __name__ == "__main__":
    # Replace 'withdrawals.json' with the path to your JSON data file
    tracker = WithdrawalTracker("withdrawals.json")

    try:
        tracker.load_data()
        tracker.display_summary()
        tracker.display_details()
    except Exception as e:
        print(f"ERROR: An unexpected error occurred - {e}")
```

### Example JSON File (`withdrawals.json`):
```json
[
    {"id": 1, "status": "confirmed", "timestamp": "2023-10-01T15:30:00"},
    {"id": 2, "status": "pending", "timestamp": "2023-10-02T12:00:00"},
    {"id": 3, "status": "confirmed", "timestamp": "2023-10-02T14:45:00"},
    {"id": 4, "status": "pending", "timestamp": "2023-10-03T09:30:00"}
]
```
