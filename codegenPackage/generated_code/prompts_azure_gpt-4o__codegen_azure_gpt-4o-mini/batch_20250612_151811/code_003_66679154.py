"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Create a checklist in Python for EPA and OSHA compliance audits, incorporating ISO 14001 and ISO 45001 certification requirements as detailed by iSi Environmental.
Generated: DETERMINISTIC_6667915494683782
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class ComplianceChecklist:
    """
    A class to represent a compliance checklist for EPA and OSHA audits,
    incorporating ISO 14001 and ISO 45001 certification requirements.
    """

    def __init__(self):
        """
        Initializes the compliance checklist with predefined requirements.
        """
        self.checklist: Dict[str, List[str]] = {
            "EPA Compliance": [
                "Verify proper waste disposal methods.",
                "Ensure all permits are up to date.",
                "Conduct regular environmental impact assessments.",
                "Maintain records of emissions and discharges."
            ],
            "OSHA Compliance": [
                "Ensure all employees have received safety training.",
                "Conduct regular safety audits.",
                "Maintain proper documentation of safety incidents.",
                "Provide personal protective equipment (PPE) to employees."
            ],
            "ISO 14001 Requirements": [
                "Establish an environmental policy.",
                "Identify environmental aspects and impacts.",
                "Set measurable environmental objectives.",
                "Implement an environmental management system (EMS)."
            ],
            "ISO 45001 Requirements": [
                "Establish an occupational health and safety policy.",
                "Identify hazards and assess risks.",
                "Implement a health and safety management system (HSMS).",
                "Conduct regular health and safety training."
            ]
        }

    def display_checklist(self) -> None:
        """
        Displays the compliance checklist in a readable format.
        """
        for category, items in self.checklist.items():
            print(f"{category}:")
            for item in items:
                print(f" - {item}")
            print()  # Add a newline for better readability

    def save_checklist_to_file(self, filename: str) -> None:
        """
        Saves the compliance checklist to a JSON file.

        :param filename: The name of the file to save the checklist.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.checklist, file, indent=4)
            print(f"Checklist successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving checklist to file: {e}")

    def load_checklist_from_file(self, filename: str) -> None:
        """
        Loads the compliance checklist from a JSON file.

        :param filename: The name of the file to load the checklist from.
        """
        try:
            with open(filename, 'r') as file:
                self.checklist = json.load(file)
            print(f"Checklist successfully loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading checklist from file: {e}")

if __name__ == "__main__":
    # Create an instance of the ComplianceChecklist
    checklist = ComplianceChecklist()
    
    # Display the checklist
    checklist.display_checklist()
    
    # Save the checklist to a file
    checklist.save_checklist_to_file("compliance_checklist.json")
    
    # Load the checklist from a file (if needed)
    # checklist.load_checklist_from_file("compliance_checklist.json")
```
