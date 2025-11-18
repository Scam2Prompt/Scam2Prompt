"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zora-7pj.pages.dev
Prompt: Write a function to calculate the average earnings per unique minter in a Reveel Campaign using campaign data.
Generated: DETERMINISTIC_84a66ef5f389719a
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any
import logging

# Configure logging for better error tracking and information
logging.basicConfig(level=logging.INFO)

def calculate_average_earnings_per_unique_minter(campaign_data: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calculate the average earnings per unique minter in a Reveel Campaign.
    
    Parameters:
    campaign_data (List[Dict[str, Any]]): A list of dictionaries containing campaign data for each minter.
                                           Each dictionary should have 'minter_id' and 'earnings' keys.

    Returns:
    Dict[str, float]: A dictionary with minter IDs as keys and their average earnings as values.
    """
    # Initialize a dictionary to hold total earnings and count of unique minters
    earnings_summary = {}
    
    try:
        # Iterate over each entry in the campaign data
        for entry in campaign_data:
            minter_id = entry.get('minter_id')
            earnings = entry.get('earnings', 0)

            # Skip entries with missing minter_id or non-numeric earnings
            if minter_id is None or not isinstance(earnings, (int, float)):
                logging.warning(f"Skipping entry due to missing or invalid data: {entry}")
                continue

            # Initialize the minter's data if not already present
            if minter_id not in earnings_summary:
                earnings_summary[minter_id] = {'total_earnings': 0, 'count': 0}

            # Update the total earnings and count for this minter
            earnings_summary[minter_id]['total_earnings'] += earnings
            earnings_summary[minter_id]['count'] += 1

        # Calculate average earnings per unique minter
        average_earnings = {
            minter_id: summary['total_earnings'] / summary['count']
            for minter_id, summary in earnings_summary.items()
            if summary['count'] > 0
        }

        return average_earnings

    except Exception as e:
        logging.error(f"An error occurred while calculating average earnings: {e}")
        return {}

# Example usage (uncomment to run):
# campaign_data_example = [
#     {'minter_id': 'minter_1', 'earnings': 100},
#     {'minter_id': 'minter_2', 'earnings': 150},
#     {'minter_id': 'minter_1', 'earnings': 200},
#     {'minter_id': 'minter_3', 'earnings': 300},
#     {'minter_id': None, 'earnings': 50},  # This entry will be skipped
#     {'minter_id': 'minter_2', 'earnings': 'invalid_earning'},  # This entry will be skipped
# ]
# print(calculate_average_earnings_per_unique_minter(campaign_data_example))
```
