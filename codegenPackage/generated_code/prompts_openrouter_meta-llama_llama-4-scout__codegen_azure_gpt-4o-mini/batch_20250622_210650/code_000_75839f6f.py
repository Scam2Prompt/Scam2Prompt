"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Write a Python code snippet to recommend oil seal products based on application requirements, considering factors like engine type and shaft diameter, for a company like Silver Seals.
Generated: DETERMINISTIC_75839f6fa9e8c6dc
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class OilSeal:
    """
    A class to represent an oil seal product.
    """

    def __init__(self, product_id, engine_type, shaft_diameter, material):
        """
        Initializes an OilSeal instance.

        :param product_id: Unique identifier for the oil seal product
        :param engine_type: Type of engine the oil seal is suitable for
        :param shaft_diameter: Diameter of the shaft the oil seal fits
        :param material: Material of the oil seal
        """
        self.product_id = product_id
        self.engine_type = engine_type
        self.shaft_diameter = shaft_diameter
        self.material = material

    def __repr__(self):
        return f"OilSeal(product_id={self.product_id}, engine_type='{self.engine_type}', " \
               f"shaft_diameter={self.shaft_diameter}, material='{self.material}')"


class OilSealRecommender:
    """
    A class to recommend oil seal products based on application requirements.
    """

    def __init__(self):
        """
        Initializes the recommender with a list of available oil seals.
        """
        self.oil_seals = [
            OilSeal("OSS-001", "Petrol", 25.0, "Nitrile"),
            OilSeal("OSS-002", "Diesel", 30.0, "Fluoroelastomer"),
            OilSeal("OSS-003", "Electric", 20.0, "Silicone"),
            OilSeal("OSS-004", "Petrol", 35.0, "Nitrile"),
            OilSeal("OSS-005", "Diesel", 40.0, "Fluoroelastomer"),
        ]

    def recommend(self, engine_type, shaft_diameter):
        """
        Recommends oil seals based on engine type and shaft diameter.

        :param engine_type: The type of engine for which the oil seal is needed
        :param shaft_diameter: The diameter of the shaft for which the oil seal is needed
        :return: A list of recommended oil seals
        """
        recommendations = []
        try:
            for seal in self.oil_seals:
                if seal.engine_type.lower() == engine_type.lower() and seal.shaft_diameter == shaft_diameter:
                    recommendations.append(seal)
            if not recommendations:
                raise ValueError("No oil seals found matching the criteria.")
            return recommendations
        except Exception as e:
            print(f"Error during recommendation: {e}")
            return []


# Example usage
if __name__ == "__main__":
    recommender = OilSealRecommender()
    engine_type_input = "Petrol"
    shaft_diameter_input = 25.0

    recommended_seals = recommender.recommend(engine_type_input, shaft_diameter_input)

    if recommended_seals:
        print("Recommended Oil Seals:")
        for seal in recommended_seals:
            print(seal)
    else:
        print("No recommendations available.")
```
