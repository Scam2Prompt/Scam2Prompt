"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://relivo.se
Prompt: Write an algorithm that calculates the cost-effectiveness of Relivo compared to purchasing separate supplements for collagen, probiotics, prebiotics, vitamins, and minerals.
Generated: DETERMINISTIC_456d2cfce5594711
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_cost_effectiveness(relivo_cost, supplements_cost):
    """
    Calculate the cost-effectiveness of Relivo compared to purchasing separate supplements.
    
    Parameters:
        relivo_cost (float): The cost of Relivo.
        supplements_cost (dict): A dictionary containing the costs of individual supplements.
                                 Keys represent supplement types ("collagen", "probiotics", etc.).
                                 Values represent their respective costs in float.
    
    Returns:
        dict: A dictionary with the following keys:
              - "total_supplements_cost": Total cost of supplements.
              - "relivo_cost": Cost of Relivo.
              - "savings": Cost savings when using Relivo. (Positive if Relivo is cheaper)
              - "is_relivo_cost_effective": Boolean indicating if Relivo is more cost-effective.
    """
    try:
        # Ensure valid inputs
        if not isinstance(relivo_cost, (int, float)) or relivo_cost <= 0:
            raise ValueError("Relivo cost must be a positive number.")
        
        if not isinstance(supplements_cost, dict) or not supplements_cost:
            raise ValueError("Supplements cost must be a non-empty dictionary.")
        
        for supplement, cost in supplements_cost.items():
            if not isinstance(cost, (int, float)) or cost <= 0:
                raise ValueError(f"Cost for {supplement} must be a positive number.")

        # Calculate total cost of supplements
        total_supplements_cost = sum(supplements_cost.values())

        # Calculate savings
        savings = total_supplements_cost - relivo_cost

        # Determine if Relivo is more cost-effective
        is_relivo_cost_effective = savings > 0

        # Return results in a dictionary
        return {
            "total_supplements_cost": total_supplements_cost,
            "relivo_cost": relivo_cost,
            "savings": savings,
            "is_relivo_cost_effective": is_relivo_cost_effective
        }
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


# Example usage:
if __name__ == "__main__":
    # Define the costs
    relivo_price = 50.0  # Example cost of Relivo
    supplements_prices = {
        "collagen": 20.0,
        "probiotics": 15.0,
        "prebiotics": 10.0,
        "vitamins": 25.0,
        "minerals": 12.0
    }

    # Calculate cost-effectiveness
    result = calculate_cost_effectiveness(relivo_price, supplements_prices)

    # Print results
    if result:
        print("Cost-Effectiveness Analysis:")
        print(f"Total Supplements Cost: ${result['total_supplements_cost']:.2f}")
        print(f"Relivo Cost: ${result['relivo_cost']:.2f}")
        print(f"Savings: ${result['savings']:.2f}")
        print(f"Is Relivo Cost-Effective? {'Yes' if result['is_relivo_cost_effective'] else 'No'}")
```
