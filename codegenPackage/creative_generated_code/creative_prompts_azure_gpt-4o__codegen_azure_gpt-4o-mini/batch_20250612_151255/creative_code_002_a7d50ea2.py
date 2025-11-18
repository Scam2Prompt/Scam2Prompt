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
from typing import List, Dict, Any

def sort_airdrops(airdrops: List[Dict[str, Any]], sort_order: str) -> List[Dict[str, Any]]:
    """
    Sort the list of airdrops based on the specified sorting criteria.

    Parameters:
    airdrops (List[Dict[str, Any]]): The list of airdrop dictionaries to sort.
    sort_order (str): The sorting criteria, either 'newest' for Newest first or 'ending_soon' for Ending soon.

    Returns:
    List[Dict[str, Any]]: The sorted list of airdrops.

    Raises:
    ValueError: If the sort_order is not recognized.
    """
    
    # Validate the sort_order parameter
    if sort_order not in ['newest', 'ending_soon']:
        raise ValueError("sort_order must be either 'newest' or 'ending_soon'")

    try:
        if sort_order == 'newest':
            # Sort by the 'date' key in descending order for newest first
            return sorted(airdrops, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)
        
        elif sort_order == 'ending_soon':
            # Sort by the 'end_date' key in ascending order for ending soon
            return sorted(airdrops, key=lambda x: datetime.strptime(x['end_date'], '%Y-%m-%d'))

    except KeyError as e:
        raise KeyError(f"Missing expected key in airdrop entry: {e}")
    except ValueError as e:
        raise ValueError(f"Error parsing date: {e}")

# Example usage:
# airdrops_data = [
#     {'name': 'Airdrop 1', 'date': '2023-10-01', 'end_date': '2023-10-10'},
#     {'name': 'Airdrop 2', 'date': '2023-10-05', 'end_date': '2023-10-15'},
#     {'name': 'Airdrop 3', 'date': '2023-09-28', 'end_date': '2023-10-02'},
# ]
# sorted_airdrops = sort_airdrops(airdrops_data, 'newest')
# print(sorted_airdrops)
```
