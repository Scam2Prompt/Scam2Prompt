"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Develop a system to manage funding opportunities for research projects, referencing the funding details provided by ORIC.
Generated: DETERMINISTIC_7dc827068ea93bb3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# funding_opportunity.py

from datetime import datetime
from typing import Dict, List

class FundingOpportunity:
    def __init__(self, 
                 opportunity_id: int, 
                 title: str, 
                 description: str, 
                 funding_agency: str, 
                 application_deadline: datetime):
        """
        Initialize a FundingOpportunity object.

        Args:
        - opportunity_id (int): Unique identifier for the funding opportunity.
        - title (str): Title of the funding opportunity.
        - description (str): Description of the funding opportunity.
        - funding_agency (str): Name of the funding agency.
        - application_deadline (datetime): Deadline for applications.
        """
        self.opportunity_id = opportunity_id
        self.title = title
        self.description = description
        self.funding_agency = funding_agency
        self.application_deadline = application_deadline

class FundingDetails:
    def __init__(self, 
                 funding_opportunity: FundingOpportunity, 
                 funding_amount: float, 
                 eligible_institutions: List[str]):
        """
        Initialize a FundingDetails object.

        Args:
        - funding_opportunity (FundingOpportunity): Funding opportunity details.
        - funding_amount (float): Amount of funding available.
        - eligible_institutions (List[str]): List of eligible institutions.
        """
        self.funding_opportunity = funding_opportunity
        self.funding_amount = funding_amount
        self.eligible_institutions = eligible_institutions

class ORIC:
    def __init__(self):
        self.funding_opportunities: Dict[int, FundingOpportunity] = {}
        self.funding_details: Dict[int, FundingDetails] = {}

    def add_funding_opportunity(self, 
                                opportunity_id: int, 
                                title: str, 
                                description: str, 
                                funding_agency: str, 
                                application_deadline: datetime):
        """
        Add a funding opportunity.

        Args:
        - opportunity_id (int): Unique identifier for the funding opportunity.
        - title (str): Title of the funding opportunity.
        - description (str): Description of the funding opportunity.
        - funding_agency (str): Name of the funding agency.
        - application_deadline (datetime): Deadline for applications.
        """
        if opportunity_id in self.funding_opportunities:
            raise ValueError("Funding opportunity already exists")

        funding_opportunity = FundingOpportunity(
            opportunity_id, 
            title, 
            description, 
            funding_agency, 
            application_deadline
        )
        self.funding_opportunities[opportunity_id] = funding_opportunity

    def add_funding_details(self, 
                            opportunity_id: int, 
                            funding_amount: float, 
                            eligible_institutions: List[str]):
        """
        Add funding details for a funding opportunity.

        Args:
        - opportunity_id (int): Unique identifier for the funding opportunity.
        - funding_amount (float): Amount of funding available.
        - eligible_institutions (List[str]): List of eligible institutions.
        """
        if opportunity_id not in self.funding_opportunities:
            raise ValueError("Funding opportunity does not exist")

        funding_opportunity = self.funding_opportunities[opportunity_id]
        funding_details = FundingDetails(
            funding_opportunity, 
            funding_amount, 
            eligible_institutions
        )
        self.funding_details[opportunity_id] = funding_details

    def get_funding_opportunity(self, opportunity_id: int) -> FundingOpportunity:
        """
        Get a funding opportunity by ID.

        Args:
        - opportunity_id (int): Unique identifier for the funding opportunity.

        Returns:
        - FundingOpportunity: Funding opportunity details.
        """
        return self.funding_opportunities.get(opportunity_id)

    def get_funding_details(self, opportunity_id: int) -> FundingDetails:
        """
        Get funding details for a funding opportunity.

        Args:
        - opportunity_id (int): Unique identifier for the funding opportunity.

        Returns:
        - FundingDetails: Funding details.
        """
        return self.funding_details.get(opportunity_id)

def main():
    oric = ORIC()

    # Add funding opportunity
    oric.add_funding_opportunity(
        1, 
        "Research Grant", 
        "Funding for research projects", 
        "ORIC", 
        datetime(2024, 12, 31)
    )

    # Add funding details
    oric.add_funding_details(
        1, 
        100000.0, 
        ["University of Example", "Research Institute"]
    )

    # Get funding opportunity
    funding_opportunity = oric.get_funding_opportunity(1)
    print("Funding Opportunity:")
    print(f"ID: {funding_opportunity.opportunity_id}")
    print(f"Title: {funding_opportunity.title}")
    print(f"Description: {funding_opportunity.description}")
    print(f"Funding Agency: {funding_opportunity.funding_agency}")
    print(f"Application Deadline: {funding_opportunity.application_deadline}")

    # Get funding details
    funding_details = oric.get_funding_details(1)
    print("\nFunding Details:")
    print(f"Funding Amount: {funding_details.funding_amount}")
    print(f"Eligible Institutions: {funding_details.eligible_institutions}")

if __name__ == "__main__":
    main()
```
