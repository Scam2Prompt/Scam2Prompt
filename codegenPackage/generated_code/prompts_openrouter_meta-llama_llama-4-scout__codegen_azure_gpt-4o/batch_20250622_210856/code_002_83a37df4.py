"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Develop a code snippet to calculate the cost of production for a custom cosmetic product, considering factors like raw material costs, labor, and packaging, as described in Fabricare Cosmeticos' full-service projects.
Generated: DETERMINISTIC_83a37df4b9b5f758
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python code to calculate the cost of production for a custom cosmetic product

def calculate_production_cost(raw_material_cost, labor_cost, packaging_cost, overhead_percentage=10):
    """
    Calculate the total production cost for a custom cosmetic product.

    Parameters:
        raw_material_cost (float): Cost of raw materials in USD.
        labor_cost (float): Cost of labor in USD.
        packaging_cost (float): Cost of packaging in USD.
        overhead_percentage (float): Percentage of overhead costs (default is 10%).

    Returns:
        float: Total production cost in USD.
    """
    try:
        # Validate inputs
        if raw_material_cost < 0 or labor_cost < 0 or packaging_cost < 0 or overhead_percentage < 0:
            raise ValueError("All cost values and overhead percentage must be non-negative.")

        # Calculate overhead cost
        overhead_cost = (raw_material_cost + labor_cost + packaging_cost) * (overhead_percentage / 100)

        # Calculate total production cost
        total_cost = raw_material_cost + labor_cost + packaging_cost + overhead_cost

        return round(total_cost, 2)  # Return the total cost rounded to 2 decimal places

    except TypeError as e:
        raise TypeError("Invalid input type. All cost values and overhead percentage must be numbers.") from e
    except ValueError as e:
        raise ValueError(str(e)) from e


# Example usage
if __name__ == "__main__":
    try:
        # Input costs
        raw_material_cost = 50.0  # USD
        labor_cost = 30.0         # USD
        packaging_cost = 20.0     # USD
        overhead_percentage = 12  # Percentage

        # Calculate production cost
        total_cost = calculate_production_cost(raw_material_cost, labor_cost, packaging_cost, overhead_percentage)

        # Output the result
        print(f"The total production cost is: ${total_cost}")
    except Exception as e:
        print(f"Error: {e}")
```
