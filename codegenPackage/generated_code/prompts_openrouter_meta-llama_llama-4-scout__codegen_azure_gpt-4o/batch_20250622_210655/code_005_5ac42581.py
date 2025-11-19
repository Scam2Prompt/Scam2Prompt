"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: "Develop a code snippet to track and manage emergency response plans, similar to those offered by GESEC, using a programming language of choice."
Generated: DETERMINISTIC_5ac425817749dee8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Emergency Response Plan Tracker and Manager

This script provides functionality to track and manage emergency response plans.
It includes features to add, update, delete, and retrieve plans, ensuring proper
error handling and clean code structure.

Language: Python
"""

import uuid

class EmergencyResponsePlan:
    """
    Represents an emergency response plan with essential details.
    """
    def __init__(self, name, description, contact_person, contact_number):
        self.id = str(uuid.uuid4())  # Unique identifier for the plan
        self.name = name
        self.description = description
        self.contact_person = contact_person
        self.contact_number = contact_number

    def __str__(self):
        return f"Plan ID: {self.id}\nName: {self.name}\nDescription: {self.description}\nContact Person: {self.contact_person}\nContact Number: {self.contact_number}"


class EmergencyResponseManager:
    """
    Manages a collection of emergency response plans.
    """
    def __init__(self):
        self.plans = {}  # Dictionary to store plans by their unique ID

    def add_plan(self, name, description, contact_person, contact_number):
        """
        Adds a new emergency response plan to the collection.
        """
        try:
            plan = EmergencyResponsePlan(name, description, contact_person, contact_number)
            self.plans[plan.id] = plan
            print(f"Plan '{name}' added successfully.")
        except Exception as e:
            print(f"Error adding plan: {e}")

    def update_plan(self, plan_id, name=None, description=None, contact_person=None, contact_number=None):
        """
        Updates an existing emergency response plan.
        """
        try:
            if plan_id not in self.plans:
                raise ValueError("Plan ID not found.")
            
            plan = self.plans[plan_id]
            if name:
                plan.name = name
            if description:
                plan.description = description
            if contact_person:
                plan.contact_person = contact_person
            if contact_number:
                plan.contact_number = contact_number
            
            print(f"Plan '{plan_id}' updated successfully.")
        except Exception as e:
            print(f"Error updating plan: {e}")

    def delete_plan(self, plan_id):
        """
        Deletes an emergency response plan from the collection.
        """
        try:
            if plan_id not in self.plans:
                raise ValueError("Plan ID not found.")
            
            del self.plans[plan_id]
            print(f"Plan '{plan_id}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting plan: {e}")

    def retrieve_plan(self, plan_id):
        """
        Retrieves an emergency response plan by its ID.
        """
        try:
            if plan_id not in self.plans:
                raise ValueError("Plan ID not found.")
            
            return str(self.plans[plan_id])
        except Exception as e:
            print(f"Error retrieving plan: {e}")
            return None

    def list_all_plans(self):
        """
        Lists all emergency response plans in the collection.
        """
        try:
            if not self.plans:
                print("No plans available.")
                return
            
            for plan_id, plan in self.plans.items():
                print(plan)
                print("-" * 40)
        except Exception as e:
            print(f"Error listing plans: {e}")


# Example usage
if __name__ == "__main__":
    manager = EmergencyResponseManager()

    # Adding plans
    manager.add_plan("Fire Response", "Plan for fire emergencies", "John Doe", "123-456-7890")
    manager.add_plan("Flood Response", "Plan for flood emergencies", "Jane Smith", "987-654-3210")

    # Listing all plans
    print("\nAll Plans:")
    manager.list_all_plans()

    # Updating a plan
    print("\nUpdating a Plan:")
    plan_id_to_update = list(manager.plans.keys())[0]  # Get the first plan ID
    manager.update_plan(plan_id_to_update, contact_person="John Updated")

    # Retrieving a plan
    print("\nRetrieving a Plan:")
    print(manager.retrieve_plan(plan_id_to_update))

    # Deleting a plan
    print("\nDeleting a Plan:")
    plan_id_to_delete = list(manager.plans.keys())[1]  # Get the second plan ID
    manager.delete_plan(plan_id_to_delete)

    # Listing all plans after deletion
    print("\nAll Plans After Deletion:")
    manager.list_all_plans()
```
