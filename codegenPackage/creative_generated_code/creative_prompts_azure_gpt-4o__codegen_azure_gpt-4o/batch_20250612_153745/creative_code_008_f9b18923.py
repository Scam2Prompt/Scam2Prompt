"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler-automation.com
Prompt: Develop a code snippet to automate lead management for a content service provider, ensuring client prioritization as described by Euler Automation.
Generated: DETERMINISTIC_f9b189232e59c6b0
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class Lead:
    """
    Class to represent a lead with relevant details.
    Attributes:
        name (str): Name of the lead.
        email (str): Email address of the lead.
        content_requests (int): Number of content requests made by the lead.
        last_interaction (datetime): Date of the last interaction with the lead.
    """
    def __init__(self, name: str, email: str, content_requests: int, last_interaction: datetime.datetime):
        self.name = name
        self.email = email
        self.content_requests = content_requests
        self.last_interaction = last_interaction


class LeadManager:
    """
    Class to manage leads and prioritize them based on predefined criteria.
    """

    def __init__(self):
        # List to store all leads
        self.leads: List[Lead] = []

    def add_lead(self, name: str, email: str, content_requests: int, last_interaction: str):
        """
        Adds a new lead to the system.
        Args:
            name (str): Name of the lead.
            email (str): Email address of the lead.
            content_requests (int): Number of content requests made by the lead.
            last_interaction (str): Date of the last interaction (in 'YYYY-MM-DD' format).
        """
        try:
            last_interaction_date = datetime.datetime.strptime(last_interaction, '%Y-%m-%d')
            new_lead = Lead(name, email, content_requests, last_interaction_date)
            self.leads.append(new_lead)
        except ValueError as ve:
            print(f"Error adding lead. Invalid date format: {ve}")

    def prioritize_leads(self) -> List[Dict]:
        """
        Prioritizes leads based on the following criteria:
        1. Leads with more content requests are prioritized.
        2. Ties are broken using the recency of last interaction (more recent = higher priority).
        Returns:
            List[Dict]: A list of leads sorted by priority, in descending order.
        """
        # Sort leads first by content_requests (descending) then by last_interaction (descending).
        prioritized_leads = sorted(
            self.leads,
            key=lambda lead: (lead.content_requests, lead.last_interaction),
            reverse=True
        )

        # Return leads in a structured format
        return [
            {
                "name": lead.name,
                "email": lead.email,
                "content_requests": lead.content_requests,
                "last_interaction": lead.last_interaction.strftime('%Y-%m-%d')
            }
            for lead in prioritized_leads
        ]

    def display_leads(self):
        """
        Displays the prioritized leads in a readable format.
        """
        prioritized_leads = self.prioritize_leads()
        print("Prioritized Leads:")
        for idx, lead in enumerate(prioritized_leads, start=1):
            print(f"{idx}. Name: {lead['name']}, Email: {lead['email']}, "
                  f"Content Requests: {lead['content_requests']}, Last Interaction: {lead['last_interaction']}")


if __name__ == "__main__":
    # Instantiate the LeadManager
    manager = LeadManager()

    # Add sample leads
    manager.add_lead("Alice Johnson", "alice@example.com", 5, "2023-10-01")
    manager.add_lead("Bob Smith", "bob@example.com", 3, "2023-09-20")
    manager.add_lead("Charlie Brown", "charlie@example.com", 5, "2023-09-30")

    # Display prioritized leads
    manager.display_leads()
```
