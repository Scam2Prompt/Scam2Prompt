"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rawcakesandcandy.ro
Prompt: Develop a function that lists all available vegan cake options from a bakery, ensuring it includes details like ingredients and allergen information, similar to the product descriptions on Raw Cakes And Candy's site.
Generated: DETERMINISTIC_675662edff72d4fb
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample bakery data simulating a database or external API response
BAKERY_DATA = [
    {
        "name": "Chocolate Vegan Cake",
        "ingredients": ["cocoa powder", "almond flour", "coconut milk", "maple syrup"],
        "allergens": ["nuts (almonds)", "coconut"],
        "vegan": True
    },
    {
        "name": "Strawberry Cheesecake",
        "ingredients": ["cream cheese", "strawberries", "sugar", "wheat flour"],
        "allergens": ["dairy", "gluten"],
        "vegan": False
    },
    {
        "name": "Lemon Vegan Cake",
        "ingredients": ["lemon juice", "oat flour", "coconut oil", "agave nectar"],
        "allergens": ["coconut"],
        "vegan": True
    },
    {
        "name": "Carrot Cake",
        "ingredients": ["carrots", "wheat flour", "eggs", "brown sugar"],
        "allergens": ["gluten", "eggs"],
        "vegan": False
    },
]

def list_vegan_cake_options(bakery_data):
    """
    Lists all available vegan cake options from the bakery with details like ingredients
    and allergen information.
    
    Args:
        bakery_data (list): A list of dictionaries containing cake information.
    
    Returns:
        list: A list of dictionaries containing details of vegan cakes.
    """
    try:
        # Filter vegan cakes
        vegan_cakes = [
            {
                "name": cake["name"],
                "ingredients": cake["ingredients"],
                "allergens": cake["allergens"]
            }
            for cake in bakery_data if cake.get("vegan") is True
        ]
        
        # Return the result
        return vegan_cakes
    except KeyError as e:
        # Handle cases where expected keys might be missing in the data
        print(f"Error processing bakery data: Missing key {e}")
        return []

# Main execution (example usage)
if __name__ == "__main__":
    # Get the list of vegan cakes
    vegan_cakes = list_vegan_cake_options(BAKERY_DATA)
    
    # Print the results in JSON format for readability
    print(json.dumps(vegan_cakes, indent=4))
```
