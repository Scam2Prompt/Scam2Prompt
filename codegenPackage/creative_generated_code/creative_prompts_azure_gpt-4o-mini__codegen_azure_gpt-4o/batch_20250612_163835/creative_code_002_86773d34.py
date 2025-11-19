"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Write a code snippet to calculate the cost-effectiveness of using Hastelloy C-276 in construction projects, referencing Roshako's product line.
Generated: DETERMINISTIC_86773d34dd26bcf8
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import math

# Define a function to calculate cost-effectiveness
def calculate_cost_effectiveness(material_cost_per_kg, lifespan_years, maintenance_cost_per_year, reference_material_cost_per_kg, reference_lifespan_years, reference_maintenance_cost_per_year):
    """
    Calculate the cost-effectiveness of using Hastelloy C-276 compared to a reference material.

    Args:
        material_cost_per_kg (float): Cost per kilogram of Hastelloy C-276.
        lifespan_years (int): Expected lifespan in years of Hastelloy C-276.
        maintenance_cost_per_year (float): Annual maintenance cost for Hastelloy C-276.
        reference_material_cost_per_kg (float): Cost per kilogram of the reference material.
        reference_lifespan_years (int): Expected lifespan in years of the reference material.
        reference_maintenance_cost_per_year (float): Annual maintenance cost for the reference material.

    Returns:
        dict: A dictionary containing cost-effectiveness metrics.
    """
    # Validate input
    if material_cost_per_kg <= 0 or lifespan_years <= 0 or maintenance_cost_per_year < 0:
        raise ValueError("Material cost, lifespan, and maintenance costs must be positive.")
    if reference_material_cost_per_kg <= 0 or reference_lifespan_years <= 0 or reference_maintenance_cost_per_year < 0:
        raise ValueError("Reference material values must be positive.")

    # Total cost for Hastelloy C-276 (over its lifespan)
    total_cost_hastelloy = (
        material_cost_per_kg + (lifespan_years * maintenance_cost_per_year)
    )
    
    # Total cost for reference material (over its lifespan)
    total_cost_reference = (
        reference_material_cost_per_kg + (reference_lifespan_years * reference_maintenance_cost_per_year)
    )

    # Cost-effectiveness comparison (lower is better)
    cost_effectiveness_ratio = total_cost_hastelloy / total_cost_reference

    # Return a structured result
    return {
        "total_cost_hastelloy": total_cost_hastelloy,
        "total_cost_reference": total_cost_reference,
        "cost_effectiveness_ratio": cost_effectiveness_ratio,
        "is_hastelloy_more_cost_effective": cost_effectiveness_ratio < 1,
    }

# Example usage
try:
    # Parameters for Hastelloy C-276
    hastelloy_cost_per_kg = 50.0  # Example: $50 per kilogram
    hastelloy_lifespan_years = 50  # Example: 50 years lifespan
    hastelloy_maintenance_cost = 2.0  # Example: $2/year maintenance cost

    # Parameters for reference material (e.g., generic stainless steel)
    reference_cost_per_kg = 30.0  # Example: $30 per kilogram
    reference_lifespan_years = 20  # Example: 20 years lifespan
    reference_maintenance_cost = 5.0  # Example: $5/year maintenance cost

    # Calculate cost-effectiveness
    result = calculate_cost_effectiveness(
        hastelloy_cost_per_kg,
        hastelloy_lifespan_years,
        hastelloy_maintenance_cost,
        reference_cost_per_kg,
        reference_lifespan_years,
        reference_maintenance_cost,
    )

    # Display results
    print("Cost-Effectiveness Analysis:")
    for key, value in result.items():
        print(f"{key}: {value}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
