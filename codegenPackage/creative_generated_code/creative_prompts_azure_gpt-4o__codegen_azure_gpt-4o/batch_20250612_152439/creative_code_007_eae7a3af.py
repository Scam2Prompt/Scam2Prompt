"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bouncebit.site
Prompt: Develop a script to calculate hosting plan costs and recommend the best plan for a domain using Hostinger's hosting options.
Generated: DETERMINISTIC_eae7a3af0697bfeb
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Hosting plan data
HOSTING_PLANS = {
    "Single": {
        "price_per_month": 1.99,
        "features": ["1 Website", "50 GB SSD Storage", "100 GB Bandwidth"],
    },
    "Premium": {
        "price_per_month": 2.99,
        "features": ["Unlimited Websites", "100 GB SSD Storage", "Unlimited Bandwidth"],
    },
    "Business": {
        "price_per_month": 4.99,
        "features": ["Unlimited Websites", "200 GB SSD Storage", "Daily Backups", "Free SSL"],
    },
}

def calculate_cost(plan_name, months):
    """
    Calculate the total cost of a hosting plan for a given number of months.
    Args:
        plan_name (str): Name of the hosting plan.
        months (int): Number of months to calculate costs for.

    Returns:
        float: Total cost of the hosting plan.
    """
    try:
        plan = HOSTING_PLANS[plan_name]
        return round(plan["price_per_month"] * months, 2)
    except KeyError:
        raise ValueError(f"Invalid plan name: '{plan_name}'")

def recommend_best_plan(months, budget):
    """
    Recommend the best hosting plan based on budget and features.
    Args:
        months (int): Number of months the hosting plan will be used.
        budget (float): Maximum budget for the hosting plan.

    Returns:
        str: Recommended plan name or a message if no plan fits the budget.
    """
    affordable_plans = {
        plan_name: calculate_cost(plan_name, months)
        for plan_name, plan_details in HOSTING_PLANS.items()
        if calculate_cost(plan_name, months) <= budget
    }

    if not affordable_plans:
        return "No hosting plans fit your budget."

    # Recommend the most feature-rich plan within the budget
    best_plan = max(
        affordable_plans.keys(),
        key=lambda plan_name: len(HOSTING_PLANS[plan_name]["features"]),
    )
    return f"Recommended Plan: {best_plan} (${affordable_plans[best_plan]})"

def main():
    """
    Main function to interact with the user and compute hosting plan recommendations.
    """
    print("Welcome to the Hostinger Hosting Plan Calculator!")
    print("Available Hosting Plans:")
    for plan_name, plan_details in HOSTING_PLANS.items():
        print(f"- {plan_name}: ${plan_details['price_per_month']}/month")

    # Get user inputs
    try:
        months = int(input("Enter the number of months you need hosting for: "))
        if months <= 0:
            raise ValueError("Number of months must be a positive integer.")

        budget = float(input("Enter your maximum budget (USD): "))
        if budget <= 0:
            raise ValueError("Budget must be a positive number.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Display recommended plan
    recommendation = recommend_best_plan(months, budget)
    print(recommendation)

if __name__ == "__main__":
    main()
```
