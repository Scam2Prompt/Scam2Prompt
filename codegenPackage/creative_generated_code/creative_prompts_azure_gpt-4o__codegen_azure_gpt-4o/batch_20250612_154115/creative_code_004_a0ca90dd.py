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
import datetime

class Lead:
    """
    Class representing a lead in the pipeline.
    Attributes:
        lead_id (int): Unique identifier for the lead.
        name (str): Name of the lead.
        email (str): Email address of the lead.
        stage (str): Current stage of the lead in the sales funnel.
        created_at (datetime): Timestamp of when the lead was created.
        updated_at (datetime): Timestamp of when the lead was last updated.
    """
    def __init__(self, lead_id, name, email, stage="Prospect"):
        self.lead_id = lead_id
        self.name = name
        self.email = email
        self.stage = stage
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def update_stage(self, new_stage):
        """
        Updates the stage of the lead and modifies the updated_at timestamp.
        Args:
            new_stage (str): The new stage to assign to the lead.
        """
        self.stage = new_stage
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        """
        Returns a string representation of the lead details.
        """
        return (f"Lead ID: {self.lead_id}, Name: {self.name}, Email: {self.email}, "
                f"Stage: {self.stage}, Created At: {self.created_at}, Updated At: {self.updated_at}")

class Pipeline:
    """
    Class representing the pipeline management system.
    Attributes:
        leads (dict): Dictionary to store leads with their lead_id as the key.
    """
    def __init__(self):
        self.leads = {}

    def add_lead(self, lead_id, name, email):
        """
        Adds a new lead to the pipeline.
        Args:
            lead_id (int): Unique identifier for the lead.
            name (str): Name of the lead.
            email (str): Email address of the lead.
        """
        if lead_id in self.leads:
            raise ValueError(f"Lead with ID {lead_id} already exists.")
        self.leads[lead_id] = Lead(lead_id, name, email)
    
    def update_lead_stage(self, lead_id, new_stage):
        """
        Updates the stage of an existing lead.
        Args:
            lead_id (int): Unique identifier for the lead.
            new_stage (str): The new stage to assign to the lead.
        """
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} not found.")
        self.leads[lead_id].update_stage(new_stage)
    
    def remove_lead(self, lead_id):
        """
        Removes a lead from the pipeline.
        Args:
            lead_id (int): Unique identifier for the lead.
        """
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} not found.")
        del self.leads[lead_id]
    
    def get_lead(self, lead_id):
        """
        Retrieves the details of a specific lead.
        Args:
            lead_id (int): Unique identifier for the lead.
        Returns:
            Lead: The lead object.
        """
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} not found.")
        return self.leads[lead_id]
    
    def list_leads(self):
        """
        Lists all the leads in the pipeline.
        Returns:
            list: List of all leads in the pipeline.
        """
        return list(self.leads.values())

# Error handling example
if __name__ == "__main__":
    try:
        pipeline = Pipeline()
        
        # Adding leads to the pipeline
        pipeline.add_lead(1, "Alice Johnson", "alice@example.com")
        pipeline.add_lead(2, "Bob Smith", "bob@example.com")

        # Updating lead stage
        pipeline.update_lead_stage(1, "Contacted")
        
        # Listing all leads
        for lead in pipeline.list_leads():
            print(lead)
        
        # Removing a lead
        pipeline.remove_lead(2)
        
        # Attempting to get details of a non-existent lead
        print(pipeline.get_lead(2))  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
```
