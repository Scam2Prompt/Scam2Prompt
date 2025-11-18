"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Write a function to recommend farming machinery like brush cutters and water pumps based on user input, using the categories listed on Dotcom Machinery's site.
Generated: DETERMINISTIC_25504fea3d7f457e
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

# Define a class to represent farming machinery recommendations
class MachineryRecommendation:
    def __init__(self):
        # Define available categories and their respective machinery
        self.categories: Dict[str, List[str]] = {
            "brush_cutters": [
                "Lightweight Brush Cutter",
                "Heavy-Duty Brush Cutter",
                "Electric Brush Cutter",
            ],
            "water_pumps": [
                "Submersible Water Pump",
                "Surface Water Pump",
                "Solar Water Pump",
            ],
            "tillers": [
                "Garden Tiller",
                "Cultivator Tiller",
                "Rear-Tine Tiller",
            ],
            "tractors": [
                "Compact Tractor",
                "Utility Tractor",
                "Garden Tractor",
            ],
        }

    def recommend_machinery(self, category: str) -> List[str]:
        """
        Recommend machinery based on the provided category.

        Args:
            category (str): The category of machinery to recommend.

        Returns:
            List[str]: A list of recommended machinery items.

        Raises:
            ValueError: If the provided category is not valid.
        """
        # Normalize the category input
        category = category.lower()

        # Check if the category exists in the predefined categories
        if category not in self.categories:
            raise ValueError(f"Invalid category '{category}'. Valid categories are: {', '.join(self.categories.keys())}")

        # Return the recommended machinery for the given category
        return self.categories[category]

# Example usage of the MachineryRecommendation class
if __name__ == "__main__":
    machinery_recommender = MachineryRecommendation()
    
    # User input (for demonstration purposes)
    user_input = "water_pumps"

    try:
        recommendations = machinery_recommender.recommend_machinery(user_input)
        print(f"Recommended machinery for category '{user_input}':")
        for machinery in recommendations:
            print(f"- {machinery}")
    except ValueError as e:
        print(e)
```
