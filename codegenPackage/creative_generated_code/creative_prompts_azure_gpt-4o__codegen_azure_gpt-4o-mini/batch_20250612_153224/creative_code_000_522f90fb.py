"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Write a Python script to automate the collection of marketing campaign performance metrics, including reach and engagement, for small and medium-sized businesses in the agricultural sector. Use APIs or libraries suitable for social media platforms like Instagram or Facebook.
Generated: DETERMINISTIC_522f90fb803684cc
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v12.0": {
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
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for API access
FACEBOOK_GRAPH_API_URL = 'https://graph.facebook.com/v12.0'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'  # Replace with your Facebook access token
PAGE_ID = 'YOUR_PAGE_ID'  # Replace with your Facebook Page ID

def get_facebook_insights(page_id, access_token):
    """
    Retrieves Facebook insights metrics for the specified page.

    Args:
        page_id (str): The ID of the Facebook page.
        access_token (str): The access token for Facebook API.

    Returns:
        dict: A dictionary containing reach and engagement metrics.
    """
    try:
        # Define the endpoint and parameters for the API call
        endpoint = f"{FACEBOOK_GRAPH_API_URL}/{page_id}/insights"
        params = {
            'metric': 'page_engaged_users,page_impressions',
            'access_token': access_token,
            'period': 'day',
            'since': (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'),  # Last 7 days
            'until': datetime.now().strftime('%Y-%m-%d')
        }

        # Make the API call
        response = requests.get(endpoint, params=params)

        # Check for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        insights = response.json()
        logging.info("Successfully retrieved Facebook insights.")
        return insights

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")

    return None

def main():
    """
    Main function to execute the performance metrics collection.
    """
    logging.info("Starting the marketing campaign performance metrics collection.")

    # Retrieve metrics from Facebook
    insights = get_facebook_insights(PAGE_ID, ACCESS_TOKEN)

    if insights:
        logging.info("Collected metrics successfully.")
        # Process and display the insights here
        for metric in insights.get('data', []):
            logging.info(f"Metric: {metric['name']}, Value: {metric['values']}")
    else:
        logging.error("Failed to collect metrics.")

if __name__ == "__main__":
    main()
```

Make sure to replace `YOUR_ACCESS_TOKEN` and `YOUR_PAGE_ID` with your actual Facebook API access token and the page ID you wish to query.
