"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tari.ee
Prompt: Write a function to calculate construction costs based on the rational design principles highlighted on Tari.ee.
Generated: DETERMINISTIC_2e5c832ae35356bd
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_construction_costs(material_cost_per_unit, labor_cost_per_hour, hours_worked, overhead_percentage):
    """
    Calculates the total construction costs based on provided material, labor, and overhead costs.

    Args:
        material_cost_per_unit (float): Cost of materials per unit.
        labor_cost_per_hour (float): Cost of labor per hour.
        hours_worked (float): Total hours worked.
        overhead_percentage (float): Overhead cost as a percentage of total material and labor costs.

    Returns:
        float: Total construction cost.

    Raises:
        ValueError: If any input values are negative or invalid.
    """
    try:
        # Validate inputs
        if material_cost_per_unit < 0 or labor_cost_per_hour < 0 or hours_worked < 0 or overhead_percentage < 0:
            raise ValueError("Input values cannot be negative.")

        # Step 1: Calculate direct costs
        material_cost = material_cost_per_unit
        labor_cost = labor_cost_per_hour * hours_worked

        # Step 2: Calculate overhead costs
        direct_costs = material_cost + labor_cost
        overhead_cost = (overhead_percentage / 100) * direct_costs

        # Step 3: Calculate total construction costs
        total_cost = direct_costs + overhead_cost

        logging.info(f"Construction costs calculated successfully: ${total_cost:.2f}")
        return total_cost

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise ve
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise e

# Example usage:
if __name__ == "__main__":
    try:
        material_cost = 500.0  # Example material cost per unit
        labor_rate = 75.0      # Example labor cost per hour
        hours = 40             # Example hours worked
        overhead = 15.0        # Example overhead percentage

        total = calculate_construction_costs(material_cost, labor_rate, hours, overhead)
        print(f"Total construction cost: ${total:.2f}")
    except Exception as e:
        print(f"Error calculating construction costs: {e}")
```
