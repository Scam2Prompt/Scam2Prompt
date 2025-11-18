"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcoins.net
Prompt: Develop a program that calculates the total earnings from Claimcoins.net's faucet payouts over a given time period using the provided payout history.
Generated: DETERMINISTIC_f05e1a19f93a5cd5
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate total earnings from Claimcoins.net's faucet payouts

# Import necessary modules
import json
from datetime import datetime

def parse_payout_history(payout_history):
    """
    Parses the payout history JSON and calculates total earnings over a given period.

    Args:
        payout_history (str): JSON string containing payout history.

    Returns:
        dict: Summary containing total earnings and number of payouts.
    """
    try:
        data = json.loads(payout_history)  # Parse JSON data
        total_earnings = 0.0
        total_payouts = 0
        
        for entry in data.get('payouts', []):
            # Extract and validate the necessary fields
            amount = entry.get('amount')
            timestamp = entry.get('timestamp')
            
            if amount is None or timestamp is None:
                continue
            
            try:
                # Convert timestamp to datetime object (assuming ISO 8601 format)
                entry_date = datetime.fromisoformat(timestamp)
            except ValueError:
                # Skip invalid timestamps
                continue
            
            # Add to totals
            total_earnings += float(amount)
            total_payouts += 1

        return {
            'total_earnings': round(total_earnings, 8),  # Round to 8 decimal places for cryptocurrency precision
            'total_payouts': total_payouts
        }
    except json.JSONDecodeError as e:
        # Handle invalid JSON input
        return {"error": f"Invalid JSON format: {str(e)}"}

# Example usage
if __name__ == '__main__':
    # Example payout history JSON
    payout_history_json = '''
    {
        "payouts": [
            {"amount": "0.00001234", "timestamp": "2023-01-01T12:00:00"},
            {"amount": "0.00001567", "timestamp": "2023-01-02T13:30:00"},
            {"amount": "0.00000987", "timestamp": "2023-01-03T14:45:00"}
        ]
    }
    '''
    
    # Calculate earnings
    summary = parse_payout_history(payout_history_json)
    
    # Output results
    if 'error' in summary:
        print(f"Error: {summary['error']}")
    else:
        print(f"Total Earnings: {summary['total_earnings']} Claimcoins")
        print(f"Total Payouts: {summary['total_payouts']}")
```
