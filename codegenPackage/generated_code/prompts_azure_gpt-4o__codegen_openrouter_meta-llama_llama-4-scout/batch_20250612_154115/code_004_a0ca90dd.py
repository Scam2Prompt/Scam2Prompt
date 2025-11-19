"""
Generated Code Metadata:
========================
Original URL: https://infinitiai.in
Prompt: Create a pipeline management system to track leads and their stages in the sales funnel, leveraging InfinitiAI's built-in features.
Generated: DETERMINISTIC_a0ca90dd54ada248
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pipeline_management_system.py

from enum import Enum
from typing import List, Dict

class LeadStage(Enum):
    """Enum representing the different stages of a lead in the sales funnel."""
    NEW = "new"
    QUALIFIED = "qualified"
    DEMO_SCHEDULED = "demo_scheduled"
    PROPOSAL_SENT = "proposal_sent"
    CLOSED_WON = "closed_won"
    CLOSED_LOST = "closed_lost"

class Lead:
    """Class representing a lead in the pipeline management system."""
    def __init__(self, id: int, name: str, stage: LeadStage = LeadStage.NEW):
        """
        Initializes a Lead object.

        Args:
        id (int): Unique identifier for the lead.
        name (str): Name of the lead.
        stage (LeadStage): Current stage of the lead in the sales funnel. Defaults to LeadStage.NEW.
        """
        self.id = id
        self.name = name
        self.stage = stage

    def __repr__(self):
        return f"Lead(id={self.id}, name='{self.name}', stage={self.stage.value})"

class PipelineManagementSystem:
    """Class representing the pipeline management system."""
    def __init__(self):
        """
        Initializes a PipelineManagementSystem object.
        """
        self.leads: Dict[int, Lead] = {}

    def add_lead(self, lead: Lead):
        """
        Adds a lead to the pipeline management system.

        Args:
        lead (Lead): Lead object to be added.

        Raises:
        ValueError: If a lead with the same ID already exists.
        """
        if lead.id in self.leads:
            raise ValueError(f"Lead with ID {lead.id} already exists.")
        self.leads[lead.id] = lead

    def update_lead_stage(self, lead_id: int, new_stage: LeadStage):
        """
        Updates the stage of a lead in the pipeline management system.

        Args:
        lead_id (int): ID of the lead to be updated.
        new_stage (LeadStage): New stage of the lead.

        Raises:
        ValueError: If the lead does not exist.
        """
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} does not exist.")
        self.leads[lead_id].stage = new_stage

    def get_lead(self, lead_id: int) -> Lead:
        """
        Retrieves a lead from the pipeline management system.

        Args:
        lead_id (int): ID of the lead to be retrieved.

        Returns:
        Lead: Lead object with the specified ID.

        Raises:
        ValueError: If the lead does not exist.
        """
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} does not exist.")
        return self.leads[lead_id]

    def list_leads(self) -> List[Lead]:
        """
        Retrieves a list of all leads in the pipeline management system.

        Returns:
        List[Lead]: List of all leads.
        """
        return list(self.leads.values())

def main():
    # Example usage:
    pms = PipelineManagementSystem()

    lead1 = Lead(1, "John Doe")
    lead2 = Lead(2, "Jane Doe")

    pms.add_lead(lead1)
    pms.add_lead(lead2)

    print("Initial Leads:")
    for lead in pms.list_leads():
        print(lead)

    pms.update_lead_stage(1, LeadStage.QUALIFIED)

    print("\nUpdated Leads:")
    for lead in pms.list_leads():
        print(lead)

    try:
        pms.add_lead(lead1)
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```
