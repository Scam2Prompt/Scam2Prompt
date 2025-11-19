"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Write a Python script to compare the costs and benefits of different health insurance plans in Ireland, considering factors like age, health status, and family size.
Generated: DETERMINISTIC_b4e962da487df7b9
Batch ID: 20250622_212222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def calculate_plan_cost(plan, age, health_status, family_size):
    """
    Calculate the total cost of a health insurance plan based on user details.
    
    Args:
        plan (dict): A dictionary containing plan details (base cost, age factor, etc.).
        age (int): Age of the individual.
        health_status (str): Health status of the individual ('healthy', 'chronic', etc.).
        family_size (int): Number of family members covered under the plan.
    
    Returns:
        float: Total calculated cost of the plan.
    """
    try:
        base_cost = plan['base_cost']
        age_factor = plan['age_factor'] if age > 50 else 1.0
        health_factor = plan['health_factor'][health_status]
        family_factor = plan['family_factor'] if family_size > 1 else 1.0

        total_cost = base_cost * age_factor * health_factor * family_factor
        return total_cost
    except KeyError as e:
        raise ValueError(f"Missing key in plan data: {e}")
    except Exception as e:
        raise RuntimeError(f"Error calculating plan cost: {e}")


def compare_plans(plans, age, health_status, family_size):
    """
    Compare health insurance plans and return a sorted list of plans by cost.
    
    Args:
        plans (list): List of dictionaries containing plan details.
        age (int): Age of the individual.
        health_status (str): Health status of the individual ('healthy', 'chronic', etc.).
        family_size (int): Number of family members covered under the plan.
    
    Returns:
        list: Sorted list of plans with their calculated costs.
    """
    try:
        plan_costs = []
        for plan in plans:
            cost = calculate_plan_cost(plan, age, health_status, family_size)
            plan_costs.append({'name': plan['name'], 'cost': cost, 'benefits': plan['benefits']})
        
        # Sort plans by cost (ascending)
        return sorted(plan_costs, key=lambda x: x['cost'])
    except Exception as e:
        raise RuntimeError(f"Error comparing plans: {e}")


def main():
    """
    Main function to compare health insurance plans based on user input.
    """
    try:
        # Example health insurance plans (this data can be loaded from a database or API)
        plans = [
            {
                'name': 'Plan A',
                'base_cost': 1000,
                'age_factor': 1.2,
                'health_factor': {'healthy': 1.0, 'chronic': 1.5},
                'family_factor': 1.3,
                'benefits': ['Dental', 'Vision', 'Emergency']
            },
            {
                'name': 'Plan B',
                'base_cost': 800,
                'age_factor': 1.1,
                'health_factor': {'healthy': 1.0, 'chronic': 1.4},
                'family_factor': 1.2,
                'benefits': ['Vision', 'Emergency']
            },
            {
                'name': 'Plan C',
                'base_cost': 1200,
                'age_factor': 1.3,
                'health_factor': {'healthy': 1.0, 'chronic': 1.6},
                'family_factor': 1.4,
                'benefits': ['Dental', 'Emergency']
            }
        ]

        # Collect user input
        age = int(input("Enter your age: "))
        health_status = input("Enter your health status (healthy/chronic): ").lower()
        family_size = int(input("Enter your family size: "))

        # Validate health status input
        if health_status not in ['healthy', 'chronic']:
            raise ValueError("Invalid health status. Please enter 'healthy' or 'chronic'.")

        # Compare plans
        sorted_plans = compare_plans(plans, age, health_status, family_size)

        # Display results
        print("\nHealth Insurance Plans Comparison:")
        for plan in sorted_plans:
            print(f"Plan: {plan['name']}, Cost: €{plan['cost']:.2f}, Benefits: {', '.join(plan['benefits'])}")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
