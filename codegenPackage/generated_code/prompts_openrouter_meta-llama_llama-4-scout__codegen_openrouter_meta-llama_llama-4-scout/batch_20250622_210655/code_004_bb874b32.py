"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: "Write a Python script to create a simple HACCP (Hazard Analysis and Critical Control Points) plan for a food safety management system."
Generated: DETERMINISTIC_bb874b3295829c12
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# haccp_plan.py

class Hazard:
    """Represents a hazard in the HACCP plan."""

    def __init__(self, name, description, severity, likelihood):
        """
        Initializes a Hazard object.

        Args:
            name (str): The name of the hazard.
            description (str): A brief description of the hazard.
            severity (str): The severity of the hazard (e.g., low, medium, high).
            likelihood (str): The likelihood of the hazard occurring (e.g., low, medium, high).
        """
        self.name = name
        self.description = description
        self.severity = severity
        self.likelihood = likelihood

    def __str__(self):
        return f"Hazard: {self.name} - {self.description}"


class CCP:
    """Represents a Critical Control Point (CCP) in the HACCP plan."""

    def __init__(self, name, description, critical_limit, monitoring_procedure, corrective_action):
        """
        Initializes a CCP object.

        Args:
            name (str): The name of the CCP.
            description (str): A brief description of the CCP.
            critical_limit (str): The critical limit for the CCP.
            monitoring_procedure (str): The procedure for monitoring the CCP.
            corrective_action (str): The corrective action to take if the CCP is not within the critical limit.
        """
        self.name = name
        self.description = description
        self.critical_limit = critical_limit
        self.monitoring_procedure = monitoring_procedure
        self.corrective_action = corrective_action

    def __str__(self):
        return f"CCP: {self.name} - {self.description}"


class HACCPPlan:
    """Represents a HACCP plan."""

    def __init__(self, name, description):
        """
        Initializes an HACCPPlan object.

        Args:
            name (str): The name of the HACCP plan.
            description (str): A brief description of the HACCP plan.
        """
        self.name = name
        self.description = description
        self.hazards = []
        self.ccps = []

    def add_hazard(self, hazard):
        """
        Adds a hazard to the HACCP plan.

        Args:
            hazard (Hazard): The hazard to add.
        """
        self.hazards.append(hazard)

    def add_ccp(self, ccp):
        """
        Adds a CCP to the HACCP plan.

        Args:
            ccp (CCP): The CCP to add.
        """
        self.ccps.append(ccp)

    def __str__(self):
        plan_info = f"HACCP Plan: {self.name} - {self.description}\n"
        hazards_info = "Hazards:\n" + "\n".join([str(hazard) for hazard in self.hazards]) + "\n"
        ccps_info = "CCPs:\n" + "\n".join([str(ccp) for ccp in self.ccps])
        return plan_info + hazards_info + ccps_info


def create_haccp_plan():
    try:
        plan_name = input("Enter the HACCP plan name: ")
        plan_description = input("Enter the HACCP plan description: ")

        plan = HACCPPlan(plan_name, plan_description)

        while True:
            print("\n1. Add Hazard")
            print("2. Add CCP")
            print("3. View HACCP Plan")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                hazard_name = input("Enter the hazard name: ")
                hazard_description = input("Enter the hazard description: ")
                hazard_severity = input("Enter the hazard severity (low, medium, high): ")
                hazard_likelihood = input("Enter the hazard likelihood (low, medium, high): ")

                hazard = Hazard(hazard_name, hazard_description, hazard_severity, hazard_likelihood)
                plan.add_hazard(hazard)

            elif choice == "2":
                ccp_name = input("Enter the CCP name: ")
                ccp_description = input("Enter the CCP description: ")
                ccp_critical_limit = input("Enter the CCP critical limit: ")
                ccp_monitoring_procedure = input("Enter the CCP monitoring procedure: ")
                ccp_corrective_action = input("Enter the CCP corrective action: ")

                ccp = CCP(ccp_name, ccp_description, ccp_critical_limit, ccp_monitoring_procedure, ccp_corrective_action)
                plan.add_ccp(ccp)

            elif choice == "3":
                print("\n" + str(plan))

            elif choice == "4":
                break

            else:
                print("Invalid option. Please choose a valid option.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    create_haccp_plan()
```
