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
"""
Commercial Leads Management System (CLMS)

This script implements a simple CLMS to manage leads, track their status, and provide
key functionalities to enhance sales efforts. Features include adding, updating, 
viewing, and deleting leads. Data is stored persistently using JSON files.

Dependencies:
- Python 3.x
"""

import json
import os

# Constants for file storage
DATA_FILE = "leads_data.json"

class Lead:
    """
    Represents a commercial lead with relevant attributes.
    """
    def __init__(self, lead_id, name, email, status="New"):
        self.lead_id = lead_id
        self.name = name
        self.email = email
        self.status = status

    def to_dict(self):
        """
        Converts the Lead object to a dictionary for storage.
        """
        return {
            "lead_id": self.lead_id,
            "name": self.name,
            "email": self.email,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a Lead object from a dictionary.
        """
        return Lead(data["lead_id"], data["name"], data["email"], data["status"])


class CLMS:
    """
    Commercial Leads Management System.
    Handles operations related to leads management.
    """
    def __init__(self):
        self.leads = {}
        self._load_data()

    def _load_data(self):
        """
        Loads leads data from the persistent storage file.
        """
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as file:
                    leads_data = json.load(file)
                    for lead_id, lead_info in leads_data.items():
                        self.leads[lead_id] = Lead.from_dict(lead_info)
            except (json.JSONDecodeError, IOError):
                print("Error loading leads data. Starting with an empty database.")

    def _save_data(self):
        """
        Saves leads data to the persistent storage file.
        """
        try:
            with open(DATA_FILE, "w") as file:
                json.dump({lead_id: lead.to_dict() for lead_id, lead in self.leads.items()}, file, indent=4)
        except IOError:
            print("Error saving leads data.")

    def add_lead(self, name, email):
        """
        Adds a new lead to the system.
        """
        lead_id = str(len(self.leads) + 1)
        if email in [lead.email for lead in self.leads.values()]:
            print("Error: Lead with this email already exists.")
            return
        new_lead = Lead(lead_id, name, email)
        self.leads[lead_id] = new_lead
        self._save_data()
        print(f"Lead added successfully. Lead ID: {lead_id}")

    def update_lead_status(self, lead_id, status):
        """
        Updates the status of an existing lead.
        """
        lead = self.leads.get(lead_id)
        if lead:
            lead.status = status
            self._save_data()
            print("Lead status updated successfully.")
        else:
            print("Error: Lead not found.")

    def view_leads(self):
        """
        Displays all leads in the system.
        """
        if not self.leads:
            print("No leads found.")
            return
        for lead in self.leads.values():
            print(f"ID: {lead.lead_id}, Name: {lead.name}, Email: {lead.email}, Status: {lead.status}")

    def delete_lead(self, lead_id):
        """
        Deletes a lead from the system.
        """
        if lead_id in self.leads:
            del self.leads[lead_id]
            self._save_data()
            print("Lead deleted successfully.")
        else:
            print("Error: Lead not found.")

# Main CLMS Execution
if __name__ == "__main__":
    clms = CLMS()

    # Example interactions
    print("Welcome to the Commercial Leads Management System (CLMS)")
    while True:
        print("\nOptions:")
        print("1. Add Lead")
        print("2. Update Lead Status")
        print("3. View Leads")
        print("4. Delete Lead")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            name = input("Enter lead name: ")
            email = input("Enter lead email: ")
            clms.add_lead(name, email)
        elif choice == "2":
            lead_id = input("Enter lead ID: ")
            status = input("Enter new status: ")
            clms.update_lead_status(lead_id, status)
        elif choice == "3":
            clms.view_leads()
        elif choice == "4":
            lead_id = input("Enter lead ID to delete: ")
            clms.delete_lead(lead_id)
        elif choice == "5":
            print("Exiting CLMS. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
```
