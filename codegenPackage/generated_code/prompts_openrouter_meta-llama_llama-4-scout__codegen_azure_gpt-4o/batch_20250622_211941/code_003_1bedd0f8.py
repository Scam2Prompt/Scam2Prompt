"""
Generated Code Metadata:
========================
Original URL: https://fxtrademasterclass.com
Prompt: Compare the features and benefits of the different investment plans offered by Fxtrademasterclass, including the Starter, Basic, Pro, and Executive plans.
Generated: DETERMINISTIC_1bedd0f88c1c1257
Batch ID: 20250622_211941
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_plans.py

# Import necessary modules
import json

# Define the investment plans with their features and benefits
investment_plans = [
    {
        "name": "Starter",
        "minimum_investment": 100,
        "maximum_investment": 999,
        "roi_percentage": 5,
        "support": "Email Support",
        "withdrawal_limit": "Monthly",
        "benefits": [
            "Low-risk investment",
            "Beginner-friendly",
            "Access to basic market insights"
        ]
    },
    {
        "name": "Basic",
        "minimum_investment": 1000,
        "maximum_investment": 4999,
        "roi_percentage": 7,
        "support": "Email and Chat Support",
        "withdrawal_limit": "Bi-weekly",
        "benefits": [
            "Moderate-risk investment",
            "Access to advanced market insights",
            "Priority support"
        ]
    },
    {
        "name": "Pro",
        "minimum_investment": 5000,
        "maximum_investment": 19999,
        "roi_percentage": 10,
        "support": "Dedicated Account Manager",
        "withdrawal_limit": "Weekly",
        "benefits": [
            "High ROI potential",
            "Access to premium market insights",
            "Dedicated account management"
        ]
    },
    {
        "name": "Executive",
        "minimum_investment": 20000,
        "maximum_investment": None,  # No upper limit
        "roi_percentage": 15,
        "support": "24/7 VIP Support",
        "withdrawal_limit": "Daily",
        "benefits": [
            "Maximum ROI potential",
            "Exclusive market insights",
            "24/7 VIP support",
            "Custom investment strategies"
        ]
    }
]

def compare_investment_plans(plans):
    """
    Compare and display the features and benefits of different investment plans.

    Args:
        plans (list): A list of dictionaries containing investment plan details.

    Returns:
        None
    """
    try:
        print("Comparison of Investment Plans:\n")
        for plan in plans:
            print(f"Plan Name: {plan['name']}")
            print(f"Minimum Investment: ${plan['minimum_investment']}")
            print(f"Maximum Investment: ${plan['maximum_investment'] if plan['maximum_investment'] else 'No Limit'}")
            print(f"ROI Percentage: {plan['roi_percentage']}%")
            print(f"Support: {plan['support']}")
            print(f"Withdrawal Limit: {plan['withdrawal_limit']}")
            print("Benefits:")
            for benefit in plan['benefits']:
                print(f"  - {benefit}")
            print("-" * 40)
    except Exception as e:
        print(f"An error occurred while comparing investment plans: {e}")

def save_plans_to_file(plans, filename="investment_plans.json"):
    """
    Save the investment plans to a JSON file.

    Args:
        plans (list): A list of dictionaries containing investment plan details.
        filename (str): The name of the file to save the plans to.

    Returns:
        None
    """
    try:
        with open(filename, "w") as file:
            json.dump(plans, file, indent=4)
        print(f"Investment plans successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving investment plans to file: {e}")

if __name__ == "__main__":
    # Compare the investment plans
    compare_investment_plans(investment_plans)

    # Save the investment plans to a file
    save_plans_to_file(investment_plans)
```
