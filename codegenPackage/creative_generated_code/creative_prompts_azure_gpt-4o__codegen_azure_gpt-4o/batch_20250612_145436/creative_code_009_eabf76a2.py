"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Write a Python script to track user engagement and subscription growth for a YouTube channel, similar to Cody Alt's channel with 740k+ followers.
Generated: DETERMINISTIC_eabf76a2f0796891
Batch ID: 20250612_145436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/youtube/v3/channels": {
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
import json
import time
from datetime import datetime
from typing import Dict

# Constants
API_KEY = 'your_youtube_api_key_here'  # Replace with your YouTube Data API v3 key
CHANNEL_ID = 'target_channel_id_here'  # Replace with the YouTube channel ID to track
API_URL = 'https://www.googleapis.com/youtube/v3/channels'
POLL_INTERVAL = 3600  # Time in seconds to wait between data fetches (e.g., 1 hour)
LOG_FILE = 'youtube_channel_metrics.log'


def fetch_channel_data(api_key: str, channel_id: str) -> Dict:
    """
    Fetch the channel statistics from YouTube Data API.
    
    :param api_key: YouTube Data API v3 key
    :param channel_id: The ID of the YouTube channel to fetch data for
    :return: A dictionary containing the channel's statistics, or None if an error occurred
    """
    try:
        # Make API request
        response = requests.get(API_URL, params={
            'part': 'statistics',
            'id': channel_id,
            'key': api_key
        })
        
        # Raise an exception if the request failed
        response.raise_for_status()
        
        # Parse response JSON
        data = response.json()
        
        # Extract statistics
        if 'items' in data and len(data['items']) > 0:
            return data['items'][0]['statistics']
        else:
            return None  # Channel ID invalid or no data found
    except requests.RequestException as e:
        log_error(f"Error fetching channel data: {e}")
        return None
    except KeyError as e:
        log_error(f"Unexpected data structure: {e}")
        return None


def log_metrics(metrics: Dict):
    """
    Log channel metrics to a file with a timestamp.
    
    :param metrics: Dictionary of channel metrics
    """
    try:
        with open(LOG_FILE, 'a') as log_file:
            timestamp = datetime.now().isoformat()
            log_file.write(f"{timestamp} - {json.dumps(metrics)}\n")
    except IOError as e:
        log_error(f"Error writing to log file: {e}")


def log_error(message: str):
    """
    Log an error message to the console and the log file.
    
    :param message: Error message to log
    """
    print(f"ERROR: {message}")
    try:
        with open(LOG_FILE, 'a') as log_file:
            timestamp = datetime.now().isoformat()
            log_file.write(f"{timestamp} - ERROR: {message}\n")
    except IOError:
        print("Failed to write to log file.")


def main():
    """
    Main function to periodically fetch and log channel metrics.
    """
    print("Starting YouTube channel metrics tracker...")
    print(f"Polling every {POLL_INTERVAL} seconds.")
    
    while True:
        # Fetch channel data
        metrics = fetch_channel_data(API_KEY, CHANNEL_ID)
        
        if metrics:
            # Log metrics if successfully fetched
            print(f"Fetched metrics: {metrics}")
            log_metrics(metrics)
        else:
            # Log an error if metrics could not be fetched
            log_error("Failed to fetch channel metrics.")
        
        # Wait before the next poll
        time.sleep(POLL_INTERVAL)


if __name__ == '__main__':
    # Run the main function
    main()
```

### Notes:
- Replace `your_youtube_api_key_here` with a valid YouTube Data API v3 key, and `target_channel_id_here` with the desired channel's ID.
- This script writes logs to `youtube_channel_metrics.log`. Ensure the script has write permissions for the current directory.
- Install the `requests` library if not already installed: `pip install requests`.
