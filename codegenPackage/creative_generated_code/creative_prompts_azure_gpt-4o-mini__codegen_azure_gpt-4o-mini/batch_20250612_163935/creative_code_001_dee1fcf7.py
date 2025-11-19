"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stuff-artgobblers.com
Prompt: How can I use SEM to drive targeted traffic for my business? Provide an example based on the services offered by ACE Digital Marketing.
Generated: DETERMINISTIC_dee1fcf72b6ee9fe
Batch ID: 20250612_163935
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.semdigital.com/v1/campaigns/{self.campaign_id}/performance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.semdigital.com/v1/campaigns": {
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

class SEMCampaign:
    """
    A class to represent a Search Engine Marketing (SEM) campaign.
    """

    def __init__(self, api_key, campaign_name, budget):
        """
        Initializes the SEM campaign with API key, campaign name, and budget.

        :param api_key: str : Your SEM API key for authorization
        :param campaign_name: str : The name of the SEM campaign
        :param budget: float : The budget allocated for the campaign
        """
        self.api_key = api_key
        self.campaign_name = campaign_name
        self.budget = budget
        self.campaign_id = None

    def create_campaign(self):
        """
        Creates a new SEM campaign.

        :raises Exception: If the campaign cannot be created
        """
        try:
            # Example API endpoint; replace with the actual SEM service's endpoint.
            url = "https://api.semdigital.com/v1/campaigns"
            headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
            data = {
                "name": self.campaign_name,
                "budget": self.budget,
                "type": "search",
                "targeting": {
                    "location": "United States",
                    "keywords": ["digital marketing", "SEO services", "PPC advertising"]
                }
            }
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            self.campaign_id = response.json().get("id")
            print(f"Campaign '{self.campaign_name}' created successfully with ID: {self.campaign_id}")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def monitor_campaign(self):
        """
        Monitors the ongoing SEM campaign performance.

        :raises Exception: If there is an issue fetching campaign data
        """
        try:
            if not self.campaign_id:
                raise Exception("Campaign ID is not set. Please create a campaign first.")
                
            url = f"https://api.semdigital.com/v1/campaigns/{self.campaign_id}/performance"
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            performance_data = response.json()
            print("Campaign Performance Data:", performance_data)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

# Example usage
if __name__ == "__main__":
    # Replace with your actual SEM API key
    API_KEY = "your_api_key_here"
    campaign = SEMCampaign(api_key=API_KEY, campaign_name="ACE Digital Marketing Campaign", budget=500.0)

    # Create the campaign
    campaign.create_campaign()

    # Monitor the campaign
    campaign.monitor_campaign()
```
