"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jamcards.io
Prompt: Generate code in Python to analyze the activity of the "Heart Full of Love JamCards" collection, including the number of unique owners and the percentage of listed items.
Generated: DETERMINISTIC_3d66883ae0462bbd
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def analyze_heart_full_of_love_collection(data):
    """
    Analyzes the "Heart Full of Love JamCards" collection.

    Args:
        data (list): List of items in the collection. Each item is a dictionary containing
                     attributes like 'owner' and 'is_listed'.

    Returns:
        dict: Analysis results including:
              - Total items
              - Number of unique owners
              - Percentage of listed items
    """
    # Error handling for incorrect data types
    if not isinstance(data, list):
        raise ValueError("Invalid input. Expected a list of collection items.")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Invalid input. Each item must be a dictionary.")

    # Calculate total items
    total_items = len(data)

    # Extract unique owners
    owners = {item.get('owner') for item in data if 'owner' in item and item.get('owner')}
    unique_owners_count = len(owners)

    # Calculate percentage of listed items
    listed_items_count = sum(1 for item in data if item.get('is_listed', False))
    percentage_listed = (listed_items_count / total_items * 100) if total_items > 0 else 0

    # Return the analysis results
    return {
        "Total Items": total_items,
        "Unique Owners": unique_owners_count,
        "Percentage Listed": round(percentage_listed, 2)
    }

# Example usage
if __name__ == "__main__":
    # Example collection data (replace with actual data)
    example_data = [
        {"owner": "User1", "is_listed": True},
        {"owner": "User2", "is_listed": False},
        {"owner": "User1", "is_listed": True},
        {"owner": "User3", "is_listed": True},
    ]

    try:
        # Analyze the collection
        results = analyze_heart_full_of_love_collection(example_data)

        # Print the results in JSON format for clarity
        print(json.dumps(results, indent=4))
    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```
