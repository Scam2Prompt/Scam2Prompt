"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fiberproximus.be
Prompt: Create a function that calculates potential savings for users switching to the best-rated Flex pack for internet, mobile, and TV services as highlighted by Fiberdeals.
Generated: DETERMINISTIC_b57de07694c60902
Batch ID: 20250612_164214
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_potential_savings(current_costs, flex_pack_cost):
    """
    Calculate potential savings for users switching to the best-rated Flex pack.

    Parameters:
        current_costs (dict): A dictionary containing current costs for internet, mobile, and TV services.
                              Example: {'internet': 60, 'mobile': 40, 'tv': 50}
        flex_pack_cost (float): The monthly cost of the best-rated Flex pack.

    Returns:
        dict: A dictionary containing the savings for each service and total savings.
              Example: {'internet_savings': 20, 'mobile_savings': 30, 'tv_savings': 10, 'total_savings': 60}
    """
    try:
        # Validate input types
        if not isinstance(current_costs, dict):
            raise ValueError("current_costs must be a dictionary.")
        if not isinstance(flex_pack_cost, (int, float)):
            raise ValueError("flex_pack_cost must be a number.")

        # Validate current_costs dictionary structure
        required_keys = {'internet', 'mobile', 'tv'}
        if not required_keys.issubset(current_costs.keys()):
            raise ValueError(f"current_costs must contain the following keys: {required_keys}")

        # Calculate savings for each service
        internet_savings = max(0, current_costs['internet'] - flex_pack_cost)
        mobile_savings = max(0, current_costs['mobile'] - flex_pack_cost)
        tv_savings = max(0, current_costs['tv'] - flex_pack_cost)

        # Calculate total savings
        total_savings = internet_savings + mobile_savings + tv_savings

        # Return savings in a structured format
        return {
            'internet_savings': internet_savings,
            'mobile_savings': mobile_savings,
            'tv_savings': tv_savings,
            'total_savings': total_savings
        }

    except ValueError as ve:
        # Handle input validation errors
        return {"error": str(ve)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage:
if __name__ == '__main__':
    current_costs_example = {
        'internet': 60,
        'mobile': 40,
        'tv': 50
    }
    flex_pack_cost_example = 30

    # Calculate savings
    savings = calculate_potential_savings(current_costs_example, flex_pack_cost_example)

    # Print the result in a readable format
    print(json.dumps(savings, indent=4))
```
