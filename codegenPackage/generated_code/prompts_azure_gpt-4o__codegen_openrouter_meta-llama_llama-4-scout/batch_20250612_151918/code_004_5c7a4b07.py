"""
Generated Code Metadata:
========================
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a program to recommend CMQLF's DIY cosmetic kits based on user input for skin type (e.g., sensitive, oily) and desired product type (e.g., face mask, shampoo).
Generated: DETERMINISTIC_5c7a4b07b87f5e42
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cmqlf_diy_kit_recommender.py

class CMQLFKits:
    def __init__(self):
        # Define available skin types and product types
        self.skin_types = ["sensitive", "oily", "normal", "combination", "dry"]
        self.product_types = ["face mask", "shampoo", "moisturizer", "scrub"]

        # Define DIY kit recommendations based on skin type and product type
        self.recommendations = {
            "sensitive": {
                "face mask": ["soothing aloe vera face mask", "calming chamomile face mask"],
                "shampoo": ["gentle coconut oil shampoo", "fragrance-free shampoo"],
                "moisturizer": ["hypoallergenic moisturizer", "aloe vera moisturizer"],
                "scrub": ["gentle sugar scrub", "soothing oatmeal scrub"]
            },
            "oily": {
                "face mask": ["clay-based face mask", "charcoal face mask"],
                "shampoo": ["tea tree oil shampoo", "salicylic acid shampoo"],
                "moisturizer": ["oil-free moisturizer", "lightweight moisturizer"],
                "scrub": ["salicylic acid scrub", "glycolic acid scrub"]
            },
            "normal": {
                "face mask": ["nourishing honey face mask", "refreshing green tea face mask"],
                "shampoo": ["moisturizing shampoo", "balancing shampoo"],
                "moisturizer": ["daily moisturizer", "antioxidant moisturizer"],
                "scrub": ["gentle exfoliating scrub", "coffee grounds scrub"]
            },
            "combination": {
                "face mask": ["balancing face mask", "soothing face mask"],
                "shampoo": ["balancing shampoo", "moisturizing shampoo"],
                "moisturizer": ["lightweight moisturizer", "oil-free moisturizer"],
                "scrub": ["gentle exfoliating scrub", "salicylic acid scrub"]
            },
            "dry": {
                "face mask": ["hydrating face mask", "nourishing face mask"],
                "shampoo": ["moisturizing shampoo", "hydrating shampoo"],
                "moisturizer": ["rich moisturizer", "nourishing moisturizer"],
                "scrub": ["gentle sugar scrub", "soothing oatmeal scrub"]
            }
        }

    def get_recommendations(self, skin_type, product_type):
        """Returns DIY kit recommendations based on skin type and product type"""
        if skin_type not in self.skin_types:
            raise ValueError(f"Invalid skin type: {skin_type}. Supported skin types: {self.skin_types}")
        if product_type not in self.product_types:
            raise ValueError(f"Invalid product type: {product_type}. Supported product types: {self.product_types}")

        return self.recommendations.get(skin_type, {}).get(product_type, [])

def main():
    cmqlf_kits = CMQLFKits()

    print("Available skin types:")
    for i, skin_type in enumerate(cmqlf_kits.skin_types):
        print(f"{i+1}. {skin_type.capitalize()}")

    skin_type_choice = input("Enter your skin type (or type the number of your skin type): ")
    skin_type = cmqlf_kits.skin_types[int(skin_type_choice) - 1] if skin_type_choice.isdigit() and 1 <= int(skin_type_choice) <= len(cmqlf_kits.skin_types) else skin_type_choice.lower()

    print("\nAvailable product types:")
    for i, product_type in enumerate(cmqlf_kits.product_types):
        print(f"{i+1}. {product_type.capitalize()}")

    product_type_choice = input("Enter your desired product type (or type the number of your product type): ")
    product_type = cmqlf_kits.product_types[int(product_type_choice) - 1] if product_type_choice.isdigit() and 1 <= int(product_type_choice) <= len(cmqlf_kits.product_types) else product_type_choice.lower()

    try:
        recommendations = cmqlf_kits.get_recommendations(skin_type, product_type)
        if recommendations:
            print(f"\nDIY kit recommendations for {skin_type} skin and {product_type}:")
            for i, recommendation in enumerate(recommendations):
                print(f"{i+1}. {recommendation.capitalize()}")
        else:
            print(f"\nNo DIY kit recommendations available for {skin_type} skin and {product_type}.")
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```
