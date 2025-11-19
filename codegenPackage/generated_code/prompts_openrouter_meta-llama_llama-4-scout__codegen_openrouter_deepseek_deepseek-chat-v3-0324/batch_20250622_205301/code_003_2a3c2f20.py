"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "What are the advantages of using Hastelloy C22 Fittings over Alloy 20 Pipes in a corrosive environment?"
Generated: DETERMINISTIC_2a3c2f20c0f29f40
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a comparison between Hastelloy C22 fittings and Alloy 20 pipes
in corrosive environments by analyzing their material properties and corrosion resistance.
"""

class MaterialProperties:
    """Class to store and compare material properties"""
    
    def __init__(self, name: str, corrosion_resistance: dict, temperature_range: tuple,
                 mechanical_properties: dict, cost_factor: float):
        """
        Initialize material properties
        
        Args:
            name: Name of the material
            corrosion_resistance: Dictionary of corrosion resistance against various chemicals
            temperature_range: Operating temperature range in Celsius (min, max)
            mechanical_properties: Dictionary of mechanical properties
            cost_factor: Relative cost factor compared to standard materials
        """
        self.name = name
        self.corrosion_resistance = corrosion_resistance
        self.temperature_range = temperature_range
        self.mechanical_properties = mechanical_properties
        self.cost_factor = cost_factor
    
    def compare_corrosion_resistance(self, other, chemical: str) -> str:
        """
        Compare corrosion resistance between two materials for a specific chemical
        
        Args:
            other: Another MaterialProperties instance to compare against
            chemical: Chemical to compare resistance against
            
        Returns:
            Comparison result string
        """
        try:
            self_res = self.corrosion_resistance[chemical]
            other_res = other.corrosion_resistance[chemical]
            
            if self_res > other_res:
                return f"{self.name} has better resistance to {chemical}"
            elif self_res < other_res:
                return f"{other.name} has better resistance to {chemical}"
            else:
                return f"Both materials have similar resistance to {chemical}"
        except KeyError as e:
            raise ValueError(f"Chemical {chemical} not found in material properties") from e

def create_hastelloy_c22() -> MaterialProperties:
    """Create Hastelloy C22 material properties"""
    corrosion_resistance = {
        'HCl': 9.5,  # Scale of 1-10
        'H2SO4': 9.0,
        'NaCl': 9.8,
        'FeCl3': 9.7,
        'Oxidizing_media': 9.5
    }
    temperature_range = (-200, 1093)  # Celsius
    mechanical_properties = {
        'tensile_strength': 690,  # MPa
        'yield_strength': 310,    # MPa
        'elongation': 45          # %
    }
    return MaterialProperties(
        "Hastelloy C22",
        corrosion_resistance,
        temperature_range,
        mechanical_properties,
        2.5  # Cost factor
    )

def create_alloy_20() -> MaterialProperties:
    """Create Alloy 20 material properties"""
    corrosion_resistance = {
        'HCl': 7.0,  # Scale of 1-10
        'H2SO4': 8.5,
        'NaCl': 8.0,
        'FeCl3': 7.5,
        'Oxidizing_media': 7.0
    }
    temperature_range = (-100, 450)  # Celsius
    mechanical_properties = {
        'tensile_strength': 620,  # MPa
        'yield_strength': 300,    # MPa
        'elongation': 30          # %
    }
    return MaterialProperties(
        "Alloy 20",
        corrosion_resistance,
        temperature_range,
        mechanical_properties,
        1.8  # Cost factor
    )

def generate_comparison_report(material1: MaterialProperties, material2: MaterialProperties) -> dict:
    """
    Generate a comprehensive comparison report between two materials
    
    Args:
        material1: First material to compare
        material2: Second material to compare
        
    Returns:
        Dictionary containing comparison results
    """
    report = {
        'materials': [material1.name, material2.name],
        'corrosion_resistance': {},
        'temperature_range': {
            material1.name: material1.temperature_range,
            material2.name: material2.temperature_range
        },
        'mechanical_properties': {
            material1.name: material1.mechanical_properties,
            material2.name: material2.mechanical_properties
        },
        'cost_comparison': f"{material1.name} is {material1.cost_factor/material2.cost_factor:.1f}x more expensive than {material2.name}"
    }
    
    # Compare corrosion resistance for all chemicals
    chemicals = set(material1.corrosion_resistance.keys()).union(set(material2.corrosion_resistance.keys()))
    for chem in chemicals:
        try:
            report['corrosion_resistance'][chem] = material1.compare_corrosion_resistance(material2, chem)
        except ValueError as e:
            report['corrosion_resistance'][chem] = str(e)
    
    return report

if __name__ == "__main__":
    try:
        # Create material instances
        hastelloy = create_hastelloy_c22()
        alloy20 = create_alloy_20()
        
        # Generate comparison report
        report = generate_comparison_report(hastelloy, alloy20)
        
        # Print summary
        print(f"Comparison between {hastelloy.name} and {alloy20.name}:")
        print("\nCorrosion Resistance:")
        for chem, result in report['corrosion_resistance'].items():
            print(f"- {chem}: {result}")
        
        print("\nTemperature Range:")
        for mat, temp_range in report['temperature_range'].items():
            print(f"- {mat}: {temp_range[0]}°C to {temp_range[1]}°C")
        
        print("\nMechanical Properties:")
        for mat, props in report['mechanical_properties'].items():
            print(f"- {mat}:")
            for prop, value in props.items():
                print(f"  - {prop}: {value}")
        
        print(f"\nCost: {report['cost_comparison']}")
        
    except Exception as e:
        print(f"Error generating comparison: {str(e)}")
```
