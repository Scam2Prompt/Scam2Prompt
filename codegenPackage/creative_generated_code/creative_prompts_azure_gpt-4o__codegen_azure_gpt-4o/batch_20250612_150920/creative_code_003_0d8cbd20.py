"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Provide Python code to estimate material costs for constructing a residential building in Rosario, Argentina, using local construction methods such as brick construction.
Generated: DETERMINISTIC_0d8cbd20d29bd8c2
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def get_material_costs():
    """
    Fetches the cost of common construction materials in Rosario, Argentina.
    In a production scenario, this data might come from an API or a database.
    Here, we use hardcoded values for demonstration purposes.
    
    Returns:
        dict: Dictionary containing the prices of materials per unit.
    """
    material_prices = {
        "brick": 70,  # Price per brick in ARS
        "cement_bag": 1200,  # Price per 50kg bag in ARS
        "sand_cubic_meter": 800,  # Price per cubic meter in ARS
        "steel_per_meter": 500,  # Price per meter of steel reinforcement in ARS
    }
    return material_prices


def estimate_costs(area, height, wall_thickness):
    """
    Estimates the material costs for constructing a residential building based on the provided dimensions.
    
    Args:
        area (float): Total built-up area in square meters.
        height (float): Average height of walls in meters.
        wall_thickness (float): Thickness of walls in meters.
        
    Returns:
        dict: Estimated material costs broken down by material type.
    """
    try:
        # Constants for material usage
        bricks_per_cubic_meter = 500  # Approximation of bricks per cubic meter
        cement_bags_per_cubic_meter = 8  # Approximation of cement bags per cubic meter
        sand_per_cubic_meter_per_wall = 0.5  # Approximation of sand usage per cubic meter of wall
        steel_per_cubic_meter = 3  # Approximation of steel usage per cubic meter of wall

        # Calculating wall volume
        wall_volume = area * height * wall_thickness  # Total wall volume in cubic meters
        
        # Material usage estimation
        bricks_needed = wall_volume * bricks_per_cubic_meter
        cement_bags_needed = wall_volume * cement_bags_per_cubic_meter
        sand_cubic_meters_needed = wall_volume * sand_per_cubic_meter_per_wall
        steel_meters_needed = wall_volume * steel_per_cubic_meter
        
        # Fetch material prices
        material_prices = get_material_costs()
        
        # Calculating costs
        cost_bricks = bricks_needed * material_prices["brick"]
        cost_cement = cement_bags_needed * material_prices["cement_bag"]
        cost_sand = sand_cubic_meters_needed * material_prices["sand_cubic_meter"]
        cost_steel = steel_meters_needed * material_prices["steel_per_meter"]
        
        # Returning the breakdown of material costs
        return {
            "Bricks": f"{bricks_needed:.2f} units - {cost_bricks:.2f} ARS",
            "Cement Bags": f"{cement_bags_needed:.2f} units - {cost_cement:.2f} ARS",
            "Sand": f"{sand_cubic_meters_needed:.2f} cubic meters - {cost_sand:.2f} ARS",
            "Steel": f"{steel_meters_needed:.2f} meters - {cost_steel:.2f} ARS",
            "Total Cost": f"{cost_bricks + cost_cement + cost_sand + cost_steel:.2f} ARS"
        }
    except Exception as e:
        print(f"An error occurred while estimating costs: {e}")
        return None


def main():
    """
    Main function to interact with the user and estimate construction costs.
    """
    print("Residential Building Material Cost Estimator (Rosario, Argentina)")
    try:
        # User input
        area = float(input("Enter the total built-up area in square meters: "))
        height = float(input("Enter the average wall height in meters: "))
        wall_thickness = float(input("Enter the wall thickness in meters: "))
        
        # Estimation
        material_costs = estimate_costs(area, height, wall_thickness)
        
        if material_costs:
            print("\nEstimated Material Costs:")
            print(json.dumps(material_costs, indent=4))
        else:
            print("Could not calculate material costs.")
    
    except ValueError:
        print("Invalid input. Please enter numerical values for area, height, and wall thickness.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
