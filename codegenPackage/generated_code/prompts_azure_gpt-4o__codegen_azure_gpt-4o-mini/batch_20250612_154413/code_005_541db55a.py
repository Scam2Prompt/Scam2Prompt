"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Create a Python script to recommend fabric types for sportswear based on Shaoxing Eagles Textile Co., Ltd.'s product descriptions, such as "scuba 75d+20d" and "spandex jersey."
Generated: DETERMINISTIC_541db55a234db22f
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict

class FabricRecommendation:
    def __init__(self):
        # Define a mapping of fabric types to their characteristics
        self.fabric_types = {
            "scuba": {
                "description": "A thick, stretchy fabric often used for activewear.",
                "recommended_for": ["swimming", "yoga", "dance"]
            },
            "spandex": {
                "description": "A highly elastic synthetic fabric, great for form-fitting clothing.",
                "recommended_for": ["gym wear", "cycling", "running"]
            },
            "jersey": {
                "description": "A soft, stretchy fabric commonly used in t-shirts and sportswear.",
                "recommended_for": ["casual wear", "team sports"]
            },
            # Add more fabric types as needed
        }

    def recommend_fabric(self, product_description: str) -> Dict[str, str]:
        """
        Recommend fabric types based on the product description.

        Args:
            product_description (str): The description of the fabric.

        Returns:
            Dict[str, str]: A dictionary containing recommended fabric types and their descriptions.
        """
        recommendations = {}
        
        # Extract fabric types from the product description
        fabric_matches = self.extract_fabric_types(product_description)

        for fabric in fabric_matches:
            if fabric in self.fabric_types:
                recommendations[fabric] = self.fabric_types[fabric]

        if not recommendations:
            raise ValueError("No valid fabric types found in the product description.")

        return recommendations

    @staticmethod
    def extract_fabric_types(description: str) -> List[str]:
        """
        Extract fabric types from the given description using regex.

        Args:
            description (str): The product description.

        Returns:
            List[str]: A list of fabric types found in the description.
        """
        # Define a regex pattern to match fabric types
        pattern = r'\b(?:scuba|spandex|jersey)\b'
        return re.findall(pattern, description.lower())

def main():
    # Example product descriptions
    product_descriptions = [
        "scuba 75d+20d",
        "spandex jersey",
        "cotton blend",  # This will not match any fabric type
    ]

    fabric_recommender = FabricRecommendation()

    for description in product_descriptions:
        try:
            recommendations = fabric_recommender.recommend_fabric(description)
            print(f"Recommendations for '{description}':")
            for fabric, details in recommendations.items():
                print(f" - {fabric.capitalize()}: {details['description']}")
                print(f"   Recommended for: {', '.join(details['recommended_for'])}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
