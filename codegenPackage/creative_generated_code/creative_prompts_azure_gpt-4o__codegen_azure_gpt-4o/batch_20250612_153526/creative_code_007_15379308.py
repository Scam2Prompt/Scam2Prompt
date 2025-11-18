"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wealthbhai.com
Prompt: Write a program to calculate the cost-effectiveness of using TP316L stainless steel pipes in medical equipment manufacturing, factoring in material quality and production techniques.
Generated: DETERMINISTIC_15379308ec1a4542
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the cost-effectiveness of using TP316L stainless steel pipes 
in medical equipment manufacturing. Factors include material quality and production techniques.
"""

# Import necessary modules
import sys

def calculate_cost_effectiveness(material_cost_per_kg, production_tech_cost, quality_score, quantity, labor_cost_per_unit):
    """
    Function to calculate cost-effectiveness based on given parameters.

    Parameters:
        material_cost_per_kg (float): Cost per kilogram of TP316L stainless steel.
        production_tech_cost (float): Cost of implementing production techniques per unit.
        quality_score (float): A score representing material quality (1 to 10, higher is better).
        quantity (int): Number of units of pipe being manufactured.
        labor_cost_per_unit (float): Labor cost per unit of pipe.

    Returns:
        float: Cost-effectiveness score.
    """
    try:
        # Validate inputs
        if material_cost_per_kg <= 0 or production_tech_cost <= 0 or quality_score <= 0 or quantity <= 0 or labor_cost_per_unit <= 0:
            raise ValueError("All inputs must be positive values.")

        # Total material cost
        total_material_cost = material_cost_per_kg * quantity

        # Total production technique cost
        total_production_cost = production_tech_cost * quantity

        # Total labor cost
        total_labor_cost = labor_cost_per_unit * quantity

        # Total cost
        total_cost = total_material_cost + total_production_cost + total_labor_cost

        # Calculate cost-effectiveness score: higher quality and lower total cost yield better scores
        cost_effectiveness = quality_score / total_cost

        return cost_effectiveness

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate cost-effectiveness.
    """
    try:
        print("Welcome to the TP316L stainless steel pipe cost-effectiveness calculator!")

        # Collect user inputs
        material_cost_per_kg = float(input("Enter the material cost per kilogram of TP316L stainless steel: "))
        production_tech_cost = float(input("Enter the production technique cost per unit: "))
        quality_score = float(input("Enter the quality score of the material (1 to 10): "))
        quantity = int(input("Enter the number of units being manufactured: "))
        labor_cost_per_unit = float(input("Enter the labor cost per unit: "))

        # Calculate cost-effectiveness
        cost_effectiveness = calculate_cost_effectiveness(
            material_cost_per_kg,
            production_tech_cost,
            quality_score,
            quantity,
            labor_cost_per_unit
        )

        if cost_effectiveness is not None:
            print(f"\nCost-effectiveness score: {cost_effectiveness:.4f}")
        else:
            print("\nUnable to calculate cost-effectiveness due to input errors.")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
