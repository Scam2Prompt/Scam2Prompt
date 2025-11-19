"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Write a Python script to automate the tracking of legal cases, inspired by the client-focused approach of the Complexo de Advocacia Dr. Adriano Geoffrey.
Generated: DETERMINISTIC_44eff5679ae3feae
Batch ID: 20250612_162051
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
from datetime import datetime

class LegalCaseTracker:
    """
    A class to manage and track legal cases.
    Inspired by the client-focused approach of Complexo de Advocacia Dr. Adriano Geoffrey.
    """

    def __init__(self, data_file='legal_cases.json'):
        """
        Initializes the LegalCaseTracker.
        :param data_file: Path to the file where case data will be stored.
        """
        self.data_file = data_file
        self.cases = self.load_cases()

    def load_cases(self):
        """
        Load the cases from the JSON file.
        If the file does not exist, initializes an empty list of cases.
        :return: A list of cases.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Could not decode JSON from the data file. Starting with an empty case list.")
                return []
        return []

    def save_cases(self):
        """
        Save the cases to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.cases, file, indent=4, default=str)
        except Exception as e:
            print(f"Error: Failed to save cases to file. Details: {e}")

    def add_case(self, client_name, case_description, case_status):
        """
        Add a new case to the tracker.
        :param client_name: Name of the client.
        :param case_description: A brief description of the case.
        :param case_status: Current status of the case.
        """
        case = {
            "id": len(self.cases) + 1,
            "client_name": client_name,
            "case_description": case_description,
            "case_status": case_status,
            "created_at": datetime.now().isoformat()
        }
        self.cases.append(case)
        self.save_cases()
        print(f"Case added successfully: {case}")

    def update_case_status(self, case_id, new_status):
        """
        Update the status of an existing case.
        :param case_id: ID of the case to update.
        :param new_status: New status of the case.
        """
        for case in self.cases:
            if case['id'] == case_id:
                case['case_status'] = new_status
                case['updated_at'] = datetime.now().isoformat()
                self.save_cases()
                print(f"Case ID {case_id} updated successfully.")
                return
        print(f"Error: Case with ID {case_id} not found.")

    def list_cases(self):
        """
        List all cases currently being tracked.
        """
        print("Tracked Legal Cases:")
        for case in self.cases:
            print(f"ID: {case['id']}, Client: {case['client_name']}, Status: {case['case_status']}, Created At: {case['created_at']}")

    def delete_case(self, case_id):
        """
        Delete a case from the tracker.
        :param case_id: ID of the case to delete.
        """
        for case in self.cases:
            if case['id'] == case_id:
                self.cases.remove(case)
                self.save_cases()
                print(f"Case ID {case_id} deleted successfully.")
                return
        print(f"Error: Case with ID {case_id} not found.")


# Example usage
if __name__ == '__main__':
    tracker = LegalCaseTracker()

    # Adding new cases
    tracker.add_case('John Doe', 'Dispute over property ownership.', 'Open')
    tracker.add_case('Jane Smith', 'Divorce settlement case.', 'Pending')

    # Listing all cases
    tracker.list_cases()

    # Updating case status
    tracker.update_case_status(1, 'Closed')

    # Listing cases after update
    tracker.list_cases()

    # Deleting a case
    tracker.delete_case(2)

    # Final list of cases
    tracker.list_cases()
```
