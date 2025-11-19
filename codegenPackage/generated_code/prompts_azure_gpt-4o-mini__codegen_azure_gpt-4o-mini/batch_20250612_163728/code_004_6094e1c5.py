"""
Generated Code Metadata:
========================
Original URL: https://pspamelaslocum.com
Prompt: Outline a strategy for an advertising campaign that utilizes both print and digital media, drawing on the expertise of PS Pamela Slocum in marketing and promotions.
Generated: DETERMINISTIC_6094e1c5a0df49df
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AdvertisingCampaign:
    """
    A class to represent an advertising campaign that utilizes both print and digital media.
    """

    def __init__(self, campaign_name, target_audience):
        """
        Initializes the AdvertisingCampaign with a name and target audience.

        :param campaign_name: Name of the advertising campaign
        :param target_audience: Target audience for the campaign
        """
        self.campaign_name = campaign_name
        self.target_audience = target_audience
        self.print_media = []
        self.digital_media = []

    def add_print_media(self, media):
        """
        Adds print media to the campaign.

        :param media: A string representing the print media to be added
        """
        if isinstance(media, str) and media:
            self.print_media.append(media)
        else:
            raise ValueError("Print media must be a non-empty string.")

    def add_digital_media(self, media):
        """
        Adds digital media to the campaign.

        :param media: A string representing the digital media to be added
        """
        if isinstance(media, str) and media:
            self.digital_media.append(media)
        else:
            raise ValueError("Digital media must be a non-empty string.")

    def outline_strategy(self):
        """
        Outlines the strategy for the advertising campaign, detailing both print and digital media.
        
        :return: A dictionary containing the campaign strategy
        """
        strategy = {
            "Campaign Name": self.campaign_name,
            "Target Audience": self.target_audience,
            "Print Media": self.print_media,
            "Digital Media": self.digital_media,
            "Strategy": self._generate_strategy()
        }
        return strategy

    def _generate_strategy(self):
        """
        Generates a detailed strategy for the campaign based on the media used.

        :return: A string summarizing the campaign strategy
        """
        return (
            f"The campaign '{self.campaign_name}' targets {self.target_audience}. "
            f"It utilizes print media such as {', '.join(self.print_media)} "
            f"and digital media including {', '.join(self.digital_media)}. "
            "The combination aims to maximize reach and engagement."
        )


# Example usage
if __name__ == "__main__":
    try:
        campaign = AdvertisingCampaign("Summer Sale", "Young Adults")
        campaign.add_print_media("Flyers")
        campaign.add_print_media("Posters")
        campaign.add_digital_media("Social Media Ads")
        campaign.add_digital_media("Email Newsletters")

        strategy = campaign.outline_strategy()
        print(strategy)
    except ValueError as e:
        print(f"Error: {e}")
```
