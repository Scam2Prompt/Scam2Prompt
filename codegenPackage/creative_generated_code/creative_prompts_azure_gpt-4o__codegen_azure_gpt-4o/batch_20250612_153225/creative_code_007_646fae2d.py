"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Write a function to calculate the cost-benefit ratio of internet plans, factoring in speed (Mbps), latency, and installation features, as described on Trindade Telecom's site.
Generated: DETERMINISTIC_646fae2dcab3a3c2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

def calculate_cost_benefit(plans: List[Dict]) -> List[Dict]:
    """
    Calculate the cost-benefit ratio for internet plans.

    Parameters:
        plans (List[Dict]): A list of dictionaries, each containing the details of an internet plan.
            Each dictionary must have the following keys:
                - 'name': str, name of the plan
                - 'cost': float, monthly cost of the plan in USD
                - 'speed': float, speed of the plan in Mbps
                - 'latency': float, average latency of the plan in milliseconds
                - 'installation_included': bool, whether installation is included for free
    
    Returns:
        List[Dict]: A list of dictionaries, sorted by cost-benefit ratio in descending order.
            Each dictionary contains:
                - 'name': str, name of the plan
                - 'cost_benefit_ratio': float, calculated cost-benefit ratio
    """
    # Validate input
    for plan in plans:
        if not all(key in plan for key in ('name', 'cost', 'speed', 'latency', 'installation_included')):
            raise ValueError("Each plan dictionary must contain 'name', 'cost', 'speed', 'latency', and 'installation_included' keys.")
        if not isinstance(plan['name'], str) or not isinstance(plan['cost'], (int, float)) or not isinstance(plan['speed'], (int, float)) \
                or not isinstance(plan['latency'], (int, float)) or not isinstance(plan['installation_included'], bool):
            raise TypeError("Invalid data type for plan details.")
    
    # Calculate cost-benefit ratio for each plan
    results = []
    for plan in plans:
        # Increase the score if installation is included
        installation_bonus = 1.2 if plan['installation_included'] else 1.0
        
        # Cost-benefit ratio formula considering speed, latency, and cost
        try:
            cost_benefit_ratio = (plan['speed'] / plan['latency']) * installation_bonus / plan['cost']
        except ZeroDivisionError:
            raise ValueError("Plan cost cannot be zero.")

        results.append({
            'name': plan['name'],
            'cost_benefit_ratio': round(cost_benefit_ratio, 2)  # Round for better readability
        })
    
    # Sort the plans by cost-benefit ratio in descending order
    results.sort(key=lambda x: x['cost_benefit_ratio'], reverse=True)
    
    return results

# Example usage
if __name__ == "__main__":
    internet_plans = [
        {'name': 'Basic Plan', 'cost': 50, 'speed': 100, 'latency': 20, 'installation_included': False},
        {'name': 'Premium Plan', 'cost': 80, 'speed': 300, 'latency': 10, 'installation_included': True},
        {'name': 'Economy Plan', 'cost': 40, 'speed': 50, 'latency': 30, 'installation_included': False},
    ]
    
    try:
        results = calculate_cost_benefit(internet_plans)
        for plan in results:
            print(f"Plan: {plan['name']}, Cost-Benefit Ratio: {plan['cost_benefit_ratio']}")
    except Exception as e:
        print(f"Error: {e}")
```
