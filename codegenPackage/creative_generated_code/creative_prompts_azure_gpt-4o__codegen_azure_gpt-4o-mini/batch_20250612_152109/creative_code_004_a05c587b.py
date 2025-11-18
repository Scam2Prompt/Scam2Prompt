"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Suggest tools or libraries for creating eco-friendly craft boxes, similar to the project described on Craft Intra.
Generated: DETERMINISTIC_a05c587bbb72edf5
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/sustainable-suppliers": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class EcoFriendlyCraftBox:
    """
    A class to represent an eco-friendly craft box project.
    
    Attributes:
        materials (list): A list of materials for the craft box.
        suppliers (dict): A dictionary of suppliers with their eco-friendly materials.
    """

    def __init__(self):
        """Initialize the EcoFriendlyCraftBox with default materials and suppliers."""
        self.materials = []
        self.suppliers = {
            'Supplier A': ['Recycled Paper', 'Natural Dye', 'Bamboo'],
            'Supplier B': ['Organic Cotton', 'Eco-Friendly Glue', 'Wooden Sticks'],
            'Supplier C': ['Compostable Plastic', 'Biodegradable Glitter', 'Hemp Rope']
        }

    def add_material(self, material):
        """
        Add a material to the craft box.
        
        Parameters:
            material (str): The material to add.
        """
        self.materials.append(material)
        print(f"Material '{material}' added to the craft box.")

    def fetch_sustainable_suppliers(self):
        """
        Fetch sustainable suppliers from an external API.
        
        Raises:
            requests.RequestException: If the API request fails.
        """
        try:
            response = requests.get('https://api.example.com/sustainable-suppliers')
            response.raise_for_status()  # Raise an error for HTTP errors
            suppliers_data = response.json()
            self.suppliers.update(suppliers_data)
            print("Sustainable suppliers fetched successfully.")
        except requests.RequestException as e:
            print(f"Error fetching sustainable suppliers: {e}")

    def display_craft_box_contents(self):
        """
        Display the contents of the craft box.
        """
        print("Craft Box Contents:")
        if self.materials:
            for material in self.materials:
                print(f"- {material}")
        else:
            print("The craft box is empty.")

    def display_suppliers(self):
        """
        Display the available suppliers and their materials.
        """
        print("Available Suppliers and Materials:")
        for supplier, materials in self.suppliers.items():
            print(f"{supplier}: {', '.join(materials)}")

if __name__ == "__main__":
    craft_box = EcoFriendlyCraftBox()

    # Adding materials to the craft box
    craft_box.add_material('Recycled Cardboard')
    craft_box.add_material('Plant-Based Paint')

    # Fetching and displaying sustainable suppliers
    craft_box.fetch_sustainable_suppliers()
    craft_box.display_suppliers()

    # Displaying the contents of the craft box
    craft_box.display_craft_box_contents()
```
