"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ldkfjslkjfklsdjfs.pages.dev
Prompt: Create a function to sort airdrops by "Newest first" and "Ending soon" from the data provided on AirdropAlert.com.
Generated: DETERMINISTIC_a7d50ea2b03d7fb3
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime

def sort_airdrops(airdrops, sort_type):
    """
    Sort airdrops based on the specified criteria.

    Parameters:
        airdrops (list of dict): List of airdrop data, where each airdrop is a dictionary with keys:
            - 'name': Name of the airdrop (str)
            - 'start_date': Start date of the airdrop (ISO format string, e.g., '2023-01-01')
            - 'end_date': End date of the airdrop (ISO format string, e.g., '2023-02-01')
        sort_type (str): Sorting criteria. Allowed values are:
            - 'newest_first': Sort by newest start date first
            - 'ending_soon': Sort by nearest end date first

    Returns:
        list of dict: Sorted list of airdrops.
    """
    try:
        # Validate sort_type
        if sort_type not in ['newest_first', 'ending_soon']:
            raise ValueError("Invalid sort_type. Must be 'newest_first' or 'ending_soon'.")

        # Convert date strings to datetime objects for sorting
        for airdrop in airdrops:
            airdrop['start_date'] = datetime.strptime(airdrop['start_date'], '%Y-%m-%d')
            airdrop['end_date'] = datetime.strptime(airdrop['end_date'], '%Y-%m-%d')

        # Sort based on sort_type
        if sort_type == 'newest_first':
            sorted_airdrops = sorted(airdrops, key=lambda x: x['start_date'], reverse=True)
        elif sort_type == 'ending_soon':
            sorted_airdrops = sorted(airdrops, key=lambda x: x['end_date'])

        # Convert datetime objects back to strings for output consistency
        for airdrop in sorted_airdrops:
            airdrop['start_date'] = airdrop['start_date'].strftime('%Y-%m-%d')
            airdrop['end_date'] = airdrop['end_date'].strftime('%Y-%m-%d')

        return sorted_airdrops

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return []

# Example usage
airdrops_data = [
    {'name': 'Airdrop1', 'start_date': '2023-09-01', 'end_date': '2023-10-01'},
    {'name': 'Airdrop2', 'start_date': '2023-08-15', 'end_date': '2023-09-30'},
    {'name': 'Airdrop3', 'start_date': '2023-09-10', 'end_date': '2023-09-25'}
]

sorted_by_newest = sort_airdrops(airdrops_data, 'newest_first')
print("Sorted by Newest First:", sorted_by_newest)

sorted_by_ending_soon = sort_airdrops(airdrops_data, 'ending_soon')
print("Sorted by Ending Soon:", sorted_by_ending_soon)
```
