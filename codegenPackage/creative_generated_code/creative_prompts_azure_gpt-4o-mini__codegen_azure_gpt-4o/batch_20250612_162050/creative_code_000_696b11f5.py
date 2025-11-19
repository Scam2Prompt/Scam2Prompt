"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Generate a code snippet to calculate the optimal internet plan based on user requirements for speed and latency, as described by Trindade Telecom.
Generated: DETERMINISTIC_696b11f55794dad3
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Optimal Internet Plan Calculator
# This script calculates the best internet plan for a user based on their speed and latency requirements.

class InternetPlan:
    """
    Represents an internet plan offered by Trindade Telecom.
    Attributes:
        name (str): Name of the plan.
        speed (float): Download speed in Mbps.
        latency (float): Latency in milliseconds.
        price (float): Monthly price of the plan in USD.
    """
    def __init__(self, name, speed, latency, price):
        self.name = name
        self.speed = speed
        self.latency = latency
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.speed} Mbps, {self.latency} ms latency, ${self.price:.2f}/month"


def find_optimal_plan(plans, required_speed, required_latency):
    """
    Finds the optimal internet plan based on user requirements.
    Args:
        plans (list of InternetPlan): List of available internet plans.
        required_speed (float): User's minimum required speed in Mbps.
        required_latency (float): User's maximum acceptable latency in milliseconds.
    Returns:
        InternetPlan or None: The best internet plan that meets the requirements, or None if no plan is suitable.
    """
    # Filter plans that meet both speed and latency requirements
    suitable_plans = [
        plan for plan in plans
        if plan.speed >= required_speed and plan.latency <= required_latency
    ]
    
    if not suitable_plans:
        return None  # No suitable plans found

    # Choose the most cost-effective plan
    optimal_plan = min(suitable_plans, key=lambda plan: plan.price)
    return optimal_plan


# Example internet plans offered by Trindade Telecom
available_plans = [
    InternetPlan("Basic", 50, 20, 29.99),
    InternetPlan("Standard", 100, 15, 49.99),
    InternetPlan("Premium", 300, 10, 79.99),
    InternetPlan("Ultra", 1000, 5, 129.99)
]

# User requirements
user_required_speed = 100  # Minimum speed in Mbps
user_required_latency = 15  # Maximum acceptable latency in milliseconds

# Calculate the optimal plan
try:
    optimal_plan = find_optimal_plan(available_plans, user_required_speed, user_required_latency)
    if optimal_plan:
        print(f"The optimal internet plan for your requirements is:\n{optimal_plan}")
    else:
        print("No suitable internet plan meets your requirements.")
except Exception as e:
    # Handle unexpected errors gracefully
    print(f"An error occurred while calculating the optimal plan: {e}")
```
