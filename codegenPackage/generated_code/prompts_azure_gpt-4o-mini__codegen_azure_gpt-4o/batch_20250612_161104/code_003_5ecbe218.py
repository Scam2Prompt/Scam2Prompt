"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Create a function that calculates the cost-effectiveness of using trailer drop services for freight forwarding, based on the operational efficiencies highlighted by Calmar Transport.
Generated: DETERMINISTIC_5ecbe218c17139bb
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict, Union

def calculate_cost_effectiveness(
    trailer_drop_cost: float, 
    operational_efficiency: Dict[str, Union[float, int]]
) -> float:
    """
    Calculate the cost-effectiveness of using trailer drop services for freight forwarding.

    Parameters:
        trailer_drop_cost (float): The cost of using trailer drop services.
        operational_efficiency (Dict[str, Union[float, int]]): A dictionary containing operational efficiency metrics.
            Expected keys:
                - 'time_saved_hours' (float): Number of hours saved using trailer drop services.
                - 'labor_cost_per_hour' (float): Cost of labor per hour.
                - 'fuel_saved_gallons' (float): Amount of fuel saved in gallons.
                - 'fuel_cost_per_gallon' (float): Cost of fuel per gallon.
                - 'additional_revenue_generated' (float): Additional revenue generated due to improved efficiency.

    Returns:
        float: The net cost-effectiveness value. Positive values indicate cost savings, 
               while negative values indicate a loss.
    """
    try:
        # Extract operational efficiency metrics
        time_saved_hours = operational_efficiency.get('time_saved_hours', 0.0)
        labor_cost_per_hour = operational_efficiency.get('labor_cost_per_hour', 0.0)
        fuel_saved_gallons = operational_efficiency.get('fuel_saved_gallons', 0.0)
        fuel_cost_per_gallon = operational_efficiency.get('fuel_cost_per_gallon', 0.0)
        additional_revenue_generated = operational_efficiency.get('additional_revenue_generated', 0.0)

        # Calculate savings from labor and fuel
        labor_savings = time_saved_hours * labor_cost_per_hour
        fuel_savings = fuel_saved_gallons * fuel_cost_per_gallon

        # Calculate total savings
        total_savings = labor_savings + fuel_savings + additional_revenue_generated

        # Calculate cost-effectiveness
        cost_effectiveness = total_savings - trailer_drop_cost

        return cost_effectiveness

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while calculating cost-effectiveness: {e}")
        return 0.0

# Example usage
if __name__ == "__main__":
    # Example operational efficiency metrics
    operational_efficiency_data = {
        'time_saved_hours': 10.5,
        'labor_cost_per_hour': 25.0,
        'fuel_saved_gallons': 50.0,
        'fuel_cost_per_gallon': 3.5,
        'additional_revenue_generated': 500.0
    }

    # Example trailer drop cost
    trailer_drop_service_cost = 800.0

    # Calculate cost-effectiveness
    result = calculate_cost_effectiveness(trailer_drop_service_cost, operational_efficiency_data)
    print(f"Cost-effectiveness of trailer drop services: ${result:.2f}")
```
