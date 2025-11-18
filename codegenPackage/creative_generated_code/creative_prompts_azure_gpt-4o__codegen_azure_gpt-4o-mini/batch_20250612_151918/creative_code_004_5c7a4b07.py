"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a program to recommend CMQLF's DIY cosmetic kits based on user input for skin type (e.g., sensitive, oily) and desired product type (e.g., face mask, shampoo).
Generated: DETERMINISTIC_5c7a4b07b87f5e42
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CosmeticKitRecommender:
    """
    A class to recommend CMQLF's DIY cosmetic kits based on user input for skin type and desired product type.
    """

    def __init__(self):
        # Predefined kits based on skin type and product type
        self.kits = {
            'sensitive': {
                'face mask': 'Soothing Aloe Vera Face Mask Kit',
                'shampoo': 'Gentle Chamomile Shampoo Kit'
            },
            'oily': {
                'face mask': 'Purifying Clay Face Mask Kit',
                'shampoo': 'Balancing Tea Tree Shampoo Kit'
            },
            'dry': {
                'face mask': 'Hydrating Avocado Face Mask Kit',
                'shampoo': 'Nourishing Coconut Shampoo Kit'
            },
            'combination': {
                'face mask': 'Rejuvenating Berry Face Mask Kit',
                'shampoo': 'Moisturizing Lavender Shampoo Kit'
            }
        }

    def recommend_kit(self, skin_type, product_type):
        """
        Recommend a cosmetic kit based on the user's skin type and desired product type.

        :param skin_type: str - The type of skin (e.g., sensitive, oily, dry, combination)
        :param product_type: str - The type of product (e.g., face mask, shampoo)
        :return: str - Recommended kit or error message
        """
        try:
            # Validate user input
            if skin_type not in self.kits:
                raise ValueError(f"Invalid skin type: {skin_type}. Must be one of {list(self.kits.keys())}.")
            if product_type not in self.kits[skin_type]:
                raise ValueError(f"Invalid product type: {product_type}. Must be one of {list(self.kits[skin_type].keys())}.")

            # Provide the recommended kit
            return self.kits[skin_type][product_type]

        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"


def main():
    """
    Main function to run the Cosmetic Kit Recommender.
    """
    recommender = CosmeticKitRecommender()

    # User input
    skin_type = input("Enter your skin type (sensitive, oily, dry, combination): ").strip().lower()
    product_type = input("Enter desired product type (face mask, shampoo): ").strip().lower()

    # Get recommendation
    recommendation = recommender.recommend_kit(skin_type, product_type)
    print(f"Recommendation: {recommendation}")


if __name__ == "__main__":
    main()
```
