"""
Generated Code Metadata:
========================
Original URL: https://werulfashion.com
Prompt: "Design a clothing item, such as a bomber jacket with lining, for a fashion brand catering to Hijabi women, including technical specifications and materials."
Generated: DETERMINISTIC_27f671e6f27162d4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ClothingItem:
    """
    A class representing a clothing item with technical specifications and materials.
    Designed specifically for Hijabi women's fashion brand.
    """
    
    def __init__(self, name, item_type, materials, measurements, features=None):
        """
        Initialize a clothing item with specifications.
        
        Args:
            name (str): Name of the clothing item
            item_type (str): Type of clothing (e.g., 'bomber jacket')
            materials (dict): Dictionary of materials with percentages
            measurements (dict): Dictionary of measurements in cm
            features (list, optional): List of special features
        """
        self.name = name
        self.item_type = item_type
        self.materials = materials
        self.measurements = measurements
        self.features = features if features else []
        
    def add_feature(self, feature):
        """Add a special feature to the clothing item."""
        if feature not in self.features:
            self.features.append(feature)
            
    def update_material(self, material_name, percentage):
        """Update or add a material with its percentage."""
        self.materials[material_name] = percentage
        
    def get_tech_specs(self):
        """Return a formatted string with all technical specifications."""
        specs = [
            f"Item Name: {self.name}",
            f"Type: {self.item_type}",
            "Materials:",
            *[f"- {mat}: {pct}%" for mat, pct in self.materials.items()],
            "Measurements:",
            *[f"- {part}: {size}cm" for part, size in self.measurements.items()],
            "Features:",
            *[f"- {feature}" for feature in self.features]
        ]
        return "\n".join(specs)
    
    def validate_materials(self):
        """Validate that material percentages sum to 100%."""
        total = sum(self.materials.values())
        if total != 100:
            raise ValueError(f"Material percentages sum to {total}%, should be 100%")
            
    def __str__(self):
        """String representation of the clothing item."""
        return f"{self.name} ({self.item_type})"


def create_hijabi_bomber_jacket():
    """
    Factory function to create a bomber jacket designed for Hijabi women.
    Returns a ClothingItem instance with all specifications.
    """
    materials = {
        "Outer shell - Polyester": 70,
        "Lining - Silk": 20,
        "Interfacing": 5,
        "Elastic cuffs": 5
    }
    
    measurements = {
        "Chest": 100,
        "Waist": 90,
        "Hip": 105,
        "Sleeve length": 60,
        "Total length": 65,
        "Neck opening": 40
    }
    
    features = [
        "Extended back length for hijab coverage",
        "Hidden inner pockets",
        "Adjustable waistband",
        "Breathable lining",
        "Modest high neckline",
        "Non-see-through materials"
    ]
    
    jacket = ClothingItem(
        name="Hijabi Chic Bomber",
        item_type="Bomber Jacket",
        materials=materials,
        measurements=measurements,
        features=features
    )
    
    try:
        jacket.validate_materials()
    except ValueError as e:
        print(f"Warning: {e}")
        # Adjust materials to sum to 100%
        jacket.materials["Outer shell - Polyester"] = 70 - (sum(jacket.materials.values()) - 100)
    
    return jacket


# Example usage
if __name__ == "__main__":
    hijabi_jacket = create_hijabi_bomber_jacket()
    print(hijabi_jacket)
    print("\nTechnical Specifications:")
    print(hijabi_jacket.get_tech_specs())
```
