"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: "Create a list of materials needed for a solar panel installation using Suporte L em Inox 304 and Arruela de Vedação EPDM."
Generated: DETERMINISTIC_67a9fc9dce70b539
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_panel_installation.py

class SolarPanelInstallation:
    """
    A class to represent a solar panel installation materials list.
    """

    def __init__(self):
        """
        Initializes the materials list for the solar panel installation.
        """
        self.materials = []

    def add_material(self, material: str, quantity: int):
        """
        Adds a material and its quantity to the materials list.

        Parameters:
        material (str): The name of the material.
        quantity (int): The quantity of the material.

        Raises:
        ValueError: If quantity is not a positive integer.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.materials.append({"material": material, "quantity": quantity})

    def get_materials(self):
        """
        Returns the list of materials needed for the installation.

        Returns:
        list: A list of dictionaries containing materials and their quantities.
        """
        return self.materials

    def display_materials(self):
        """
        Displays the materials list in a readable format.
        """
        if not self.materials:
            print("No materials added yet.")
            return
        
        print("Materials needed for Solar Panel Installation:")
        for item in self.materials:
            print(f"- {item['quantity']} x {item['material']}")

def main():
    """
    Main function to create a materials list for solar panel installation.
    """
    try:
        installation = SolarPanelInstallation()
        
        # Adding materials to the installation
        installation.add_material("Suporte L em Inox 304", 10)
        installation.add_material("Arruela de Vedação EPDM", 20)

        # Displaying the materials list
        installation.display_materials()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
