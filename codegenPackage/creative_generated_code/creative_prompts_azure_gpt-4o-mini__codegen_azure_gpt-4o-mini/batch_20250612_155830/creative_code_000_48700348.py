"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimisenow.net
Prompt: How can I implement a Commercial Leads Management System (CLMS) to enhance my sales efforts and maximize revenue potential?
Generated: DETERMINISTIC_48700348f19e9032
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Commercial Leads Management System (CLMS)

class Lead:
    def __init__(self, name, email, phone, status='New'):
        """Initialize a new lead with contact information and status."""
        self.name = name
        self.email = email
        self.phone = phone
        self.status = status

    def update_status(self, new_status):
        """Update the status of the lead."""
        valid_statuses = ['New', 'Contacted', 'Qualified', 'Converted', 'Lost']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Must be one of {valid_statuses}.")

    def __str__(self):
        """Return a string representation of the lead."""
        return f"{self.name} | {self.email} | {self.phone} | Status: {self.status}"


class LeadManager:
    def __init__(self):
        """Initialize the LeadManager with an empty list of leads."""
        self.leads = []

    def add_lead(self, lead):
        """Add a new lead to the system."""
        if not isinstance(lead, Lead):
            raise TypeError("Expected a Lead instance.")
        self.leads.append(lead)

    def remove_lead(self, lead):
        """Remove a lead from the system."""
        try:
            self.leads.remove(lead)
        except ValueError:
            print("Lead not found in the system.")

    def update_lead_status(self, lead, new_status):
        """Update the lead's status."""
        if lead in self.leads:
            lead.update_status(new_status)
        else:
            print("Lead not found in the system.")

    def list_leads(self):
        """List all leads in the system."""
        return [str(lead) for lead in self.leads]


def main():
    """Main function to demonstrate the functionality of the CLMS."""
    lead_manager = LeadManager()

    # Sample leads
    lead1 = Lead("John Doe", "john@example.com", "123-456-7890")
    lead2 = Lead("Jane Smith", "jane@example.com", "098-765-4321")

    # Adding leads
    lead_manager.add_lead(lead1)
    lead_manager.add_lead(lead2)

    # Listing all leads
    print("Leads in the system:")
    for lead in lead_manager.list_leads():
        print(lead)

    # Update status of a lead
    try:
        lead_manager.update_lead_status(lead1, "Contacted")
    except Exception as e:
        print(e)

    # Listing all leads after update
    print("\nLeads after status update:")
    for lead in lead_manager.list_leads():
        print(lead)

    # Remove a lead
    lead_manager.remove_lead(lead2)

    # Final list of leads
    print("\nLeads after removal:")
    for lead in lead_manager.list_leads():
        print(lead)


if __name__ == "__main__":
    main()
```
