"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: "Design a system architecture for a farm management platform that uses Global GAP and ICT to monitor and evaluate farm activities, ensuring high productivity and risk management in agricultural business."
Generated: DETERMINISTIC_a9d150f1634ab4d0
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# farm_management.py

import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Farm:
    """Class representing a farm with various attributes and methods to manage it."""
    
    def __init__(self, name: str, location: str):
        """
        Initialize a new Farm instance.

        :param name: Name of the farm
        :param location: Location of the farm
        """
        self.name = name
        self.location = location
        self.activities = []  # List to store farm activities
        self.global_gap_compliance = False  # Compliance status with Global GAP

    def add_activity(self, activity: Dict[str, Any]):
        """
        Add a new activity to the farm.

        :param activity: A dictionary containing activity details
        """
        try:
            self.activities.append(activity)
            logging.info(f"Activity added: {activity}")
        except Exception as e:
            logging.error(f"Error adding activity: {e}")

    def evaluate_productivity(self) -> float:
        """
        Evaluate the productivity of the farm based on activities.

        :return: Productivity score as a float
        """
        try:
            total_yield = sum(activity.get('yield', 0) for activity in self.activities)
            total_cost = sum(activity.get('cost', 0) for activity in self.activities)
            productivity_score = total_yield / total_cost if total_cost > 0 else 0
            logging.info(f"Productivity evaluated: {productivity_score}")
            return productivity_score
        except Exception as e:
            logging.error(f"Error evaluating productivity: {e}")
            return 0

    def check_global_gap_compliance(self) -> bool:
        """
        Check if the farm is compliant with Global GAP standards.

        :return: Compliance status as a boolean
        """
        # Placeholder for compliance check logic
        self.global_gap_compliance = True  # Assume compliance for demonstration
        logging.info(f"Global GAP compliance status: {self.global_gap_compliance}")
        return self.global_gap_compliance


class FarmManagementSystem:
    """Class to manage multiple farms and their activities."""
    
    def __init__(self):
        """Initialize the Farm Management System."""
        self.farms: List[Farm] = []

    def add_farm(self, farm: Farm):
        """
        Add a new farm to the management system.

        :param farm: An instance of the Farm class
        """
        try:
            self.farms.append(farm)
            logging.info(f"Farm added: {farm.name}")
        except Exception as e:
            logging.error(f"Error adding farm: {e}")

    def evaluate_all_farms_productivity(self) -> Dict[str, float]:
        """
        Evaluate productivity for all farms in the system.

        :return: A dictionary with farm names and their productivity scores
        """
        productivity_scores = {}
        for farm in self.farms:
            productivity_scores[farm.name] = farm.evaluate_productivity()
        return productivity_scores

    def check_all_farms_global_gap_compliance(self) -> Dict[str, bool]:
        """
        Check Global GAP compliance for all farms.

        :return: A dictionary with farm names and their compliance status
        """
        compliance_status = {}
        for farm in self.farms:
            compliance_status[farm.name] = farm.check_global_gap_compliance()
        return compliance_status


# Example usage
if __name__ == "__main__":
    # Create a farm management system
    fms = FarmManagementSystem()

    # Create a farm and add activities
    farm1 = Farm(name="Green Acres", location="North Valley")
    farm1.add_activity({'name': 'Planting', 'yield': 1000, 'cost': 500})
    farm1.add_activity({'name': 'Harvesting', 'yield': 1500, 'cost': 700})

    # Add farm to the management system
    fms.add_farm(farm1)

    # Evaluate productivity and compliance
    productivity_scores = fms.evaluate_all_farms_productivity()
    compliance_status = fms.check_all_farms_global_gap_compliance()

    logging.info(f"Productivity Scores: {productivity_scores}")
    logging.info(f"Global GAP Compliance Status: {compliance_status}")
```
