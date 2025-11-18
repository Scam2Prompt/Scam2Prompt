"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Write Python code to create a product recommendation system for bariatric patients, specifically referencing categories like "Compass Products" for gastric bypass and "Believe Products" for sleeve gastrectomy from the PlusMedica Shop website.
Generated: DETERMINISTIC_a10e3579270f668a
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ProductRecommendationSystem:
    """
    A class to recommend products for bariatric patients based on their surgery type.
    """

    def __init__(self):
        """
        Initializes the ProductRecommendationSystem with predefined product categories.
        """
        self.product_catalog = {
            "gastric_bypass": ["Compass Multivitamin", "Compass Calcium Chews", "Compass Iron Capsules"],
            "sleeve_gastrectomy": ["Believe Protein Drink", "Believe Snack Bar", "Believe Multivitamin"]
        }

    def recommend_products(self, surgery_type):
        """
        Recommends products based on the type of bariatric surgery.
        
        Args:
            surgery_type (str): The type of bariatric surgery ('gastric_bypass' or 'sleeve_gastrectomy').
        
        Returns:
            list: A list of recommended products or an error message if surgery type is invalid.
        """
        try:
            # Validate input
            if surgery_type not in self.product_catalog:
                raise ValueError(f"Invalid surgery type: {surgery_type}. Please choose 'gastric_bypass' or 'sleeve_gastrectomy'.")
            
            # Return recommended products
            return self.product_catalog[surgery_type]
        except Exception as e:
            # Handle any unexpected errors
            return {"error": str(e)}

    def to_json(self, data):
        """
        Converts the recommended products or error message to a JSON string.
        
        Args:
            data (list or dict): The data to convert to JSON format.
        
        Returns:
            str: JSON representation of the data.
        """
        try:
            return json.dumps(data, indent=4)
        except Exception as e:
            return json.dumps({"error": f"Failed to convert data to JSON: {str(e)}"}, indent=4)


if __name__ == "__main__":
    # Create an instance of the ProductRecommendationSystem
    recommender = ProductRecommendationSystem()

    # Example usage
    print("Welcome to the Bariatric Product Recommendation System!")
    surgery_type = input("Enter surgery type ('gastric_bypass' or 'sleeve_gastrectomy'): ").strip().lower()

    # Get product recommendations
    recommendations = recommender.recommend_products(surgery_type)

    # Output recommendations in JSON format
    print("\nRecommended Products:")
    print(recommender.to_json(recommendations))
```
