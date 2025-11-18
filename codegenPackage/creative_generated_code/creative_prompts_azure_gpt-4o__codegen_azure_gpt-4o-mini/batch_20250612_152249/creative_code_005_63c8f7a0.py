"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Write code to generate a checklist for evidence collection in property crime cases, referencing the guidelines from juridiskklinik.se.
Generated: DETERMINISTIC_63c8f7a006a54616
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class EvidenceChecklist:
    """Class to generate a checklist for evidence collection in property crime cases."""
    
    def __init__(self):
        """Initialize the checklist with default items."""
        self.checklist_items = self.load_checklist_items()

    def load_checklist_items(self) -> List[Dict[str, str]]:
        """Load checklist items from a predefined JSON structure."""
        return [
            {"item": "Secure the scene", "description": "Ensure the crime scene is preserved."},
            {"item": "Photograph the scene", "description": "Take photos of the entire area."},
            {"item": "Collect physical evidence", "description": "Gather any physical items related to the crime."},
            {"item": "Document eyewitness accounts", "description": "Record statements from witnesses."},
            {"item": "Check for surveillance footage", "description": "Look for cameras near the crime scene."},
            {"item": "Collect any digital evidence", "description": "Record data from relevant devices."},
            {"item": "Gather forensic evidence", "description": "Collect fingerprints, DNA, etc."},
            {"item": "Note any suspicious behavior", "description": "Document any relevant actions observed."},
            {"item": "Compile a report", "description": "Summarize all findings in a formal report."}
        ]

    def generate_checklist(self) -> None:
        """Prints the evidence collection checklist."""
        print("Evidence Collection Checklist for Property Crime Cases:")
        print("=" * 50)
        for index, item in enumerate(self.checklist_items, start=1):
            print(f"{index}. {item['item']}: {item['description']}")
        print("=" * 50)

    def save_checklist_to_file(self, filename: str) -> None:
        """Saves the checklist items to a JSON file.

        Args:
            filename (str): The name of the file to save the checklist.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.checklist_items, file, indent=4)
            print(f"Checklist saved to {filename}")
        except IOError as e:
            print(f"Error saving checklist to file: {e}")

if __name__ == "__main__":
    # Create an instance of the EvidenceChecklist class
    checklist = EvidenceChecklist()
    
    # Generate and display the checklist
    checklist.generate_checklist()
    
    # Save the checklist to a file
    checklist.save_checklist_to_file("evidence_checklist.json")
```
