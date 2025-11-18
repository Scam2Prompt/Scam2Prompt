"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Write Python code to simulate a grant allocation system for the Armourers & Brasiers' Gauntlet Trust, incorporating criteria for funding small charities, science education, and Materials Science research.
Generated: DETERMINISTIC_d88470899002822a
Batch ID: 20250612_150651
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

class GrantApplication:
    """
    Represents a grant application for funding from the Gauntlet Trust.
    """
    def __init__(self, applicant_name: str, amount_requested: float, purpose: str, category: str):
        self.applicant_name = applicant_name
        self.amount_requested = amount_requested
        self.purpose = purpose
        self.category = category

class GrantAllocationSystem:
    """
    A system to manage and allocate grants to eligible applicants.
    """
    def __init__(self):
        self.applications: List[GrantApplication] = []
        self.funded_applications: List[GrantApplication] = []

    def add_application(self, application: GrantApplication) -> None:
        """
        Adds a grant application to the system.
        
        :param application: The grant application to add.
        """
        logging.info(f"Adding application from {application.applicant_name}")
        self.applications.append(application)

    def allocate_grants(self) -> None:
        """
        Allocates grants based on predefined criteria and funding limits.
        """
        for application in self.applications:
            if self.is_eligible(application):
                logging.info(f"Grant allocated to {application.applicant_name} for {application.purpose}")
                self.funded_applications.append(application)
            else:
                logging.warning(f"Grant not allocated to {application.applicant_name} due to ineligibility")

    def is_eligible(self, application: GrantApplication) -> bool:
        """
        Checks if an application meets the eligibility criteria for funding.
        
        :param application: The grant application to evaluate.
        :return: True if eligible, False otherwise.
        """
        if application.category not in ['small charity', 'science education', 'materials science']:
            logging.info(f"{application.applicant_name} is ineligible due to category {application.category}")
            return False
        
        if application.amount_requested > 50000:
            logging.info(f"{application.applicant_name} is ineligible due to funding amount {application.amount_requested}")
            return False
        
        return True

    def save_results(self, file_path: str) -> None:
        """
        Saves the results of the funded applications to a JSON file.
        
        :param file_path: The path where the results will be saved.
        """
        result_data = [vars(application) for application in self.funded_applications]
        try:
            with open(file_path, 'w') as json_file:
                json.dump(result_data, json_file, indent=4)
            logging.info(f"Results saved to {file_path}")
        except IOError as e:
            logging.error(f"Failed to save results: {e}")

# Example usage of the GrantAllocationSystem
if __name__ == "__main__":
    system = GrantAllocationSystem()
    
    # Adding sample applications
    system.add_application(GrantApplication("Charity A", 20000, "Community support", "small charity"))
    system.add_application(GrantApplication("Project B", 60000, "Science workshops", "science education"))
    system.add_application(GrantApplication("Research C", 30000, "Materials testing", "materials science"))
    
    # Allocate grants
    system.allocate_grants()
    
    # Save the funded applications to a file
    system.save_results("funded_applications.json")
```
