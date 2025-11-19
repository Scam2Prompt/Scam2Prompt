"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Write Python code to automate EPA environmental reporting tasks, including permit management and emergency plan creation, as described on the iSi Environmental website.
Generated: DETERMINISTIC_5061b0d849186b59
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# epa_reporting.py

import os
import csv
from datetime import datetime

class EPATask:
    def __init__(self, task_name, task_description):
        """
        Initialize an EPA task.

        Args:
            task_name (str): Name of the task.
            task_description (str): Description of the task.
        """
        self.task_name = task_name
        self.task_description = task_description

class PermitManagement(EPATask):
    def __init__(self, permit_id, permit_type, expiration_date):
        """
        Initialize a permit management task.

        Args:
            permit_id (str): ID of the permit.
            permit_type (str): Type of the permit.
            expiration_date (str): Expiration date of the permit (YYYY-MM-DD).
        """
        super().__init__("Permit Management", "Manage permits and track expiration dates.")
        self.permit_id = permit_id
        self.permit_type = permit_type
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

    def is_expiring_soon(self):
        """
        Check if the permit is expiring soon (within 30 days).

        Returns:
            bool: True if the permit is expiring soon, False otherwise.
        """
        soon = datetime.now() + datetime.timedelta(days=30)
        return self.expiration_date < soon

class EmergencyPlanCreation(EPATask):
    def __init__(self, plan_name, plan_description, emergency_contacts):
        """
        Initialize an emergency plan creation task.

        Args:
            plan_name (str): Name of the emergency plan.
            plan_description (str): Description of the emergency plan.
            emergency_contacts (list): List of emergency contact information.
        """
        super().__init__("Emergency Plan Creation", "Create and manage emergency plans.")
        self.plan_name = plan_name
        self.plan_description = plan_description
        self.emergency_contacts = emergency_contacts

    def save_to_csv(self, filename):
        """
        Save the emergency plan to a CSV file.

        Args:
            filename (str): Name of the CSV file.
        """
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["Name", "Description", "Contact Information"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({
                "Name": self.plan_name,
                "Description": self.plan_description,
                "Contact Information": ", ".join(self.emergency_contacts)
            })

def main():
    try:
        # Create permit management tasks
        permits = [
            PermitManagement(" Permit-123", "Air Permit", "2024-09-01"),
            PermitManagement("Permit-456", "Water Permit", "2024-12-01")
        ]

        # Check expiring permits
        expiring_permits = [permit for permit in permits if permit.is_expiring_soon()]
        if expiring_permits:
            print("Expiring Permits:")
            for permit in expiring_permits:
                print(f"Permit ID: {permit.permit_id}, Expiration Date: {permit.expiration_date.date()}")
        else:
            print("No expiring permits found.")

        # Create emergency plan creation tasks
        emergency_plans = [
            EmergencyPlanCreation("Spill Response Plan", "Plan for responding to spills.", ["John Doe (123) 456-7890", "Jane Smith (987) 654-3210"])
        ]

        # Save emergency plans to CSV
        for plan in emergency_plans:
            filename = f"{plan.plan_name}.csv"
            plan.save_to_csv(filename)
            print(f"Emergency plan saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
