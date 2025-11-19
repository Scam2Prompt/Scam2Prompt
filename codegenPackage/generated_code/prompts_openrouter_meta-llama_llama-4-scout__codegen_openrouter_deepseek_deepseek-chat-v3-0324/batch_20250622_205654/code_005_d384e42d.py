"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: "Design a custom, handmade Barbie dollhouse quilt using upcycled materials, with a focus on sustainability and eco-friendliness, and provide a list of materials and instructions for its creation."
Generated: DETERMINISTIC_d384e42d0f4ea6f0
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Barbie Dollhouse Quilt Designer - Sustainable Edition

This script generates a custom quilt design for a Barbie dollhouse using upcycled materials.
It provides a materials list and step-by-step instructions for creating an eco-friendly quilt.
"""

import random
from typing import List, Dict, Tuple

class SustainableQuiltDesigner:
    def __init__(self):
        self.common_upcycled_materials = [
            "old cotton t-shirts",
            "denim jeans",
            "linen curtains",
            "wool sweaters",
            "flannel shirts",
            "silk scarves",
            "bamboo fabric scraps",
            "organic cotton remnants"
        ]
        
        self.eco_friendly_fillings = [
            "organic cotton batting",
            "bamboo fiber filling",
            "recycled polyester filling",
            "wool scraps",
            "upcycled fabric scraps"
        ]
        
        self.sustainable_threads = [
            "organic cotton thread",
            "bamboo thread",
            "recycled polyester thread"
        ]
        
        self.barbie_dollhouse_dimensions = {
            "standard": (18, 24),  # inches (width, height)
            "large": (24, 36)
        }
        
        self.quilt_patterns = [
            "patchwork squares",
            "log cabin",
            "flying geese",
            "nine-patch",
            "starburst"
        ]

    def generate_materials_list(self, size: str = "standard") -> Dict[str, List[str]]:
        """Generate a sustainable materials list for the quilt"""
        if size not in self.barbie_dollhouse_dimensions:
            raise ValueError("Invalid size. Choose 'standard' or 'large'.")
            
        num_fabrics = random.randint(3, 6)
        selected_fabrics = random.sample(self.common_upcycled_materials, num_fabrics)
        
        return {
            "fabric": selected_fabrics,
            "filling": [random.choice(self.eco_friendly_fillings)],
            "thread": [random.choice(self.sustainable_threads)],
            "other": ["scissors", "pins", "measuring tape", "sewing needle"],
            "dimensions": self.barbie_dollhouse_dimensions[size]
        }

    def generate_instructions(self, materials: Dict[str, List[str]]) -> List[str]:
        """Generate step-by-step instructions for creating the quilt"""
        pattern = random.choice(self.quilt_patterns)
        width, height = materials["dimensions"]
        
        instructions = [
            f"1. Wash and iron all upcycled fabrics to prepare them for sewing.",
            f"2. Cut fabrics into pieces suitable for the {pattern} pattern. For a {width}x{height} inch quilt:",
            "   - For squares: cut 2-4 inch squares (varied sizes add charm)",
            "   - For strips: cut 1.5-3 inch wide strips of varying lengths",
            "3. Arrange your cut pieces in the desired {pattern} design on a flat surface.",
            "4. Sew pieces together to form the quilt top, pressing seams as you go.",
            "5. Cut your {filling} to match the quilt top dimensions.".format(filling=materials["filling"][0]),
            "6. Layer the quilt:",
            "   - Place backing fabric right side down",
            "   - Add filling layer",
            "   - Place quilt top right side up",
            "7. Pin or baste layers together to prevent shifting.",
            f"8. Quilt as desired using {materials['thread'][0]}:",
            "   - Stitch in the ditch between blocks",
            "   - Or create free-motion designs",
            "9. Trim edges to even up the quilt.",
            "10. Create binding from leftover fabric strips and attach to finish edges.",
            "11. Give your sustainable Barbie dollhouse quilt a final press and enjoy!"
        ]
        
        return instructions

    def design_quilt(self, size: str = "standard") -> Tuple[Dict[str, List[str]], List[str]]:
        """Generate a complete quilt design with materials and instructions"""
        try:
            materials = self.generate_materials_list(size)
            instructions = self.generate_instructions(materials)
            return materials, instructions
        except Exception as e:
            print(f"Error generating quilt design: {e}")
            raise

def main():
    """Main function to demonstrate quilt design generation"""
    try:
        designer = SustainableQuiltDesigner()
        materials, instructions = designer.design_quilt()
        
        print("\n=== Sustainable Barbie Dollhouse Quilt ===")
        print("\nMaterials Needed:")
        for category, items in materials.items():
            if category != "dimensions":
                print(f"  {category.capitalize()}:")
                for item in items:
                    print(f"    - {item}")
        
        print("\nInstructions:")
        for step in instructions:
            print(step)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
