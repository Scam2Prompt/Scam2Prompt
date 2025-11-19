"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Create a program to recommend the best material (e.g., PVC expanded, acrylic sheets) for retail display applications, based on the use cases provided on the unitramabrazz website.
Generated: DETERMINISTIC_e3a5e531ffa3cde8
Batch ID: 20250612_151040
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
    """Class representing a material with its properties and use cases."""
    
    def __init__(self, name, properties, use_cases):
        """
        Initialize a Material instance.

        Args:
            name (str): The name of the material.
            properties (dict): A dictionary of properties of the material.
            use_cases (list): A list of use cases for the material.
        """
        self.name = name
        self.properties = properties
        self.use_cases = use_cases

    def __str__(self):
        """Return a string representation of the material."""
        return f"{self.name}: {self.properties}, Use Cases: {', '.join(self.use_cases)}"


class MaterialRecommender:
    """Class to recommend materials based on use cases."""
    
    def __init__(self):
        """Initialize the recommender with predefined materials."""
        self.materials = [
            Material("PVC Expanded", 
                     {"Durability": "High", "Weight": "Light", "Cost": "Low"},
                     ["Signage", "Display Boards", "Exhibits"]),
            Material("Acrylic Sheets", 
                     {"Durability": "Medium", "Weight": "Light", "Cost": "Medium"},
                     ["Display Cases", "Store Fixtures", "Point of Purchase Displays"]),
            Material("Wood", 
                     {"Durability": "High", "Weight": "Heavy", "Cost": "High"},
                     ["Custom Displays", "Furniture", "Decorative Elements"]),
            Material("Metal", 
                     {"Durability": "Very High", "Weight": "Heavy", "Cost": "High"},
                     ["Structural Displays", "High-End Fixtures"]),
        ]

    def recommend_material(self, use_case):
        """
        Recommend a material based on the provided use case.

        Args:
            use_case (str): The use case for which a material is needed.

        Returns:
            str: A recommendation message with the suitable materials.
        """
        recommended_materials = [
            material for material in self.materials if use_case in material.use_cases
        ]

        if not recommended_materials:
            return f"No suitable materials found for the use case: '{use_case}'."

        recommendations = "\n".join(str(material) for material in recommended_materials)
        return f"Recommended materials for '{use_case}':\n{recommendations}"


def main():
    """Main function to run the material recommender."""
    recommender = MaterialRecommender()
    
    # Example use cases to test the recommender
    use_cases = [
        "Signage",
        "Display Cases",
        "Custom Displays",
        "High-End Fixtures",
        "Unknown Use Case"
    ]

    for use_case in use_cases:
        try:
            print(recommender.recommend_material(use_case))
            print("-" * 50)  # Separator for readability
        except Exception as e:
            print(f"An error occurred while recommending materials: {e}")


if __name__ == "__main__":
    main()
```
