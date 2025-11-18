"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a script to recommend CMQLF's solid cosmetics for travel, like "coffrets nomades bio," based on user preferences for portability and zero-waste.
Generated: DETERMINISTIC_6b86bad341b43a0e
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class SolidCosmeticsRecommender:
    """
    A class to recommend solid cosmetics based on user preferences for portability and zero-waste.
    """

    def __init__(self):
        # Sample data representing available cosmetics
        self.cosmetics_data = [
            {"name": "Coffret Nomade Bio", "type": "coffret", "portable": True, "zero_waste": True},
            {"name": "Solid Shampoo Bar", "type": "shampoo", "portable": True, "zero_waste": True},
            {"name": "Lip Balm", "type": "lip care", "portable": True, "zero_waste": True},
            {"name": "Solid Conditioner Bar", "type": "conditioner", "portable": True, "zero_waste": True},
            {"name": "Face Cleanser Bar", "type": "cleanser", "portable": False, "zero_waste": True},
            {"name": "Travel Size Lotion Bar", "type": "lotion", "portable": True, "zero_waste": False},
        ]

    def recommend(self, portable: bool, zero_waste: bool) -> List[Dict]:
        """
        Recommend solid cosmetics based on user preferences.
        
        Args:
            portable (bool): User preference for portability.
            zero_waste (bool): User preference for zero-waste products.

        Returns:
            List[Dict]: A list of recommended cosmetics.
        """
        recommendations = []
        try:
            for cosmetic in self.cosmetics_data:
                if (cosmetic["portable"] == portable) and (cosmetic["zero_waste"] == zero_waste):
                    recommendations.append(cosmetic)
            return recommendations
        except Exception as e:
            print(f"An error occurred while recommending products: {e}")
            return []

    def display_recommendations(self, recommendations: List[Dict]) -> None:
        """
        Display the recommended cosmetics in a readable format.

        Args:
            recommendations (List[Dict]): List of recommended cosmetics.
        """
        if not recommendations:
            print("No recommendations found based on your preferences.")
            return
        
        print("Recommended Solid Cosmetics:")
        for cosmetic in recommendations:
            print(f"- {cosmetic['name']} ({cosmetic['type']})")

if __name__ == "__main__":
    # Example usage of the SolidCosmeticsRecommender class

    # Create an instance of the recommender
    recommender = SolidCosmeticsRecommender()

    # User preferences
    user_portable = True
    user_zero_waste = True

    # Get recommendations
    recommended_cosmetics = recommender.recommend(user_portable, user_zero_waste)

    # Display the recommendations
    recommender.display_recommendations(recommended_cosmetics)
```
