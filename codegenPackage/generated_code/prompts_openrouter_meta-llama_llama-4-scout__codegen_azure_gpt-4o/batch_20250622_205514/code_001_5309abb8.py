"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Recommend a hair care product for damaged and processed hair, describing its benefits and usage, similar to ZENTO POTION 10 KÖPÜK.
Generated: DETERMINISTIC_5309abb80776c140
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define a function to recommend a hair care product
def recommend_hair_care_product(hair_type):
    """
    Recommend a hair care product based on the hair type.
    
    Parameters:
        hair_type (str): The type of hair (e.g., "damaged", "processed").
    
    Returns:
        dict: A dictionary containing product details, benefits, and usage instructions.
    """
    try:
        # Dictionary of hair care products
        products = {
            "damaged": {
                "name": "ZENTO Potion 10 Foam",
                "benefits": [
                    "Repairs and strengthens damaged hair",
                    "Provides hydration and shine",
                    "Protects against further damage"
                ],
                "usage": "Apply a small amount to damp hair, distribute evenly, and style as desired."
            },
            "processed": {
                "name": "ZENTO Potion 10 Foam",
                "benefits": [
                    "Restores vitality to chemically processed hair",
                    "Improves texture and manageability",
                    "Adds softness and reduces frizz"
                ],
                "usage": "Apply to towel-dried hair, comb through, and style as usual."
            }
        }
        
        # Check if the hair type exists in the dictionary
        if hair_type.lower() in products:
            return products[hair_type.lower()]
        else:
            raise ValueError("Hair type not recognized. Please choose 'damaged' or 'processed'.")
    
    except ValueError as ve:
        # Handle invalid hair type input
        return {"error": str(ve)}
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Main function to demonstrate the recommendation system
def main():
    """
    Main function to interact with the user and recommend a hair care product.
    """
    print("Welcome to the Hair Care Product Recommendation System!")
    hair_type = input("Please enter your hair type (e.g., 'damaged', 'processed'): ").strip()
    
    # Get the recommended product
    recommendation = recommend_hair_care_product(hair_type)
    
    # Display the recommendation
    if "error" in recommendation:
        print(f"Error: {recommendation['error']}")
    else:
        print("\nRecommended Product:")
        print(f"Name: {recommendation['name']}")
        print("Benefits:")
        for benefit in recommendation['benefits']:
            print(f"- {benefit}")
        print(f"Usage: {recommendation['usage']}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
