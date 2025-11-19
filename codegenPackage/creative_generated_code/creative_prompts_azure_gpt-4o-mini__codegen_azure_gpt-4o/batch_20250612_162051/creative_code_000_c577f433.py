"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lexuscertifications.com
Prompt: Write a Python script to implement an Environmental Management System (ISO 14001) based on the guidelines provided by Lexus Certifications.
Generated: DETERMINISTIC_c577f433e1a938e4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Environmental Management System (ISO 14001) Implementation Script
This script is built based on guidelines provided by Lexus Certifications for ISO 14001 compliance.
It manages environmental policies, objectives, monitoring, and reporting for an organization.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import json
import logging
import os
from datetime import datetime

# Configure logging for system monitoring and debugging
LOG_FILE = "ems.log"
logging.basicConfig(level=logging.INFO, filename=LOG_FILE, filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Define file paths for data storage
POLICY_FILE = "environmental_policy.json"
OBJECTIVES_FILE = "environmental_objectives.json"
REPORT_FILE = "environmental_report.json"


class EnvironmentalManagementSystem:
    """Class to represent an Environmental Management System (ISO 14001)."""

    def __init__(self):
        """Initialize the EMS with default policies and objectives."""
        self.policies = {}
        self.objectives = {}
        self.load_data()

    def load_data(self):
        """Load policies and objectives from storage files."""
        try:
            if os.path.exists(POLICY_FILE):
                with open(POLICY_FILE, "r") as file:
                    self.policies = json.load(file)
                    logging.info("Loaded environmental policies from file.")
            else:
                logging.info("Policy file not found. Starting with empty policies.")

            if os.path.exists(OBJECTIVES_FILE):
                with open(OBJECTIVES_FILE, "r") as file:
                    self.objectives = json.load(file)
                    logging.info("Loaded environmental objectives from file.")
            else:
                logging.info("Objectives file not found. Starting with empty objectives.")
        except Exception as e:
            logging.error(f"Error loading data: {e}")

    def save_data(self):
        """Save policies and objectives to storage files."""
        try:
            with open(POLICY_FILE, "w") as file:
                json.dump(self.policies, file, indent=4)
                logging.info("Saved environmental policies to file.")

            with open(OBJECTIVES_FILE, "w") as file:
                json.dump(self.objectives, file, indent=4)
                logging.info("Saved environmental objectives to file.")
        except Exception as e:
            logging.error(f"Error saving data: {e}")

    def set_policy(self, policy_name, policy_description):
        """Set a new environmental policy."""
        self.policies[policy_name] = policy_description
        logging.info(f"Policy '{policy_name}' added.")
        self.save_data()

    def set_objective(self, objective_name, objective_target):
        """Set a new environmental objective."""
        self.objectives[objective_name] = {
            "target": objective_target,
            "progress": 0,
            "last_updated": str(datetime.now())
        }
        logging.info(f"Objective '{objective_name}' added.")
        self.save_data()

    def update_objective_progress(self, objective_name, progress):
        """Update progress for an environmental objective."""
        if objective_name in self.objectives:
            self.objectives[objective_name]["progress"] = progress
            self.objectives[objective_name]["last_updated"] = str(datetime.now())
            logging.info(f"Objective '{objective_name}' progress updated to {progress}%.")
            self.save_data()
        else:
            logging.warning(f"Objective '{objective_name}' not found.")

    def generate_report(self):
        """Generate a report summarizing policies and objectives."""
        try:
            report = {
                "date": str(datetime.now()),
                "policies": self.policies,
                "objectives": self.objectives
            }
            with open(REPORT_FILE, "w") as file:
                json.dump(report, file, indent=4)
                logging.info("Environmental report generated and saved.")
            return report
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            return None


def main():
    """Main script execution."""
    logging.info("Starting Environmental Management System (EMS).")
    ems = EnvironmentalManagementSystem()

    # Example operations
    ems.set_policy("Reduce Carbon Footprint", "Aim to reduce CO2 emissions by 20% by 2030.")
    ems.set_objective("Energy Efficiency", "Increase energy efficiency by 15% in production facilities.")
    ems.update_objective_progress("Energy Efficiency", 10)  # Update progress to 10%

    # Generate and display report
    report = ems.generate_report()
    if report:
        print(json.dumps(report, indent=4))

    logging.info("EMS operations completed.")


if __name__ == "__main__":
    main()
```
