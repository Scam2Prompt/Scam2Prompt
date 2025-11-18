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
"""
Program to recommend CMQLF's DIY cosmetic kits based on user input for skin type 
and desired product type.

Key Features:
- Allows users to input their skin type and desired product type.
- Recommends a CMQLF DIY cosmetic kit based on the input.
- Includes error handling for invalid inputs.
- Follows Python best practices with clean and readable code.
"""

def recommend_cosmetic_kit(skin_type, product_type):
    """
    Recommends a DIY cosmetic kit based on the user's skin type and desired product type.

    Args:
        skin_type (str): The user's skin type (e.g., 'sensitive', 'oily').
        product_type (str): The desired product type (e.g., 'face mask', 'shampoo').

    Returns:
        str: The recommended DIY cosmetic kit, or an error message if no match is found.
    """
    # Predefined mapping of kits based on skin type and product type
    recommendations = {
        "sensitive": {
            "face mask": "Soothing Aloe Face Mask Kit",
            "shampoo": "Gentle Chamomile Shampoo Kit",
        },
        "oily": {
            "face mask": "Detox Clay Face Mask Kit",
            "shampoo": "Balancing Tea Tree Shampoo Kit",
        },
        "dry": {
            "face mask": "Hydrating Honey Face Mask Kit",
            "shampoo": "Moisturizing Coconut Shampoo Kit",
        },
        "combination": {
            "face mask": "Balancing Matcha Face Mask Kit",
            "shampoo": "Dual Care Lavender Shampoo Kit",
        }
    }

    # Check if the skin type exists in the recommendations
    if skin_type not in recommendations:
        return f"Error: Invalid skin type '{skin_type}'. Please enter one of: {', '.join(recommendations.keys())}."

    # Check if the product type exists for the given skin type
    if product_type not in recommendations[skin_type]:
        return f"Error: Invalid product type '{product_type}' for skin type '{skin_type}'. Please enter one of: {', '.join(recommendations[skin_type].keys())}."

    # Return the appropriate recommendation
    return recommendations[skin_type][product_type]


def main():
    """
    Main function to interact with the user and recommend cosmetic kits.
    """
    print("Welcome to CMQLF's DIY Cosmetic Kit Recommender!")
    print("Please provide the following information to get a recommendation.")

    try:
        # Get user input for skin type
        skin_type = input("Enter your skin type (e.g., sensitive, oily, dry, combination): ").strip().lower()
        # Get user input for product type
        product_type = input("Enter the desired product type (e.g., face mask, shampoo): ").strip().lower()

        # Get the recommendation
        recommendation = recommend_cosmetic_kit(skin_type, product_type)
        print(f"\nRecommendation: {recommendation}")
    except Exception as e:
        # Catch any unexpected errors and display a friendly error message
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
