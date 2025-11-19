"""
Generated Code Metadata:
========================
Original URL: https://www.insectshieldzoro.com
Prompt: "Compare the features of different mosquito net materials, such as Stainless Steel 304 Mesh Rolls and Fiber Glass Mesh Rolls, used by Insect Shield ZORO."
Generated: DETERMINISTIC_3544544201a5da09
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MosquitoNetMaterial:
    """
    Represents a mosquito net material with its properties.
    """
    
    def __init__(self, name, material_type, mesh_size, durability, uv_resistance, 
                 corrosion_resistance, weight, price_per_sqft):
        """
        Initialize a mosquito net material with its properties.
        
        Args:
            name (str): Name of the material
            material_type (str): Type of material (e.g., stainless steel, fiber glass)
            mesh_size (str): Mesh size specification
            durability (str): Durability rating
            uv_resistance (str): UV resistance rating
            corrosion_resistance (str): Corrosion resistance rating
            weight (str): Weight per unit area
            price_per_sqft (float): Price per square foot
        """
        self.name = name
        self.material_type = material_type
        self.mesh_size = mesh_size
        self.durability = durability
        self.uv_resistance = uv_resistance
        self.corrosion_resistance = corrosion_resistance
        self.weight = weight
        self.price_per_sqft = price_per_sqft
    
    def __str__(self):
        """Return a string representation of the material."""
        return (f"{self.name} ({self.material_type}):\n"
                f"  Mesh Size: {self.mesh_size}\n"
                f"  Durability: {self.durability}\n"
                f"  UV Resistance: {self.uv_resistance}\n"
                f"  Corrosion Resistance: {self.corrosion_resistance}\n"
                f"  Weight: {self.weight}\n"
                f"  Price/sqft: ${self.price_per_sqft:.2f}")


class MaterialComparator:
    """
    Compares different mosquito net materials.
    """
    
    def __init__(self):
        """Initialize with default materials."""
        self.materials = []
    
    def add_material(self, material):
        """Add a material to compare."""
        if not isinstance(material, MosquitoNetMaterial):
            raise ValueError("Only MosquitoNetMaterial objects can be added")
        self.materials.append(material)
    
    def compare_materials(self):
        """Compare all added materials and return comparison results."""
        if not self.materials:
            raise ValueError("No materials to compare")
        
        comparison = []
        for material in self.materials:
            comparison.append({
                'Name': material.name,
                'Material Type': material.material_type,
                'Mesh Size': material.mesh_size,
                'Durability': material.durability,
                'UV Resistance': material.uv_resistance,
                'Corrosion Resistance': material.corrosion_resistance,
                'Weight': material.weight,
                'Price/sqft': f"${material.price_per_sqft:.2f}"
            })
        
        return comparison
    
    def get_comparison_table(self):
        """Return a formatted comparison table."""
        comparison = self.compare_materials()
        if not comparison:
            return "No materials to compare"
        
        # Get all field names
        fields = list(comparison[0].keys())
        
        # Calculate column widths
        col_widths = {field: len(field) for field in fields}
        for material in comparison:
            for field in fields:
                col_widths[field] = max(col_widths[field], len(str(material[field])))
        
        # Build header
        header = "|".join([f" {field.ljust(col_widths[field])} " for field in fields])
        separator = "+".join(["-" * (col_widths[field] + 2) for field in fields])
        
        # Build rows
        rows = []
        for material in comparison:
            row = "|".join([f" {str(material[field]).ljust(col_widths[field])} " 
                           for field in fields])
            rows.append(row)
        
        # Combine all parts
        return "\n".join([separator, header, separator] + rows + [separator])


# Example usage
if __name__ == "__main__":
    # Create material instances
    stainless_steel = MosquitoNetMaterial(
        name="Stainless Steel 304 Mesh Roll",
        material_type="Stainless Steel",
        mesh_size="20 x 20 mesh",
        durability="High",
        uv_resistance="Excellent",
        corrosion_resistance="Excellent",
        weight="0.5 lbs/sqft",
        price_per_sqft=2.50
    )
    
    fiber_glass = MosquitoNetMaterial(
        name="Fiber Glass Mesh Roll",
        material_type="Fiber Glass",
        mesh_size="18 x 16 mesh",
        durability="Medium",
        uv_resistance="Good",
        corrosion_resistance="Excellent",
        weight="0.3 lbs/sqft",
        price_per_sqft=1.75
    )
    
    # Compare materials
    comparator = MaterialComparator()
    comparator.add_material(stainless_steel)
    comparator.add_material(fiber_glass)
    
    # Print comparison table
    print("Mosquito Net Material Comparison:")
    print(comparator.get_comparison_table())
```
