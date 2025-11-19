"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applovin.in
Prompt: Generate a sample ad campaign using SparkLabs to create high-performing ads for a fitness app.
Generated: DETERMINISTIC_a44eafc4613ff191
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import spark_spark as spark
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class FitnessAppAdCampaign:
    def __init__(self, campaign_name, target_audience):
        """
        Initializes the ad campaign with a given name and target audience.
        
        :param campaign_name: Name of the ad campaign
        :param target_audience: Target audience for the ads
        """
        self.campaign_name = campaign_name
        self.target_audience = target_audience
        self.ads = []

    def create_ad(self, ad_content, ad_type):
        """
        Creates a new ad for the campaign.

        :param ad_content: Content of the ad
        :param ad_type: Type of the ad (e.g., video, image, text)
        :return: None
        """
        if ad_type not in ['video', 'image', 'text']:
            logging.error(f"Invalid ad type: {ad_type}. Must be one of ['video', 'image', 'text'].")
            raise ValueError("Invalid ad type specified.")
        
        ad = {'content': ad_content, 'type': ad_type}
        self.ads.append(ad)
        logging.info(f"Ad created: {ad}")

    def run_campaign(self):
        """
        Runs the ad campaign, sending ads to SparkLabs for processing.
        
        :return: None
        """
        if not self.ads:
            logging.warning("No ads to run in the campaign.")
            return
        
        try:
            # Assume 'spark.run_ads' is a method provided by SparkLabs for running ads
            spark.run_ads(self.campaign_name, self.ads, self.target_audience)
            logging.info(f"Campaign '{self.campaign_name}' running with {len(self.ads)} ads.")
        except Exception as e:
            logging.error(f"Error running the campaign: {e}")
            raise

# Sample usage
if __name__ == "__main__":
    try:
        campaign = FitnessAppAdCampaign(campaign_name="GetFit2023", target_audience="Fitness Enthusiasts")
        campaign.create_ad("Join our 30-day fitness challenge!", "image")
        campaign.create_ad("Get personalized workouts tailored for you.", "video")
        campaign.create_ad("Download our app today and start your journey!", "text")
        campaign.run_campaign()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
