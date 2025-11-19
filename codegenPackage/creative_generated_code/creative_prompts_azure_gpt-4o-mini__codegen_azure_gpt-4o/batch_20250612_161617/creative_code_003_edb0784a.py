"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agenciainside.com
Prompt: Create a sample project proposal that incorporates the design and marketing services offered by Agência inSIDE, focusing on client customization.
Generated: DETERMINISTIC_edb0784a654c844e
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ProjectProposal:
    """
    Represents a project proposal for Agência inSIDE's design and marketing services.
    Includes client-specific customization details.
    """

    def __init__(self, client_name, client_industry, client_needs):
        """
        Initializes a new proposal instance.

        :param client_name: Name of the client.
        :param client_industry: Industry the client belongs to.
        :param client_needs: Specific needs of the client (list of strings).
        """
        self.client_name = client_name
        self.client_industry = client_industry
        self.client_needs = client_needs
        self.services_offered = ["Graphic Design", "Web Design", "Brand Development", "Digital Marketing"]
        self.proposal_summary = ""

    def generate_summary(self):
        """
        Generates a summary of the proposal based on client needs and offered services.
        """
        self.proposal_summary = (
            f"Proposal for {self.client_name}, operating in the {self.client_industry} industry.\n\n"
            f"Agência inSIDE is pleased to offer customized services to meet your unique needs:\n\n"
            f"Client Needs:\n- " + "\n- ".join(self.client_needs) + "\n\n"
            f"Services Offered:\n- " + "\n- ".join(self.services_offered) + "\n\n"
            "We will work closely with you to ensure all deliverables align with your vision and goals."
        )

    def export_to_json(self, file_name="proposal.json"):
        """
        Exports the proposal details to a JSON file.

        :param file_name: Name of the file to save the proposal (default "proposal.json").
        """
        try:
            proposal_data = {
                "client_name": self.client_name,
                "client_industry": self.client_industry,
                "client_needs": self.client_needs,
                "services_offered": self.services_offered,
                "proposal_summary": self.proposal_summary,
            }

            with open(file_name, "w") as json_file:
                json.dump(proposal_data, json_file, indent=4)

            print(f"Proposal successfully saved to {file_name}.")
        except Exception as e:
            print(f"An error occurred while saving the proposal: {e}")

    def display_proposal(self):
        """
        Displays the proposal summary in the console.
        """
        if self.proposal_summary:
            print(self.proposal_summary)
        else:
            print("Proposal summary not yet generated. Please call generate_summary() first.")


# Main execution
if __name__ == "__main__":
    # Sample client details
    client_name = "Acme Corp"
    client_industry = "E-commerce"
    client_needs = [
        "Improve brand identity",
        "Redesign company website",
        "Launch a digital marketing campaign",
    ]

    # Create a project proposal instance
    proposal = ProjectProposal(client_name, client_industry, client_needs)

    # Generate proposal summary
    proposal.generate_summary()

    # Display the proposal
    proposal.display_proposal()

    # Export proposal to JSON
    proposal.export_to_json("acme_corp_proposal.json")
```
