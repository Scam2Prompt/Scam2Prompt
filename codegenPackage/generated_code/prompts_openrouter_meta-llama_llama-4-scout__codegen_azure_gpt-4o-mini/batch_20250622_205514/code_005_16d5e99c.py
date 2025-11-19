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
import json
from datetime import datetime

class SocialMediaCampaignProposal:
    def __init__(self, client_name, field, team_expertise):
        """
        Initializes the SocialMediaCampaignProposal with client details and team expertise.

        :param client_name: Name of the client
        :param field: Field of the client (e.g., endocrinology)
        :param team_expertise: Expertise of the team (e.g., creating engaging visuals and animations)
        """
        self.client_name = client_name
        self.field = field
        self.team_expertise = team_expertise
        self.proposal = {
            "client_name": self.client_name,
            "field": self.field,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "campaign_details": []
        }

    def add_campaign_detail(self, title, description, visuals_required):
        """
        Adds a campaign detail to the proposal.

        :param title: Title of the campaign
        :param description: Description of the campaign
        :param visuals_required: List of visuals required for the campaign
        """
        campaign_detail = {
            "title": title,
            "description": description,
            "visuals_required": visuals_required
        }
        self.proposal["campaign_details"].append(campaign_detail)

    def generate_proposal(self):
        """
        Generates the final proposal in JSON format.

        :return: JSON string of the proposal
        """
        try:
            return json.dumps(self.proposal, indent=4)
        except (TypeError, ValueError) as e:
            print(f"Error generating proposal: {e}")
            return None

    def save_proposal_to_file(self, filename):
        """
        Saves the proposal to a JSON file.

        :param filename: Name of the file to save the proposal
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.proposal, file, indent=4)
            print(f"Proposal saved to {filename}")
        except IOError as e:
            print(f"Error saving proposal to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new campaign proposal for a client in the endocrinology field
    campaign_proposal = SocialMediaCampaignProposal("HealthFirst Endocrinology", "Endocrinology", "Team Adver's expertise in creating engaging visuals and animations")

    # Add campaign details
    campaign_proposal.add_campaign_detail(
        title="Thyroid Awareness Month",
        description="A campaign to raise awareness about thyroid health and its impact on overall well-being.",
        visuals_required=["infographics", "animated videos", "social media posts"]
    )

    campaign_proposal.add_campaign_detail(
        title="Diabetes Management Tips",
        description="Educational content focusing on effective diabetes management strategies.",
        visuals_required=["tutorial videos", "interactive posts", "infographics"]
    )

    # Generate and print the proposal
    proposal_json = campaign_proposal.generate_proposal()
    if proposal_json:
        print(proposal_json)

    # Save the proposal to a file
    campaign_proposal.save_proposal_to_file("endocrinology_campaign_proposal.json")
```
