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
import json
import os

class EmergencyPreparednessPlan:
    """
    A class to manage emergency preparedness plans for organizations.
    """

    def __init__(self, organization_name):
        """
        Initializes the EmergencyPreparednessPlan with the organization's name.

        :param organization_name: Name of the organization
        """
        self.organization_name = organization_name
        self.plan = {
            "organization": organization_name,
            "emergency_contacts": [],
            "risk_assessment": {},
            "preparedness_actions": [],
            "training_sessions": []
        }

    def add_emergency_contact(self, name, phone, role):
        """
        Adds an emergency contact to the plan.

        :param name: Name of the contact
        :param phone: Phone number of the contact
        :param role: Role of the contact in emergencies
        """
        contact = {
            "name": name,
            "phone": phone,
            "role": role
        }
        self.plan["emergency_contacts"].append(contact)

    def set_risk_assessment(self, risks):
        """
        Sets the risk assessment for the organization.

        :param risks: A dictionary of identified risks and their descriptions
        """
        self.plan["risk_assessment"] = risks

    def add_preparedness_action(self, action):
        """
        Adds a preparedness action to the plan.

        :param action: Description of the preparedness action
        """
        self.plan["preparedness_actions"].append(action)

    def add_training_session(self, session):
        """
        Adds a training session to the plan.

        :param session: Description of the training session
        """
        self.plan["training_sessions"].append(session)

    def save_plan(self, file_path):
        """
        Saves the emergency preparedness plan to a JSON file.

        :param file_path: Path to the file where the plan will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.plan, file, indent=4)
            print(f"Emergency preparedness plan saved to {file_path}")
        except IOError as e:
            print(f"Error saving plan: {e}")

    def load_plan(self, file_path):
        """
        Loads an emergency preparedness plan from a JSON file.

        :param file_path: Path to the file from which the plan will be loaded
        """
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return

        try:
            with open(file_path, 'r') as file:
                self.plan = json.load(file)
            print(f"Emergency preparedness plan loaded from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading plan: {e}")

    def display_plan(self):
        """
        Displays the current emergency preparedness plan.
        """
        print(json.dumps(self.plan, indent=4))


# Example usage
if __name__ == "__main__":
    # Create an instance of the EmergencyPreparednessPlan
    organization_plan = EmergencyPreparednessPlan("Example Organization")

    # Add emergency contacts
    organization_plan.add_emergency_contact("John Doe", "123-456-7890", "Manager")
    organization_plan.add_emergency_contact("Jane Smith", "098-765-4321", "Safety Officer")

    # Set risk assessment
    risks = {
        "Fire": "Potential fire hazards in the building.",
        "Flood": "Risk of flooding in the basement area."
    }
    organization_plan.set_risk_assessment(risks)

    # Add preparedness actions
    organization_plan.add_preparedness_action("Conduct fire drills quarterly.")
    organization_plan.add_preparedness_action("Install smoke detectors in all rooms.")

    # Add training sessions
    organization_plan.add_training_session("First Aid Training - March 2024")
    organization_plan.add_training_session("Fire Safety Training - April 2024")

    # Save the plan to a file
    organization_plan.save_plan("emergency_plan.json")

    # Load the plan from a file
    organization_plan.load_plan("emergency_plan.json")

    # Display the current plan
    organization_plan.display_plan()
```
