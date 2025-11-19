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
# oil_seal_recommender.py

class OilSeal:
    def __init__(self, product_id, engine_type, shaft_diameter, material):
        """
        Initialize an OilSeal object.

        Args:
            product_id (str): Unique product identifier.
            engine_type (str): Type of engine (e.g., gasoline, diesel).
            shaft_diameter (float): Diameter of the shaft.
            material (str): Material used for the seal (e.g., rubber, silicone).
        """
        self.product_id = product_id
        self.engine_type = engine_type
        self.shaft_diameter = shaft_diameter
        self.material = material

class OilSealRecommender:
    def __init__(self):
        """
        Initialize an OilSealRecommender object.

        Attributes:
            oil_seals (list): List of available OilSeal products.
        """
        self.oil_seals = [
            OilSeal("SS-001", "gasoline", 20.0, "rubber"),
            OilSeal("SS-002", "diesel", 25.0, "silicone"),
            OilSeal("SS-003", "gasoline", 30.0, "rubber"),
            OilSeal("SS-004", "diesel", 20.0, "silicone"),
            # Add more products here...
        ]

    def recommend(self, engine_type, shaft_diameter):
        """
        Recommend oil seal products based on application requirements.

        Args:
            engine_type (str): Type of engine (e.g., gasoline, diesel).
            shaft_diameter (float): Diameter of the shaft.

        Returns:
            list: List of recommended OilSeal products.

        Raises:
            ValueError: If engine type or shaft diameter is invalid.
        """
        if not engine_type or not shaft_diameter:
            raise ValueError("Engine type and shaft diameter are required.")

        recommended_seals = [seal for seal in self.oil_seals 
                             if seal.engine_type == engine_type.lower() 
                             and abs(seal.shaft_diameter - shaft_diameter) <= 1.0]

        return recommended_seals

def main():
    try:
        recommender = OilSealRecommender()
        engine_type = input("Enter engine type (gasoline/diesel): ")
        shaft_diameter = float(input("Enter shaft diameter (mm): "))

        recommended_seals = recommender.recommend(engine_type, shaft_diameter)

        if recommended_seals:
            print("Recommended Oil Seal Products:")
            for seal in recommended_seals:
                print(f"Product ID: {seal.product_id}, Engine Type: {seal.engine_type}, Shaft Diameter: {seal.shaft_diameter}mm, Material: {seal.material}")
        else:
            print("No matching products found.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
