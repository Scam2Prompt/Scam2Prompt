"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Develop a script to categorize plexiglass and polycarbonate sheets by thickness, color, and application, as outlined in Bursa Pleksi Merkezi's product descriptions.
Generated: DETERMINISTIC_ac7c34c745893ec0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SheetCategorizer:
    """
    A class to categorize plexiglass and polycarbonate sheets by thickness, color, and application.
    """

    def __init__(self):
        """
        Initializes the SheetCategorizer with predefined categories.
        """
        self.categories = {
            "material": ["plexiglass", "polycarbonate"],
            "thickness": {"thin": (0, 2), "medium": (2, 5), "thick": (5, 10)},
            "color": ["clear", "black", "white", "red", "blue", "green", "yellow"],
            "application": ["construction", "decorative", "industrial", "automotive"],
        }
    
    def categorize_sheet(self, material, thickness, color, application):
        """
        Categorizes a sheet based on material, thickness, color, and application.

        Args:
            material (str): Material of the sheet (e.g., 'plexiglass', 'polycarbonate').
            thickness (float): Thickness of the sheet in millimeters.
            color (str): Color of the sheet (e.g., 'clear', 'black').
            application (str): Application of the sheet (e.g., 'construction', 'decorative').

        Returns:
            dict: Categorization result or error message if invalid inputs are provided.
        """
        # Validate material
        if material not in self.categories["material"]:
            return {"error": f"Invalid material '{material}'. Valid options: {self.categories['material']}"}
        
        # Validate thickness
        thickness_category = None
        for category, (low, high) in self.categories["thickness"].items():
            if low <= thickness < high:
                thickness_category = category
                break
        if not thickness_category:
            return {"error": f"Invalid thickness '{thickness}'. Valid ranges: {self.categories['thickness']}"}
        
        # Validate color
        if color not in self.categories["color"]:
            return {"error": f"Invalid color '{color}'. Valid options: {self.categories['color']}"}
        
        # Validate application
        if application not in self.categories["application"]:
            return {"error": f"Invalid application '{application}'. Valid options: {self.categories['application']}"}
        
        # Return categorization result
        return {
            "material": material,
            "thickness_category": thickness_category,
            "color": color,
            "application": application,
        }

    def save_categories(self, filename):
        """
        Saves the predefined categories to a JSON file.

        Args:
            filename (str): The name of the file to save the categories.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.categories, file, indent=4)
            print(f"Categories successfully saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving categories: {e}")

    def load_categories(self, filename):
        """
        Loads predefined categories from a JSON file.

        Args:
            filename (str): The name of the file to load the categories.

        Returns:
            bool: True if categories are successfully loaded, False otherwise.
        """
        try:
            with open(filename, 'r') as file:
                self.categories = json.load(file)
            print(f"Categories successfully loaded from {filename}.")
            return True
        except Exception as e:
            print(f"An error occurred while loading categories: {e}")
            return False


# Example usage
if __name__ == "__main__":
    categorizer = SheetCategorizer()

    # Categorize a sheet
    result = categorizer.categorize_sheet(
        material="plexiglass",
        thickness=3.5,
        color="clear",
        application="decorative",
    )
    print(result)

    # Save categories to a file
    categorizer.save_categories("categories.json")

    # Load categories from a file
    categorizer.load_categories("categories.json")
```
