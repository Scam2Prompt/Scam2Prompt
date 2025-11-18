"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gesec.com.co
Prompt: Write a script to manage emergency preparedness plans for organizations, incorporating key elements from GESEC's "Plan y Preparación ante Emergencias" service.
Generated: DETERMINISTIC_f72636dfbb5b7d63
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class EmergencyPreparednessPlan:
    """
    Class to manage emergency preparedness plans for organizations.
    """

    def __init__(self, organization_name):
        """
        Initializes the EmergencyPreparednessPlan instance.

        Args:
            organization_name (str): The name of the organization.
        """
        self.organization_name = organization_name
        self.plan = {
            'organization': organization_name,
            'emergency_contacts': [],
            'risks_assessment': {},
            'emergency_response': {},
            'training_schedule': []
        }
        self.file_path = f"{organization_name}_preparedness_plan.json"

    def add_emergency_contact(self, name, phone, role):
        """
        Adds an emergency contact to the plan.

        Args:
            name (str): Name of the contact person.
            phone (str): Phone number of the contact person.
            role (str): Role of the contact person in emergency situations.
        """
        contact = {
            'name': name,
            'phone': phone,
            'role': role
        }
        self.plan['emergency_contacts'].append(contact)

    def set_risk_assessment(self, risk, description):
        """
        Sets the risk assessment for the organization.

        Args:
            risk (str): The identified risk.
            description (str): Description of the risk.
        """
        self.plan['risks_assessment'][risk] = description

    def add_emergency_response(self, emergency_type, response_plan):
        """
        Adds an emergency response plan for a specific type of emergency.

        Args:
            emergency_type (str): The type of emergency (e.g., fire, flood).
            response_plan (str): The plan to respond to the emergency.
        """
        self.plan['emergency_response'][emergency_type] = response_plan

    def add_training(self, date, topic, participants):
        """
        Adds a training session to the preparedness plan.

        Args:
            date (str): Date of the training session.
            topic (str): The topic of the training.
            participants (list): List of participants in the training.
        """
        training = {
            'date': date,
            'topic': topic,
            'participants': participants
        }
        self.plan['training_schedule'].append(training)

    def save_plan(self):
        """
        Saves the emergency preparedness plan to a JSON file.
        """
        try:
            with open(self.file_path, 'w') as json_file:
                json.dump(self.plan, json_file, indent=4)
            print(f"Emergency preparedness plan saved to {self.file_path}.")
        except IOError as e:
            print(f"Error saving the plan: {e}")

    def load_plan(self):
        """
        Loads the emergency preparedness plan from a JSON file.
        """
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as json_file:
                    self.plan = json.load(json_file)
                print(f"Emergency preparedness plan loaded from {self.file_path}.")
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading the plan: {e}")
        else:
            print("No existing plan found to load.")

if __name__ == "__main__":
    # Example usage
    org_name = "Sample Organization"
    preparedness_plan = EmergencyPreparednessPlan(org_name)

    # Load existing plan if available
    preparedness_plan.load_plan()
    
    # Add emergency contacts
    preparedness_plan.add_emergency_contact("John Doe", "123-456-7890", "Safety Officer")
    
    # Set risk assessments
    preparedness_plan.set_risk_assessment("Fire", "High risk due to proximity to forests.")
    
    # Add emergency response plans
    preparedness_plan.add_emergency_response("Fire", "Evacuate the building and call 911.")
    
    # Schedule training
    preparedness_plan.add_training("2023-10-30", "Fire Safety Training", ["John Doe", "Jane Smith"])
    
    # Save the updated plan
    preparedness_plan.save_plan()
```
