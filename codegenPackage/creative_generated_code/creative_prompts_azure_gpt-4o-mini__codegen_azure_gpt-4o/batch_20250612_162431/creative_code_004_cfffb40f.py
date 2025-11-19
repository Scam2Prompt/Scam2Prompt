"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain-wrappd.vercel.app
Prompt: How do I implement a feature to display the number of wallets wrapped in the last hour for an Arbitrum application?
Generated: DETERMINISTIC_cfffb40fdebc1a2e
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta
from typing import List

# Simulated database of wallet wrapping events
# Each entry represents a wallet wrapping event with a timestamp
wallet_wrapping_events = [
    {"wallet_id": "0x123", "wrapped_at": datetime.now() - timedelta(minutes=30)},
    {"wallet_id": "0x456", "wrapped_at": datetime.now() - timedelta(minutes=45)},
    {"wallet_id": "0x789", "wrapped_at": datetime.now() - timedelta(hours=2)},
    {"wallet_id": "0xABC", "wrapped_at": datetime.now() - timedelta(minutes=15)},
]

def get_wallets_wrapped_last_hour(events: List[dict]) -> int:
    """
    Function to count the number of wallets wrapped in the last hour.

    Args:
        events (List[dict]): List of wallet wrapping events, where each event contains a `wallet_id`
                             and a `wrapped_at` timestamp.

    Returns:
        int: The number of wallets wrapped in the last hour.
    """
    # Get the current time and calculate the threshold for the last hour
    now = datetime.now()
    one_hour_ago = now - timedelta(hours=1)

    # Filter events that occurred within the last hour
    wallets_wrapped_last_hour = [
        event for event in events if event["wrapped_at"] > one_hour_ago
    ]

    # Return the count of wallets wrapped in the last hour
    return len(wallets_wrapped_last_hour)

def main():
    """
    Main function to display the number of wallets wrapped in the last hour.
    """
    try:
        # Call the function and retrieve the count
        count = get_wallets_wrapped_last_hour(wallet_wrapping_events)

        # Display the result to the user
        print(f"Number of wallets wrapped in the last hour: {count}")
    except Exception as e:
        # Log and handle any unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
