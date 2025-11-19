"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: "Compare the properties and uses of organic and inorganic pigments in the textile industry."
Generated: DETERMINISTIC_12454df11f1613a6
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a comparison between organic and inorganic pigments used in the textile industry.
It includes their properties, uses, advantages, and disadvantages.
"""

class Pigment:
    """Base class representing a pigment with common properties."""
    def __init__(self, name, chemical_composition, lightfastness, heat_resistance):
        """
        Initialize a pigment with basic properties.
        
        Args:
            name (str): Name of the pigment
            chemical_composition (str): Chemical composition
            lightfastness (int): Resistance to fading (1-5 scale)
            heat_resistance (int): Resistance to heat (1-5 scale)
        """
        self.name = name
        self.chemical_composition = chemical_composition
        self.lightfastness = lightfastness
        self.heat_resistance = heat_resistance
        self.type = "Generic Pigment"
    
    def get_properties(self):
        """Return a dictionary of the pigment's properties."""
        return {
            "Name": self.name,
            "Type": self.type,
            "Chemical Composition": self.chemical_composition,
            "Lightfastness": self.lightfastness,
            "Heat Resistance": self.heat_resistance
        }
    
    def common_uses(self):
        """Return common uses of the pigment."""
        return ["Generic textile applications"]

class OrganicPigment(Pigment):
    """Class representing organic pigments."""
    def __init__(self, name, chemical_composition, lightfastness, heat_resistance, solubility):
        """
        Initialize an organic pigment.
        
        Args:
            solubility (str): Solubility characteristics
        """
        super().__init__(name, chemical_composition, lightfastness, heat_resistance)
        self.type = "Organic Pigment"
        self.solubility = solubility
    
    def get_properties(self):
        """Return properties including organic-specific attributes."""
        properties = super().get_properties()
        properties.update({
            "Solubility": self.solubility,
            "Advantages": "Bright colors, high tinting strength",
            "Disadvantages": "Lower lightfastness compared to inorganic"
        })
        return properties
    
    def common_uses(self):
        """Return common uses of organic pigments."""
        return [
            "Fashion textiles requiring bright colors",
            "Printing inks for textiles",
            "Applications where color intensity is prioritized over durability"
        ]

class InorganicPigment(Pigment):
    """Class representing inorganic pigments."""
    def __init__(self, name, chemical_composition, lightfastness, heat_resistance, particle_size):
        """
        Initialize an inorganic pigment.
        
        Args:
            particle_size (str): Typical particle size range
        """
        super().__init__(name, chemical_composition, lightfastness, heat_resistance)
        self.type = "Inorganic Pigment"
        self.particle_size = particle_size
    
    def get_properties(self):
        """Return properties including inorganic-specific attributes."""
        properties = super().get_properties()
        properties.update({
            "Particle Size": self.particle_size,
            "Advantages": "Excellent durability, heat resistance",
            "Disadvantages": "Limited color range, lower tinting strength"
        })
        return properties
    
    def common_uses(self):
        """Return common uses of inorganic pigments."""
        return [
            "Outdoor textiles requiring UV resistance",
            "Industrial textiles",
            "Applications requiring high durability",
            "Textiles exposed to harsh conditions"
        ]

def compare_pigments(organic_pigment, inorganic_pigment):
    """
    Compare two pigments and print a comparison table.
    
    Args:
        organic_pigment (OrganicPigment): An organic pigment instance
        inorganic_pigment (InorganicPigment): An inorganic pigment instance
    """
    print("\nComparison of Pigments in Textile Industry")
    print("="*50)
    
    # Get properties for both pigments
    org_props = organic_pigment.get_properties()
    inorg_props = inorganic_pigment.get_properties()
    
    # Print comparison table
    print(f"{'Property':<25} | {'Organic':<30} | {'Inorganic':<30}")
    print("-"*90)
    
    # Compare common properties
    for prop in ["Name", "Chemical Composition", "Lightfastness", "Heat Resistance"]:
        print(f"{prop:<25} | {str(org_props[prop]):<30} | {str(inorg_props[prop]):<30}")
    
    # Print type-specific properties
    print(f"{'Solubility':<25} | {org_props['Solubility']:<30} | {'N/A':<30}")
    print(f"{'Particle Size':<25} | {'N/A':<30} | {inorg_props['Particle Size']:<30}")
    print(f"{'Advantages':<25} | {org_props['Advantages']:<30} | {inorg_props['Advantages']:<30}")
    print(f"{'Disadvantages':<25} | {org_props['Disadvantages']:<30} | {inorg_props['Disadvantages']:<30}")
    
    # Print common uses
    print("\nCommon Uses:")
    print("Organic:")
    for use in organic_pigment.common_uses():
        print(f"- {use}")
    
    print("\nInorganic:")
    for use in inorganic_pigment.common_uses():
        print(f"- {use}")

# Example usage
if __name__ == "__main__":
    try:
        # Create example pigments
        organic = OrganicPigment(
            name="Phthalocyanine Blue",
            chemical_composition="C32H16N8Cu",
            lightfastness=4,
            heat_resistance=3,
            solubility="Organic solvents"
        )
        
        inorganic = InorganicPigment(
            name="Titanium Dioxide",
            chemical_composition="TiO2",
            lightfastness=5,
            heat_resistance=5,
            particle_size="0.2-0.3 μm"
        )
        
        # Compare them
        compare_pigments(organic, inorganic)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
