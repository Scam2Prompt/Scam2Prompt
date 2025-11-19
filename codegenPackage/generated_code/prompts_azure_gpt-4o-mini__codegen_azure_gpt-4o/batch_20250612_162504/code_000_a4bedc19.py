"""
Generated Code Metadata:
========================
Original URL: https://gematria.com
Prompt: Generate a Python script that utilizes the science-backed supplements from Gematria to enhance digestive health, referencing Dr. Todd Ovokaitys' research.
Generated: DETERMINISTIC_a4bedc19f91acf03
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides information about science-backed supplements for digestive health
based on Dr. Todd Ovokaitys' research and Gematria's formulations. It is designed to
educate users about the supplements and their benefits.

Note: This script does not provide medical advice. Consult a healthcare professional
before using any supplements.
"""

import sys

def get_digestive_health_supplements():
    """
    Returns a list of science-backed supplements for digestive health
    based on Dr. Todd Ovokaitys' research and Gematria's formulations.
    """
    supplements = [
        {
            "name": "Digestive Enzyme Complex",
            "description": "Supports optimal digestion by breaking down proteins, fats, and carbohydrates.",
            "key_ingredients": ["Protease", "Lipase", "Amylase"]
        },
        {
            "name": "Probiotic Formula",
            "description": "Promotes gut health by restoring beneficial bacteria in the digestive tract.",
            "key_ingredients": ["Lactobacillus acidophilus", "Bifidobacterium bifidum"]
        },
        {
            "name": "L-Glutamine",
            "description": "Helps repair and maintain the intestinal lining, supporting gut integrity.",
            "key_ingredients": ["L-Glutamine"]
        },
        {
            "name": "Aloe Vera Extract",
            "description": "Soothes the digestive system and supports healthy bowel movements.",
            "key_ingredients": ["Aloe Vera"]
        },
        {
            "name": "Slippery Elm Bark",
            "description": "Provides mucilage to coat and soothe the digestive tract.",
            "key_ingredients": ["Slippery Elm Bark"]
        }
    ]
    return supplements

def display_supplements(supplements):
    """
    Displays the list of supplements and their details in a user-friendly format.
    """
    print("Science-Backed Supplements for Digestive Health:\n")
    for idx, supplement in enumerate(supplements, start=1):
        print(f"{idx}. {supplement['name']}")
        print(f"   Description: {supplement['description']}")
        print(f"   Key Ingredients: {', '.join(supplement['key_ingredients'])}\n")

def main():
    """
    Main function to execute the script.
    """
    try:
        # Fetch the list of supplements
        supplements = get_digestive_health_supplements()
        
        # Display the supplements to the user
        display_supplements(supplements)
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the script
    main()
```
