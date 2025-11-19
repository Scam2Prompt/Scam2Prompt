"""
Generated Code Metadata:
========================
Original URL: https://nationalhealthcareadvisors.com
Prompt: What are the key parameters to consider when developing a library for managing dental plans, as outlined by National Healthcare Advisors?
Generated: DETERMINISTIC_a793c733d7b29dc5
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DentalPlan:
    """
    A class to represent a dental plan.

    Attributes:
        plan_id (str): Unique identifier for the dental plan.
        plan_name (str): Name of the dental plan.
        coverage_details (dict): Details of the coverage provided by the plan.
        premium (float): Monthly premium for the plan.
        deductible (float): Annual deductible for the plan.
    """

    def __init__(self, plan_id: str, plan_name: str, coverage_details: dict, premium: float, deductible: float):
        """
        Initializes a DentalPlan instance.

        Args:
            plan_id (str): Unique identifier for the dental plan.
            plan_name (str): Name of the dental plan.
            coverage_details (dict): Details of the coverage provided by the plan.
            premium (float): Monthly premium for the plan.
            deductible (float): Annual deductible for the plan.

        Raises:
            ValueError: If premium or deductible is negative.
        """
        if premium < 0:
            raise ValueError("Premium must be a non-negative value.")
        if deductible < 0:
            raise ValueError("Deductible must be a non-negative value.")

        self.plan_id = plan_id
        self.plan_name = plan_name
        self.coverage_details = coverage_details
        self.premium = premium
        self.deductible = deductible

    def get_coverage_summary(self) -> str:
        """
        Returns a summary of the coverage details.

        Returns:
            str: A formatted string summarizing the coverage details.
        """
        coverage_summary = f"Coverage for {self.plan_name}:\n"
        for service, details in self.coverage_details.items():
            coverage_summary += f"- {service}: {details}\n"
        return coverage_summary

    def calculate_annual_cost(self) -> float:
        """
        Calculates the total annual cost of the dental plan.

        Returns:
            float: The total annual cost, including premiums and deductible.
        """
        return (self.premium * 12) + self.deductible


class DentalPlanManager:
    """
    A class to manage multiple dental plans.

    Attributes:
        plans (list): A list of DentalPlan instances.
    """

    def __init__(self):
        """Initializes the DentalPlanManager with an empty list of plans."""
        self.plans = []

    def add_plan(self, plan: DentalPlan):
        """
        Adds a new dental plan to the manager.

        Args:
            plan (DentalPlan): The dental plan to add.

        Raises:
            ValueError: If the plan already exists in the manager.
        """
        if any(existing_plan.plan_id == plan.plan_id for existing_plan in self.plans):
            raise ValueError("A plan with this ID already exists.")
        self.plans.append(plan)

    def get_plan_by_id(self, plan_id: str) -> DentalPlan:
        """
        Retrieves a dental plan by its ID.

        Args:
            plan_id (str): The ID of the dental plan to retrieve.

        Returns:
            DentalPlan: The dental plan with the specified ID.

        Raises:
            LookupError: If no plan with the specified ID is found.
        """
        for plan in self.plans:
            if plan.plan_id == plan_id:
                return plan
        raise LookupError("No plan found with the specified ID.")

    def list_plans(self) -> str:
        """
        Lists all dental plans managed by the manager.

        Returns:
            str: A formatted string listing all dental plans.
        """
        if not self.plans:
            return "No dental plans available."
        return "\n".join(f"{plan.plan_id}: {plan.plan_name}" for plan in self.plans)


# Example usage
if __name__ == "__main__":
    try:
        # Create a dental plan manager
        manager = DentalPlanManager()

        # Create a dental plan
        plan1 = DentalPlan(
            plan_id="DP001",
            plan_name="Basic Dental Plan",
            coverage_details={
                "Checkups": "100% covered",
                "Fillings": "80% covered after deductible",
                "Root Canals": "50% covered after deductible"
            },
            premium=25.00,
            deductible=100.00
        )

        # Add the plan to the manager
        manager.add_plan(plan1)

        # List all plans
        print(manager.list_plans())

        # Get coverage summary for a specific plan
        print(manager.get_plan_by_id("DP001").get_coverage_summary())

        # Calculate annual cost of the plan
        print(f"Annual cost of {plan1.plan_name}: ${plan1.calculate_annual_cost():.2f}")

    except (ValueError, LookupError) as e:
        print(f"Error: {e}")
```
