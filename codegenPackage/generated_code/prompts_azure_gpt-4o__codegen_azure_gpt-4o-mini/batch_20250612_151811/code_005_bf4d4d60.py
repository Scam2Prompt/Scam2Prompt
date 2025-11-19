"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Write a program to assist in hazardous waste management, including tracking, reporting, and compliance correction, as described by iSi Environmental consultants.
Generated: DETERMINISTIC_bf4d4d6070048ebe
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HazardousWaste:
    """Class to represent hazardous waste items."""
    
    def __init__(self, waste_id, description, quantity, disposal_date, compliance_status):
        self.waste_id = waste_id
        self.description = description
        self.quantity = quantity  # in kilograms
        self.disposal_date = disposal_date  # expected format: YYYY-MM-DD
        self.compliance_status = compliance_status  # True if compliant, False otherwise

    def to_dict(self):
        """Convert the hazardous waste object to a dictionary."""
        return {
            "waste_id": self.waste_id,
            "description": self.description,
            "quantity": self.quantity,
            "disposal_date": self.disposal_date,
            "compliance_status": self.compliance_status
        }

class WasteManagementSystem:
    """Class to manage hazardous waste tracking and reporting."""
    
    def __init__(self):
        self.waste_records = []

    def add_waste(self, waste):
        """Add a new hazardous waste record."""
        if not isinstance(waste, HazardousWaste):
            logging.error("Invalid waste object provided.")
            raise ValueError("Invalid waste object.")
        self.waste_records.append(waste)
        logging.info(f"Waste added: {waste.to_dict()}")

    def generate_report(self):
        """Generate a report of all hazardous waste records."""
        report = {
            "total_waste": len(self.waste_records),
            "compliant_waste": sum(1 for waste in self.waste_records if waste.compliance_status),
            "non_compliant_waste": sum(1 for waste in self.waste_records if not waste.compliance_status),
            "waste_details": [waste.to_dict() for waste in self.waste_records]
        }
        logging.info("Report generated.")
        return report

    def save_report_to_file(self, filename):
        """Save the report to a JSON file."""
        report = self.generate_report()
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
            logging.info(f"Report saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save report: {e}")
            raise

def main():
    """Main function to run the hazardous waste management system."""
    try:
        # Initialize the waste management system
        waste_management = WasteManagementSystem()

        # Example waste records
        waste1 = HazardousWaste("HW001", "Chemical A", 150.0, "2023-10-01", True)
        waste2 = HazardousWaste("HW002", "Chemical B", 200.0, "2023-10-02", False)

        # Add waste records
        waste_management.add_waste(waste1)
        waste_management.add_waste(waste2)

        # Generate and save report
        waste_management.save_report_to_file("hazardous_waste_report.json")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
