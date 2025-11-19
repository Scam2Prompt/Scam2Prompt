"""
Generated Code Metadata:
========================
Original URL: https://heavymetaldetox.org
Prompt: Generate a list of lifestyle changes to avoid exposure to heavy metals, including suggestions for water filters and detoxifying foods, based on the content of the Heavy Metal Detox website.
Generated: DETERMINISTIC_43fe7dedc5adcad5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class HeavyMetalDetoxGuide:
    """
    A class to generate lifestyle recommendations for avoiding heavy metal exposure.
    Includes water filter suggestions and detoxifying foods.
    """

    def __init__(self):
        self.recommendations = {
            "general_lifestyle": [
                "Avoid smoking and secondhand smoke exposure",
                "Choose organic foods to reduce pesticide exposure",
                "Use natural cleaning products",
                "Avoid aluminum cookware and opt for stainless steel or cast iron",
                "Be cautious with cosmetics - choose products free from lead, mercury, and other heavy metals",
                "Test your home for lead paint if it was built before 1978",
                "Remove shoes before entering home to reduce tracking in contaminants"
            ],
            "water_filters": [
                {
                    "type": "Reverse Osmosis",
                    "description": "Effective at removing heavy metals including lead, arsenic, and mercury",
                    "note": "May remove beneficial minerals; consider remineralization"
                },
                {
                    "type": "Activated Carbon",
                    "description": "Good for removing chlorine and some heavy metals",
                    "note": "Needs regular replacement"
                },
                {
                    "type": "Distillation",
                    "description": "Removes nearly all heavy metals and other contaminants",
                    "note": "Energy intensive process"
                },
                {
                    "type": "Ceramic Filters",
                    "description": "Effective for bacteria and some heavy metals",
                    "note": "Often combined with carbon filters"
                }
            ],
            "detox_foods": [
                "Cilantro - helps remove mercury, lead, and aluminum",
                "Chlorella - binds to heavy metals and aids elimination",
                "Garlic - contains sulfur which helps detoxify",
                "Spirulina - helps remove arsenic",
                "Brazil nuts - high in selenium which protects against mercury",
                "Leafy greens - high in chlorophyll which binds to metals",
                "Pectin-rich fruits (apples, citrus) - helps eliminate metals",
                "Probiotic foods (yogurt, kefir) - support gut health for detoxification"
            ],
            "additional_tips": [
                "Stay hydrated to support kidney function and detoxification",
                "Exercise regularly to promote sweating (another detox pathway)",
                "Consider sauna therapy to enhance heavy metal elimination through sweat",
                "Get adequate sleep to support natural detoxification processes",
                "Manage stress as it can impair detoxification pathways"
            ]
        }

    def get_recommendations(self, category: str = None) -> Dict[str, List]:
        """
        Get detox recommendations by category or all recommendations.
        
        Args:
            category (str, optional): Specific category to retrieve. 
                Options: 'general_lifestyle', 'water_filters', 'detox_foods', 'additional_tips'
                If None, returns all recommendations.
        
        Returns:
            Dict[str, List]: Dictionary containing the requested recommendations
        
        Raises:
            ValueError: If invalid category is provided
        """
        if category:
            if category not in self.recommendations:
                raise ValueError(f"Invalid category. Available options: {list(self.recommendations.keys())}")
            return {category: self.recommendations[category]}
        return self.recommendations

    def save_to_json(self, filename: str = "heavy_metal_detox_guide.json"):
        """
        Save recommendations to a JSON file.
        
        Args:
            filename (str): Name of the file to save to
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.recommendations, f, indent=4)
        except IOError as e:
            print(f"Error saving file: {e}")

    def print_recommendations(self, category: str = None):
        """
        Print recommendations to console in a readable format.
        
        Args:
            category (str, optional): Specific category to print. If None, prints all.
        """
        recs = self.get_recommendations(category)
        
        for category, items in recs.items():
            print(f"\n=== {category.replace('_', ' ').title()} ===")
            if isinstance(items[0], dict):  # For water filters which are dicts
                for item in items:
                    print(f"\n* {item['type']}")
                    print(f"  - {item['description']}")
                    if item['note']:
                        print(f"  Note: {item['note']}")
            else:
                for item in items:
                    print(f"* {item}")


# Example usage
if __name__ == "__main__":
    guide = HeavyMetalDetoxGuide()
    
    # Print all recommendations
    guide.print_recommendations()
    
    # Save to JSON file
    guide.save_to_json()
```
