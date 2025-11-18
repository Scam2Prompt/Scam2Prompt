"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sheout.vip
Prompt: Generate a script to filter and sort pop-up store listings by category or location, referencing the filters and sorting options mentioned on Sheout.vip.
Generated: DETERMINISTIC_cdcdf1331c45bab9
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_and_sort_stores(store_data, filters=None, sort_by=None):
    """
    Filters and sorts pop-up store listings based on category or location.
    
    Parameters:
        store_data (list): List of dictionaries containing store information.
        filters (dict): Dictionary containing filter criteria (e.g., {'category': 'Fashion', 'location': 'New York'}).
        sort_by (str): Key to sort the results by (e.g., 'category', 'location', or 'name').
    
    Returns:
        list: Filtered and sorted list of store dictionaries.
    """
    try:
        # Validate input
        if not isinstance(store_data, list):
            raise ValueError("store_data must be a list of dictionaries.")

        if filters and not isinstance(filters, dict):
            raise ValueError("filters must be a dictionary.")

        if sort_by and not isinstance(sort_by, str):
            raise ValueError("sort_by must be a string.")

        # Apply filters
        if filters:
            for key, value in filters.items():
                store_data = [
                    store for store in store_data if store.get(key, "").lower() == value.lower()
                ]

        # Sort data if requested
        if sort_by:
            store_data = sorted(store_data, key=lambda x: x.get(sort_by, "").lower())

        return store_data

    except Exception as e:
        print(f"Error occurred: {e}")
        return []

# Sample store data
store_data = [
    {"name": "Urban Trendy", "category": "Fashion", "location": "New York"},
    {"name": "Tech Bazaar", "category": "Technology", "location": "San Francisco"},
    {"name": "Artisan Alley", "category": "Art & Craft", "location": "New York"},
    {"name": "Gadget World", "category": "Technology", "location": "Chicago"},
]

# Filters and sorting options (example usage)
filters = {"category": "Technology", "location": "San Francisco"}
sort_by = "name"

filtered_and_sorted_stores = filter_and_sort_stores(store_data, filters, sort_by)

# Output the results
print(json.dumps(filtered_and_sorted_stores, indent=4))
```
