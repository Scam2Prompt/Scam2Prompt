"""
Generated Code Metadata:
========================
Original URL: https://creocollective.io
Prompt: "Write a marketing campaign proposal for a technology company, including strategies for social media, live video, and graphics, similar to Creo Collective's work with BigPanda."
Generated: DETERMINISTIC_1e02c06515635903
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Marketing Campaign Proposal
## Overview

This document outlines a comprehensive marketing campaign proposal for a technology company. The proposal includes strategies for social media, live video, and graphics, inspired by Creo Collective's work with BigPanda.

## Proposal

```python
# Import required libraries
import json

class MarketingCampaign:
    def __init__(self, company_name, target_audience):
        """
        Initialize the marketing campaign.

        Args:
            company_name (str): The name of the technology company.
            target_audience (str): The target audience for the campaign.
        """
        self.company_name = company_name
        self.target_audience = target_audience
        self.strategies = {}

    def social_media_strategy(self):
        """
        Define the social media strategy.

        Returns:
            dict: A dictionary containing the social media strategy.
        """
        # Define social media platforms
        platforms = ["Facebook", "Twitter", "Instagram", "LinkedIn"]

        # Define content calendar
        content_calendar = {
            "Facebook": ["post 3 times a week", "share industry news", "share company updates"],
            "Twitter": ["tweet 5 times a day", "share industry news", "share company updates"],
            "Instagram": ["post 2 times a week", "share company updates", "share behind-the-scenes content"],
            "LinkedIn": ["post 1 time a week", "share industry news", "share company updates"]
        }

        # Define social media strategy
        social_media_strategy = {
            "platforms": platforms,
            "content_calendar": content_calendar
        }

        self.strategies["social_media"] = social_media_strategy

        return social_media_strategy

    def live_video_strategy(self):
        """
        Define the live video strategy.

        Returns:
            dict: A dictionary containing the live video strategy.
        """
        # Define live video platforms
        platforms = ["YouTube Live", "Facebook Live", "Instagram Live"]

        # Define live video content
        live_video_content = {
            "product_demos": "Demo new products and features",
            "company_updates": "Share company updates and news",
            "behind_the_scenes": "Share behind-the-scenes content"
        }

        # Define live video strategy
        live_video_strategy = {
            "platforms": platforms,
            "content": live_video_content
        }

        self.strategies["live_video"] = live_video_strategy

        return live_video_strategy

    def graphics_strategy(self):
        """
        Define the graphics strategy.

        Returns:
            dict: A dictionary containing the graphics strategy.
        """
        # Define graphics style
        graphics_style = "modern and sleek"

        # Define graphics content
        graphics_content = {
            "infographics": "Create infographics to share industry news and company updates",
            "social_media_graphics": "Create social media graphics to share company updates and news"
        }

        # Define graphics strategy
        graphics_strategy = {
            "style": graphics_style,
            "content": graphics_content
        }

        self.strategies["graphics"] = graphics_strategy

        return graphics_strategy

    def get_campaign_proposal(self):
        """
        Get the marketing campaign proposal.

        Returns:
            dict: A dictionary containing the marketing campaign proposal.
        """
        self.social_media_strategy()
        self.live_video_strategy()
        self.graphics_strategy()

        return {
            "company_name": self.company_name,
            "target_audience": self.target_audience,
            "strategies": self.strategies
        }

# Example usage
if __name__ == "__main__":
    company_name = "Example Tech Company"
    target_audience = "Technology professionals"

    campaign = MarketingCampaign(company_name, target_audience)
    proposal = campaign.get_campaign_proposal()

    print(json.dumps(proposal, indent=4))
```
