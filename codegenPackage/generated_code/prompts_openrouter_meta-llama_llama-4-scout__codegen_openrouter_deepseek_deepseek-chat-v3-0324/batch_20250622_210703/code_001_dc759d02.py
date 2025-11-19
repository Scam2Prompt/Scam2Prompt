"""
Generated Code Metadata:
========================
Original URL: https://paintersmorningtonpeninsula.com.au
Prompt: Write a Python script to generate a color palette for a residential painting project in Mornington Peninsula, considering factors like natural lighting, existing decor, and personal preferences, as discussed on the Painters Mornington Peninsula website.
Generated: DETERMINISTIC_dc759d02205fe8fc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import colorsys
import random
import json
from typing import List, Dict, Tuple

class ColorPaletteGenerator:
    """
    Generates a color palette for residential painting projects.
    Considers natural lighting, existing decor, and personal preferences.
    """
    
    def __init__(self):
        self.base_colors = {
            'coastal': [(200, 218, 229), (163, 196, 218), (95, 158, 198)],
            'earthy': [(210, 180, 140), (188, 152, 98), (139, 105, 70)],
            'modern': [(240, 240, 240), (200, 200, 200), (160, 160, 160)],
            'traditional': [(245, 235, 220), (220, 210, 190), (195, 180, 160)]
        }
        self.lighting_adjustments = {
            'north': 1.1,  # Cooler, more blue
            'south': 0.9,  # Warmer, more yellow
            'east': 1.0,
            'west': 1.0
        }
    
    def adjust_for_lighting(self, color: Tuple[int, int, int], direction: str) -> Tuple[int, int, int]:
        """
        Adjusts color based on natural lighting direction.
        """
        if direction.lower() not in self.lighting_adjustments:
            raise ValueError("Invalid lighting direction. Must be north, south, east, or west.")
        
        factor = self.lighting_adjustments[direction.lower()]
        h, l, s = colorsys.rgb_to_hls(*[x/255 for x in color])
        
        # Adjust hue based on lighting
        if direction.lower() == 'north':
            h = min(h + 0.02, 1.0)
        elif direction.lower() == 'south':
            h = max(h - 0.02, 0.0)
        
        # Adjust lightness
        l = min(max(l * factor, 0.0), 1.0)
        
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return (int(r * 255), int(g * 255), int(b * 255))
    
    def generate_palette(self, style: str, lighting: str, existing_decor: List[Tuple[int, int, int]] = None) -> Dict:
        """
        Generates a color palette based on style, lighting, and existing decor.
        
        Args:
            style: One of 'coastal', 'earthy', 'modern', 'traditional'
            lighting: Lighting direction ('north', 'south', 'east', 'west')
            existing_decor: List of existing decor colors as RGB tuples
            
        Returns:
            Dictionary containing primary, secondary, and accent colors
        """
        if style.lower() not in self.base_colors:
            raise ValueError("Invalid style. Must be coastal, earthy, modern, or traditional.")
        
        # Get base colors for the selected style
        base_palette = self.base_colors[style.lower()]
        
        # Adjust for lighting
        adjusted_colors = [self.adjust_for_lighting(color, lighting) for color in base_palette]
        
        # Harmonize with existing decor if provided
        if existing_decor:
            adjusted_colors = self.harmonize_with_decor(adjusted_colors, existing_decor)
        
        return {
            'primary': adjusted_colors[0],
            'secondary': adjusted_colors[1],
            'accent': adjusted_colors[2]
        }
    
    def harmonize_with_decor(self, palette: List[Tuple[int, int, int]], decor_colors: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
        """
        Adjusts palette to harmonize with existing decor colors.
        """
        # Calculate average decor color
        avg_r = sum(c[0] for c in decor_colors) // len(decor_colors)
        avg_g = sum(c[1] for c in decor_colors) // len(decor_colors)
        avg_b = sum(c[2] for c in decor_colors) // len(decor_colors)
        
        # Adjust palette colors towards the average decor color
        harmonized = []
        for color in palette:
            new_r = (color[0] + avg_r) // 2
            new_g = (color[1] + avg_g) // 2
            new_b = (color[2] + avg_b) // 2
            harmonized.append((new_r, new_g, new_b))
        
        return harmonized
    
    def rgb_to_hex(self, color: Tuple[int, int, int]) -> str:
        """
        Converts RGB color tuple to hexadecimal string.
        """
        return '#{:02x}{:02x}{:02x}'.format(*color)
    
    def save_palette(self, palette: Dict, filename: str = 'color_palette.json') -> None:
        """
        Saves the generated palette to a JSON file.
        """
        hex_palette = {
            'primary': self.rgb_to_hex(palette['primary']),
            'secondary': self.rgb_to_hex(palette['secondary']),
            'accent': self.rgb_to_hex(palette['accent'])
        }
        
        with open(filename, 'w') as f:
            json.dump(hex_palette, f, indent=4)

def main():
    generator = ColorPaletteGenerator()
    
    try:
        # Example usage
        print("Mornington Peninsula Color Palette Generator")
        print("Available styles: coastal, earthy, modern, traditional")
        
        style = input("Enter preferred style: ")
        lighting = input("Enter primary lighting direction (north/south/east/west): ")
        
        decor_input = input("Enter existing decor colors as comma-separated hex values (optional): ")
        decor_colors = []
        
        if decor_input:
            for hex_color in decor_input.split(','):
                hex_color = hex_color.strip().lstrip('#')
                decor_colors.append(tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)))
        
        palette = generator.generate_palette(style, lighting, decor_colors if decor_colors else None)
        
        print("\nGenerated Color Palette:")
        print(f"Primary: {generator.rgb_to_hex(palette['primary'])}")
        print(f"Secondary: {generator.rgb_to_hex(palette['secondary'])}")
        print(f"Accent: {generator.rgb_to_hex(palette['accent'])}")
        
        save = input("\nSave palette to file? (y/n): ")
        if save.lower() == 'y':
            generator.save_palette(palette)
            print("Palette saved to color_palette.json")
    
    except Exception as e:
        print(f"Error generating palette: {str(e)}")

if __name__ == "__main__":
    main()
```
