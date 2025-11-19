"""
Generated Code Metadata:
========================
Original URL: https://pinkpolkadotcreations.com
Prompt: "Create a sewing tutorial for making easy zippered pouches using a serger, similar to the project mentioned in the sewing class for Relief Society."
Generated: DETERMINISTIC_21a1884a7acf7098
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sewing Tutorial Generator for Zippered Pouches using a Serger

This script generates a step-by-step sewing tutorial for making easy zippered pouches
using a serger machine, similar to projects taught in sewing classes.

Features:
- Materials list
- Step-by-step instructions
- Measurement calculations
- Error checking for fabric dimensions
"""

class ZipperedPouchTutorial:
    """Generates a tutorial for making zippered pouches with a serger."""
    
    def __init__(self, width=6, height=4, unit='inches'):
        """
        Initialize tutorial with pouch dimensions.
        
        Args:
            width (float): Desired width of pouch in specified unit
            height (float): Desired height of pouch in specified unit
            unit (str): Measurement unit ('inches' or 'cm')
        """
        self.width = width
        self.height = height
        self.unit = unit.lower()
        self.validate_measurements()
        
    def validate_measurements(self):
        """Ensure measurements are valid and positive."""
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive numbers")
        if self.unit not in ['inches', 'cm']:
            raise ValueError("Unit must be 'inches' or 'cm'")
    
    def calculate_fabric_dimensions(self):
        """
        Calculate required fabric pieces based on pouch dimensions.
        
        Returns:
            dict: Fabric dimensions for exterior, lining, and interfacing
        """
        seam_allowance = 0.5 if self.unit == 'inches' else 1.27
        width_with_allowance = self.width + (2 * seam_allowance)
        height_with_allowance = (self.height * 2) + (2 * seam_allowance)
        
        return {
            'exterior': {
                'width': width_with_allowance,
                'height': height_with_allowance,
                'pieces': 2
            },
            'lining': {
                'width': width_with_allowance,
                'height': height_with_allowance,
                'pieces': 2
            },
            'interfacing': {
                'width': self.width,
                'height': self.height,
                'pieces': 2
            }
        }
    
    def generate_materials_list(self):
        """Generate list of required materials."""
        fabric_dims = self.calculate_fabric_dimensions()
        
        materials = [
            f"Exterior fabric: 2 pieces {fabric_dims['exterior']['width']}x{fabric_dims['exterior']['height']} {self.unit}",
            f"Lining fabric: 2 pieces {fabric_dims['lining']['width']}x{fabric_dims['lining']['height']} {self.unit}",
            f"Interfacing: 2 pieces {fabric_dims['interfacing']['width']}x{fabric_dims['interfacing']['height']} {self.unit}",
            f"Zipper: 1 piece {self.width} {self.unit} long",
            "Matching thread",
            "Serger thread (4 cones)",
            "Fabric scissors",
            "Pins or clips",
            "Iron and ironing board",
            "Serger machine",
            "Zipper foot for serger (optional)"
        ]
        
        return materials
    
    def generate_instructions(self):
        """Generate step-by-step sewing instructions."""
        instructions = [
            "1. Prepare all fabric pieces by cutting to required dimensions.",
            "2. Apply interfacing to the wrong side of both exterior fabric pieces.",
            "3. Serge all raw edges of exterior and lining pieces to prevent fraying.",
            "4. Place exterior pieces right sides together. Serge along both sides, leaving top open.",
            "5. Repeat with lining pieces, but leave a 3-4 inch opening at the bottom for turning.",
            "6. Box the corners by measuring 1 inch from corner, marking, and serging across.",
            "7. Attach zipper: Place zipper face down on right side of exterior fabric top edge.",
            "8. Serge zipper to fabric using zipper foot or standard foot with careful alignment.",
            "9. Repeat for other side, ensuring zipper is centered and fabric is aligned.",
            "10. Turn pouch right side out through the lining opening.",
            "11. Hand stitch or serge the lining opening closed.",
            "12. Press pouch with iron for a professional finish."
        ]
        
        return instructions
    
    def generate_tutorial(self):
        """Generate complete tutorial with materials and instructions."""
        try:
            tutorial = {
                'title': f"Easy Zippered Pouch Tutorial ({self.width}x{self.height} {self.unit})",
                'materials': self.generate_materials_list(),
                'instructions': self.generate_instructions(),
                'notes': [
                    "Use contrasting thread colors for decorative serging if desired.",
                    "Practice serging on scrap fabric before starting the project.",
                    "Go slowly when serging over the zipper teeth."
                ]
            }
            return tutorial
        except Exception as e:
            return f"Error generating tutorial: {str(e)}"

# Example usage
if __name__ == "__main__":
    try:
        tutorial = ZipperedPouchTutorial(width=6, height=4, unit='inches')
        result = tutorial.generate_tutorial()
        
        # Print tutorial
        print(f"\n{result['title']}\n")
        print("Materials Needed:")
        for item in result['materials']:
            print(f"- {item}")
        
        print("\nInstructions:")
        for step in result['instructions']:
            print(step)
        
        print("\nNotes:")
        for note in result['notes']:
            print(f"- {note}")
            
    except ValueError as e:
        print(f"Error: {str(e)}")
```
