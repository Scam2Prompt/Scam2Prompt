"""
Generated Code Metadata:
========================
Original URL: https://watpac.in
Prompt: Generate a code snippet that uses Watpac's waterproofing solutions for a construction project, including specific products like Watpac Exterior Shield and Crack Fillers.
Generated: DETERMINISTIC_383d97b7a6fd122f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# watpac_waterproofing.py

class WatpacWaterproofing:
    """
    A class to represent Watpac's waterproofing solutions for a construction project.
    Includes methods to apply specific products like Exterior Shield and Crack Fillers.
    """

    def __init__(self, project_name):
        """
        Initialize the waterproofing project with a name.
        :param project_name: Name of the construction project
        """
        self.project_name = project_name
        self.applied_products = []

    def apply_exterior_shield(self, area):
        """
        Apply Watpac Exterior Shield to a specified area.
        :param area: Area in square meters to apply the Exterior Shield
        :raises ValueError: If the area is not a positive number
        """
        if area <= 0:
            raise ValueError("Area must be a positive number.")
        self.applied_products.append(f"Exterior Shield applied to {area} sq.m.")
        print(f"Watpac Exterior Shield successfully applied to {area} square meters.")

    def apply_crack_filler(self, crack_length):
        """
        Apply Watpac Crack Filler to a specified crack length.
        :param crack_length: Length of the crack in meters to fill
        :raises ValueError: If the crack length is not a positive number
        """
        if crack_length <= 0:
            raise ValueError("Crack length must be a positive number.")
        self.applied_products.append(f"Crack Filler applied to {crack_length} meters.")
        print(f"Watpac Crack Filler successfully applied to {crack_length} meters.")

    def get_applied_products(self):
        """
        Get a summary of all applied products.
        :return: List of applied products
        """
        return self.applied_products


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the waterproofing project
        project = WatpacWaterproofing("Downtown Office Building")

        # Apply Watpac Exterior Shield to 500 square meters
        project.apply_exterior_shield(500)

        # Apply Watpac Crack Filler to 20 meters of cracks
        project.apply_crack_filler(20)

        # Print a summary of applied products
        print("\nSummary of Applied Products:")
        for product in project.get_applied_products():
            print(product)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
