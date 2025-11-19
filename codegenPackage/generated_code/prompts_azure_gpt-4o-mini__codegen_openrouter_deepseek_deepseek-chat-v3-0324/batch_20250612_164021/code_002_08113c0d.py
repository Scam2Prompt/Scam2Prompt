"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Create a code snippet for a digital illustration project that incorporates elements of color theory, as taught in the painting courses at Ânima.
Generated: DETERMINISTIC_08113c0d965175f2
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Illustration Color Theory Tool
Inspired by Ânima painting courses' color theory principles.

This script provides utilities for working with color harmonies,
generating color palettes, and analyzing color relationships.
"""

import colorsys
from typing import List, Tuple
import random

class ColorTheoryTool:
    """
    A collection of color theory utilities for digital illustration.
    Supports various color harmonies and conversions.
    """
    
    def __init__(self):
        self.color_formats = ['hex', 'rgb', 'hsv']
    
    @staticmethod
    def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        """
        Convert hex color to RGB tuple.
        
        Args:
            hex_color: Hex string (e.g., '#FF5733')
            
        Returns:
            Tuple of (R, G, B) values (0-255)
            
        Raises:
            ValueError: If hex format is invalid
        """
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            raise ValueError("Hex color must be 6 characters long")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
        """
        Convert RGB tuple to hex color.
        
        Args:
            rgb: Tuple of (R, G, B) values (0-255)
            
        Returns:
            Hex color string
        """
        return '#{:02x}{:02x}{:02x}'.format(*rgb)
    
    @staticmethod
    def rgb_to_hsv(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
        """
        Convert RGB to HSV color space.
        
        Args:
            rgb: Tuple of (R, G, B) values (0-255)
            
        Returns:
            Tuple of (H, S, V) values (0-1)
        """
        r, g, b = [x/255.0 for x in rgb]
        return colorsys.rgb_to_hsv(r, g, b)
    
    @staticmethod
    def hsv_to_rgb(hsv: Tuple[float, float, float]) -> Tuple[int, int, int]:
        """
        Convert HSV to RGB color space.
        
        Args:
            hsv: Tuple of (H, S, V) values (0-1)
            
        Returns:
            Tuple of (R, G, B) values (0-255)
        """
        r, g, b = colorsys.hsv_to_rgb(*hsv)
        return (int(r*255), int(g*255), int(b*255))
    
    def generate_analogous_palette(self, base_color: str, num_colors: int = 3, 
                                 hue_range: float = 30.0) -> List[str]:
        """
        Generate analogous color palette based on color theory principles.
        
        Args:
            base_color: Base color in hex format
            num_colors: Number of colors to generate
            hue_range: Range of hues to include (in degrees)
            
        Returns:
            List of hex color strings
        """
        try:
            rgb = self.hex_to_rgb(base_color)
            h, s, v = self.rgb_to_hsv(rgb)
            
            palette = []
            hue_step = hue_range / (num_colors - 1)
            
            for i in range(num_colors):
                new_h = (h * 360 + (i * hue_step) - (hue_range/2)) % 360 / 360
                new_rgb = self.hsv_to_rgb((new_h, s, v))
                palette.append(self.rgb_to_hex(new_rgb))
                
            return palette
            
        except ValueError as e:
            print(f"Error generating analogous palette: {e}")
            return []
    
    def generate_complementary_palette(self, base_color: str) -> List[str]:
        """
        Generate complementary color palette.
        
        Args:
            base_color: Base color in hex format
            
        Returns:
            List of two hex color strings (base and complement)
        """
        try:
            rgb = self.hex_to_rgb(base_color)
            h, s, v = self.rgb_to_hsv(rgb)
            comp_h = (h + 0.5) % 1.0
            comp_rgb = self.hsv_to_rgb((comp_h, s, v))
            return [base_color, self.rgb_to_hex(comp_rgb)]
            
        except ValueError as e:
            print(f"Error generating complementary palette: {e}")
            return []
    
    def generate_triadic_palette(self, base_color: str) -> List[str]:
        """
        Generate triadic color palette.
        
        Args:
            base_color: Base color in hex format
            
        Returns:
            List of three hex color strings
        """
        try:
            rgb = self.hex_to_rgb(base_color)
            h, s, v = self.rgb_to_hsv(rgb)
            triad1_h = (h + 120/360) % 1.0
            triad2_h = (h + 240/360) % 1.0
            
            triad1_rgb = self.hsv_to_rgb((triad1_h, s, v))
            triad2_rgb = self.hsv_to_rgb((triad2_h, s, v))
            
            return [base_color, self.rgb_to_hex(triad1_rgb), self.rgb_to_hex(triad2_rgb)]
            
        except ValueError as e:
            print(f"Error generating triadic palette: {e}")
            return []
    
    def generate_tetradic_palette(self, base_color: str) -> List[str]:
        """
        Generate tetradic (rectangle) color palette.
        
        Args:
            base_color: Base color in hex format
            
        Returns:
            List of four hex color strings
        """
        try:
            rgb = self.hex_to_rgb(base_color)
            h, s, v = self.rgb_to_hsv(rgb)
            colors = [base_color]
            
            for angle in [90, 180, 270]:
                new_h = (h + angle/360) % 1.0
                new_rgb = self.hsv_to_rgb((new_h, s, v))
                colors.append(self.rgb_to_hex(new_rgb))
                
            return colors
            
        except ValueError as e:
            print(f"Error generating tetradic palette: {e}")
            return []
    
    def generate_random_palette(self, palette_type: str = 'analogous') -> List[str]:
        """
        Generate random color palette of specified type.
        
        Args:
            palette_type: Type of palette ('analogous', 'complementary', 
                          'triadic', 'tetradic')
                          
        Returns:
            List of hex color strings
        """
        # Generate random base color
        h = random.random()
        s = 0.7 + random.random() * 0.3
        v = 0.5 + random.random() * 0.5
        base_rgb = self.hsv_to_rgb((h, s, v))
        base_color = self.rgb_to_hex(base_rgb)
        
        # Generate palette based on type
        if palette_type == 'analogous':
            return self.generate_analogous_palette(base_color, 5)
        elif palette_type == 'complementary':
            return self.generate_complementary_palette(base_color)
        elif palette_type == 'triadic':
            return self.generate_triadic_palette(base_color)
        elif palette_type == 'tetradic':
            return self.generate_tetradic_palette(base_color)
        else:
            print(f"Unknown palette type: {palette_type}")
            return []
    
    def calculate_luminance(self, hex_color: str) -> float:
        """
        Calculate relative luminance of a color (WCAG standard).
        
        Args:
            hex_color: Color in hex format
            
        Returns:
            Luminance value (0-1)
        """
        try:
            r, g, b = self.hex_to_rgb(hex_color)
            rsrgb = r/255.0
            gsrgb = g/255.0
            bsrgb = b/255.0
            
            r = rsrgb/12.92 if rsrgb <= 0.03928 else ((rsrgb+0.055)/1.055)**2.4
            g = gsrgb/12.92 if gsrgb <= 0.03928 else ((gsrgb+0.055)/1.055)**2.4
            b = bsrgb/12.92 if bsrgb <= 0.03928 else ((bsrgb+0.055)/1.055)**2.4
            
            return 0.2126 * r + 0.7152 * g + 0.0722 * b
            
        except ValueError as e:
            print(f"Error calculating luminance: {e}")
            return 0.0
    
    def get_contrast_ratio(self, color1: str, color2: str
