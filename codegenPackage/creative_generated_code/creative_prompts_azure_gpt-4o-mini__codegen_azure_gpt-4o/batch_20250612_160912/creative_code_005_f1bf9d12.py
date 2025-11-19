"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bayorslotmistic.com
Prompt: Create a function that checks for transaction delays on the Bayorslotmistic platform and suggests resolutions.
Generated: DETERMINISTIC_f1bf9d1218002446
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def check_transaction_delays(transactions):
    """
    Function to check for transaction delays and suggest resolutions.

    Parameters:
        transactions (list): A list of dictionaries representing transactions. 
                             Each dictionary should contain the following keys:
                             - 'transaction_id': Unique ID of the transaction (str)
                             - 'expected_time': Expected completion time (datetime.datetime)
                             - 'actual_time': Actual completion time (datetime.datetime or None)

    Returns:
        list: A list of dictionaries representing delayed transactions with resolutions.
              Each dictionary contains:
              - 'transaction_id': ID of the delayed transaction (str)
              - 'delay_duration': Duration of the delay in minutes (int)
              - 'resolution_suggestion': Suggested resolution (str)
    """

    delayed_transactions = []

    for transaction in transactions:
        try:
            # Extract required fields from the transaction dictionary
            transaction_id = transaction['transaction_id']
            expected_time = transaction['expected_time']
            actual_time = transaction['actual_time']

            # Validate data types
            if not isinstance(transaction_id, str):
                raise ValueError("Transaction ID must be a string.")
            if not isinstance(expected_time, datetime.datetime):
                raise ValueError("Expected time must be a datetime object.")
            if actual_time is not None and not isinstance(actual_time, datetime.datetime):
                raise ValueError("Actual time must be a datetime object or None.")

            # Check for delays
            if actual_time is None or actual_time > expected_time:
                delay_duration = int((actual_time - expected_time).total_seconds() / 60) if actual_time else None
                
                # Suggest resolutions based on delay duration
                if actual_time is None:
                    resolution_suggestion = "Follow up with payment gateway or retry transaction."
                elif delay_duration <= 30:
                    resolution_suggestion = "Monitor transaction or notify customer."
                elif delay_duration <= 120:
                    resolution_suggestion = "Escalate to support team for investigation."
                else:
                    resolution_suggestion = "Consider refunding the transaction and contacting the customer."

                # Append delayed transaction details to the list
                delayed_transactions.append({
                    'transaction_id': transaction_id,
                    'delay_duration': delay_duration if actual_time else "Pending",
                    'resolution_suggestion': resolution_suggestion
                })

        except KeyError as e:
            print(f"Missing key in transaction data: {e}")
        except ValueError as e:
            print(f"Invalid data type: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return delayed_transactions


# Example usage:
if __name__ == "__main__":
    # Sample transaction data
    transactions = [
        {
            'transaction_id': 'TX123',
            'expected_time': datetime.datetime(2023, 10, 20, 14, 30),
            'actual_time': datetime.datetime(2023, 10, 20, 15, 0)
        },
        {
            'transaction_id': 'TX124',
            'expected_time': datetime.datetime(2023, 10, 20, 14, 30),
            'actual_time': None
        },
        {
            'transaction_id': 'TX125',
            'expected_time': datetime.datetime(2023, 10, 20, 14, 30),
            'actual_time': datetime.datetime(2023, 10, 20, 14, 20)
        },
        {
            'transaction_id': 'TX126',
            'expected_time': datetime.datetime(2023, 10, 20, 10, 0),
            'actual_time': datetime.datetime(2023, 10, 20, 14, 0)
        }
    ]

    # Check for transaction delays
    result = check_transaction_delays(transactions)
    for item in result:
        print(item)
```
