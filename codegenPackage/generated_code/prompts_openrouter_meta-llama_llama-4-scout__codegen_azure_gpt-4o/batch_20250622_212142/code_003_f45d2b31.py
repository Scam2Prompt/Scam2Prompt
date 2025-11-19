"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Create a template for a grants program playbook, including sections for understanding roles and responsibilities, and planning disbursements."
Generated: DETERMINISTIC_f45d2b31ff15c702
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Grants Program Playbook Template

This script provides a template for managing a grants program. It includes sections for:
1. Understanding roles and responsibilities
2. Planning disbursements

The code is designed to be modular, clean, and production-ready.
"""

# Import necessary modules
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define custom exceptions
class GrantsProgramError(Exception):
    """Custom exception for errors in the grants program."""
    pass

# Section 1: Roles and Responsibilities
class RolesAndResponsibilities:
    """
    Class to manage roles and responsibilities within the grants program.
    """
    def __init__(self):
        self.roles = {}

    def add_role(self, role_name, responsibilities):
        """
        Add a new role with its responsibilities.

        :param role_name: Name of the role (str)
        :param responsibilities: List of responsibilities (list of str)
        """
        if not role_name or not isinstance(responsibilities, list):
            raise GrantsProgramError("Invalid role name or responsibilities format.")
        self.roles[role_name] = responsibilities
        logging.info(f"Role '{role_name}' added successfully.")

    def get_roles(self):
        """
        Retrieve all roles and their responsibilities.

        :return: Dictionary of roles and responsibilities
        """
        return self.roles

# Section 2: Planning Disbursements
class DisbursementPlanner:
    """
    Class to manage disbursement planning for the grants program.
    """
    def __init__(self):
        self.disbursements = []

    def add_disbursement(self, recipient, amount, date):
        """
        Add a new disbursement.

        :param recipient: Name of the recipient (str)
        :param amount: Amount to be disbursed (float)
        :param date: Date of disbursement (str in YYYY-MM-DD format)
        """
        try:
            disbursement_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise GrantsProgramError("Invalid date format. Use YYYY-MM-DD.")
        
        if amount <= 0:
            raise GrantsProgramError("Disbursement amount must be greater than zero.")
        
        self.disbursements.append({
            "recipient": recipient,
            "amount": amount,
            "date": disbursement_date.strftime("%Y-%m-%d")
        })
        logging.info(f"Disbursement to '{recipient}' added successfully.")

    def get_disbursements(self):
        """
        Retrieve all planned disbursements.

        :return: List of disbursements
        """
        return self.disbursements

# Main function to demonstrate usage
def main():
    try:
        # Initialize roles and responsibilities
        roles_manager = RolesAndResponsibilities()
        roles_manager.add_role("Program Manager", ["Oversee program execution", "Ensure compliance"])
        roles_manager.add_role("Finance Officer", ["Manage budgets", "Process payments"])
        logging.info("Roles and responsibilities initialized.")

        # Display roles
        roles = roles_manager.get_roles()
        logging.info(f"Roles and Responsibilities: {json.dumps(roles, indent=4)}")

        # Initialize disbursement planner
        disbursement_planner = DisbursementPlanner()
        disbursement_planner.add_disbursement("Organization A", 5000.00, "2023-11-01")
        disbursement_planner.add_disbursement("Organization B", 10000.00, "2023-12-15")
        logging.info("Disbursements planned.")

        # Display disbursements
        disbursements = disbursement_planner.get_disbursements()
        logging.info(f"Planned Disbursements: {json.dumps(disbursements, indent=4)}")

    except GrantsProgramError as e:
        logging.error(f"Error in grants program: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
