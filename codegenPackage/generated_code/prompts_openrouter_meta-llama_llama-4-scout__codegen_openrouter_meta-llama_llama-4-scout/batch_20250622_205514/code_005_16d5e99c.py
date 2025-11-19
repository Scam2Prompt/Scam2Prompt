"""
Generated Code Metadata:
========================
Original URL: https://teamadver.com
Prompt: Generate a social media campaign proposal for a new client in the endocrinology field, incorporating Team Adver's expertise in creating engaging visuals and animations.
Generated: DETERMINISTIC_16d5e99c63a24fd6
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
from datetime import datetime, timedelta

class SocialMediaCampaignProposal:
    def __init__(self, client_name, campaign_name, endocrinology_focus):
        """
        Initialize a social media campaign proposal.

        Args:
            client_name (str): Name of the client.
            campaign_name (str): Name of the campaign.
            endocrinology_focus (str): Focus area within endocrinology.
        """
        self.client_name = client_name
        self.campaign_name = campaign_name
        self.endocrinology_focus = endocrinology_focus
        self.objectives = []
        self.target_audience = []
        self.content_strategy = []
        self.visuals_and_animations = []

    def add_objective(self, objective):
        """
        Add a campaign objective.

        Args:
            objective (str): Objective of the campaign.
        """
        self.objectives.append(objective)

    def add_target_audience(self, audience):
        """
        Add a target audience segment.

        Args:
            audience (dict): Dictionary containing audience demographics.
        """
        self.target_audience.append(audience)

    def add_content_strategy(self, strategy):
        """
        Add a content strategy.

        Args:
            strategy (str): Content strategy.
        """
        self.content_strategy.append(strategy)

    def add_visuals_and_animations(self, visual):
        """
        Add a visual or animation.

        Args:
            visual (dict): Dictionary containing visual or animation details.
        """
        self.visuals_and_animations.append(visual)

    def generate_proposal(self):
        """
        Generate a social media campaign proposal.

        Returns:
            dict: Dictionary containing the campaign proposal.
        """
        proposal = {
            "client_name": self.client_name,
            "campaign_name": self.campaign_name,
            "endocrinology_focus": self.endocrinology_focus,
            "objectives": self.objectives,
            "target_audience": self.target_audience,
            "content_strategy": self.content_strategy,
            "visuals_and_animations": self.visuals_and_animations,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return proposal

    def save_proposal(self, filename):
        """
        Save the campaign proposal to a JSON file.

        Args:
            filename (str): Name of the file to save the proposal to.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.generate_proposal(), file, indent=4)
            print(f"Proposal saved to {filename} successfully.")
        except Exception as e:
            print(f"Error saving proposal: {str(e)}")


def main():
    # Create a new social media campaign proposal
    proposal = SocialMediaCampaignProposal(
        client_name="New Client",
        campaign_name="Endocrinology Awareness",
        endocrinology_focus="Diabetes Management"
    )

    # Add campaign objectives
    proposal.add_objective("Increase brand awareness by 20%")
    proposal.add_objective("Drive website traffic by 50%")

    # Add target audience segments
    proposal.add_target_audience({
        "age": "25-45",
        "interests": ["healthcare", "wellness", "endocrinology"]
    })

    # Add content strategies
    proposal.add_content_strategy("Create engaging social media posts")
    proposal.add_content_strategy("Utilize influencer marketing")

    # Add visuals and animations
    proposal.add_visuals_and_animations({
        "type": "infographic",
        "description": "Illustrate the importance of diabetes management"
    })

    # Save the proposal to a JSON file
    proposal.save_proposal("social_media_campaign_proposal.json")


if __name__ == "__main__":
    main()
```
