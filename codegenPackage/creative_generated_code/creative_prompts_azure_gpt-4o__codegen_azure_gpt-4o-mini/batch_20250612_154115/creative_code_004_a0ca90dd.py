"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Create a pipeline management system to track leads and their stages in the sales funnel, leveraging InfinitiAI's built-in features.
Generated: DETERMINISTIC_a0ca90dd54ada248
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict, Optional

class Lead:
    """Class representing a sales lead."""
    
    def __init__(self, lead_id: int, name: str, email: str):
        """
        Initializes a new lead.
        
        :param lead_id: Unique identifier for the lead.
        :param name: Name of the lead.
        :param email: Email address of the lead.
        """
        self.lead_id = lead_id
        self.name = name
        self.email = email
        self.stage = "Initial Contact"  # Default stage
        
    def update_stage(self, new_stage: str):
        """
        Updates the stage of the lead.
        
        :param new_stage: New stage to assign to the lead.
        """
        self.stage = new_stage

    def __repr__(self):
        return f"Lead({self.lead_id}, {self.name}, {self.email}, {self.stage})"


class Pipeline:
    """Class representing a sales pipeline."""
    
    def __init__(self):
        """Initializes an empty pipeline."""
        self.leads: Dict[int, Lead] = {}  # Dictionary to store leads by ID

    def add_lead(self, lead: Lead):
        """
        Adds a new lead to the pipeline.
        
        :param lead: Lead object to be added.
        :raises ValueError: If lead ID already exists.
        """
        if lead.lead_id in self.leads:
            raise ValueError(f"Lead with ID {lead.lead_id} already exists.")
        self.leads[lead.lead_id] = lead

    def update_lead_stage(self, lead_id: int, new_stage: str):
        """
        Updates the stage of a lead by its ID.
        
        :param lead_id: Unique identifier for the lead.
        :param new_stage: New stage to assign to the lead.
        :raises KeyError: If lead ID does not exist.
        """
        if lead_id not in self.leads:
            raise KeyError(f"Lead with ID {lead_id} not found.")
        self.leads[lead_id].update_stage(new_stage)

    def get_leads(self) -> List[Lead]:
        """Returns a list of all leads in the pipeline."""
        return list(self.leads.values())

    def __repr__(self):
        return f"Pipeline({self.leads})"


# Example usage
if __name__ == "__main__":
    # Create a new pipeline
    pipeline = Pipeline()

    # Add some leads
    lead1 = Lead(1, "Alice Smith", "alice@example.com")
    lead2 = Lead(2, "Bob Johnson", "bob@example.com")

    # Add leads to the pipeline
    try:
        pipeline.add_lead(lead1)
        pipeline.add_lead(lead2)
    except ValueError as e:
        print(f"Error adding lead: {e}")

    # Update a lead's stage
    try:
        pipeline.update_lead_stage(1, "Qualified")
    except KeyError as e:
        print(f"Error updating lead stage: {e}")

    # Print all leads in the pipeline
    for lead in pipeline.get_leads():
        print(lead)
```
