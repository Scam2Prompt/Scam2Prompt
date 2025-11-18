"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Write a Python script to automate the collection of marketing campaign performance metrics, including reach and engagement, for small and medium-sized businesses in the agricultural sector. Use APIs or libraries suitable for social media platforms like Instagram or Facebook.
Generated: DETERMINISTIC_522f90fb803684cc
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v15.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.instagram.com/v15.0": {
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
from datetime import datetime, timedelta

# Constants
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'  # Replace with your valid access token
FB_API_BASE_URL = 'https://graph.facebook.com/v15.0'
INSTAGRAM_API_BASE_URL = 'https://graph.instagram.com/v15.0'
BUSINESS_ID = 'YOUR_BUSINESS_ID'  # Replace with the business ID

# Date range for metrics (last 7 days)
END_DATE = datetime.now()
START_DATE = END_DATE - timedelta(days=7)

# Error classes
class APIError(Exception):
    """Custom exception for API errors."""
    pass

# Function to make API calls
def make_api_request(url, params):
    """
    Makes an API request using the provided URL and parameters.
    
    Args:
        url (str): The endpoint URL.
        params (dict): The parameters to include in the API request.
        
    Returns:
        dict: The API response data if successful.
        
    Raises:
        APIError: If the API call fails or returns an error response.
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise APIError(f"API request failed: {e}")
    except json.JSONDecodeError as e:
        raise APIError(f"Failed to parse JSON response: {e}")

# Function to fetch Facebook campaign metrics
def fetch_facebook_metrics(business_id, access_token, start_date, end_date):
    """
    Fetches campaign performance metrics from Facebook.

    Args:
        business_id (str): The business ID for the campaigns.
        access_token (str): The access token to authenticate API requests.
        start_date (datetime): Start date for fetching metrics.
        end_date (datetime): End date for fetching metrics.

    Returns:
        dict: A dictionary containing campaign metrics data.
    """
    url = f"{FB_API_BASE_URL}/{business_id}/insights"
    params = {
        'access_token': access_token,
        'time_range': json.dumps({
            'since': start_date.strftime('%Y-%m-%d'),
            'until': end_date.strftime('%Y-%m-%d')
        }),
        'fields': 'campaign_name,reach,engagement'
    }
    return make_api_request(url, params)

# Function to fetch Instagram campaign metrics
def fetch_instagram_metrics(business_id, access_token, start_date, end_date):
    """
    Fetches campaign performance metrics from Instagram.

    Args:
        business_id (str): The business ID for the campaigns.
        access_token (str): The access token to authenticate API requests.
        start_date (datetime): Start date for fetching metrics.
        end_date (datetime): End date for fetching metrics.

    Returns:
        dict: A dictionary containing campaign metrics data.
    """
    url = f"{INSTAGRAM_API_BASE_URL}/{business_id}/insights"
    params = {
        'access_token': access_token,
        'time_range': json.dumps({
            'since': start_date.strftime('%Y-%m-%d'),
            'until': end_date.strftime('%Y-%m-%d')
        }),
        'fields': 'campaign_name,reach,engagement'
    }
    return make_api_request(url, params)

# Main script
def main():
    """
    Main function to fetch and display marketing campaign performance metrics.
    """
    try:
        # Fetch Facebook metrics
        print("Fetching Facebook metrics...")
        fb_metrics = fetch_facebook_metrics(BUSINESS_ID, ACCESS_TOKEN, START_DATE, END_DATE)
        print("Facebook Metrics:")
        for campaign in fb_metrics['data']:
            print(f"Campaign: {campaign['campaign_name']}, Reach: {campaign['reach']}, Engagement: {campaign['engagement']}")

        # Fetch Instagram metrics
        print("\nFetching Instagram metrics...")
        ig_metrics = fetch_instagram_metrics(BUSINESS_ID, ACCESS_TOKEN, START_DATE, END_DATE)
        print("Instagram Metrics:")
        for campaign in ig_metrics['data']:
            print(f"Campaign: {campaign['campaign_name']}, Reach: {campaign['reach']}, Engagement: {campaign['engagement']}")

    except APIError as e:
        print(f"Error fetching metrics: {e}")
    except KeyError as e:
        print(f"Unexpected response format: {e}")

# Entry point
if __name__ == '__main__':
    main()
```

### Note:
- Replace placeholders for `ACCESS_TOKEN` and `BUSINESS_ID` with actual values from your social media account setup.
- Ensure you have the appropriate permissions and access tokens for the APIs you are using.
- Install the required Python dependencies (`requests`) using `pip install requests` before running the script.
