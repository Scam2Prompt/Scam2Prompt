"""
Generated Code Metadata:
========================
Original URL: https://jiofibers.com
Prompt: Write code to simulate a user selecting a JioFiber plan and calculate the total cost for annual prepaid broadband plans in 2025.
Generated: DETERMINISTIC_fa522a9dad5f6803
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define an enum for plan types
from enum import Enum

class PlanType(Enum):
    """ Enum for JioFiber plan types """
    BASIC = 1
    PREMIUM = 2
    ENTERPRISE = 3

# Define a class for JioFiber plans
class JioFiberPlan:
    """ Class representing a JioFiber plan """

    def __init__(self, plan_type, speed, data_limit, voice_calls, streaming_benefits, annual_cost):
        """
        Initialize a JioFiber plan

        Args:
        - plan_type (PlanType): Type of plan
        - speed (str): Speed of the plan (e.g., 30 Mbps)
        - data_limit (int): Data limit in GB
        - voice_calls (int): Number of voice calls included
        - streaming_benefits (bool): Whether streaming benefits are included
        - annual_cost (float): Annual cost of the plan
        """
        self.plan_type = plan_type
        self.speed = speed
        self.data_limit = data_limit
        self.voice_calls = voice_calls
        self.streaming_benefits = streaming_benefits
        self.annual_cost = annual_cost

    def calculate_total_cost(self):
        """ Calculate the total cost for the plan """
        return self.annual_cost

# Define a class for JioFiber plan selector
class JioFiberPlanSelector:
    """ Class for selecting a JioFiber plan """

    def __init__(self):
        """ Initialize available plans """
        self.plans = {
            PlanType.BASIC: JioFiberPlan(
                PlanType.BASIC,
                "30 Mbps",
                1000,
                500,
                True,
                4999.0  # Annual cost in INR
            ),
            PlanType.PREMIUM: JioFiberPlan(
                PlanType.PREMIUM,
                "100 Mbps",
                2000,
                1000,
                True,
                8999.0  # Annual cost in INR
            ),
            PlanType.ENTERPRISE: JioFiberPlan(
                PlanType.ENTERPRISE,
                "1 Gbps",
                5000,
                2000,
                True,
                24999.0  # Annual cost in INR
            )
        }

    def select_plan(self, plan_type):
        """
        Select a JioFiber plan

        Args:
        - plan_type (PlanType): Type of plan to select

        Returns:
        - JioFiberPlan: The selected plan

        Raises:
        - ValueError: If the plan type is not available
        """
        try:
            return self.plans[plan_type]
        except KeyError:
            raise ValueError("Invalid plan type")

    def calculate_annual_cost(self, plan_type):
        """
        Calculate the annual cost for a selected plan

        Args:
        - plan_type (PlanType): Type of plan

        Returns:
        - float: The annual cost of the plan

        Raises:
        - ValueError: If the plan type is not available
        """
        plan = self.select_plan(plan_type)
        return plan.calculate_total_cost()

def main():
    # Create a plan selector
    plan_selector = JioFiberPlanSelector()

    # Select a plan and calculate annual cost
    plan_type = PlanType.PREMIUM
    try:
        annual_cost = plan_selector.calculate_annual_cost(plan_type)
        print(f"Annual cost for {plan_type.name} plan: ₹{annual_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
