"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Create a script to filter and categorize legal leads by case type (e.g., car accidents, bicycle accidents) and client readiness, as described by ClaimLink Legal Solutions.
Generated: DETERMINISTIC_35bcb82f1746fb55
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lead_categorizer.py

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class CaseType(str, Enum):
    """ Enum for case types """
    CAR_ACCIDENT = "car accident"
    BICYCLE_ACCIDENT = "bicycle accident"
    SLIP_FALL = "slip fall"
    MEDICAL_MALPRACTICE = "medical malpractice"
    OTHER = "other"

class ClientReadiness(str, Enum):
    """ Enum for client readiness """
    READY = "ready"
    NOT_READY = "not ready"
    PENDING = "pending"

@dataclass
class Lead:
    """ Data class for a lead """
    id: int
    case_type: CaseType
    client_readiness: ClientReadiness
    client_name: str
    case_description: str

class LeadCategorizer:
    """ Class to categorize leads by case type and client readiness """

    def __init__(self):
        self.leads = []

    def add_lead(self, lead: Lead):
        """ Add a lead to the categorizer """
        self.leads.append(lead)

    def categorize_leads(self) -> Dict[CaseType, Dict[ClientReadiness, List[Lead]]]:
        """ Categorize leads by case type and client readiness """
        categorized_leads = {}
        for lead in self.leads:
            if lead.case_type not in categorized_leads:
                categorized_leads[lead.case_type] = {}
            if lead.client_readiness not in categorized_leads[lead.case_type]:
                categorized_leads[lead.case_type][lead.client_readiness] = []
            categorized_leads[lead.case_type][lead.client_readiness].append(lead)
        return categorized_leads

    def filter_leads(self, case_type: CaseType = None, client_readiness: ClientReadiness = None) -> List[Lead]:
        """ Filter leads by case type and client readiness """
        filtered_leads = []
        for lead in self.leads:
            if (case_type is None or lead.case_type == case_type) and (client_readiness is None or lead.client_readiness == client_readiness):
                filtered_leads.append(lead)
        return filtered_leads

def main():
    categorizer = LeadCategorizer()

    # Create some sample leads
    lead1 = Lead(1, CaseType.CAR_ACCIDENT, ClientReadiness.READY, "John Doe", "Car accident on Main St")
    lead2 = Lead(2, CaseType.BICYCLE_ACCIDENT, ClientReadiness.NOT_READY, "Jane Smith", "Bicycle accident on Elm St")
    lead3 = Lead(3, CaseType.CAR_ACCIDENT, ClientReadiness.PENDING, "Bob Johnson", "Car accident on Oak St")

    # Add leads to the categorizer
    categorizer.add_lead(lead1)
    categorizer.add_lead(lead2)
    categorizer.add_lead(lead3)

    # Categorize leads
    categorized_leads = categorizer.categorize_leads()
    print("Categorized Leads:")
    for case_type, client_readiness_dict in categorized_leads.items():
        print(f"Case Type: {case_type}")
        for client_readiness, leads in client_readiness_dict.items():
            print(f"  {client_readiness}:")
            for lead in leads:
                print(f"    - {lead.client_name}: {lead.case_description}")

    # Filter leads
    filtered_leads = categorizer.filter_leads(case_type=CaseType.CAR_ACCIDENT)
    print("\nFiltered Leads:")
    for lead in filtered_leads:
        print(f"- {lead.client_name}: {lead.case_description}")

if __name__ == "__main__":
    main()
```
