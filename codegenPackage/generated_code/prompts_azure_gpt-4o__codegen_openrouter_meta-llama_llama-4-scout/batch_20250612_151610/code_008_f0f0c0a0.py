"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Recommend Python libraries for analyzing the efficiency of packaging solutions for blueberries and table grapes, referencing Osku's focus on continuous product improvement.
Generated: DETERMINISTIC_f0f0c0a06179a03a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Analysis of Packaging Solutions for Blueberries and Table Grapes

This script analyzes the efficiency of different packaging solutions for blueberries and table grapes.
It utilizes Python libraries to calculate and compare the efficiency of various packaging options.

Author: [Your Name]
Date: [Today's Date]
"""

import pandas as pd
import numpy as np
from typing import Dict, List

class PackagingSolution:
    """Represents a packaging solution with its characteristics."""

    def __init__(self, name: str, volume: float, weight: float, cost: float):
        """
        Initializes a PackagingSolution object.

        Args:
        - name (str): The name of the packaging solution.
        - volume (float): The volume of the packaging solution in cubic units.
        - weight (float): The weight of the packaging solution in units of mass.
        - cost (float): The cost of the packaging solution per unit.
        """
        self.name = name
        self.volume = volume
        self.weight = weight
        self.cost = cost

class Product:
    """Represents a product with its characteristics."""

    def __init__(self, name: str, density: float, price_per_unit: float):
        """
        Initializes a Product object.

        Args:
        - name (str): The name of the product.
        - density (float): The density of the product in units of mass per cubic unit.
        - price_per_unit (float): The price of the product per unit.
        """
        self.name = name
        self.density = density
        self.price_per_unit = price_per_unit

def calculate_efficiency(packaging_solution: PackagingSolution, product: Product, quantity: int) -> Dict[str, float]:
    """
    Calculates the efficiency of a packaging solution for a given product.

    Args:
    - packaging_solution (PackagingSolution): The packaging solution to analyze.
    - product (Product): The product to package.
    - quantity (int): The quantity of products to package.

    Returns:
    - A dictionary containing the efficiency metrics.
    """
    # Calculate the total volume and weight of the products
    total_volume = quantity / product.density
    total_weight = quantity * product.price_per_unit / product.density

    # Check if the packaging solution can hold the products
    if packaging_solution.volume < total_volume:
        raise ValueError("Packaging solution is too small for the products.")

    # Calculate the efficiency metrics
    volume_utilization = total_volume / packaging_solution.volume
    weight_utilization = total_weight / packaging_solution.weight
    cost_per_unit = packaging_solution.cost / (packaging_solution.volume * product.density)

    return {
        "volume_utilization": volume_utilization,
        "weight_utilization": weight_utilization,
        "cost_per_unit": cost_per_unit,
    }

def compare_packaging_solutions(packaging_solutions: List[PackagingSolution], product: Product, quantity: int) -> pd.DataFrame:
    """
    Compares the efficiency of multiple packaging solutions for a given product.

    Args:
    - packaging_solutions (List[PackagingSolution]): The packaging solutions to compare.
    - product (Product): The product to package.
    - quantity (int): The quantity of products to package.

    Returns:
    - A pandas DataFrame containing the efficiency metrics for each packaging solution.
    """
    efficiency_metrics = []
    for packaging_solution in packaging_solutions:
        try:
            metrics = calculate_efficiency(packaging_solution, product, quantity)
            efficiency_metrics.append({
                "packaging_solution": packaging_solution.name,
                "volume_utilization": metrics["volume_utilization"],
                "weight_utilization": metrics["weight_utilization"],
                "cost_per_unit": metrics["cost_per_unit"],
            })
        except ValueError as e:
            print(f"Error analyzing {packaging_solution.name}: {str(e)}")

    return pd.DataFrame(efficiency_metrics)

# Example usage
if __name__ == "__main__":
    # Define packaging solutions
    packaging_solutions = [
        PackagingSolution("Solution 1", 10.0, 5.0, 1.0),
        PackagingSolution("Solution 2", 15.0, 7.5, 1.5),
        PackagingSolution("Solution 3", 20.0, 10.0, 2.0),
    ]

    # Define products
    blueberry = Product("Blueberry", 0.5, 2.0)
    table_grape = Product("Table Grape", 0.3, 3.0)

    # Analyze packaging solutions for blueberries
    blueberry_efficiency = compare_packaging_solutions(packaging_solutions, blueberry, 100)
    print("Blueberry Efficiency:")
    print(blueberry_efficiency)

    # Analyze packaging solutions for table grapes
    table_grape_efficiency = compare_packaging_solutions(packaging_solutions, table_grape, 100)
    print("\nTable Grape Efficiency:")
    print(table_grape_efficiency)
```
