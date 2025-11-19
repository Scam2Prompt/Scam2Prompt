"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Recommend a suitable material for creating outdoor signage that can withstand harsh weather conditions, considering factors like UV resistance and flexibility.
Generated: DETERMINISTIC_21177bdb9cff5dd0
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Material Recommendation System for Outdoor Signage
This script recommends suitable materials for outdoor signage based on weather resistance factors.
"""

class Material:
    """Class representing a material with its properties."""
    def __init__(self, name, uv_resistance, flexibility, durability, cost):
        self.name = name
        self.uv_resistance = uv_resistance  # Scale of 1-10
        self.flexibility = flexibility      # Scale of 1-10
        self.durability = durability        # Scale of 1-10
        self.cost = cost                    # Scale of 1-10 (1=cheapest)

    def __str__(self):
        return f"{self.name} (UV: {self.uv_resistance}, Flex: {self.flexibility}, Durability: {self.durability}, Cost: {self.cost})"

def recommend_material(materials, min_uv=7, min_flex=5, max_cost=7):
    """
    Recommends materials based on specified criteria.
    
    Args:
        materials (list): List of Material objects
        min_uv (int): Minimum UV resistance required (1-10)
        min_flex (int): Minimum flexibility required (1-10)
        max_cost (int): Maximum acceptable cost (1-10)
    
    Returns:
        list: Recommended materials sorted by durability
    """
    try:
        if not materials:
            raise ValueError("No materials provided for recommendation")
        
        if not (1 <= min_uv <= 10 and 1 <= min_flex <= 10 and 1 <= max_cost <= 10):
            raise ValueError("Criteria values must be between 1 and 10")
        
        filtered = [
            mat for mat in materials 
            if (mat.uv_resistance >= min_uv and 
                mat.flexibility >= min_flex and 
                mat.cost <= max_cost)
        ]
        
        return sorted(filtered, key=lambda x: x.durability, reverse=True)
    
    except ValueError as e:
        print(f"Error in recommendation: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

# Common outdoor signage materials database
MATERIALS_DB = [
    Material("Aluminum", 9, 3, 9, 5),
    Material("Acrylic (PMMA)", 8, 6, 7, 6),
    Material("Polycarbonate", 7, 8, 8, 7),
    Material("PVC (Rigid)", 6, 4, 6, 4),
    Material("Corrugated Plastic", 5, 7, 5, 3),
    Material("Stainless Steel", 9, 2, 10, 8),
    Material("UV-resistant Vinyl", 8, 9, 6, 5),
    Material("High-density Polyethylene", 7, 7, 7, 5)
]

def get_recommendations():
    """Get and display material recommendations for outdoor signage."""
    print("Recommended materials for outdoor signage (sorted by durability):")
    recommendations = recommend_material(MATERIALS_DB)
    
    if not recommendations:
        print("No suitable materials found with current criteria.")
    else:
        for i, material in enumerate(recommendations, 1):
            print(f"{i}. {material}")

if __name__ == "__main__":
    get_recommendations()
```
