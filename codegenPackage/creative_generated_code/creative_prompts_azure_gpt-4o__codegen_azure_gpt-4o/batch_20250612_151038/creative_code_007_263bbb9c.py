"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordriomint.pages.dev
Prompt: Write a Python script to calculate the percentage of inscriptions held by the top 10 holders on Ord.io, using the rank and balance data provided.
Generated: DETERMINISTIC_263bbb9cbd3a75b3
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_top_10_percentage(data):
    """
    Calculate the percentage of inscriptions held by the top 10 holders.

    Parameters:
    - data (list of dict): A list of dictionaries containing rank and balance information.
                           Example: [{'rank': 1, 'balance': 1000}, {'rank': 2, 'balance': 800}, ...]

    Returns:
    - float: Percentage of inscriptions held by the top 10 holders.
    """
    try:
        # Ensure the data is a list of dictionaries
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Input data must be a list of dictionaries.")

        # Calculate the total balance of all holders
        total_balance = sum(item['balance'] for item in data if 'balance' in item and isinstance(item['balance'], (int, float)))

        if total_balance == 0:
            raise ValueError("Total balance of inscriptions cannot be zero.")

        # Sort data by rank and calculate the balance of top 10 holders
        top_10_balance = sum(item['balance'] for item in sorted(data, key=lambda x: x['rank'])[:10])

        # Calculate the percentage
        percentage = (top_10_balance / total_balance) * 100

        return round(percentage, 2)

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except KeyError as ke:
        print(f"KeyError: Missing keys in data - {ke}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example data (replace this with actual data from Ord.io)
    example_data = [
        {'rank': 1, 'balance': 1000},
        {'rank': 2, 'balance': 800},
        {'rank': 3, 'balance': 600},
        {'rank': 4, 'balance': 500},
        {'rank': 5, 'balance': 400},
        {'rank': 6, 'balance': 300},
        {'rank': 7, 'balance': 200},
        {'rank': 8, 'balance': 100},
        {'rank': 9, 'balance': 50},
        {'rank': 10, 'balance': 25},
        {'rank': 11, 'balance': 10},
        {'rank': 12, 'balance': 5},
    ]

    # Calculate the top 10 percentage
    result = calculate_top_10_percentage(example_data)

    # Print the result
    if result is not None:
        print(f"Top 10 holders hold {result}% of total inscriptions.")
```
