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
import json
from datetime import datetime

def generate_campaign_proposal(client_name, services, objectives, budget):
    """
    Generates a marketing campaign proposal for a digital agency.

    Args:
        client_name (str): The name of the client.
        services (list): List of services offered (e.g., ['Audiovisual Production', 'Social Media Management']).
        objectives (list): List of objectives for the campaign (e.g., ['Increase brand awareness', 'Engage target audience']).
        budget (float): Total budget allocated for the campaign.

    Returns:
        dict: A proposal containing campaign details.
    """
    try:
        # Validate input data
        if not isinstance(client_name, str) or not client_name.strip():
            raise ValueError("Client name must be a non-empty string.")
        if not isinstance(services, list) or len(services) == 0:
            raise ValueError("Services must be a non-empty list.")
        if not isinstance(objectives, list) or len(objectives) == 0:
            raise ValueError("Objectives must be a non-empty list.")
        if not isinstance(budget, (int, float)) or budget <= 0:
            raise ValueError("Budget must be a positive number.")

        # Generate proposal data
        proposal = {
            "client_name": client_name,
            "campaign_title": f"{client_name} Digital Marketing Campaign",
            "services": services,
            "objectives": objectives,
            "budget": f"${budget:,.2f}",
            "proposal_date": datetime.now().strftime("%Y-%m-%d"),
            "details": {
                "strategy": "Multi-platform engagement with tailored content for target audiences.",
                "timeline": "3 months from the start date.",
                "deliverables": [
                    "High-quality video production for advertisements and social media.",
                    "Weekly analytics reports to track campaign success.",
                    "Social media management, including scheduled posts and audience interaction.",
                ],
            },
            "contact": {
                "email": "contact@digitalagency.com",
                "phone": "+1-800-123-4567",
            },
        }

        return proposal

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error generating proposal: {e}")
        return None


def save_proposal_to_file(proposal, filename="campaign_proposal.json"):
    """
    Saves the campaign proposal to a JSON file.

    Args:
        proposal (dict): The campaign proposal data.
        filename (str): Name of the file to save the proposal (default is 'campaign_proposal.json').

    Returns:
        None
    """
    try:
        # Validate proposal data
        if not proposal or not isinstance(proposal, dict):
            raise ValueError("Invalid proposal data.")

        # Save proposal to file
        with open(filename, "w") as file:
            json.dump(proposal, file, indent=4)
        print(f"Proposal saved successfully to {filename}")

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error saving proposal to file: {e}")


# Example usage
if __name__ == "__main__":
    # Generate a sample proposal
    client_name = "moOve Digital Agency"
    services = ["Audiovisual Production", "Social Media Management"]
    objectives = ["Increase brand awareness", "Engage target audience", "Drive conversions"]
    budget = 50000

    proposal = generate_campaign_proposal(client_name, services, objectives, budget)

    if proposal:
        print("Generated Proposal:")
        print(json.dumps(proposal, indent=4))

        # Save the proposal to a file
        save_proposal_to_file(proposal)
```
