"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ideo-marketing.fr
Prompt: Write a script that automates the collection of marketing data as described on IDEO Marketing's site.
Generated: DETERMINISTIC_f0232e903c56f4b3
Batch ID: 20250612_164206
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.ideomarketing.com/api/marketing-data": {
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
import csv
from datetime import datetime

# Define constants for the script
IDEO_MARKETING_URL = "https://www.ideomarketing.com/api/marketing-data"
OUTPUT_FILE = "marketing_data.csv"
REQUEST_TIMEOUT = 10  # Timeout for API requests in seconds

# Function to fetch marketing data from IDEO Marketing's API
def fetch_marketing_data():
    try:
        # Send GET request to IDEO Marketing's API
        response = requests.get(IDEO_MARKETING_URL, timeout=REQUEST_TIMEOUT)
        # Raise exception if the response is not successful
        response.raise_for_status()
        
        # Parse the JSON data from the response
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        # Log error and exit if a network-related or HTTP error occurs
        print(f"Error fetching marketing data: {e}")
        return None

# Function to save marketing data to a CSV file
def save_to_csv(data):
    try:
        # Extract headers from the data keys (assuming a list of dictionaries)
        headers = data[0].keys() if data else []
        
        # Open CSV file for writing
        with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            
            # Write headers to the CSV file
            writer.writeheader()
            
            # Write rows to the CSV file
            writer.writerows(data)
        
        print(f"Marketing data successfully saved to {OUTPUT_FILE}")
    except Exception as e:
        # Log error if there is an issue saving the file
        print(f"Error saving data to CSV: {e}")

# Main entry point of the script
def main():
    print("Starting data collection...")
    
    # Fetch marketing data
    marketing_data = fetch_marketing_data()
    
    # If data is fetched successfully, save it to CSV
    if marketing_data:
        save_to_csv(marketing_data)
    else:
        print("No data to save. Exiting...")

    print("Data collection completed.")

# Only execute the script if it's run directly
if __name__ == "__main__":
    main()
```

**Notes:**
- Replace `IDEO_MARKETING_URL` with the actual API endpoint provided by IDEO Marketing's site.
- Ensure the API endpoint supports JSON responses compatible with this script format.
- The script assumes the API returns a list of dictionaries, with each dictionary representing a record in the data.
- This code is designed to be clean, efficient, and production-ready, adhering to the principles of error handling, modular design, and best practices.
