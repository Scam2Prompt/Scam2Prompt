"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casadelospastes.com
Prompt: Generate a recipe for making traditional Mexican pastes, incorporating ingredients like potato, beef, and green chilies, as inspired by La Casa de los Pastes.
Generated: DETERMINISTIC_d31f30f7aa504162
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def create_mexican_paste_recipe():
    """
    Generates a traditional recipe for making Mexican pastes with potato, beef, and green chilies.
    Inspired by La Casa de los Pastes.
    Returns the recipe as a JSON object.
    """
    try:
        # Define the recipe as a dictionary
        recipe = {
            "name": "Traditional Mexican Pastes",
            "description": "A savory pastry filled with potato, beef, and green chilies, inspired by the flavors of La Casa de los Pastes.",
            "prep_time_minutes": 40,
            "cook_time_minutes": 25,
            "servings": 8,
            "ingredients": [
                {"name": "All-purpose flour", "quantity": "3 cups"},
                {"name": "Unsalted butter", "quantity": "1 cup (cold, diced)"},
                {"name": "Salt", "quantity": "1/2 teaspoon"},
                {"name": "Cold water", "quantity": "1/2 cup"},
                {"name": "Ground beef", "quantity": "1 lb"},
                {"name": "Potatoes", "quantity": "2 medium, peeled and diced into small cubes"},
                {"name": "Green chilies", "quantity": "2, finely chopped"},
                {"name": "Onion", "quantity": "1 small, finely chopped"},
                {"name": "Garlic", "quantity": "2 cloves, minced"},
                {"name": "Ground cumin", "quantity": "1 teaspoon"},
                {"name": "Vegetable oil", "quantity": "2 tablespoons"},
                {"name": "Egg", "quantity": "1 (for egg wash)"},
            ],
            "instructions": [
                "1. Preheat your oven to 375°F (190°C).",
                "2. In a large mixing bowl, combine the flour and salt. Add the cold butter and use a pastry cutter or your fingers to blend until the mixture resembles coarse crumbs.",
                "3. Gradually add cold water, 1 tablespoon at a time, and mix until the dough comes together. Form into a ball, wrap in plastic, and refrigerate for at least 30 minutes.",
                "4. Heat the vegetable oil in a skillet over medium heat. Sauté the onions and garlic until softened.",
                "5. Add the ground beef to the skillet and cook until browned. Stir in the diced potatoes, green chilies, cumin, and salt to taste. Cook for 8–10 minutes until the potatoes are tender. Set aside to cool.",
                "6. Roll out the chilled pastry dough on a floured surface to about 1/8 inch thickness. Cut into 6-inch circles.",
                "7. Place a spoonful of the beef mixture in the center of each circle. Fold the dough over to form a half-moon shape and seal the edges by crimping with a fork.",
                "8. Beat the egg and brush it over the pastes for a golden finish.",
                "9. Place the pastes on a baking sheet lined with parchment paper. Bake in the preheated oven for 25–30 minutes or until golden brown.",
                "10. Let the pastes cool slightly before serving. Enjoy!"
            ]
        }

        # Convert the recipe dictionary to a JSON object for output
        recipe_json = json.dumps(recipe, indent=4)
        return recipe_json

    except Exception as e:
        # Handle any unexpected errors
        return json.dumps({"error": f"An error occurred: {str(e)}"})

if __name__ == "__main__":
    # Generate the recipe and print it in JSON format
    print(create_mexican_paste_recipe())
```
