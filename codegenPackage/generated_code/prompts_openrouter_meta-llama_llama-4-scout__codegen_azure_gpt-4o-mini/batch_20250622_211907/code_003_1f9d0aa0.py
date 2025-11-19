"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Generate a sample investment proposal for a startup in the telecommunications sector in Hungary, using Initia Capital's investment approach and philosophy.
Generated: DETERMINISTIC_1f9d0aa053711b2e
Batch ID: 20250622_211907
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

class InvestmentProposal:
    """
    A class to represent an investment proposal for a startup in the telecommunications sector.
    """

    def __init__(self, startup_name, sector, location, funding_amount, equity_offered, proposal_details):
        """
        Initializes the InvestmentProposal with the necessary attributes.

        :param startup_name: Name of the startup
        :param sector: Sector of the startup
        :param location: Location of the startup
        :param funding_amount: Amount of funding requested
        :param equity_offered: Percentage of equity offered
        :param proposal_details: Detailed description of the proposal
        """
        self.startup_name = startup_name
        self.sector = sector
        self.location = location
        self.funding_amount = funding_amount
        self.equity_offered = equity_offered
        self.proposal_details = proposal_details
        self.created_at = datetime.now()

    def to_dict(self):
        """
        Converts the InvestmentProposal instance to a dictionary.

        :return: A dictionary representation of the investment proposal
        """
        return {
            "startup_name": self.startup_name,
            "sector": self.sector,
            "location": self.location,
            "funding_amount": self.funding_amount,
            "equity_offered": self.equity_offered,
            "proposal_details": self.proposal_details,
            "created_at": self.created_at.isoformat()
        }

    def save_to_file(self, filename):
        """
        Saves the investment proposal to a JSON file.

        :param filename: The name of the file to save the proposal
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
            print(f"Proposal saved to {filename}")
        except IOError as e:
            print(f"Error saving proposal to file: {e}")

def main():
    """
    Main function to create and save an investment proposal.
    """
    # Sample data for the investment proposal
    startup_name = "Telecom Innovators"
    sector = "Telecommunications"
    location = "Budapest, Hungary"
    funding_amount = 500000  # in HUF
    equity_offered = 10  # in percentage
    proposal_details = (
        "Telecom Innovators aims to revolutionize the telecommunications sector in Hungary "
        "by providing high-speed internet access to underserved areas. Our innovative technology "
        "and strategic partnerships will ensure rapid growth and a strong market presence."
    )

    # Create an investment proposal instance
    proposal = InvestmentProposal(
        startup_name,
        sector,
        location,
        funding_amount,
        equity_offered,
        proposal_details
    )

    # Save the proposal to a JSON file
    proposal.save_to_file("investment_proposal.json")

if __name__ == "__main__":
    main()
```
