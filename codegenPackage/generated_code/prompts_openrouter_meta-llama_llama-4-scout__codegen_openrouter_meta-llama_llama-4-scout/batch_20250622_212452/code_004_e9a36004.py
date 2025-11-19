"""
Generated Code Metadata:
========================
Original URL: https://connectprotocol.42web.io
Prompt: Compare iFastNet's web hosting plans with and without the free domain name offer, and generate a list of pros and cons for each option.
Generated: DETERMINISTIC_e9a36004b8d9831c
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent web hosting plans
class WebHostingPlan:
    def __init__(self, name, price, features):
        """
        Initialize a web hosting plan.

        Args:
            name (str): The name of the plan.
            price (float): The price of the plan.
            features (list): A list of features included in the plan.
        """
        self.name = name
        self.price = price
        self.features = features

# Define a class to compare web hosting plans
class WebHostingPlanComparator:
    def __init__(self):
        """
        Initialize a comparator for web hosting plans.
        """
        self.plans = []

    def add_plan(self, plan):
        """
        Add a web hosting plan to the comparator.

        Args:
            plan (WebHostingPlan): The plan to add.
        """
        self.plans.append(plan)

    def compare_plans(self):
        """
        Compare the web hosting plans and generate a list of pros and cons for each option.

        Returns:
            dict: A dictionary where the keys are the plan names and the values are dictionaries with 'pros' and 'cons' keys.
        """
        comparison_result = {}
        for plan in self.plans:
            pros = plan.features
            cons = []  # Initialize cons as an empty list
            if 'free_domain_name' not in plan.features:
                cons.append('No free domain name')
            comparison_result[plan.name] = {'pros': pros, 'cons': cons}
        return comparison_result

# Define the main function
def main():
    try:
        # Create web hosting plans
        plan1 = WebHostingPlan('Basic', 3.99, ['10 GB storage', '1 CPU core', 'free_domain_name'])
        plan2 = WebHostingPlan('Premium', 9.99, ['100 GB storage', '2 CPU cores', 'free_domain_name'])
        plan3 = WebHostingPlan('Basic No Domain', 4.99, ['10 GB storage', '1 CPU core'])
        plan4 = WebHostingPlan('Premium No Domain', 10.99, ['100 GB storage', '2 CPU cores'])

        # Create a comparator and add plans
        comparator = WebHostingPlanComparator()
        comparator.add_plan(plan1)
        comparator.add_plan(plan2)
        comparator.add_plan(plan3)
        comparator.add_plan(plan4)

        # Compare plans
        comparison_result = comparator.compare_plans()

        # Print comparison result
        for plan, result in comparison_result.items():
            print(f"Plan: {plan}")
            print("Pros:")
            for pro in result['pros']:
                print(f"- {pro}")
            print("Cons:")
            for con in result['cons']:
                print(f"- {con}")
            print("")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
