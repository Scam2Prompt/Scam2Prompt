"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Create a calculator to estimate the cost of a pool building project based on factors like pool type, size, location, and materials, using data from the Poolz website.
Generated: DETERMINISTIC_537d14c85cd3a778
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def get_pool_cost(pool_type, size, location, material):
    """
    Estimate the cost of a pool building project based on the given parameters.

    Parameters:
        pool_type (str): Type of pool (e.g., "in-ground", "above-ground").
        size (float): Size of the pool in square meters.
        location (str): Location of the project (e.g., "urban", "rural").
        material (str): Material used for the pool (e.g., "concrete", "fiberglass").

    Returns:
        float: Estimated cost of the pool building project.
    """
    # Base costs for pool types
    pool_type_cost = {
        "in-ground": 500,
        "above-ground": 300
    }

    # Location adjustment factors
    location_factor = {
        "urban": 1.2,
        "rural": 1.0
    }

    # Material cost per square meter
    material_cost = {
        "concrete": 100,
        "fiberglass": 80
    }

    # Validate inputs
    if pool_type not in pool_type_cost:
        raise ValueError(f"Invalid pool type: {pool_type}. Choose 'in-ground' or 'above-ground'.")
    if location not in location_factor:
        raise ValueError(f"Invalid location: {location}. Choose 'urban' or 'rural'.")
    if material not in material_cost:
        raise ValueError(f"Invalid material: {material}. Choose 'concrete' or 'fiberglass'.")
    if size <= 0:
        raise ValueError("Size must be a positive number.")

    # Calculate cost
    base_cost = pool_type_cost[pool_type]
    material_total_cost = material_cost[material] * size
    location_adjustment = location_factor[location]

    total_cost = (base_cost + material_total_cost) * location_adjustment
    return total_cost


def main():
    """
    Main function to interact with the user and calculate pool building costs.
    """
    print("Welcome to the Pool Building Cost Calculator!")
    try:
        # Get user inputs
        pool_type = input("Enter pool type (in-ground/above-ground): ").strip().lower()
        size = float(input("Enter pool size in square meters: "))
        location = input("Enter location (urban/rural): ").strip().lower()
        material = input("Enter material (concrete/fiberglass): ").strip().lower()

        # Calculate cost
        estimated_cost = get_pool_cost(pool_type, size, location, material)
        print(f"The estimated cost of building your pool is: ${estimated_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Pool Building Cost Calculator!")


if __name__ == "__main__":
    main()
```
