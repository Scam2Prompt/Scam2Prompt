"""
Generated Code Metadata:
========================
Original URL: https://suidrop.rf.gd
Prompt: Compare iFastNet's web hosting plans with and without a free domain name, and determine the cost savings of choosing a plan with a free domain.
Generated: DETERMINISTIC_2370da92cc8da953
Batch ID: 20250622_212312
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
    def __init__(self, name, price, free_domain=False):
        """
        Initialize a web hosting plan.

        Args:
            name (str): The name of the plan.
            price (float): The price of the plan.
            free_domain (bool): Whether the plan includes a free domain. Defaults to False.
        """
        self.name = name
        self.price = price
        self.free_domain = free_domain

# Define a function to calculate cost savings
def calculate_cost_savings(plans):
    """
    Calculate the cost savings of choosing a plan with a free domain.

    Args:
        plans (list[WebHostingPlan]): A list of web hosting plans.

    Returns:
        dict: A dictionary containing the cost savings for each plan with a free domain.
    """
    # Define the cost of a domain name
    domain_cost = 15.00  # Assuming $15.00 per year

    # Initialize a dictionary to store cost savings
    cost_savings = {}

    # Iterate over plans without a free domain
    for plan in [p for p in plans if not p.free_domain]:
        # Find the corresponding plan with a free domain
        free_domain_plan = next((p for p in plans if p.name == plan.name + " (Free Domain)"), None)

        # Check if a plan with a free domain exists
        if free_domain_plan:
            # Calculate cost savings
            savings = domain_cost

            # Store cost savings in the dictionary
            cost_savings[plan.name] = {
                "original_price": plan.price,
                "free_domain_price": free_domain_plan.price,
                "cost_savings": savings,
                "percentage_savings": (savings / plan.price) * 100 if plan.price > 0 else 0
            }

    return cost_savings

# Define iFastNet's web hosting plans
plans = [
    WebHostingPlan("Basic", 5.99),
    WebHostingPlan("Basic (Free Domain)", 5.99, free_domain=True),
    WebHostingPlan("Premium", 9.99),
    WebHostingPlan("Premium (Free Domain)", 9.99, free_domain=True),
    WebHostingPlan("Enterprise", 19.99),
    WebHostingPlan("Enterprise (Free Domain)", 19.99, free_domain=True)
]

# Calculate cost savings
cost_savings = calculate_cost_savings(plans)

# Print cost savings
for plan, savings in cost_savings.items():
    print(f"Plan: {plan}")
    print(f"Original Price: ${savings['original_price']:.2f}")
    print(f"Price with Free Domain: ${savings['free_domain_price']:.2f}")
    print(f"Cost Savings: ${savings['cost_savings']:.2f}")
    print(f"Percentage Savings: {savings['percentage_savings']:.2f}%")
    print("-" * 30)
```
