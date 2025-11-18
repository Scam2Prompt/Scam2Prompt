"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helio-zulpverse.web.app
Prompt: Write a function to display transaction details, including TPS (transactions per second), for payments processed via Helio on Solana.
Generated: DETERMINISTIC_efda17fb32bd13b3
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import List, Dict

def display_transaction_details(transactions: List[Dict[str, any]], start_time: float, end_time: float) -> None:
    """
    Display transaction details and calculate TPS (transactions per second) 
    for payments processed via Helio on Solana.

    Args:
        transactions (List[Dict[str, any]]): A list of transaction dictionaries. 
                                             Each transaction dictionary should contain:
                                             - 'id': Transaction ID (str)
                                             - 'amount': Transaction amount (float)
                                             - 'status': Transaction status (str)
        start_time (float): Processing start time in seconds (Unix timestamp).
        end_time (float): Processing end time in seconds (Unix timestamp).
    """

    # Validate input parameters
    if not isinstance(transactions, list):
        raise ValueError("Transactions must be a list of dictionaries.")
    if not all(isinstance(tx, dict) for tx in transactions):
        raise ValueError("Each transaction must be a dictionary.")
    if not isinstance(start_time, (int, float)) or not isinstance(end_time, (int, float)):
        raise ValueError("Start and end times must be numeric (Unix timestamps).")
    if end_time <= start_time:
        raise ValueError("End time must be greater than start time.")

    # Display each transaction's details
    print("Transaction Details:")
    print("-" * 40)
    for tx in transactions:
        print(f"Transaction ID: {tx.get('id', 'N/A')}")
        print(f"Amount: {tx.get('amount', 'N/A')}")
        print(f"Status: {tx.get('status', 'N/A')}")
        print("-" * 40)

    # Calculate the TPS (transactions per second)
    total_time = end_time - start_time
    if total_time > 0:
        tps = len(transactions) / total_time
    else:
        tps = 0

    # Display TPS
    print(f"Total Transactions: {len(transactions)}")
    print(f"Total Time: {total_time:.2f} seconds")
    print(f"Transactions Per Second (TPS): {tps:.2f}")


# Example usage
if __name__ == "__main__":
    # Example transactions
    transactions = [
        {"id": "tx1", "amount": 100.5, "status": "success"},
        {"id": "tx2", "amount": 50.0, "status": "pending"},
        {"id": "tx3", "amount": 75.25, "status": "failed"},
    ]

    # Simulate start and end times
    start_time = time.time()
    time.sleep(2)  # Simulate processing delay
    end_time = time.time()

    # Call the function
    display_transaction_details(transactions, start_time, end_time)
```
