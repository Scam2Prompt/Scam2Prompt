"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://churchproweb.com
Prompt: Provide a step-by-step guide for implementing PPC campaigns tailored for church websites, as described in ChurchProWeb's digital marketing services. Include example ad copy and targeting parameters.
Generated: DETERMINISTIC_b46aadb3c7a4c813
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
import logging

# Configure logging for tracking errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PPCampaign:
    def __init__(self, campaign_name, target_audience, budget):
        """
        Initialize a PPCampaign instance.

        :param campaign_name: Name of the PPC campaign
        :param target_audience: Description of the target audience
        :param budget: Budget allocated for the campaign
        """
        self.campaign_name = campaign_name
        self.target_audience = target_audience
        self.budget = budget
        self.ad_copies = []
        self.targeting_parameters = {}

    def add_ad_copy(self, ad_copy):
        """
        Add an advertisement copy to the campaign.

        :param ad_copy: The advertisement copy to add
        """
        if not isinstance(ad_copy, str) or len(ad_copy) == 0:
            logging.error("Invalid ad copy provided. Must be a non-empty string.")
            raise ValueError("Ad copy must be a non-empty string.")
        self.ad_copies.append(ad_copy)
        logging.info(f"Ad copy added: {ad_copy}")

    def set_targeting_parameters(self, parameters):
        """
        Set targeting parameters for the PPC campaign.

        :param parameters: Dictionary of targeting parameters
        """
        if not isinstance(parameters, dict):
            logging.error("Targeting parameters must be a dictionary.")
            raise ValueError("Targeting parameters must be a dictionary.")
        self.targeting_parameters = parameters
        logging.info("Targeting parameters set.")

    def generate_campaign_summary(self):
        """
        Generate a summary of the PPC campaign.

        :return: JSON formatted summary of the campaign
        """
        try:
            summary = {
                "Campaign Name": self.campaign_name,
                "Target Audience": self.target_audience,
                "Budget": self.budget,
                "Ad Copies": self.ad_copies,
                "Targeting Parameters": self.targeting_parameters
            }
            return json.dumps(summary, indent=4)
        except Exception as e:
            logging.error(f"Error generating campaign summary: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Create a PPC campaign tailored for a church website
        church_campaign = PPCampaign(campaign_name="Community Outreach", 
                                     target_audience="Local community members interested in church events", 
                                     budget=500)

        # Add example ad copy
        church_campaign.add_ad_copy("Join us this Sunday for uplifting worship and fellowship!")
        church_campaign.add_ad_copy("Discover your purpose and connect with others at our church.")

        # Set targeting parameters
        targeting_params = {
            "Location": "City Center",
            "Age Range": "25-45",
            "Interests": ["Community Service", "Faith", "Family Activities"]
        }
        church_campaign.set_targeting_parameters(targeting_params)

        # Generate and print the campaign summary
        summary = church_campaign.generate_campaign_summary()
        print(summary)

    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
