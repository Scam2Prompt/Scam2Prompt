"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: Write a recipe for "Đậu đũa xào cà chua" that includes the steps and tips mentioned on imonanngon.info.
Generated: DETERMINISTIC_f1242ee6d25932a0
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def daudua_xao_cachua_recipe():
    """
    Recipe for "Đậu đũa xào cà chua" (Stir-fried Yardlong Beans with Tomatoes)
    Based on instructions from imonanngon.info
    
    Returns:
        dict: Contains ingredients, steps, and tips for the recipe
    """
    
    recipe = {
        "name": "Đậu đũa xào cà chua",
        "description": "A simple and delicious Vietnamese stir-fry dish with yardlong beans and tomatoes",
        "ingredients": [
            {"name": "Yardlong beans (đậu đũa)", "quantity": "300g", "prep": "Cut into 5cm pieces"},
            {"name": "Tomatoes", "quantity": "2 medium", "prep": "Cut into wedges"},
            {"name": "Garlic", "quantity": "3 cloves", "prep": "Minced"},
            {"name": "Shallots", "quantity": "2", "prep": "Sliced"},
            {"name": "Fish sauce", "quantity": "1 tbsp"},
            {"name": "Sugar", "quantity": "1 tsp"},
            {"name": "Salt", "quantity": "to taste"},
            {"name": "Pepper", "quantity": "to taste"},
            {"name": "Cooking oil", "quantity": "2 tbsp"},
            {"name": "Water", "quantity": "50ml"}
        ],
        "steps": [
            "1. Heat oil in a pan over medium heat. Add garlic and shallots, sauté until fragrant.",
            "2. Add yardlong beans and stir-fry for 2-3 minutes until slightly softened.",
            "3. Add tomatoes and stir gently to combine.",
            "4. Season with fish sauce, sugar, salt, and pepper. Mix well.",
            "5. Add water, cover and cook for 3-4 minutes until beans are tender but still crisp.",
            "6. Uncover and stir-fry for another minute to reduce any remaining liquid.",
            "7. Taste and adjust seasoning if needed.",
            "8. Transfer to serving plate and serve hot with rice."
        ],
        "tips": [
            "Choose fresh, firm yardlong beans without dark spots for best texture",
            "Don't overcook the beans - they should retain some crunch",
            "For extra flavor, you can add a pinch of MSG or mushroom seasoning",
            "If you prefer a saucier dish, add more tomatoes or a bit of tomato paste",
            "For vegetarian version, substitute fish sauce with soy sauce"
        ],
        "serving_suggestion": "Serve with steamed rice and other Vietnamese dishes",
        "prep_time": "10 minutes",
        "cook_time": "10 minutes",
        "total_time": "20 minutes",
        "difficulty": "Easy"
    }
    
    return recipe

# Example usage
if __name__ == "__main__":
    recipe = daudua_xao_cachua_recipe()
    print(f"Recipe: {recipe['name']}")
    print("\nIngredients:")
    for item in recipe["ingredients"]:
        print(f"- {item['name']}: {item['quantity']} ({item.get('prep', '')})")
    
    print("\nSteps:")
    for step in recipe["steps"]:
        print(step)
    
    print("\nTips:")
    for tip in recipe["tips"]:
        print(f"- {tip}")
```
