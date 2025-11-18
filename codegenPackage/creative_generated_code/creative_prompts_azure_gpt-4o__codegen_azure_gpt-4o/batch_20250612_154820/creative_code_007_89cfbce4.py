"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Create a Python function to calculate potential savings when switching health insurance providers, based on data like premium costs and benefits, as discussed on the Health Insurance Shop blog.
Generated: DETERMINISTIC_89cfbce49f8180a2
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# health_insurance_savings.py

def calculate_savings(current_plan, new_plan):
    """
    Calculate potential savings when switching health insurance providers.

    Parameters:
        current_plan (dict): A dictionary containing details of the current insurance plan.
                             Expected keys: 'premium_cost', 'deductible', 'out_of_pocket_limit', 'benefits_coverage'
        new_plan (dict): A dictionary containing details of the new insurance plan.
                         Expected keys: 'premium_cost', 'deductible', 'out_of_pocket_limit', 'benefits_coverage'

    Returns:
        dict: A dictionary containing potential savings and a breakdown of the comparison.
              Keys: 'annual_premium_savings', 'deductible_savings', 'total_savings', 'is_new_plan_better'
    """
    
    # Validate input data
    try:
        required_keys = {'premium_cost', 'deductible', 'out_of_pocket_limit', 'benefits_coverage'}
        if not all(key in current_plan for key in required_keys):
            raise ValueError("Missing required keys in current_plan dictionary.")
        if not all(key in new_plan for key in required_keys):
            raise ValueError("Missing required keys in new_plan dictionary.")
    except ValueError as e:
        return {"error": str(e)}

    # Extract relevant data
    current_premium = current_plan.get('premium_cost', 0)
    new_premium = new_plan.get('premium_cost', 0)
    current_deductible = current_plan.get('deductible', 0)
    new_deductible = new_plan.get('deductible', 0)
    current_out_of_pocket = current_plan.get('out_of_pocket_limit', 0)
    new_out_of_pocket = new_plan.get('out_of_pocket_limit', 0)
    current_benefits = current_plan.get('benefits_coverage', 0)
    new_benefits = new_plan.get('benefits_coverage', 0)

    # Calculate savings
    annual_premium_savings = current_premium - new_premium
    deductible_savings = current_deductible - new_deductible
    total_savings = annual_premium_savings + deductible_savings
    is_new_plan_better = total_savings > 0 and new_benefits >= current_benefits

    # Generate result dictionary
    result = {
        'annual_premium_savings': annual_premium_savings,
        'deductible_savings': deductible_savings,
        'total_savings': total_savings,
        'is_new_plan_better': is_new_plan_better
    }

    return result


# Example usage:
if __name__ == "__main__":
    current_plan_data = {
        'premium_cost': 5000,
        'deductible': 1000,
        'out_of_pocket_limit': 7000,
        'benefits_coverage': 80  # Percentage of benefits covered
    }

    new_plan_data = {
        'premium_cost': 4500,
        'deductible': 800,
        'out_of_pocket_limit': 6000,
        'benefits_coverage': 90  # Percentage of benefits covered
    }

    # Perform savings calculation
    savings = calculate_savings(current_plan_data, new_plan_data)
    print("Savings Analysis:", savings)
```
