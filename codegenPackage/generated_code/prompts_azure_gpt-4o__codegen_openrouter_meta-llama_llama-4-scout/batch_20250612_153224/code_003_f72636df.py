"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: Write a script to manage emergency preparedness plans for organizations, incorporating key elements from GESEC's "Plan y Preparación ante Emergencias" service.
Generated: DETERMINISTIC_f72636dfbb5b7d63
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# emergency_preparedness_plan.py

import datetime
import json

class EmergencyPreparednessPlan:
    def __init__(self, organization_name, plan_name):
        """
        Initialize an emergency preparedness plan.

        Args:
            organization_name (str): Name of the organization.
            plan_name (str): Name of the plan.
        """
        self.organization_name = organization_name
        self.plan_name = plan_name
        self.plan_elements = {
            "emergency_contacts": [],
            "emergency_procedures": [],
            "evacuation_routes": [],
            "emergency_equipment": []
        }

    def add_emergency_contact(self, name, phone_number, email):
        """
        Add an emergency contact to the plan.

        Args:
            name (str): Name of the contact.
            phone_number (str): Phone number of the contact.
            email (str): Email of the contact.
        """
        self.plan_elements["emergency_contacts"].append({
            "name": name,
            "phone_number": phone_number,
            "email": email
        })

    def add_emergency_procedure(self, procedure):
        """
        Add an emergency procedure to the plan.

        Args:
            procedure (str): Description of the procedure.
        """
        self.plan_elements["emergency_procedures"].append(procedure)

    def add_evacuation_route(self, route):
        """
        Add an evacuation route to the plan.

        Args:
            route (str): Description of the route.
        """
        self.plan_elements["evacuation_routes"].append(route)

    def add_emergency_equipment(self, equipment):
        """
        Add emergency equipment to the plan.

        Args:
            equipment (str): Description of the equipment.
        """
        self.plan_elements["emergency_equipment"].append(equipment)

    def save_plan(self, filename):
        """
        Save the plan to a JSON file.

        Args:
            filename (str): Name of the file to save to.

        Raises:
            Exception: If the file cannot be written.
        """
        try:
            with open(filename, "w") as f:
                json.dump(self.plan_elements, f, indent=4)
        except Exception as e:
            print(f"Error saving plan: {e}")

    def load_plan(self, filename):
        """
        Load a plan from a JSON file.

        Args:
            filename (str): Name of the file to load from.

        Raises:
            Exception: If the file cannot be read.
        """
        try:
            with open(filename, "r") as f:
                self.plan_elements = json.load(f)
        except Exception as e:
            print(f"Error loading plan: {e}")


def main():
    plan = EmergencyPreparednessPlan("Example Organization", "Emergency Preparedness Plan")

    while True:
        print("\nEmergency Preparedness Plan Management")
        print("1. Add emergency contact")
        print("2. Add emergency procedure")
        print("3. Add evacuation route")
        print("4. Add emergency equipment")
        print("5. Save plan")
        print("6. Load plan")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            plan.add_emergency_contact(name, phone_number, email)
        elif choice == "2":
            procedure = input("Enter emergency procedure: ")
            plan.add_emergency_procedure(procedure)
        elif choice == "3":
            route = input("Enter evacuation route: ")
            plan.add_evacuation_route(route)
        elif choice == "4":
            equipment = input("Enter emergency equipment: ")
            plan.add_emergency_equipment(equipment)
        elif choice == "5":
            filename = input("Enter filename to save to: ")
            plan.save_plan(filename)
        elif choice == "6":
            filename = input("Enter filename to load from: ")
            plan.load_plan(filename)
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
