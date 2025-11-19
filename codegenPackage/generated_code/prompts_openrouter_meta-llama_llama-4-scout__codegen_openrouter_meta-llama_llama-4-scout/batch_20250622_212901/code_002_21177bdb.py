"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Recommend a suitable material for creating outdoor signage that can withstand harsh weather conditions, considering factors like UV resistance and flexibility.
Generated: DETERMINISTIC_21177bdb9cff5dd0
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# material_recommender.py

class Material:
    def __init__(self, name, uv_resistance, flexibility, weather_resistance):
        """
        Initialize a Material object.

        Args:
            name (str): Material name.
            uv_resistance (int): UV resistance level (1-10).
            flexibility (int): Flexibility level (1-10).
            weather_resistance (int): Weather resistance level (1-10).
        """
        self.name = name
        self.uv_resistance = uv_resistance
        self.flexibility = flexibility
        self.weather_resistance = weather_resistance

    def __str__(self):
        return f"{self.name}: UV Resistance={self.uv_resistance}, Flexibility={self.flexibility}, Weather Resistance={self.weather_resistance}"


class MaterialRecommender:
    def __init__(self):
        """
        Initialize a MaterialRecommender object.
        """
        self.materials = [
            Material("Acrylic", 8, 6, 9),
            Material("Polycarbonate", 9, 8, 9),
            Material("PVC", 6, 7, 7),
            Material("Aluminum Composite Panel", 9, 5, 9),
            Material("Corrugated Plastic", 5, 8, 6),
        ]

    def recommend_material(self, min_uv_resistance=7, min_flexibility=6, min_weather_resistance=8):
        """
        Recommend a suitable material for outdoor signage.

        Args:
            min_uv_resistance (int): Minimum UV resistance level (default=7).
            min_flexibility (int): Minimum flexibility level (default=6).
            min_weather_resistance (int): Minimum weather resistance level (default=8).

        Returns:
            list: Recommended materials.
        """
        recommended_materials = [
            material for material in self.materials
            if material.uv_resistance >= min_uv_resistance
            and material.flexibility >= min_flexibility
            and material.weather_resistance >= min_weather_resistance
        ]
        return recommended_materials


def main():
    try:
        recommender = MaterialRecommender()
        recommended_materials = recommender.recommend_material()
        if recommended_materials:
            print("Recommended materials:")
            for material in recommended_materials:
                print(material)
        else:
            print("No materials meet the specified criteria.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
