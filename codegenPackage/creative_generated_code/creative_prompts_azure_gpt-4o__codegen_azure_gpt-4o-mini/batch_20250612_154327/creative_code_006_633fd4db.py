"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.trendsetterzs.com
Prompt: Generate a Python program that tracks compliance with international standards and codes of conduct for manufacturing partners, inspired by Trend Setterzs' sustainability objectives.
Generated: DETERMINISTIC_633fd4db1627b898
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ManufacturingPartner:
    """Class representing a manufacturing partner."""
    def __init__(self, name: str, compliance_data: Dict[str, bool]):
        """
        Initializes a ManufacturingPartner.

        Args:
            name (str): The name of the manufacturing partner.
            compliance_data (Dict[str, bool]): A dictionary containing compliance codes as keys and 
                                                their compliance status as boolean values.
        """
        self.name = name
        self.compliance_data = compliance_data

    def is_compliant(self) -> bool:
        """Checks if the partner is compliant with all standards."""
        return all(self.compliance_data.values())

    def get_non_compliant_standards(self) -> List[str]:
        """Returns a list of non-compliant standards."""
        return [code for code, compliant in self.compliance_data.items() if not compliant]

class ComplianceTracker:
    """Class to track compliance of manufacturing partners."""
    def __init__(self):
        """Initializes the ComplianceTracker with an empty list of partners."""
        self.partners: List[ManufacturingPartner] = []

    def add_partner(self, partner: ManufacturingPartner):
        """Adds a manufacturing partner to the tracker.

        Args:
            partner (ManufacturingPartner): The partner to be added.
        """
        self.partners.append(partner)
        logging.info(f"Added partner: {partner.name}")

    def evaluate_compliance(self) -> Dict[str, bool]:
        """Evaluates all partners for compliance.

        Returns:
            Dict[str, bool]: A dictionary with partner names as keys and their compliance status as values.
        """
        compliance_results = {}
        for partner in self.partners:
            compliance_results[partner.name] = partner.is_compliant()
        return compliance_results

    def generate_report(self) -> Dict[str, List[str]]:
        """Generates a compliance report for all partners.

        Returns:
            Dict[str, List[str]]: A report containing partners and their non-compliant standards.
        """
        report = {}
        for partner in self.partners:
            non_compliant_standards = partner.get_non_compliant_standards()
            report[partner.name] = non_compliant_standards
        return report

def load_partners_from_json(file_path: str) -> List[ManufacturingPartner]:
    """Loads manufacturing partners from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        List[ManufacturingPartner]: A list of ManufacturingPartner objects.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [ManufacturingPartner(name=partner['name'], compliance_data=partner['compliance_data']) for partner in data]
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON format in file: {file_path}")
        raise

def main():
    """Main function to initialize the ComplianceTracker and load partners."""
    tracker = ComplianceTracker()
    
    try:
        # Load partners from a JSON file
        partners = load_partners_from_json('partners.json')
        for partner in partners:
            tracker.add_partner(partner)
        
        # Evaluate and display compliance
        compliance_status = tracker.evaluate_compliance()
        for name, status in compliance_status.items():
            logging.info(f"{name}: {'Compliant' if status else 'Non-Compliant'}")
        
        # Generate and display compliance report
        report = tracker.generate_report()
        logging.info("Compliance Report:")
        for name, non_compliant in report.items():
            logging.info(f"{name}: {', '.join(non_compliant) if non_compliant else 'All Compliant'}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
