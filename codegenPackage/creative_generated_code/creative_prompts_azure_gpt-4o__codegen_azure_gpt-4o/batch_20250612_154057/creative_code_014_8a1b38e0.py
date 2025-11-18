"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwstayloud.io
Prompt: Write a script to calculate the percentage change in mindshare for Loud contributors based on hourly updates from the Kaito feed.
Generated: DETERMINISTIC_8a1b38e04a21216a
Batch ID: 20250612_154057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://kaito-feed.example.com/hourly-updates": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import datetime

def fetch_kaito_feed():
    """
    Fetches hourly updates from the Kaito feed.
    Returns:
        list of dict: A list of records with contributor data including mindshare.
    Raises:
        Exception: If the feed cannot be fetched or the response is invalid.
    """
    try:
        # Replace with the actual Kaito feed URL
        feed_url = "https://kaito-feed.example.com/hourly-updates"
        response = requests.get(feed_url)
        response.raise_for_status()  # Raise an error for HTTP request issues
        data = response.json()
        if not isinstance(data, list):
            raise ValueError("Invalid feed format: expected a list of records.")
        return data
    except Exception as e:
        print(f"Error fetching Kaito feed: {e}")
        raise

def calculate_percentage_change(old_value, new_value):
    """
    Calculates the percentage change between two values.
    Args:
        old_value (float): The previous value.
        new_value (float): The updated value.
    Returns:
        float: Percentage change from old_value to new_value.
    """
    try:
        if old_value == 0:
            return float('inf')  # Infinite change if old_value is zero
        return ((new_value - old_value) / abs(old_value)) * 100
    except Exception as e:
        print(f"Error calculating percentage change: {e}")
        raise

def process_mindshare_updates(feed_data):
    """
    Processes mindshare updates for Loud contributors and calculates percentage change.
    Args:
        feed_data (list of dict): Input feed data containing mindshare information.
    Returns:
        dict: Contributors with their name and percentage change in mindshare.
    """
    try:
        changes = {}
        for record in feed_data:
            if record.get("contributor") == "Loud":
                old_mindshare = record.get("previous_mindshare")
                new_mindshare = record.get("current_mindshare")
                
                if old_mindshare is None or new_mindshare is None:
                    raise ValueError("Missing mindshare values for a contributor.")

                percentage_change = calculate_percentage_change(old_mindshare, new_mindshare)
                changes[record["name"]] = percentage_change
        return changes
    except Exception as e:
        print(f"Error processing mindshare updates: {e}")
        raise

def main():
    """
    Main function to fetch the Kaito feed, process mindshare updates,
    and display the percentage change for Loud contributors.
    """
    try:
        print("Fetching Kaito feed...")
        feed_data = fetch_kaito_feed()

        print("Processing mindshare updates...")
        changes = process_mindshare_updates(feed_data)

        print("Percentage change in mindshare for Loud contributors:")
        for name, change in changes.items():
            print(f"{name}: {change:.2f}%")
    except Exception as e:
        print(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    main()
```
