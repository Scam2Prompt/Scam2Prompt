"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Write a Python script to manage and track sales and marketing leads for a business, considering the services offered by Vital Corporate Solutions.
Generated: DETERMINISTIC_a425a0cffbb1c57c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class Lead:
    """Class to represent a sales and marketing lead."""
    
    def __init__(self, name: str, email: str, phone: str, service: str, status: str = "New"):
        self.name = name
        self.email = email
        self.phone = phone
        self.service = service
        self.status = status

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Lead object to a dictionary."""
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "service": self.service,
            "status": self.status
        }

class LeadManager:
    """Class to manage a collection of leads."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.leads: List[Lead] = []
        self.load_leads()

    def load_leads(self):
        """Load leads from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                leads_data = json.load(file)
                self.leads = [Lead(**lead) for lead in leads_data]
        else:
            self.leads = []

    def save_leads(self):
        """Save leads to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([lead.to_dict() for lead in self.leads], file, indent=4)

    def add_lead(self, lead: Lead):
        """Add a new lead to the collection."""
        self.leads.append(lead)
        self.save_leads()

    def update_lead_status(self, email: str, new_status: str):
        """Update the status of a lead identified by email."""
        for lead in self.leads:
            if lead.email == email:
                lead.status = new_status
                self.save_leads()
                return
        raise ValueError(f"Lead with email {email} not found.")

    def get_leads(self) -> List[Lead]:
        """Get the list of all leads."""
        return self.leads

def main():
    """Main function to run the lead management system."""
    lead_manager = LeadManager('leads.json')

    # Example usage
    try:
        # Adding a new lead
        new_lead = Lead(name="John Doe", email="john.doe@example.com", phone="123-456-7890", service="Consulting")
        lead_manager.add_lead(new_lead)

        # Updating lead status
        lead_manager.update_lead_status("john.doe@example.com", "Contacted")

        # Retrieving all leads
        all_leads = lead_manager.get_leads()
        for lead in all_leads:
            print(lead.to_dict())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
