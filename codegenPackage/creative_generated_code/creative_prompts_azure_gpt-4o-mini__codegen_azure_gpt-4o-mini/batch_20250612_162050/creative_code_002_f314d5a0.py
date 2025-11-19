"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://efficiencydigitalmarketing.com.br
Prompt: Generate a sample Facebook Ads campaign targeting specific demographics to boost lead generation, inspired by the strategies outlined on Efficiency Digital Marketing's website.
Generated: DETERMINISTIC_f314d5a0c7857c34
Batch ID: 20250612_162050
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

class FacebookAds:
    def __init__(self, access_token):
        """Initialize the FacebookAds with an access token."""
        self.base_url = 'https://graph.facebook.com/v12.0'
        self.access_token = access_token

    def create_campaign(self, account_id, campaign_name, objective):
        """Create a new ad campaign for the specified account."""
        url = f"{self.base_url}/act_{account_id}/campaigns"
        payload = {
            'name': campaign_name,
            'objective': objective,
            'status': 'ACTIVE',
            'access_token': self.access_token
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def create_ad_set(self, campaign_id, ad_set_name, targeting, daily_budget):
        """Create a new ad set under the specified campaign."""
        url = f"{self.base_url}/act_{campaign_id}/adsets"
        payload = {
            'name': ad_set_name,
            'campaign_id': campaign_id,
            'targeting': targeting,
            'daily_budget': daily_budget,
            'status': 'ACTIVE',
            'access_token': self.access_token
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def create_ad(self, ad_set_id, ad_name, creative):
        """Create a new ad under the specified ad set."""
        url = f"{self.base_url}/act_{ad_set_id}/ads"
        payload = {
            'name': ad_name,
            'adset_id': ad_set_id,
            'creative': creative,
            'status': 'ACTIVE',
            'access_token': self.access_token
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Usage example
if __name__ == "__main__":
    ACCESS_TOKEN = 'your_access_token_here'
    ACCOUNT_ID = 'your_ad_account_id_here'

    facebook_ads = FacebookAds(ACCESS_TOKEN)

    # Create a campaign
    campaign = facebook_ads.create_campaign(ACCOUNT_ID, "Lead Generation Campaign", "LEAD_GENERATION")
    if campaign:
        print("Campaign created:", campaign)

        # Define targeting parameters (example for illustrative purposes)
        targeting = {
            'geo_locations': {
                'countries': ['US'],
            },
            'age_min': 25,
            'age_max': 45,
            'genders': [1],  # 1 for male, 2 for female
        }

        # Create an ad set
        ad_set = facebook_ads.create_ad_set(campaign['id'], "Lead Gen Ad Set", targeting, 1000)
        if ad_set:
            print("Ad set created:", ad_set)

            # Create an ad creative (example creative ID, replace with actual)
            creative = {
                'creative_id': 'your_creative_id_here'
            }

            # Create an ad
            ad = facebook_ads.create_ad(ad_set['id'], "Lead Gen Ad", creative)
            if ad:
                print("Ad created:", ad)
```
