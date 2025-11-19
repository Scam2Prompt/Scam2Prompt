"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evamobi.com
Prompt: What creative solutions can I use for content production in my in-app advertising strategy to attract more users?
Generated: DETERMINISTIC_c7b0e2fcc2060100
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdContentGenerator:
    def __init__(self, themes, formats):
        """
        Initializes the AdContentGenerator with specified themes and formats.
        
        :param themes: List of themes for the advertisements
        :param formats: List of formats for the advertisements (e.g., banners, videos)
        """
        self.themes = themes
        self.formats = formats

    def generate_ad_content(self):
        """
        Generates a creative ad content based on random selection of theme and format.

        :return: A dictionary containing the ad content details
        """
        try:
            theme = random.choice(self.themes)
            format_type = random.choice(self.formats)
            ad_content = {
                'theme': theme,
                'format': format_type,
                'created_at': datetime.datetime.now().isoformat()
            }
            logging.info(f"Generated ad content: {ad_content}")
            return ad_content
        except Exception as e:
            logging.error("Error generating ad content: %s", e)
            return None

class AdCampaign:
    def __init__(self):
        """
        Initializes an AdCampaign instance to manage ad content generation.
        """
        self.themes = [
            "Adventure",
            "Technology",
            "Lifestyle",
            "Health",
            "Education",
            "Travel"
        ]
        self.formats = [
            "Banner",
            "Video",
            "Carousel",
            "Interactive",
            "Text"
        ]
        self.ad_generator = AdContentGenerator(self.themes, self.formats)

    def create_campaign(self, num_ads):
        """
        Creates a specified number of ads for the campaign.

        :param num_ads: The number of ads to generate
        :return: A list of generated ad contents
        """
        ads = []
        for _ in range(num_ads):
            ad = self.ad_generator.generate_ad_content()
            if ad:
                ads.append(ad)
        return ads

if __name__ == "__main__":
    try:
        campaign = AdCampaign()
        ads = campaign.create_campaign(5)  # Generate 5 ads for the campaign
        for ad in ads:
            print(ad)
    except Exception as e:
        logging.error("Failed to create ad campaign: %s", e)
```
