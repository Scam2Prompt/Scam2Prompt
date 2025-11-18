"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Provide a Python script to automate the selection of fasteners like "Parafuso Cabeça de Martelo" and "Porcas" based on the material type of the roof structure in a solar energy project.
Generated: DETERMINISTIC_b7f09434b602123d
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FastenerSelector:
    """A class to select fasteners based on the material type of the roof structure."""

    def __init__(self):
        """Initialize the fastener selection criteria."""
        self.fastener_options = {
            'metal': {
                'screws': 'Parafuso Cabeça de Martelo',
                'nuts': 'Porcas'
            },
            'wood': {
                'screws': 'Wood Screws',
                'nuts': 'N/A'  # Wood does not use nuts
            },
            'concrete': {
                'screws': 'Concrete Screws',
                'nuts': 'N/A'  # Concrete does not use nuts
            }
        }

    def select_fasteners(self, material_type):
        """Selects fasteners based on the given material type.

        Args:
            material_type (str): The type of roof material.

        Returns:
            dict: A dictionary containing the selected screws and nuts.

        Raises:
            ValueError: If the provided material type is not recognized.
        """
        material_type = material_type.lower()
        if material_type not in self.fastener_options:
            raise ValueError(f"Unrecognized material type: '{material_type}'. "
                             "Please use one of the following: 'metal', 'wood', 'concrete'.")

        return self.fastener_options[material_type]

def main():
    """Main function to run the fastener selection process."""
    selector = FastenerSelector()
    
    # Example material types for testing
    material_types = ['metal', 'wood', 'concrete', 'plastic']

    # Iterate through the list of material types
    for material in material_types:
        try:
            fasteners = selector.select_fasteners(material)
            print(f"Material: {material.title()}")
            print(f"Selected Screws: {fasteners['screws']}")
            print(f"Selected Nuts: {fasteners['nuts']}")
            print('-' * 30)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
