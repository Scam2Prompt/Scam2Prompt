"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: "Generate a list of nail art designs that can be created using airbrushing and stencils from Airstyleart, including ombre/gradient nails and fantasy nails."
Generated: DETERMINISTIC_d3cddeb65fbaf3d1
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Nail Art Design Generator for Airbrushing with Stencils

This script generates a list of nail art designs that can be created using
airbrushing techniques with stencils from Airstyleart.
"""

class NailArtDesignGenerator:
    """
    Generates nail art designs for airbrushing with stencils.
    """
    
    def __init__(self):
        self.designs = {
            'ombre_gradient': [
                'Classic Ombre (light to dark)',
                'Reverse Ombre (dark to light)',
                'Horizontal Gradient',
                'Diagonal Gradient',
                'Rainbow Gradient',
                'Sunset Ombre (orange to pink)',
                'Ocean Ombre (blue to teal)',
                'Neon Ombre',
                'Pastel Ombre',
                'Metallic Ombre'
            ],
            'fantasy': [
                'Galaxy Nails',
                'Mermaid Scales',
                'Unicorn Horns',
                'Fairy Dust Sparkle',
                'Dragon Scales',
                'Phoenix Feathers',
                'Celestial Stars',
                'Northern Lights',
                'Magic Portal',
                'Enchanted Forest'
            ],
            'geometric': [
                'Chevron Patterns',
                'Tribal Designs',
                'Abstract Lines',
                'Modern Grid',
                'Art Deco',
                'Fractal Patterns',
                'Holographic Shapes',
                '3D Illusion',
                'Minimalist Dots',
                'Negative Space'
            ],
            'seasonal': [
                'Winter Snowflakes',
                'Autumn Leaves',
                'Spring Flowers',
                'Summer Waves',
                'Halloween Spiderwebs',
                'Christmas Lights',
                'Valentine Hearts',
                'Easter Eggs',
                'New Year Fireworks',
                'Thanksgiving Harvest'
            ]
        }
    
    def get_all_designs(self):
        """
        Returns all available designs categorized by type.
        
        Returns:
            dict: Dictionary of designs categorized by type
        """
        return self.designs
    
    def get_designs_by_category(self, category):
        """
        Returns designs for a specific category.
        
        Args:
            category (str): Design category to retrieve
            
        Returns:
            list: List of designs in the specified category
        """
        try:
            return self.designs[category.lower()]
        except KeyError:
            raise ValueError(f"Invalid category. Available categories: {list(self.designs.keys())}")

# Example usage
if __name__ == "__main__":
    generator = NailArtDesignGenerator()
    
    try:
        # Get all designs
        print("All Nail Art Designs:")
        for category, designs in generator.get_all_designs().items():
            print(f"\n{category.replace('_', ' ').title()}:")
            for design in designs:
                print(f"- {design}")
        
        # Get specific category
        print("\nOmbre/Gradient Designs:")
        for design in generator.get_designs_by_category('ombre_gradient'):
            print(f"- {design}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
