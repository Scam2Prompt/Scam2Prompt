"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarketscanner.com
Prompt: Develop a Python script that integrates with Polymarket Scanner to fetch and store aggregated poll data for further analysis.
Generated: DETERMINISTIC_00a723a73302408f
Batch ID: 20250612_150227
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polymarket.com/v1/markets": {
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
import os
from datetime import datetime

# Constants
API_ENDPOINT = "https://api.polymarket.com/v1/markets"
OUTPUT_FILE = "polymarket_data.json"

def fetch_polymarket_data():
    """
    Fetches aggregated poll data from Polymarket Scanner API.
    Returns the JSON response if successful.
    """
    try:
        response = requests.get(API_ENDPOINT)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Parse JSON and return
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Polymarket API: {e}")
        return None

def save_data_to_file(data, file_path):
    """
    Saves the fetched data into a local JSON file.
    If the file already exists, it appends a timestamp to create a new file.
    """
    try:
        if os.path.exists(file_path):
            # Append timestamp to avoid overwriting existing file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = f"{os.path.splitext(file_path)[0]}_{timestamp}{os.path.splitext(file_path)[1]}"
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to file: {e}")

def main():
    """
    Main function to integrate fetching and storing of Polymarket data.
    """
    print("Fetching data from Polymarket API...")
    data = fetch_polymarket_data()
    
    if data:
        print("Data fetched successfully. Saving to file...")
        save_data_to_file(data, OUTPUT_FILE)
    else:
        print("Failed to fetch or process data.")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
