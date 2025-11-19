"""
Generated Code Metadata:
========================
Original URL: https://optimisenow.net
Prompt: How can I implement a Commercial Leads Management System (CLMS) to enhance my sales efforts and maximize revenue potential?
Generated: DETERMINISTIC_48700348f19e9032
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# commercial_leads_management_system.py

from datetime import datetime
from typing import Dict, List

class Lead:
    """Represents a commercial lead."""

    def __init__(self, id: int, name: str, email: str, phone: str, source: str):
        """
        Initializes a Lead object.

        Args:
        id (int): Unique identifier for the lead.
        name (str): Name of the lead.
        email (str): Email address of the lead.
        phone (str): Phone number of the lead.
        source (str): Source of the lead.
        """
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.source = source
        self.status = "New"  # Default status is "New"
        self.created_at = datetime.now()

    def update_status(self, status: str):
        """Updates the status of the lead."""
        self.status = status

    def __str__(self):
        return f"Lead {self.id}: {self.name}, {self.email}, {self.phone}, {self.source}, {self.status}"


class CommercialLeadsManagementSystem:
    """Manages commercial leads."""

    def __init__(self):
        self.leads: Dict[int, Lead] = {}
        self.next_id = 1

    def add_lead(self, name: str, email: str, phone: str, source: str) -> Lead:
        """
        Adds a new lead to the system.

        Args:
        name (str): Name of the lead.
        email (str): Email address of the lead.
        phone (str): Phone number of the lead.
        source (str): Source of the lead.

        Returns:
        Lead: The newly added lead.
        """
        if not name or not email or not phone or not source:
            raise ValueError("Name, email, phone, and source are required.")

        lead = Lead(self.next_id, name, email, phone, source)
        self.leads[self.next_id] = lead
        self.next_id += 1
        return lead

    def get_lead(self, id: int) -> Lead:
        """
        Retrieves a lead by its ID.

        Args:
        id (int): ID of the lead.

        Returns:
        Lead: The lead with the specified ID, or None if not found.
        """
        return self.leads.get(id)

    def update_lead_status(self, id: int, status: str):
        """
        Updates the status of a lead.

        Args:
        id (int): ID of the lead.
        status (str): New status of the lead.

        Raises:
        ValueError: If the lead is not found.
        """
        lead = self.get_lead(id)
        if lead:
            lead.update_status(status)
        else:
            raise ValueError("Lead not found.")

    def delete_lead(self, id: int):
        """
        Deletes a lead by its ID.

        Args:
        id (int): ID of the lead.

        Raises:
        ValueError: If the lead is not found.
        """
        if id in self.leads:
            del self.leads[id]
        else:
            raise ValueError("Lead not found.")

    def list_leads(self) -> List[Lead]:
        """Returns a list of all leads."""
        return list(self.leads.values())


def main():
    clms = CommercialLeadsManagementSystem()

    # Add leads
    lead1 = clms.add_lead("John Doe", "john.doe@example.com", "123-456-7890", "Social Media")
    lead2 = clms.add_lead("Jane Smith", "jane.smith@example.com", "987-654-3210", "Referral")

    # List leads
    print("Leads:")
    for lead in clms.list_leads():
        print(lead)

    # Update lead status
    clms.update_lead_status(lead1.id, "Contacted")

    # Get lead
    retrieved_lead = clms.get_lead(lead1.id)
    print(f"\nRetrieved Lead: {retrieved_lead}")

    # Delete lead
    clms.delete_lead(lead2.id)

    # List leads again
    print("\nLeads after deletion:")
    for lead in clms.list_leads():
        print(lead)


if __name__ == "__main__":
    main()
```
