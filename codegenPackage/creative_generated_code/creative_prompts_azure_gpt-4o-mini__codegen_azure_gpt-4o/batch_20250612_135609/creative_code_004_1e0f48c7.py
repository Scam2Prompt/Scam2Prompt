"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peacecitycontracting.com
Prompt: Develop a library function that calculates the estimated costs for fit-out works based on material and labor inputs in a contracting context.
Generated: DETERMINISTIC_1e0f48c751fe221e
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# fit_out_costs.py

"""
Library that calculates estimated costs for fit-out works based on material and labor inputs.
This module is designed for use in a contracting context and adheres to best programming practices.
"""

def calculate_fit_out_costs(material_costs, labor_hours, hourly_labor_rate):
    """
    Calculate the total estimated cost for fit-out works.

    Parameters:
        material_costs (list of float): A list of material costs in the fit-out project.
                                        Each value represents the cost of a specific material.
        labor_hours (float): The total number of labor hours required for the fit-out works.
        hourly_labor_rate (float): The cost per labor hour.

    Returns:
        dict: A dictionary containing the breakdown of the costs:
              - "material_total": Total cost of materials.
              - "labor_total": Total cost of labor.
              - "grand_total": Combined total cost of materials and labor.

    Raises:
        ValueError: If any of the inputs are negative or invalid.
    """
    # Validate inputs
    if not isinstance(material_costs, list) or not all(isinstance(cost, (int, float)) for cost in material_costs):
        raise ValueError("material_costs must be a list of numeric values.")
    if not isinstance(labor_hours, (int, float)) or labor_hours < 0:
        raise ValueError("labor_hours must be a positive numeric value.")
    if not isinstance(hourly_labor_rate, (int, float)) or hourly_labor_rate < 0:
        raise ValueError("hourly_labor_rate must be a positive numeric value.")

    # Calculate total material costs
    material_total = sum(material_costs)

    # Calculate total labor costs
    labor_total = labor_hours * hourly_labor_rate

    # Calculate grand total cost
    grand_total = material_total + labor_total

    # Return the breakdown of costs
    return {
        "material_total": round(material_total, 2),
        "labor_total": round(labor_total, 2),
        "grand_total": round(grand_total, 2)
    }


if __name__ == "__main__":
    # Example usage
    try:
        materials = [1200.50, 800.75, 450.30]  # Example material costs
        hours = 40  # Example labor hours
        rate = 25.00  # Example hourly labor rate

        result = calculate_fit_out_costs(materials, hours, rate)
        print("Cost Breakdown:")
        print(f"Material Total: ${result['material_total']}")
        print(f"Labor Total: ${result['labor_total']}")
        print(f"Grand Total: ${result['grand_total']}")
    except ValueError as e:
        print(f"Error: {e}")
```
