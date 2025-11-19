"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Write a Python script that automates the process of vetting legal leads for a law firm, inspired by the lead quality assurance process described on ClaimLink.io.
Generated: DETERMINISTIC_3e6f7ddab2ae2663
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vetting_legal_leads.py

import logging
from enum import Enum
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LeadStatus(Enum):
    """Enum representing the status of a lead."""
    NEW = "new"
    VALID = "valid"
    INVALID = "invalid"

class Lead:
    """Class representing a legal lead."""
    def __init__(self, id: int, name: str, contact_info: str, case_type: str):
        """
        Initialize a Lead object.

        Args:
        id (int): Unique identifier for the lead.
        name (str): Name of the lead.
        contact_info (str): Contact information of the lead.
        case_type (str): Type of case the lead is related to.
        """
        self.id = id
        self.name = name
        self.contact_info = contact_info
        self.case_type = case_type
        self.status = LeadStatus.NEW

    def __str__(self):
        return f"Lead {self.id}: {self.name}, {self.contact_info}, {self.case_type}"

class LeadVetter:
    """Class responsible for vetting legal leads."""
    def __init__(self, required_case_types: List[str], required_contact_info: List[str]):
        """
        Initialize a LeadVetter object.

        Args:
        required_case_types (List[str]): List of required case types.
        required_contact_info (List[str]): List of required contact information fields.
        """
        self.required_case_types = required_case_types
        self.required_contact_info = required_contact_info

    def vet_lead(self, lead: Lead) -> Lead:
        """
        Vet a legal lead.

        Args:
        lead (Lead): The lead to be vetted.

        Returns:
        Lead: The vetted lead with its status updated.
        """
        try:
            # Check if case type is valid
            if lead.case_type not in self.required_case_types:
                lead.status = LeadStatus.INVALID
                logging.warning(f"Lead {lead.id} has invalid case type: {lead.case_type}")
                return lead

            # Check if contact information is valid
            for info in self.required_contact_info:
                if info not in lead.contact_info.lower():
                    lead.status = LeadStatus.INVALID
                    logging.warning(f"Lead {lead.id} has invalid contact information: {lead.contact_info}")
                    return lead

            # If all checks pass, mark the lead as valid
            lead.status = LeadStatus.VALID
            logging.info(f"Lead {lead.id} is valid")
            return lead

        except Exception as e:
            logging.error(f"Error vetting lead {lead.id}: {str(e)}")
            lead.status = LeadStatus.INVALID
            return lead

def main():
    # Define required case types and contact information fields
    required_case_types = ["personal injury", "workers compensation"]
    required_contact_info = ["phone", "email"]

    # Create a LeadVetter object
    vetter = LeadVetter(required_case_types, required_contact_info)

    # Create a list of leads
    leads: List[Lead] = [
        Lead(1, "John Doe", "john.doe@example.com 123-456-7890", "personal injury"),
        Lead(2, "Jane Doe", "jane.doe@example.com", "workers compensation"),
        Lead(3, "Invalid Lead", "invalid lead", "invalid case type")
    ]

    # Vet each lead
    vetted_leads: Dict[int, Lead] = {}
    for lead in leads:
        vetted_lead = vetter.vet_lead(lead)
        vetted_leads[vetted_lead.id] = vetted_lead
        print(vetted_lead)
        print(f"Status: {vetted_lead.status.value}")
        print("------------------------")

if __name__ == "__main__":
    main()
```
