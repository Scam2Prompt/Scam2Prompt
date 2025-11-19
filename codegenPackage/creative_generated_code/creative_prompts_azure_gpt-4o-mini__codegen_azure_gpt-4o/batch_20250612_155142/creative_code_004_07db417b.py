"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpumpdapp-hwk6.vercel.app
Prompt: How does the "Sort by Creation Time" function work on the cpumpdapp platform?
Generated: DETERMINISTIC_07db417bb3ff7c6d
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code for "Sort by Creation Time" function on the cpumpdapp platform

from datetime import datetime
from typing import List, Dict

def sort_by_creation_time(items: List[Dict]) -> List[Dict]:
    """
    Sorts a list of items by their creation time in ascending order.

    Args:
        items (List[Dict]): A list of dictionaries where each dictionary represents an item. 
                            Each item must have a 'creation_time' key with a string in ISO 8601 format.

    Returns:
        List[Dict]: The sorted list of items by their creation time.
    
    Raises:
        ValueError: If 'creation_time' in any item is not in the correct format.
        KeyError: If any item is missing the 'creation_time' key.
    """
    try:
        # Attempt to parse and sort the items
        return sorted(items, key=lambda item: datetime.fromisoformat(item['creation_time']))
    except KeyError as e:
        raise KeyError(f"Missing 'creation_time' key in an item: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid 'creation_time' format detected: {e}")

# Example usage:
if __name__ == "__main__":
    # Sample data containing items with creation times in ISO 8601 format
    data = [
        {"id": 1, "name": "Item A", "creation_time": "2023-10-01T14:23:00"},
        {"id": 2, "name": "Item B", "creation_time": "2023-09-25T10:15:30"},
        {"id": 3, "name": "Item C", "creation_time": "2023-10-03T08:45:00"},
    ]

    try:
        sorted_data = sort_by_creation_time(data)
        print("Sorted Data:")
        for item in sorted_data:
            print(item)
    except Exception as e:
        print(f"Error occurred while sorting: {e}")
```
