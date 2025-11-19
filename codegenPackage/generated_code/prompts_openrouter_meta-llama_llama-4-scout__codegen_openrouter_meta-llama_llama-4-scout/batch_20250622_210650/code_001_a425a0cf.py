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
# lead_tracker.py

class Lead:
    """Represents a sales or marketing lead."""

    def __init__(self, name, email, phone, service):
        """
        Initializes a Lead object.

        Args:
            name (str): Lead's name.
            email (str): Lead's email address.
            phone (str): Lead's phone number.
            service (str): Service offered by Vital Corporate Solutions.
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.service = service
        self.status = "New"  # Initial status

    def update_status(self, status):
        """Updates the lead's status."""
        self.status = status


class LeadTracker:
    """Manages and tracks sales and marketing leads."""

    def __init__(self):
        """Initializes a LeadTracker object."""
        self.leads = []

    def add_lead(self, lead):
        """
        Adds a new lead to the tracker.

        Args:
            lead (Lead): Lead object to add.
        """
        self.leads.append(lead)

    def view_leads(self):
        """Displays all leads in the tracker."""
        for i, lead in enumerate(self.leads, start=1):
            print(f"Lead {i}:")
            print(f"Name: {lead.name}")
            print(f"Email: {lead.email}")
            print(f"Phone: {lead.phone}")
            print(f"Service: {lead.service}")
            print(f"Status: {lead.status}")
            print("-" * 30)

    def update_lead_status(self, lead_name, new_status):
        """
        Updates the status of a lead.

        Args:
            lead_name (str): Name of the lead to update.
            new_status (str): New status of the lead.
        """
        for lead in self.leads:
            if lead.name == lead_name:
                lead.update_status(new_status)
                print(f"Lead '{lead_name}' status updated to '{new_status}'.")
                return
        print(f"Lead '{lead_name}' not found.")

    def delete_lead(self, lead_name):
        """
        Deletes a lead from the tracker.

        Args:
            lead_name (str): Name of the lead to delete.
        """
        for lead in self.leads:
            if lead.name == lead_name:
                self.leads.remove(lead)
                print(f"Lead '{lead_name}' deleted.")
                return
        print(f"Lead '{lead_name}' not found.")


def main():
    tracker = LeadTracker()

    while True:
        print("\nVital Corporate Solutions Lead Tracker")
        print("1. Add Lead")
        print("2. View Leads")
        print("3. Update Lead Status")
        print("4. Delete Lead")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter lead's name: ")
                email = input("Enter lead's email: ")
                phone = input("Enter lead's phone: ")
                service = input("Enter service (e.g., HR, Marketing, IT): ")
                lead = Lead(name, email, phone, service)
                tracker.add_lead(lead)
                print(f"Lead '{name}' added.")

            elif choice == "2":
                tracker.view_leads()

            elif choice == "3":
                lead_name = input("Enter lead's name: ")
                new_status = input("Enter new status (e.g., New, Qualified, Converted): ")
                tracker.update_lead_status(lead_name, new_status)

            elif choice == "4":
                lead_name = input("Enter lead's name: ")
                tracker.delete_lead(lead_name)

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid option. Please choose a valid option.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
