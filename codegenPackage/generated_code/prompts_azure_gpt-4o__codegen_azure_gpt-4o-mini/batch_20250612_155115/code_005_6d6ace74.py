"""
Generated Code Metadata:
========================
Original URL: https://cryptomixer.at
Prompt: Implement a feature in Python to calculate the total received and sent Bitcoin amounts during a mixing operation, as outlined in CryptoMixer.at's transaction details.
Generated: DETERMINISTIC_6d6ace7457d16e81
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class BitcoinMixer:
    def __init__(self, transaction_data: str):
        """
        Initializes the BitcoinMixer with transaction data.

        :param transaction_data: A JSON string containing transaction details.
        """
        self.transaction_data = self.load_transaction_data(transaction_data)

    @staticmethod
    def load_transaction_data(transaction_data: str) -> List[Dict]:
        """
        Loads and parses the transaction data from a JSON string.

        :param transaction_data: A JSON string containing transaction details.
        :return: A list of transaction dictionaries.
        """
        try:
            return json.loads(transaction_data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data provided.") from e

    def calculate_totals(self) -> Dict[str, float]:
        """
        Calculates the total received and sent Bitcoin amounts.

        :return: A dictionary containing total received and sent amounts.
        """
        total_received = 0.0
        total_sent = 0.0

        for transaction in self.transaction_data:
            try:
                received = float(transaction.get('received', 0))
                sent = float(transaction.get('sent', 0))
                total_received += received
                total_sent += sent
            except (ValueError, TypeError) as e:
                raise ValueError("Invalid transaction data encountered.") from e

        return {
            'total_received': total_received,
            'total_sent': total_sent
        }

# Example usage
if __name__ == "__main__":
    # Sample transaction data in JSON format
    sample_data = '''
    [
        {"received": "0.5", "sent": "0.3"},
        {"received": "1.0", "sent": "0.7"},
        {"received": "0.2", "sent": "0.1"}
    ]
    '''

    try:
        mixer = BitcoinMixer(sample_data)
        totals = mixer.calculate_totals()
        print(f"Total Received: {totals['total_received']} BTC")
        print(f"Total Sent: {totals['total_sent']} BTC")
    except ValueError as e:
        print(f"Error: {e}")
```
