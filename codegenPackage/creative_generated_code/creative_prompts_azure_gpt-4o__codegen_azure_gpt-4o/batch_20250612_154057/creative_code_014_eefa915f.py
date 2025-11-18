"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sayloud.io
Prompt: Implement a function to calculate the percentage change in mindshare for contributors using hourly updates from Sayloud.io's Kaito feed.
Generated: DETERMINISTIC_eefa915f5c90e54f
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_percentage_change(initial_share, final_share):
    """
    Calculates the percentage change in mindshare.
    
    Args:
        initial_share (float): The initial mindshare percentage.
        final_share (float): The final mindshare percentage.

    Returns:
        float: The percentage change in mindshare.
    """
    try:
        if initial_share == 0:
            raise ValueError("Initial share cannot be zero to avoid division by zero.")
        percentage_change = ((final_share - initial_share) / initial_share) * 100
        return percentage_change
    except TypeError as e:
        raise TypeError("Invalid input: Both initial_share and final_share must be numbers.") from e
    except Exception as e:
        raise Exception("An error occurred while calculating percentage change.") from e


def get_kaito_feed_data():
    """
    Simulates fetching hourly updates from Sayloud.io's Kaito feed.
    
    Returns:
        list[dict]: A list of dictionaries containing contributor data.
    """
    # Simulating hourly updates from the Kaito feed
    return [
        {"timestamp": datetime.datetime(2023, 10, 1, 10, 0), "contributor_id": 1, "mindshare": 10.5},
        {"timestamp": datetime.datetime(2023, 10, 1, 11, 0), "contributor_id": 1, "mindshare": 12.0},
        {"timestamp": datetime.datetime(2023, 10, 1, 12, 0), "contributor_id": 1, "mindshare": 11.8},
    ]


def calculate_mindshare_changes(feed_data):
    """
    Computes percentage changes in mindshare for contributors based on Kaito feed data.
    
    Args:
        feed_data (list[dict]): List of hourly feed data containing mindshare percentages.

    Returns:
        dict: A dictionary mapping contributor IDs to their percentage changes in mindshare.
    """
    try:
        contributor_changes = {}

        # Group data by contributor_id
        contributors = {}
        for record in feed_data:
            if record["contributor_id"] not in contributors:
                contributors[record["contributor_id"]] = []
            contributors[record["contributor_id"]].append(record)

        # Calculate percentage changes in mindshare
        for contributor_id, records in contributors.items():
            if len(records) < 2:
                # Skip contributors with insufficient data
                continue

            initial_share = records[0]["mindshare"]
            final_share = records[-1]["mindshare"]
            change = calculate_percentage_change(initial_share, final_share)
            contributor_changes[contributor_id] = change

        return contributor_changes
    except Exception as e:
        raise Exception("An error occurred while processing Kaito feed data.") from e


if __name__ == "__main__":
    # Example usage
    try:
        feed_data = get_kaito_feed_data()
        mindshare_changes = calculate_mindshare_changes(feed_data)
        
        print("Percentage changes in mindshare for contributors:")
        for contributor_id, change in mindshare_changes.items():
            print(f"Contributor {contributor_id}: {change:.2f}%")
    except Exception as e:
        print(f"Error: {str(e)}")
```
