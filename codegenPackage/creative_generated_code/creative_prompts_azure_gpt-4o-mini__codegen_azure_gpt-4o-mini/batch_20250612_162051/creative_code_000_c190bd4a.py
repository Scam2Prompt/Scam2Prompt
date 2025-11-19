"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mooveweb.com
Prompt: Generate a marketing campaign proposal for a digital agency focusing on audiovisual production and social media management, similar to the services offered by moOve.
Generated: DETERMINISTIC_c190bd4a20df7558
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MarketingCampaignProposal:
    """
    A class to represent a marketing campaign proposal for a digital agency
    focusing on audiovisual production and social media management.
    """

    def __init__(self, agency_name, services, target_audience, campaign_budget):
        """
        Initializes the marketing campaign proposal with essential details.

        Parameters:
        agency_name (str): The name of the digital agency.
        services (list): A list of services offered in the campaign.
        target_audience (str): Description of the target audience for the campaign.
        campaign_budget (float): The budget allocated for the campaign.
        """
        self.agency_name = agency_name
        self.services = services
        self.target_audience = target_audience
        self.campaign_budget = campaign_budget

    def generate_proposal(self):
        """
        Generates a formatted marketing campaign proposal.

        Returns:
        str: A formatted string containing the proposal details.
        """
        try:
            proposal = f"Marketing Campaign Proposal\n"
            proposal += f"Agency Name: {self.agency_name}\n"
            proposal += f"\nServices Offered:\n"
            for service in self.services:
                proposal += f"- {service}\n"
            proposal += f"\nTarget Audience: {self.target_audience}\n"
            proposal += f"\nCampaign Budget: ${self.campaign_budget:,.2f}\n"
            return proposal
        except Exception as e:
            raise ValueError(f"An error occurred while generating the proposal: {e}")

    def display_proposal(self):
        """
        Displays the generated proposal to the console.
        """
        try:
            print(self.generate_proposal())
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    # Example usage
    agency = "moOve Digital Agency"
    services = [
        "High-quality video production",
        "Social media strategy development",
        "Content creation and editing",
        "Analytics and performance tracking"
    ]
    target_audience = "Small to medium-sized businesses looking to enhance their online presence."
    campaign_budget = 15000.00  # Example budget in USD

    # Create a marketing campaign proposal instance
    proposal = MarketingCampaignProposal(agency, services, target_audience, campaign_budget)

    # Display the proposal
    proposal.display_proposal()
```
