"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintrends.org
Prompt: Write a script to generate alerts for forex market highlights, incorporating features similar to FinTrends' Market Highlights TV.
Generated: DETERMINISTIC_2d95c96d106cd031
Batch ID: 20250612_145924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.forexdata.com/market-highlights": {
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
from datetime import datetime

# Constants
API_URL = "https://api.forexdata.com/market-highlights"  # Replace with actual API URL
API_KEY = "your_api_key_here"  # Replace with your API key
ALERT_THRESHOLD = 0.5  # Example threshold for generating alerts (e.g., 0.5%)

# Function to fetch market highlights from the API
def fetch_market_highlights(api_url, api_key):
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching market highlights: {e}")
        return None

# Function to check for significant changes and generate alerts
def generate_alerts(highlights, threshold):
    alerts = []
    for highlight in highlights:
        try:
            # Extract relevant data
            currency_pair = highlight.get("currency_pair", "Unknown")
            change_percentage = highlight.get("change_percentage", 0)

            # Check if the change exceeds the threshold
            if abs(change_percentage) >= threshold:
                alert_message = (
                    f"ALERT: {currency_pair} has moved by {change_percentage:.2f}%."
                )
                alerts.append(alert_message)
        except (TypeError, ValueError) as e:
            print(f"Error processing highlight data: {e}")
            continue

    return alerts

# Main function
def main():
    print("Fetching Forex market highlights...")
    highlights = fetch_market_highlights(API_URL, API_KEY)

    if highlights:
        print("Processing highlights for alerts...")
        alerts = generate_alerts(highlights, ALERT_THRESHOLD)

        if alerts:
            print("\nGenerated Alerts:")
            for alert in alerts:
                print(alert)
        else:
            print("No significant changes detected.")
    else:
        print("Failed to fetch market highlights.")

# Entry point
if __name__ == "__main__":
    try:
        print(f"Script started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        main()
        print(f"Script completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

Note: Replace `API_URL` and `API_KEY` with actual values for your Forex data provider. Also, ensure the provider's response structure aligns with the parsing logic used here.
