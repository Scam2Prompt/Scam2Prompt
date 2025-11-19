"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Write a Python script to recommend aerography paints, such as neon, metallic, and pastel colors, based on user-selected nail art themes.
Generated: DETERMINISTIC_f0283e52e3e6ecba
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional

class AerographyPaintRecommender:
    """
    A class to recommend aerography paints based on nail art themes.
    Supports neon, metallic, and pastel color recommendations.
    """
    
    def __init__(self):
        """
        Initialize the paint recommendations database with theme-color mappings.
        """
        self.theme_colors = {
            # Theme: {color_type: [colors]}
            'festive': {
                'neon': ['electric pink', 'lime green', 'vivid orange', 'bright yellow'],
                'metallic': ['gold', 'silver', 'rose gold', 'bronze'],
                'pastel': ['soft pink', 'mint green', 'lavender', 'baby blue']
            },
            'elegant': {
                'neon': ['hot pink', 'bright purple', 'electric blue'],
                'metallic': ['platinum', 'champagne', 'gunmetal'],
                'pastel': ['peach', 'powder blue', 'pale lilac']
            },
            'gothic': {
                'neon': ['neon red', 'neon purple', 'acid green'],
                'metallic': ['black metallic', 'dark silver', 'obsidian'],
                'pastel': ['dusty rose', 'muted lavender', 'ash gray']
            },
            'summer': {
                'neon': ['coral', 'turquoise', 'sunshine yellow'],
                'metallic': ['copper', 'sunset gold', 'aqua metallic'],
                'pastel': ['seafoam green', 'peach', 'sky blue']
            },
            'winter': {
                'neon': ['icy blue', 'frost pink', 'snow white'],
                'metallic': ['silver frost', 'pearl', 'ice blue metallic'],
                'pastel': ['frosted mint', 'winter lilac', 'pale blue']
            }
        }
    
    def get_available_themes(self) -> List[str]:
        """
        Returns a list of available nail art themes.
        
        Returns:
            List[str]: Available themes
        """
        return list(self.theme_colors.keys())
    
    def get_available_color_types(self) -> List[str]:
        """
        Returns a list of available color types.
        
        Returns:
            List[str]: Available color types (neon, metallic, pastel)
        """
        return ['neon', 'metallic', 'pastel']
    
    def recommend_paints(
        self,
        theme: str,
        color_type: Optional[str] = None,
        num_recommendations: int = 3
    ) -> Dict[str, List[str]]:
        """
        Recommends paints based on theme and optionally color type.
        
        Args:
            theme: Selected nail art theme
            color_type: Optional filter for color type (neon/metallic/pastel)
            num_recommendations: Number of colors to recommend per type
            
        Returns:
            Dict[str, List[str]]: Recommended colors grouped by color type
            
        Raises:
            ValueError: If theme or color type is invalid
        """
        if theme not in self.theme_colors:
            raise ValueError(f"Invalid theme. Available themes: {self.get_available_themes()}")
        
        recommendations = {}
        
        if color_type:
            if color_type not in self.get_available_color_types():
                raise ValueError(f"Invalid color type. Available types: {self.get_available_color_types()}")
            
            colors = self.theme_colors[theme].get(color_type, [])
            if not colors:
                return {color_type: []}
            
            recommendations[color_type] = random.sample(
                colors,
                min(num_recommendations, len(colors))
            )
        else:
            for c_type in self.get_available_color_types():
                colors = self.theme_colors[theme].get(c_type, [])
                if colors:
                    recommendations[c_type] = random.sample(
                        colors,
                        min(num_recommendations, len(colors))
                    )
        
        return recommendations

def main():
    """
    Main function to demonstrate the paint recommender with user interaction.
    """
    recommender = AerographyPaintRecommender()
    
    print("Welcome to the Aerography Paint Recommender!")
    print(f"Available themes: {', '.join(recommender.get_available_themes())}")
    print(f"Available color types: {', '.join(recommender.get_available_color_types())}")
    
    try:
        theme = input("Enter your desired nail art theme: ").strip().lower()
        color_type = input("Enter color type (neon/metallic/pastel) or leave blank for all: ").strip().lower()
        if not color_type:
            color_type = None
        
        num_rec = input("How many recommendations per color type? (default 3): ").strip()
        num_rec = int(num_rec) if num_rec.isdigit() else 3
        
        recommendations = recommender.recommend_paints(theme, color_type, num_rec)
        
        print("\nRecommended paints:")
        for c_type, colors in recommendations.items():
            print(f"{c_type.capitalize()}: {', '.join(colors)}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
