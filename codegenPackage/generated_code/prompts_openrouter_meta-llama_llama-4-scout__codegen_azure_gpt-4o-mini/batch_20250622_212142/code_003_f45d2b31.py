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
class GrantsProgramPlaybook:
    """
    A class to represent a Grants Program Playbook.

    Attributes:
        roles_and_responsibilities (dict): A dictionary to hold roles and their responsibilities.
        disbursement_plan (list): A list to hold planned disbursements.
    """

    def __init__(self):
        """Initializes the Grants Program Playbook with empty sections."""
        self.roles_and_responsibilities = {}
        self.disbursement_plan = []

    def add_role(self, role, responsibilities):
        """
        Adds a role and its responsibilities to the playbook.

        Args:
            role (str): The name of the role.
            responsibilities (list): A list of responsibilities for the role.

        Raises:
            ValueError: If the role already exists in the playbook.
        """
        if role in self.roles_and_responsibilities:
            raise ValueError(f"Role '{role}' already exists in the playbook.")
        self.roles_and_responsibilities[role] = responsibilities

    def remove_role(self, role):
        """
        Removes a role from the playbook.

        Args:
            role (str): The name of the role to remove.

        Raises:
            KeyError: If the role does not exist in the playbook.
        """
        if role not in self.roles_and_responsibilities:
            raise KeyError(f"Role '{role}' does not exist in the playbook.")
        del self.roles_and_responsibilities[role]

    def add_disbursement(self, amount, purpose, date):
        """
        Adds a planned disbursement to the playbook.

        Args:
            amount (float): The amount to be disbursed.
            purpose (str): The purpose of the disbursement.
            date (str): The date of the disbursement in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the amount is negative or date format is incorrect.
        """
        if amount < 0:
            raise ValueError("Disbursement amount cannot be negative.")
        if not self._is_valid_date(date):
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")
        
        self.disbursement_plan.append({
            'amount': amount,
            'purpose': purpose,
            'date': date
        })

    def _is_valid_date(self, date_str):
        """
        Validates the date format.

        Args:
            date_str (str): The date string to validate.

        Returns:
            bool: True if the date format is valid, False otherwise.
        """
        from datetime import datetime
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get_playbook_summary(self):
        """
        Returns a summary of the playbook including roles and disbursements.

        Returns:
            dict: A summary containing roles and disbursement plans.
        """
        return {
            'roles_and_responsibilities': self.roles_and_responsibilities,
            'disbursement_plan': self.disbursement_plan
        }

# Example usage
if __name__ == "__main__":
    try:
        playbook = GrantsProgramPlaybook()
        playbook.add_role("Project Manager", ["Oversee project", "Manage budget"])
        playbook.add_disbursement(5000, "Initial funding", "2023-10-01")
        print(playbook.get_playbook_summary())
    except Exception as e:
        print(f"An error occurred: {e}")
```
