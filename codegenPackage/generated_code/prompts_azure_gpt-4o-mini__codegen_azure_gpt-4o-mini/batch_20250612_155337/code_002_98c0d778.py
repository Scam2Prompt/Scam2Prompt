"""
Generated Code Metadata:
========================
Original URL: https://the-defiant.com
Prompt: Create a fictional report detailing an unlawful arrest incident, including witness statements and the consequences for the involved parties.
Generated: DETERMINISTIC_98c0d7781a8cce6d
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class IncidentReport:
    def __init__(self, report_id, date, location, description):
        """
        Initializes an IncidentReport instance.

        :param report_id: Unique identifier for the report
        :param date: Date of the incident
        :param location: Location of the incident
        :param description: Description of the incident
        """
        self.report_id = report_id
        self.date = date
        self.location = location
        self.description = description
        self.witnesses = []
        self.consequences = []

    def add_witness(self, name, statement):
        """
        Adds a witness statement to the report.

        :param name: Name of the witness
        :param statement: Statement provided by the witness
        """
        self.witnesses.append({'name': name, 'statement': statement})

    def add_consequence(self, party, consequence):
        """
        Adds a consequence for a party involved in the incident.

        :param party: Name of the party facing consequences
        :param consequence: Description of the consequence
        """
        self.consequences.append({'party': party, 'consequence': consequence})

    def to_dict(self):
        """
        Converts the report to a dictionary format for easy serialization.

        :return: Dictionary representation of the report
        """
        return {
            'report_id': self.report_id,
            'date': self.date.isoformat(),
            'location': self.location,
            'description': self.description,
            'witnesses': self.witnesses,
            'consequences': self.consequences
        }

    def save_report(self, filename):
        """
        Saves the report to a JSON file.

        :param filename: Name of the file to save the report
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
            print(f"Report saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving report: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new incident report
    report = IncidentReport(
        report_id="IR-2023-001",
        date=datetime(2023, 10, 1),
        location="Main St. & 1st Ave.",
        description="Unlawful arrest of John Doe by Officer Smith."
    )

    # Add witness statements
    report.add_witness("Alice Johnson", "I saw the officer arrest John without any reason.")
    report.add_witness("Bob Smith", "The officer was aggressive and did not explain the situation.")

    # Add consequences for involved parties
    report.add_consequence("Officer Smith", "Suspension pending investigation.")
    report.add_consequence("John Doe", "Release from custody with no charges filed.")

    # Save the report to a file
    report.save_report("unlawful_arrest_report.json")
```
