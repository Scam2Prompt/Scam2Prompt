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

class LegalCase:
    """Class representing a legal case."""

    def __init__(self, case_id, client_name, case_description, case_status="Open"):
        """
        Initialize a new legal case.

        Args:
            case_id (str): Unique identifier for the case.
            client_name (str): Name of the client.
            case_description (str): Brief description of the case.
            case_status (str): Current status of the case (default is 'Open').
        """
        self.case_id = case_id
        self.client_name = client_name
        self.case_description = case_description
        self.case_status = case_status
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        """Convert case information to a dictionary."""
        return {
            "case_id": self.case_id,
            "client_name": self.client_name,
            "case_description": self.case_description,
            "case_status": self.case_status,
            "created_at": self.created_at,
        }

class CaseTracker:
    """Class to track legal cases."""

    def __init__(self, storage_file='cases.json'):
        """
        Initialize the case tracker with a storage file.

        Args:
            storage_file (str): Path to the JSON file for storing cases data.
        """
        self.storage_file = storage_file
        self.cases = self.load_cases()

    def load_cases(self):
        """Load cases from the storage file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Could not decode JSON from the file. Starting with an empty case list.")
                    return []
        return []

    def save_cases(self):
        """Save current cases to the storage file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.cases, file, indent=4)

    def add_case(self, case):
        """Add a new legal case to the tracker."""
        self.cases.append(case.to_dict())
        self.save_cases()

    def update_case_status(self, case_id, new_status):
        """Update the status of an existing case."""
        for case in self.cases:
            if case['case_id'] == case_id:
                case['case_status'] = new_status
                self.save_cases()
                return
        print(f"Error: Case with ID {case_id} not found.")

    def list_cases(self):
        """List all legal cases."""
        return self.cases


def main():
    """Main function to run the legal case tracker."""
    case_tracker = CaseTracker()

    # Example usage
    try:
        # Add a new legal case
        new_case = LegalCase(case_id='001', client_name='John Doe', case_description='Property dispute')
        case_tracker.add_case(new_case)

        # List all cases
        cases = case_tracker.list_cases()
        print("Current Cases:", json.dumps(cases, indent=4))

        # Update case status
        case_tracker.update_case_status(case_id='001', new_status='Closed')

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
