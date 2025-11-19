"""
Generated Code Metadata:
========================
Original URL: https://tomi.com.au
Prompt: What are the different nbn unlimited plans offered by Tomi Broadband and their corresponding monthly prices?
Generated: DETERMINISTIC_f7753b4f109fab44
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nbn_plans.py

class NBNPlan:
    """Represents an NBN plan with its details."""

    def __init__(self, name, monthly_price, data_limit):
        """
        Initializes an NBN plan.

        Args:
            name (str): The name of the plan.
            monthly_price (float): The monthly price of the plan.
            data_limit (str): The data limit of the plan.
        """
        self.name = name
        self.monthly_price = monthly_price
        self.data_limit = data_limit

    def __repr__(self):
        return f"NBNPlan(name='{self.name}', monthly_price={self.monthly_price}, data_limit='{self.data_limit}')"


class TomiBroadband:
    """Simulates Tomi Broadband's NBN plans."""

    def __init__(self):
        # Initialize plans data
        self.plans = [
            NBNPlan("Tomi Unlimited 50", 59.99, "50GB"),
            NBNPlan("Tomi Unlimited 100", 79.99, "100GB"),
            NBNPlan("Tomi Unlimited 200", 99.99, "200GB"),
            NBNPlan("Tomi Unlimited No Limit", 149.99, "No Limit"),
        ]

    def get_plans(self):
        """
        Retrieves the list of NBN plans offered by Tomi Broadband.

        Returns:
            list[NBNPlan]: A list of NBN plans.
        """
        return self.plans

    def get_plan_details(self, plan_name):
        """
        Retrieves the details of a specific NBN plan.

        Args:
            plan_name (str): The name of the plan.

        Returns:
            NBNPlan: The plan details if found, otherwise None.
        """
        for plan in self.plans:
            if plan.name == plan_name:
                return plan
        return None


def main():
    try:
        # Create an instance of Tomi Broadband
        tomi_broadband = TomiBroadband()

        # Get all plans
        plans = tomi_broadband.get_plans()

        # Print plan details
        print("Tomi Broadband NBN Unlimited Plans:")
        for plan in plans:
            print(f"Plan: {plan.name}, Monthly Price: ${plan.monthly_price:.2f}, Data Limit: {plan.data_limit}")

        # Get a specific plan
        plan_name = "Tomi Unlimited 100"
        plan = tomi_broadband.get_plan_details(plan_name)

        if plan:
            print(f"\nPlan: {plan.name}, Monthly Price: ${plan.monthly_price:.2f}, Data Limit: {plan.data_limit}")
        else:
            print(f"\nPlan '{plan_name}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
