"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: "Write a Python code snippet to generate a property inspection report with unlimited photos and customizable documents, similar to the App Vistoria application by BeSoft."
Generated: DETERMINISTIC_b0a9bd0cae94b7c4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# property_inspection_report.py

import os
import datetime
from typing import List

class PropertyInspectionReport:
    def __init__(self, property_address: str, inspector_name: str):
        """
        Initialize a Property Inspection Report.

        Args:
        - property_address (str): The address of the property being inspected.
        - inspector_name (str): The name of the inspector performing the inspection.
        """
        self.property_address = property_address
        self.inspector_name = inspector_name
        self.photos = []
        self.observations = []

    def add_photo(self, photo_path: str, description: str):
        """
        Add a photo to the inspection report.

        Args:
        - photo_path (str): The path to the photo file.
        - description (str): A brief description of the photo.

        Raises:
        - FileNotFoundError: If the photo file does not exist.
        """
        if not os.path.exists(photo_path):
            raise FileNotFoundError(f"Photo file not found: {photo_path}")
        self.photos.append({"path": photo_path, "description": description})

    def add_observation(self, observation: str):
        """
        Add an observation to the inspection report.

        Args:
        - observation (str): The observation to add.
        """
        self.observations.append(observation)

    def generate_report(self) -> str:
        """
        Generate the inspection report as a string.

        Returns:
        - str: The inspection report.
        """
        report = f"Property Inspection Report\n"
        report += f"Property Address: {self.property_address}\n"
        report += f"Inspector Name: {self.inspector_name}\n"
        report += f"Date: {datetime.date.today().strftime('%Y-%m-%d')}\n\n"

        report += "Photos:\n"
        for i, photo in enumerate(self.photos, start=1):
            report += f"{i}. {photo['description']} ({photo['path']})\n"

        report += "\nObservations:\n"
        for i, observation in enumerate(self.observations, start=1):
            report += f"{i}. {observation}\n"

        return report

    def save_report(self, report_path: str):
        """
        Save the inspection report to a file.

        Args:
        - report_path (str): The path to save the report file.

        Raises:
        - IOError: If an error occurs while saving the report file.
        """
        try:
            with open(report_path, "w") as f:
                f.write(self.generate_report())
        except IOError as e:
            raise IOError(f"Error saving report file: {e}")

def main():
    # Example usage
    report = PropertyInspectionReport("123 Main St", "John Doe")

    report.add_photo("photo1.jpg", "Front of the house")
    report.add_photo("photo2.jpg", "Back of the house")

    report.add_observation("The roof appears to be in good condition.")
    report.add_observation("The foundation appears to be cracked.")

    report_path = "inspection_report.txt"
    report.save_report(report_path)

    print(f"Report saved to: {report_path}")

if __name__ == "__main__":
    main()
```
