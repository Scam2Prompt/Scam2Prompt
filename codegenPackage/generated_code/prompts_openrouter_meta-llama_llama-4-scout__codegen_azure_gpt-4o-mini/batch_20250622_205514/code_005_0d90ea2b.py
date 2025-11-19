"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Design a hair care product recommendation system based on user input, such as hair type and concerns, and suggest products from Zento's product line.
Generated: DETERMINISTIC_0d90ea2b39ec94ad
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hair_care_recommendation.py

class HairCareProduct:
    """Class representing a hair care product."""
    
    def __init__(self, name, hair_type, concerns):
        """
        Initialize a new hair care product.

        :param name: str - The name of the product
        :param hair_type: list - List of hair types suitable for the product
        :param concerns: list - List of hair concerns the product addresses
        """
        self.name = name
        self.hair_type = hair_type
        self.concerns = concerns

    def is_suitable(self, user_hair_type, user_concerns):
        """
        Check if the product is suitable for the user's hair type and concerns.

        :param user_hair_type: str - The user's hair type
        :param user_concerns: list - List of user's hair concerns
        :return: bool - True if suitable, False otherwise
        """
        return (user_hair_type in self.hair_type) and any(concern in self.concerns for concern in user_concerns)


class HairCareRecommendationSystem:
    """Class to recommend hair care products based on user input."""
    
    def __init__(self):
        """Initialize the recommendation system with Zento's product line."""
        self.products = [
            HairCareProduct("Zento Moisturizing Shampoo", ["dry", "curly"], ["dryness", "frizz"]),
            HairCareProduct("Zento Strengthening Conditioner", ["normal", "wavy"], ["breakage", "dryness"]),
            HairCareProduct("Zento Anti-Dandruff Treatment", ["oily", "normal"], ["dandruff"]),
            HairCareProduct("Zento Nourishing Hair Mask", ["curly", "coily"], ["dryness", "frizz"]),
            HairCareProduct("Zento Volume Boost Spray", ["fine", "normal"], ["flatness"]),
        ]

    def recommend_products(self, user_hair_type, user_concerns):
        """
        Recommend products based on user hair type and concerns.

        :param user_hair_type: str - The user's hair type
        :param user_concerns: list - List of user's hair concerns
        :return: list - List of suitable products
        """
        if not isinstance(user_hair_type, str) or not isinstance(user_concerns, list):
            raise ValueError("Invalid input: user_hair_type must be a string and user_concerns must be a list.")

        recommended = []
        for product in self.products:
            if product.is_suitable(user_hair_type, user_concerns):
                recommended.append(product.name)

        return recommended


def main():
    """Main function to run the hair care recommendation system."""
    try:
        # Example user input
        user_hair_type = "curly"
        user_concerns = ["dryness", "frizz"]

        # Create a recommendation system instance
        recommendation_system = HairCareRecommendationSystem()

        # Get product recommendations
        recommendations = recommendation_system.recommend_products(user_hair_type, user_concerns)

        # Display recommendations
        if recommendations:
            print("Recommended Products:")
            for product in recommendations:
                print(f"- {product}")
        else:
            print("No suitable products found for your hair type and concerns.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
