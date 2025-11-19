"""
Generated Code Metadata:
========================
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a script to recommend CMQLF's solid cosmetics for travel, like "coffrets nomades bio," based on user preferences for portability and zero-waste.
Generated: DETERMINISTIC_6b86bad341b43a0e
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

# Define a class for CosmeticProduct
class CosmeticProduct:
    def __init__(self, name, portability_score, zero_waste_score, description):
        """
        Initialize a CosmeticProduct object.

        Args:
        - name (str): Name of the cosmetic product.
        - portability_score (int): Score for portability (1-5).
        - zero_waste_score (int): Score for zero-waste (1-5).
        - description (str): Description of the product.
        """
        self.name = name
        self.portability_score = portability_score
        self.zero_waste_score = zero_waste_score
        self.description = description

# Define a class for CosmeticRecommender
class CosmeticRecommender:
    def __init__(self, products):
        """
        Initialize a CosmeticRecommender object.

        Args:
        - products (list): List of CosmeticProduct objects.
        """
        self.products = products

    def recommend(self, min_portability_score, min_zero_waste_score):
        """
        Recommend cosmetic products based on user preferences.

        Args:
        - min_portability_score (int): Minimum portability score.
        - min_zero_waste_score (int): Minimum zero-waste score.

        Returns:
        - list: List of recommended CosmeticProduct objects.
        """
        recommended_products = [
            product for product in self.products 
            if product.portability_score >= min_portability_score 
            and product.zero_waste_score >= min_zero_waste_score
        ]
        return recommended_products

# Load data on cosmetic products
def load_products():
    try:
        data = {
            "name": ["Coffret Nomade Bio", "Travel-sized Makeup Kit", "Eco-friendly Skincare Set"],
            "portability_score": [5, 4, 5],
            "zero_waste_score": [5, 3, 4],
            "description": ["A travel-friendly, bio-based makeup coffret.", "A compact makeup kit for on-the-go.", "A set of eco-friendly skincare products."]
        }
        df = pd.DataFrame(data)
        products = [
            CosmeticProduct(row["name"], row["portability_score"], row["zero_waste_score"], row["description"]) 
            for index, row in df.iterrows()
        ]
        return products
    except Exception as e:
        print(f"Error loading products: {str(e)}")
        return []

# Main function
def main():
    products = load_products()
    recommender = CosmeticRecommender(products)

    # Get user preferences
    min_portability_score = int(input("Enter minimum portability score (1-5): "))
    min_zero_waste_score = int(input("Enter minimum zero-waste score (1-5): "))

    # Recommend products
    recommended_products = recommender.recommend(min_portability_score, min_zero_waste_score)

    # Display recommended products
    if recommended_products:
        print("Recommended products:")
        for product in recommended_products:
            print(f"Name: {product.name}")
            print(f"Description: {product.description}")
            print(f"Portability Score: {product.portability_score}/5")
            print(f"Zero-waste Score: {product.zero_waste_score}/5")
            print("------------------------")
    else:
        print("No products match your preferences.")

if __name__ == "__main__":
    main()
```
