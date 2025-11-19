"""
Generated Code Metadata:
========================
Original URL: https://efficiencydigitalmarketing.com.br
Prompt: Generate a sample Facebook Ads campaign targeting specific demographics to boost lead generation, inspired by the strategies outlined on Efficiency Digital Marketing's website.
Generated: DETERMINISTIC_f314d5a0c7857c34
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import facebook
from facebook import GraphAPI
import pandas as pd

# Define Facebook API credentials
FACEBOOK_APP_ID = 'your_app_id'
FACEBOOK_APP_SECRET = 'your_app_secret'
FACEBOOK_ACCESS_TOKEN = 'your_access_token'

# Define campaign details
CAMPAIGN_NAME = 'Lead Generation Campaign'
CAMPAIGN_OBJECTIVE = 'LEAD'
TARGETING_GENDER = ['male', 'female']
TARGETING_AGE = [25, 45]
TARGETING_LOCATIONS = ['US', 'CA']

# Define lead ad form details
LEAD_AD_FORM_TITLE = 'Sign up for our newsletter'
LEAD_AD_FORM_DESCRIPTION = 'Get the latest updates from our company'
LEAD_AD_FORM_QUESTION1 = 'What is your name?'
LEAD_AD_FORM_QUESTION2 = 'What is your email address?'

def create_facebook_campaign(api, campaign_name, campaign_objective):
    try:
        # Create campaign
        campaign = api.create_campaign(
            name=campaign_name,
            objective=campaign_objective,
            status='active'
        )
        campaign_id = campaign['id']
        print(f'Campaign created with ID: {campaign_id}')
        return campaign_id
    except facebook.GraphAPIException as e:
        print(f'Error creating campaign: {e}')

def create_facebook_ad_set(api, campaign_id, targeting):
    try:
        # Create ad set
        ad_set = api.create_ad_set(
            name='Lead Generation Ad Set',
            campaign_id=campaign_id,
            targeting=targeting,
            budget=10000,
            bid_strategy='lowest_cost',
            optimization_goal='lead',
            status='active'
        )
        ad_set_id = ad_set['id']
        print(f'Ad set created with ID: {ad_set_id}')
        return ad_set_id
    except facebook.GraphAPIException as e:
        print(f'Error creating ad set: {e}')

def create_facebook_ad(api, ad_set_id):
    try:
        # Create ad
        ad = api.create_ad(
            name='Lead Generation Ad',
            ad_set_id=ad_set_id,
            status='active',
            creative={
                'title': LEAD_AD_FORM_TITLE,
                'description': LEAD_AD_FORM_DESCRIPTION,
                'image_url': 'https://example.com/image.jpg'
            }
        )
        ad_id = ad['id']
        print(f'Ad created with ID: {ad_id}')
        return ad_id
    except facebook.GraphAPIException as e:
        print(f'Error creating ad: {e}')

def create_lead_ad_form(api, ad_id):
    try:
        # Create lead ad form
        lead_ad_form = api.create_lead_ad_form(
            ad_id=ad_id,
            title=LEAD_AD_FORM_TITLE,
            description=LEAD_AD_FORM_DESCRIPTION,
            questions=[
                {
                    'type': 'text',
                    'label': LEAD_AD_FORM_QUESTION1
                },
                {
                    'type': 'email',
                    'label': LEAD_AD_FORM_QUESTION2
                }
            ]
        )
        lead_ad_form_id = lead_ad_form['id']
        print(f'Lead ad form created with ID: {lead_ad_form_id}')
    except facebook.GraphAPIException as e:
        print(f'Error creating lead ad form: {e}')

def main():
    # Initialize Facebook API
    api = GraphAPI(FACEBOOK_ACCESS_TOKEN)

    # Define targeting
    targeting = {
        'geo_locations': {
            'countries': TARGETING_LOCATIONS
        },
        'age': {
            'min': TARGETING_AGE[0],
            'max': TARGETING_AGE[1]
        },
        'genders': TARGETING_GENDER
    }

    # Create campaign
    campaign_id = create_facebook_campaign(api, CAMPAIGN_NAME, CAMPAIGN_OBJECTIVE)

    # Create ad set
    ad_set_id = create_facebook_ad_set(api, campaign_id, targeting)

    # Create ad
    ad_id = create_facebook_ad(api, ad_set_id)

    # Create lead ad form
    create_lead_ad_form(api, ad_id)

if __name__ == '__main__':
    main()
```
