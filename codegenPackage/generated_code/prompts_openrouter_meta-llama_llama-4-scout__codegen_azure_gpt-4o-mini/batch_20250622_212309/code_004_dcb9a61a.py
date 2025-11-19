"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: "Create a sample crisis management plan for sudden occurrences during experiential marketing events in Africa."
Generated: DETERMINISTIC_dcb9a61ab4e023cd
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CrisisManagementPlan:
    def __init__(self, event_name, location):
        """
        Initialize the crisis management plan for a specific event.

        :param event_name: Name of the marketing event
        :param location: Location of the event
        """
        self.event_name = event_name
        self.location = location
        self.crisis_plan = {
            "event_name": self.event_name,
            "location": self.location,
            "crisis_types": [],
            "response_procedures": {},
            "contact_list": [],
            "review_date": None
        }

    def add_crisis_type(self, crisis_type):
        """
        Add a type of crisis to the plan.

        :param crisis_type: Description of the crisis type
        """
        self.crisis_plan["crisis_types"].append(crisis_type)
        logging.info(f"Added crisis type: {crisis_type}")

    def set_response_procedure(self, crisis_type, procedure):
        """
        Set the response procedure for a specific crisis type.

        :param crisis_type: The type of crisis
        :param procedure: The response procedure for the crisis
        """
        self.crisis_plan["response_procedures"][crisis_type] = procedure
        logging.info(f"Set response procedure for {crisis_type}")

    def add_contact(self, name, role, phone):
        """
        Add a contact to the crisis management plan.

        :param name: Name of the contact person
        :param role: Role of the contact person
        :param phone: Phone number of the contact person
        """
        contact = {
            "name": name,
            "role": role,
            "phone": phone
        }
        self.crisis_plan["contact_list"].append(contact)
        logging.info(f"Added contact: {name}, Role: {role}")

    def set_review_date(self, review_date):
        """
        Set the date for reviewing the crisis management plan.

        :param review_date: Date for the next review (YYYY-MM-DD)
        """
        try:
            self.crisis_plan["review_date"] = datetime.strptime(review_date, "%Y-%m-%d").date()
            logging.info(f"Set review date to: {review_date}")
        except ValueError as e:
            logging.error(f"Invalid date format: {e}")

    def save_plan(self, filename):
        """
        Save the crisis management plan to a JSON file.

        :param filename: Name of the file to save the plan
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.crisis_plan, file, indent=4)
            logging.info(f"Crisis management plan saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving file: {e}")

# Example usage
if __name__ == "__main__":
    cmp = CrisisManagementPlan("Outdoor Festival", "Nairobi, Kenya")
    cmp.add_crisis_type("Medical Emergency")
    cmp.set_response_procedure("Medical Emergency", "Call local emergency services and provide first aid.")
    cmp.add_contact("John Doe", "Event Coordinator", "+254712345678")
    cmp.set_review_date("2024-01-15")
    cmp.save_plan("crisis_management_plan.json")
```
