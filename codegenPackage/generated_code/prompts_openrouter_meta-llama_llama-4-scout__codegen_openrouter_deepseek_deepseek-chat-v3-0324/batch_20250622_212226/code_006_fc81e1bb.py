"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: "Suggest a set of topes para puertas that DEVA could offer, based on common sizes and materials used in construction."
Generated: DETERMINISTIC_fc81e1bbcd9a80ae
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class DoorTopesGenerator:
    """
    A class to generate common door tope (door stop) options that DEVA could offer.
    """
    
    # Common materials for door topes
    MATERIALS = [
        "rubber",
        "plastic",
        "metal",
        "wood",
        "silicone"
    ]
    
    # Common sizes in mm (height, width, depth)
    SIZES = [
        (50, 30, 20),
        (60, 40, 25),
        (70, 50, 30),
        (80, 60, 35),
        (100, 80, 40)
    ]
    
    # Common colors
    COLORS = [
        "black",
        "white",
        "brown",
        "gray",
        "transparent"
    ]
    
    # Common mounting types
    MOUNTING_TYPES = [
        "wall-mounted",
        "floor-mounted",
        "door-mounted",
        "hinge-mounted"
    ]
    
    @classmethod
    def generate_topes(cls) -> List[Dict[str, any]]:
        """
        Generate a list of door tope options with various combinations of materials, sizes, colors, and mounting types.
        
        Returns:
            List[Dict[str, any]]: A list of dictionaries, each representing a door tope option
        """
        tope_options = []
        
        for material in cls.MATERIALS:
            for size in cls.SIZES:
                for color in cls.COLORS:
                    for mount_type in cls.MOUNTING_TYPES:
                        tope_options.append({
                            "material": material,
                            "size": {
                                "height_mm": size[0],
                                "width_mm": size[1],
                                "depth_mm": size[2]
                            },
                            "color": color,
                            "mounting_type": mount_type,
                            "sku": f"DT-{material[:3].upper()}-{size[0]}-{color[:3].upper()}-{mount_type[:3].upper()}"
                        })
        
        return tope_options

    @classmethod
    def get_filtered_topes(cls, 
                          material_filter: str = None, 
                          min_size: tuple = None, 
                          color_filter: str = None,
                          mounting_filter: str = None) -> List[Dict[str, any]]:
        """
        Get filtered door tope options based on specified criteria.
        
        Args:
            material_filter: Filter by material type
            min_size: Minimum size as tuple (height, width, depth)
            color_filter: Filter by color
            mounting_filter: Filter by mounting type
            
        Returns:
            List[Dict[str, any]]: Filtered list of door tope options
        """
        all_topes = cls.generate_topes()
        filtered = all_topes
        
        if material_filter:
            filtered = [t for t in filtered if t["material"].lower() == material_filter.lower()]
        
        if min_size:
            filtered = [t for t in filtered if (t["size"]["height_mm"] >= min_size[0] and
                                              t["size"]["width_mm"] >= min_size[1] and
                                              t["size"]["depth_mm"] >= min_size[2])]
        
        if color_filter:
            filtered = [t for t in filtered if t["color"].lower() == color_filter.lower()]
        
        if mounting_filter:
            filtered = [t for t in filtered if t["mounting_type"].lower() == mounting_filter.lower()]
        
        return filtered

# Example usage
if __name__ == "__main__":
    # Get all possible tope options
    all_topes = DoorTopesGenerator.generate_topes()
    print(f"Total tope options generated: {len(all_topes)}")
    
    # Get filtered options
    rubber_topes = DoorTopesGenerator.get_filtered_topes(material_filter="rubber")
    large_topes = DoorTopesGenerator.get_filtered_topes(min_size=(80, 60, 35))
    white_wall_topes = DoorTopesGenerator.get_filtered_topes(color_filter="white", mounting_filter="wall-mounted")
    
    print(f"Rubber topes: {len(rubber_topes)} options")
    print(f"Large topes: {len(large_topes)} options")
    print(f"White wall-mounted topes: {len(white_wall_topes)} options")
```
