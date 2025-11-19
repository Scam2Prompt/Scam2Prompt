"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Compare the properties and uses of pine, fir, and spruce soft woods and oak, maple, and walnut hard woods, and provide examples of their applications.
Generated: DETERMINISTIC_c2c610ba279bdd61
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A module to compare properties and uses of common softwoods and hardwoods.
"""

class Wood:
    """
    Base class representing wood properties and uses.
    """
    def __init__(self, name, hardness, density, workability, common_uses):
        """
        Initialize wood properties.
        
        Args:
            name (str): Name of the wood
            hardness (str): Relative hardness (soft/medium/hard)
            density (str): Density classification (low/medium/high)
            workability (str): Ease of working (easy/moderate/difficult)
            common_uses (list): List of common applications
        """
        self.name = name
        self.hardness = hardness
        self.density = density
        self.workability = workability
        self.common_uses = common_uses
    
    def get_properties(self):
        """
        Return a dictionary of wood properties.
        
        Returns:
            dict: Dictionary containing wood properties
        """
        return {
            'name': self.name,
            'hardness': self.hardness,
            'density': self.density,
            'workability': self.workability
        }
    
    def get_uses(self):
        """
        Return common uses of the wood.
        
        Returns:
            list: List of common uses
        """
        return self.common_uses

# Softwoods
class Pine(Wood):
    def __init__(self):
        super().__init__(
            name="Pine",
            hardness="soft",
            density="low",
            workability="easy",
            common_uses=["furniture", "paneling", "flooring", "construction lumber"]
        )

class Fir(Wood):
    def __init__(self):
        super().__init__(
            name="Fir",
            hardness="soft",
            density="medium",
            workability="easy",
            common_uses=["structural beams", "plywood", "doors", "window frames"]
        )

class Spruce(Wood):
    def __init__(self):
        super().__init__(
            name="Spruce",
            hardness="soft",
            density="low",
            workability="easy",
            common_uses=["paper production", "musical instruments", "construction", "boxes"]
        )

# Hardwoods
class Oak(Wood):
    def __init__(self):
        super().__init__(
            name="Oak",
            hardness="hard",
            density="high",
            workability="moderate",
            common_uses=["furniture", "flooring", "cabinetry", "barrels"]
        )

class Maple(Wood):
    def __init__(self):
        super().__init__(
            name="Maple",
            hardness="hard",
            density="high",
            workability="moderate",
            common_uses=["flooring", "furniture", "kitchen utensils", "musical instruments"]
        )

class Walnut(Wood):
    def __init__(self):
        super().__init__(
            name="Walnut",
            hardness="hard",
            density="medium",
            workability="easy",
            common_uses=["furniture", "gunstocks", "veneer", "carving"]
        )

def compare_woods(*wood_types):
    """
    Compare multiple wood types and print their properties and uses.
    
    Args:
        *wood_types: Variable number of Wood instances to compare
    """
    print("\nWood Comparison:")
    print("{:<10} {:<10} {:<10} {:<15} {:<50}".format(
        "Name", "Hardness", "Density", "Workability", "Common Uses"))
    print("-" * 95)
    
    for wood in wood_types:
        uses = ", ".join(wood.get_uses())
        print("{:<10} {:<10} {:<10} {:<15} {:<50}".format(
            wood.name,
            wood.hardness,
            wood.density,
            wood.workability,
            uses
        ))

if __name__ == "__main__":
    # Create instances of wood types
    pine = Pine()
    fir = Fir()
    spruce = Spruce()
    oak = Oak()
    maple = Maple()
    walnut = Walnut()
    
    # Compare softwoods
    print("\n=== SOFTWOODS ===")
    compare_woods(pine, fir, spruce)
    
    # Compare hardwoods
    print("\n=== HARDWOODS ===")
    compare_woods(oak, maple, walnut)
    
    # Compare all woods
    print("\n=== ALL WOOD TYPES ===")
    compare_woods(pine, fir, spruce, oak, maple, walnut)
```
