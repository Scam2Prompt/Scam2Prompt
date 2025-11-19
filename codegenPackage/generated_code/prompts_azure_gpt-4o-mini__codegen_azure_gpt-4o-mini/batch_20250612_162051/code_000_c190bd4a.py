"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Generate a marketing campaign proposal for a digital agency focusing on audiovisual production and social media management, similar to the services offered by moOve.
Generated: DETERMINISTIC_c190bd4a20df7558
Batch ID: 20250612_162051
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

class MarketingCampaignProposal:
    def __init__(self, client_name, agency_name, services, budget, duration):
        """
        Initializes the MarketingCampaignProposal with client details and campaign specifics.

        :param client_name: Name of the client
        :param agency_name: Name of the agency
        :param services: List of services to be offered
        :param budget: Total budget for the campaign
        :param duration: Duration of the campaign in weeks
        """
        self.client_name = client_name
        self.agency_name = agency_name
        self.services = services
        self.budget = budget
        self.duration = duration
        self.proposal_date = datetime.now().strftime("%Y-%m-%d")

    def generate_proposal(self):
        """
        Generates a marketing campaign proposal in JSON format.

        :return: JSON string of the proposal
        """
        proposal = {
            "client_name": self.client_name,
            "agency_name": self.agency_name,
            "services": self.services,
            "budget": self.budget,
            "duration": self.duration,
            "proposal_date": self.proposal_date
        }
        return json.dumps(proposal, indent=4)

    def save_proposal(self, filename):
        """
        Saves the generated proposal to a JSON file.

        :param filename: Name of the file to save the proposal
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_proposal())
            print(f"Proposal saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving proposal to file: {e}")

# Example usage
if __name__ == "__main__":
    # Define campaign details
    client_name = "ABC Corp"
    agency_name = "Creative Agency"
    services = [
        "Audiovisual Production",
        "Social Media Management",
        "Content Creation",
        "Digital Marketing Strategy"
    ]
    budget = 15000  # in USD
    duration = 12   # in weeks

    # Create a marketing campaign proposal
    proposal = MarketingCampaignProposal(client_name, agency_name, services, budget, duration)

    # Generate and save the proposal
    proposal_filename = "marketing_campaign_proposal.json"
    proposal.save_proposal(proposal_filename)
```
