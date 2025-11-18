"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-started.pages.dev
Prompt: Create a function in Python to calculate the total points pledged to environmental charities based on Everyworld's payout data.
Generated: DETERMINISTIC_ca86520484720b3e
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

def calculate_total_points pledged(data: List[Dict[str, int]]) -> int:
    """
    Calculate the total points pledged to environmental charities.

    Parameters:
    data (List[Dict[str, int]]): A list of dictionaries containing charity data.
                                  Each dictionary should have a 'charity_type' key
                                  and a 'points' key.

    Returns:
    int: The total points pledged to environmental charities.
    """
    total_points = 0

    for entry in data:
        try:
            # Check if the required keys are present in the entry
            if 'charity_type' not in entry or 'points' not in entry:
                raise KeyError("Missing 'charity_type' or 'points' in entry")
            
            # Sum points only for environmental charities
            if entry['charity_type'].lower() == 'environmental':
                total_points += entry['points']
        
        except KeyError as e:
            print(f"Error: {e} in entry {entry}")
            continue  # Skip the current entry on error

    return total_points

# Example usage:
if __name__ == "__main__":
    # Sample data structure representing pledged points
    sample_data = [
        {"charity_type": "Environmental", "points": 100},
        {"charity_type": "Health", "points": 50},
        {"charity_type": "Environmental", "points": 200},
        {"charity_type": "Education", "points": 150}
    ]

    try:
        total = calculate_total_points_pledged(sample_data)
        print(f"Total points pledged to environmental charities: {total}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
