"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdexdoc.gitbook.io
Prompt: Write a Python script to monitor the repurchase and burn activity of MDX tokens on MDEX and display the total burned tokens over time.
Generated: DETERMINISTIC_0fd8f85dd17eb159
Batch ID: 20250612_145823
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mdex.com/statistics/tokenBurn": {
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
import time
import logging

# Configure logging for monitoring the script
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Constants
API_URL = "https://api.mdex.com/statistics/tokenBurn"  # Replace with the actual API endpoint if different
POLL_INTERVAL = 60  # Time interval in seconds to check the API

# Function to fetch token burn data from MDEX API
def fetch_burn_data():
    try:
        response = requests.get(API_URL, timeout=10)  # Timeout for handling network delays
        response.raise_for_status()  # Raise an error for HTTP response codes >= 400
        data = response.json()  # Parse JSON response
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from API: {e}")
        return None

# Main function to monitor token burn activity
def monitor_mdex_burn():
    total_burned_tokens = 0  # Counter to track the total number of tokens burned

    while True:
        logging.info("Fetching burn data...")
        burn_data = fetch_burn_data()

        if burn_data:
            try:
                # Extract burn amount from the fetched data
                burned_tokens = float(burn_data.get("burnedTokens", 0))
                total_burned_tokens += burned_tokens

                # Log the current and total burned tokens
                logging.info(f"Current burn: {burned_tokens} MDX tokens")
                logging.info(f"Total burned tokens: {total_burned_tokens} MDX tokens")
            except (ValueError, TypeError) as e:
                logging.error(f"Error processing burn data: {e}")
        else:
            logging.warning("No data received. Retrying in the next interval.")

        # Wait for the next poll interval
        time.sleep(POLL_INTERVAL)

# Entry point for the script
if __name__ == "__main__":
    try:
        logging.info("Starting MDEX token burn monitor...")
        monitor_mdex_burn()
    except KeyboardInterrupt:
        logging.info("Monitor stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
