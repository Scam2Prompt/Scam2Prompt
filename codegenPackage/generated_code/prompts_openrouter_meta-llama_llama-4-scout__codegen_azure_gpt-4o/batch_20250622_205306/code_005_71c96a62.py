"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Write a code snippet to calculate the environmental impact of packaging materials used for exporting fruits, considering factors like carbon footprint and recyclability."
Generated: DETERMINISTIC_71c96a62e4447689
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PackagingMaterial:
    """
    Class to represent a packaging material and calculate its environmental impact.
    """
    def __init__(self, name, carbon_footprint_per_kg, recyclability_score):
        """
        Initialize a packaging material.

        :param name: Name of the packaging material (e.g., 'Plastic', 'Cardboard').
        :param carbon_footprint_per_kg: Carbon footprint per kilogram of the material (in kg CO2).
        :param recyclability_score: Recyclability score (0 to 1, where 1 is fully recyclable).
        """
        self.name = name
        self.carbon_footprint_per_kg = carbon_footprint_per_kg
        self.recyclability_score = recyclability_score

    def calculate_impact(self, weight_in_kg):
        """
        Calculate the environmental impact of the material based on weight.

        :param weight_in_kg: Weight of the material used (in kg).
        :return: Dictionary containing carbon footprint and recyclability score.
        """
        if weight_in_kg < 0:
            raise ValueError("Weight cannot be negative.")
        
        carbon_footprint = self.carbon_footprint_per_kg * weight_in_kg
        return {
            "material": self.name,
            "carbon_footprint": carbon_footprint,
            "recyclability_score": self.recyclability_score
        }

def calculate_total_impact(materials, weights):
    """
    Calculate the total environmental impact for multiple packaging materials.

    :param materials: List of PackagingMaterial objects.
    :param weights: List of weights corresponding to each material (in kg).
    :return: Dictionary containing total carbon footprint and average recyclability score.
    """
    if len(materials) != len(weights):
        raise ValueError("Materials and weights lists must have the same length.")
    
    total_carbon_footprint = 0
    total_recyclability_score = 0
    total_weight = 0

    for material, weight in zip(materials, weights):
        impact = material.calculate_impact(weight)
        total_carbon_footprint += impact["carbon_footprint"]
        total_recyclability_score += impact["recyclability_score"] * weight
        total_weight += weight

    average_recyclability_score = total_recyclability_score / total_weight if total_weight > 0 else 0

    return {
        "total_carbon_footprint": total_carbon_footprint,
        "average_recyclability_score": average_recyclability_score
    }

def main():
    """
    Main function to demonstrate the calculation of environmental impact.
    """
    try:
        # Define packaging materials
        plastic = PackagingMaterial("Plastic", carbon_footprint_per_kg=6.0, recyclability_score=0.3)
        cardboard = PackagingMaterial("Cardboard", carbon_footprint_per_kg=1.5, recyclability_score=0.8)
        glass = PackagingMaterial("Glass", carbon_footprint_per_kg=2.0, recyclability_score=0.9)

        # Define weights used for exporting fruits (in kg)
        weights = [10, 20, 15]  # Plastic: 10kg, Cardboard: 20kg, Glass: 15kg

        # Calculate total impact
        total_impact = calculate_total_impact([plastic, cardboard, glass], weights)

        # Print results
        print(json.dumps(total_impact, indent=4))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
