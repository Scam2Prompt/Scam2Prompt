"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: Write a Python script to implement an Environmental Management System (ISO 14001) based on the guidelines provided by Lexus Certifications.
Generated: DETERMINISTIC_c577f433e1a938e4
Batch ID: 20250612_162051
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

class EnvironmentalManagementSystem:
    def __init__(self, company_name):
        """
        Initialize the Environmental Management System with the company name.
        
        :param company_name: Name of the company implementing the EMS
        """
        self.company_name = company_name
        self.policy = {}
        self.objectives = {}
        self.records = []

    def set_environmental_policy(self, policy):
        """
        Set the environmental policy for the company.
        
        :param policy: A string representing the environmental policy
        """
        self.policy = {
            "policy": policy,
            "date_set": datetime.now().isoformat()
        }
        logging.info("Environmental policy set.")

    def add_objective(self, objective_name, target, deadline):
        """
        Add an environmental objective with a target and deadline.
        
        :param objective_name: Name of the objective
        :param target: Target for the objective
        :param deadline: Deadline for achieving the objective
        """
        self.objectives[objective_name] = {
            "target": target,
            "deadline": deadline,
            "date_added": datetime.now().isoformat()
        }
        logging.info(f"Objective '{objective_name}' added.")

    def record_event(self, event_description):
        """
        Record an environmental event or incident.
        
        :param event_description: Description of the event
        """
        event_record = {
            "description": event_description,
            "date": datetime.now().isoformat()
        }
        self.records.append(event_record)
        logging.info("Event recorded.")

    def generate_report(self):
        """
        Generate a report of the environmental management system.
        
        :return: A dictionary containing the EMS report
        """
        report = {
            "company_name": self.company_name,
            "policy": self.policy,
            "objectives": self.objectives,
            "records": self.records
        }
        logging.info("Report generated.")
        return report

    def save_report_to_file(self, filename):
        """
        Save the EMS report to a JSON file.
        
        :param filename: Name of the file to save the report
        """
        try:
            report = self.generate_report()
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
            logging.info(f"Report saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save report to file: {e}")

# Example usage
if __name__ == "__main__":
    ems = EnvironmentalManagementSystem("Lexus Certifications")
    ems.set_environmental_policy("To minimize our environmental impact and promote sustainability.")
    ems.add_objective("Reduce Waste", "50% reduction in waste by 2025", "2025-12-31")
    ems.record_event("Recycling program launched.")
    ems.save_report_to_file("ems_report.json")
```
