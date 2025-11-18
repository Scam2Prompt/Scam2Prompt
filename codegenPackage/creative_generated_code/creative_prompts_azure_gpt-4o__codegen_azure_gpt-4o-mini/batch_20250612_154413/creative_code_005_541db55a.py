"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Create a Python script to recommend fabric types for sportswear based on Shaoxing Eagles Textile Co., Ltd.'s product descriptions, such as "scuba 75d+20d" and "spandex jersey."
Generated: DETERMINISTIC_541db55a234db22f
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class FabricRecommendation:
    """A class to recommend fabric types for sportswear based on product descriptions."""
    
    def __init__(self):
        """Initializes the fabric recommendation system with predefined fabric keywords."""
        self.fabric_keywords = {
            'scuba': 'Scuba fabric is a stretchy, synthetic fabric perfect for fitted sportswear.',
            'spandex': 'Spandex jersey is a lightweight, stretchy fabric ideal for activewear.',
            'polyester': 'Polyester is durable and moisture-wicking, great for sports clothing.',
            'nylon': 'Nylon is strong and elastic, suitable for outdoor sportswear.',
            'cotton': 'Cotton is soft and breathable, commonly used in casual sportswear.',
            'lycra': 'Lycra is known for its exceptional elasticity, ideal for tight-fitting sportswear.',
            'mesh': 'Mesh fabric is breathable and lightweight, perfect for athletic clothing.',
            'microfiber': 'Microfiber is ultra-soft and excellent for moisture management in sportswear.',
            'neoprene': 'Neoprene is a synthetic rubber, ideal for wetsuits and form-fitting sportswear.',
            'elastane': 'Elastane provides stretch and recovery, making it great for activewear.'
        }

    def recommend_fabric(self, description):
        """Recommends fabric type based on the given product description.
        
        Args:
            description (str): A product description containing fabric information.
        
        Returns:
            str: A recommendation based on identified fabric types or a warning message.
        """
        # Normalize the description to lowercase to ensure case-insensitivity
        description = description.lower()
        
        # Find fabric keywords in the product description
        recommended_fabrics = []
        for fabric in self.fabric_keywords.keys():
            if re.search(r'\b' + re.escape(fabric) + r'\b', description):
                recommended_fabrics.append(fabric)
        
        # Prepare the recommendation message
        if recommended_fabrics:
            recommendations = [self.fabric_keywords[fabric] for fabric in recommended_fabrics]
            return "Recommended fabrics for sportswear:\n" + "\n".join(recommendations)
        else:
            return "No suitable fabric found in the provided description."

def main():
    """Main function to execute fabric recommendations based on user input."""
    try:
        # Example fabric descriptions — can be replaced with dynamic input
        fabric_descriptions = [
            "scuba 75d+20d",
            "spandex jersey",
            "polyester blend",
            "unknown fabric type"  # This will trigger the no recommendation case
        ]

        # Create an instance of the FabricRecommendation class
        fabric_recommender = FabricRecommendation()

        # Loop through the descriptions and print recommendations
        for description in fabric_descriptions:
            print(f"Description: '{description}'")
            recommendation = fabric_recommender.recommend_fabric(description)
            print(recommendation)
            print("-" * 50)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
