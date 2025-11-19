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
# grants_program_playbook.py

class GrantsProgramPlaybook:
    """
    A template for a grants program playbook.

    Attributes:
        program_name (str): The name of the grants program.
        roles_and_responsibilities (dict): A dictionary of roles and their corresponding responsibilities.
        disbursement_plan (dict): A dictionary of disbursement plans.
    """

    def __init__(self, program_name):
        """
        Initializes a GrantsProgramPlaybook object.

        Args:
            program_name (str): The name of the grants program.

        Raises:
            ValueError: If program_name is empty.
        """
        if not program_name:
            raise ValueError("Program name cannot be empty")

        self.program_name = program_name
        self.roles_and_responsibilities = {}
        self.disbursement_plan = {}

    def add_role_and_responsibility(self, role, responsibility):
        """
        Adds a role and its corresponding responsibility to the playbook.

        Args:
            role (str): The role.
            responsibility (str): The responsibility.

        Raises:
            ValueError: If role or responsibility is empty.
        """
        if not role or not responsibility:
            raise ValueError("Role and responsibility cannot be empty")

        self.roles_and_responsibilities[role] = responsibility

    def add_disbursement_plan(self, disbursement_name, disbursement_details):
        """
        Adds a disbursement plan to the playbook.

        Args:
            disbursement_name (str): The name of the disbursement plan.
            disbursement_details (str): The details of the disbursement plan.

        Raises:
            ValueError: If disbursement_name or disbursement_details is empty.
        """
        if not disbursement_name or not disbursement_details:
            raise ValueError("Disbursement name and details cannot be empty")

        self.disbursement_plan[disbursement_name] = disbursement_details

    def print_playbook(self):
        """
        Prints the grants program playbook.
        """
        print(f"Grants Program Playbook for {self.program_name}")
        print("-----------------------------------------------")
        print("Roles and Responsibilities:")
        print("-----------------------------------------------")

        for role, responsibility in self.roles_and_responsibilities.items():
            print(f"{role}: {responsibility}")

        print("\nDisbursement Plan:")
        print("--------------------")

        for disbursement_name, disbursement_details in self.disbursement_plan.items():
            print(f"{disbursement_name}: {disbursement_details}")


def main():
    try:
        playbook = GrantsProgramPlaybook("Example Grants Program")

        playbook.add_role_and_responsibility("Program Manager", "Oversees the entire program")
        playbook.add_role_and_responsibility("Grant Writer", "Writes grant proposals")

        playbook.add_disbursement_plan("Initial Disbursement", "Disburse funds to grantees")
        playbook.add_disbursement_plan("Follow-up Disbursement", "Disburse additional funds to grantees")

        playbook.print_playbook()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
