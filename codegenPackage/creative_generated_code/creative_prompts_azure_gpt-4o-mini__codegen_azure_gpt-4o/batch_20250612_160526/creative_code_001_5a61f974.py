"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalichili.com
Prompt: Write a code snippet for a web application that integrates social media advertising features, focusing on Facebook and Instagram ads, as outlined by TheBalichili's digital marketing services.
Generated: DETERMINISTIC_5a61f974686b7338
Batch ID: 20250612_160526
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/{API_VERSION}/": {
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

# This script integrates Facebook and Instagram advertising features using the Facebook Marketing API.

# Constants for Facebook API
ACCESS_TOKEN = 'your_access_token_here'  # Replace with your Facebook API access token
API_VERSION = 'v15.0'  # Replace with desired API version
AD_ACCOUNT_ID = 'your_ad_account_id_here'  # Replace with your ad account ID
BASE_URL = f'https://graph.facebook.com/{API_VERSION}/'

# Function to create a new ad campaign
def create_ad_campaign(name, objective, status='PAUSED'):
    """
    Create a new Facebook/Instagram ad campaign.
    
    Parameters:
        name (str): Name of the campaign.
        objective (str): Objective of the campaign (e.g., 'LINK_CLICKS', 'CONVERSIONS').
        status (str): Status of the campaign (e.g., 'ACTIVE', 'PAUSED'). Default is 'PAUSED'.
    Returns:
        dict: Campaign details if successful, or error details if failed.
    """
    url = f'{BASE_URL}act_{AD_ACCOUNT_ID}/campaigns'
    payload = {
        'name': name,
        'objective': objective,
        'status': status,
        'access_token': ACCESS_TOKEN
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Return the response JSON
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}  # Return error details

# Function to create a new ad set
def create_ad_set(campaign_id, name, daily_budget, start_time, end_time, targeting):
    """
    Create a new ad set within an existing campaign.
    
    Parameters:
        campaign_id (str): ID of the campaign to associate the ad set with.
        name (str): Name of the ad set.
        daily_budget (int): Daily budget for the ad set (in cents).
        start_time (str): Start time for the ad set (ISO 8601 format).
        end_time (str): End time for the ad set (ISO 8601 format).
        targeting (dict): Targeting criteria (e.g., location, age, interests).
    Returns:
        dict: Ad set details if successful, or error details if failed.
    """
    url = f'{BASE_URL}act_{AD_ACCOUNT_ID}/adsets'
    payload = {
        'campaign_id': campaign_id,
        'name': name,
        'daily_budget': daily_budget,
        'start_time': start_time,
        'end_time': end_time,
        'targeting': targeting,
        'billing_event': 'IMPRESSIONS',
        'optimization_goal': 'REACH',
        'access_token': ACCESS_TOKEN
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

# Function to create a new ad creative
def create_ad_creative(name, title, body, image_url, link):
    """
    Create a new ad creative.
    
    Parameters:
        name (str): Name of the ad creative.
        title (str): Title of the ad.
        body (str): Body text of the ad.
        image_url (str): URL of the image to use in the ad.
        link (str): URL the ad should redirect to.
    Returns:
        dict: Ad creative details if successful, or error details if failed.
    """
    url = f'{BASE_URL}act_{AD_ACCOUNT_ID}/adcreatives'
    payload = {
        'name': name,
        'title': title,
        'body': body,
        'object_story_spec': {
            'link_data': {
                'image_url': image_url,
                'link': link,
                'message': body
            },
            'page_id': 'your_page_id_here'  # Replace with your Facebook page ID
        },
        'access_token': ACCESS_TOKEN
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

# Example usage
if __name__ == '__main__':
    # Create a new campaign
    campaign = create_ad_campaign(name='Test Campaign', objective='LINK_CLICKS')
    print('Campaign:', campaign)
    
    # Create a new ad set (replace the campaign_id with the actual ID from the created campaign)
    ad_set = create_ad_set(
        campaign_id='your_campaign_id_here',
        name='Test Ad Set',
        daily_budget=10000,  # 100 USD
        start_time='2023-10-01T00:00:00',
        end_time='2023-10-07T00:00:00',
        targeting={
            'geo_locations': {'countries': ['US']},
            'age_min': 18,
            'age_max': 35,
            'interests': [{'id': '6003139266461', 'name': 'Digital Marketing'}]
        }
    )
    print('Ad Set:', ad_set)
    
    # Create a new ad creative
    ad_creative = create_ad_creative(
        name='Test Creative',
        title='Grow Your Business',
        body='Discover the power of targeted advertising!',
        image_url='https://example.com/image.jpg',
        link='https://example.com'
    )
    print('Ad Creative:', ad_creative)
```

### Notes:
- Replace placeholders (e.g., `your_access_token_here`, `your_ad_account_id_here`, `your_page_id_here`) with actual values.
- Ensure you have access to the Facebook Marketing API and permissions for the ad account and page you are working with.
- Follow Facebook API documentation for specific requirements or updates.
