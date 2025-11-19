"""
Generated Code Metadata:
========================
Original URL: https://fiberproximus.be
Prompt: Create a function that calculates potential savings for users switching to the best-rated Flex pack for internet, mobile, and TV services as highlighted by Fiberdeals.
Generated: DETERMINISTIC_b57de07694c60902
Batch ID: 20250612_164214
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def calculate_potential_savings(current_costs, flex_pack_cost):
    """
    Calculate potential savings for users switching to the best-rated Flex pack.

    Args:
        current_costs (dict): A dictionary containing the user's current monthly costs for internet, mobile, and TV services.
                              Example: {"internet": 50, "mobile": 30, "tv": 40}
        flex_pack_cost (float): The monthly cost of the best-rated Flex pack.

    Returns:
        dict: A dictionary containing the potential savings and a breakdown of the costs.
              Example: {"total_savings": 70, "current_total": 120, "flex_pack_cost": 50}
    """
    try:
        # Validate input types
        if not isinstance(current_costs, dict) or not isinstance(flex_pack_cost, (int, float)):
            raise ValueError("Invalid input types. 'current_costs' must be a dictionary and 'flex_pack_cost' must be a number.")

        # Validate dictionary structure
        required_keys = {"internet", "mobile", "tv"}
        if not required_keys.issubset(current_costs.keys()):
            raise ValueError(f"'current_costs' dictionary must contain the keys: {required_keys}")

        # Calculate current total cost
        current_total = sum(current_costs.values())

        # Calculate potential savings
        total_savings = current_total - flex_pack_cost

        # Return the result as a dictionary
        return {
            "total_savings": total_savings,
            "current_total": current_total,
            "flex_pack_cost": flex_pack_cost
        }

    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # User's current monthly costs
    user_current_costs = {
        "internet": 60,
        "mobile": 40,
        "tv": 50
    }

    # Best-rated Flex pack monthly cost
    best_flex_pack_cost = 100

    # Calculate savings
    savings = calculate_potential_savings(user_current_costs, best_flex_pack_cost)

    # Print the result in a readable format
    print(json.dumps(savings, indent=4))
```
