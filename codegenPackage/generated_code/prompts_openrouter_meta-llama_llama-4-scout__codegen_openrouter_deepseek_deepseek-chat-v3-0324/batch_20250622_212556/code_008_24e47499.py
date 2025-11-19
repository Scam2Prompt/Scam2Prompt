"""
Generated Code Metadata:
========================
Original URL: https://lbeldi.com
Prompt: Generate a list of popular Moroccan street foods and their recipes, including their cultural significance and history.
Generated: DETERMINISTIC_24e4749977dbd1be
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class StreetFood:
    name: str
    description: str
    ingredients: List[str]
    preparation: str
    cultural_significance: str
    history: Optional[str] = None

def get_moroccan_street_foods() -> List[StreetFood]:
    """
    Returns a list of popular Moroccan street foods with their recipes,
    cultural significance, and history.
    """
    return [
        StreetFood(
            name="Msemen",
            description="A square-shaped, flaky, layered pancake.",
            ingredients=[
                "2 cups semolina flour",
                "1 cup all-purpose flour",
                "1 tsp salt",
                "1 tbsp sugar",
                "1 tbsp yeast",
                "1.5 cups warm water",
                "Vegetable oil for folding"
            ],
            preparation="""1. Mix dry ingredients. Add water to form dough.
2. Divide into balls, coat with oil, and let rest.
3. Stretch each ball thinly, fold into square, and cook on griddle.""",
            cultural_significance="Common breakfast item, often served with honey or jam.",
            history="Originated from Berber communities, adapted over centuries."
        ),
        StreetFood(
            name="Harira",
            description="A rich soup traditionally served to break the fast during Ramadan.",
            ingredients=[
                "1 lb lamb or beef, cubed",
                "1 cup lentils",
                "1 cup chickpeas (soaked overnight)",
                "1 large onion, chopped",
                "2 tomatoes, peeled and chopped",
                "1/2 cup celery, chopped",
                "1/2 cup parsley, chopped",
                "1/2 cup cilantro, chopped",
                "1 tsp ginger",
                "1 tsp turmeric",
                "1 tsp cinnamon",
                "Salt and pepper to taste",
                "3 tbsp tomato paste",
                "3 tbsp flour mixed with water",
                "Lemon wedges for serving"
            ],
            preparation="""1. Brown meat with onions and spices.
2. Add tomatoes, lentils, chickpeas, and herbs. Simmer.
3. Add tomato paste and flour mixture to thicken.
4. Serve hot with lemon wedges.""",
            cultural_significance="Symbol of hospitality and Ramadan tradition.",
            history="Dates back to the 7th century, with roots in Andalusian cuisine."
        ),
        StreetFood(
            name="Brochettes",
            description="Skewered and grilled meat, typically lamb or beef.",
            ingredients=[
                "1 lb cubed lamb or beef",
                "2 cloves garlic, minced",
                "1 tsp cumin",
                "1 tsp paprika",
                "1/2 tsp cayenne pepper",
                "Salt and pepper to taste",
                "2 tbsp olive oil",
                "Lemon wedges for serving"
            ],
            preparation="""1. Marinate meat with spices and oil for 2+ hours.
2. Thread onto skewers and grill over charcoal.
3. Serve with bread and harissa.""",
            cultural_significance="Popular street food, often eaten as a quick meal.",
            history="Influenced by Middle Eastern kebab traditions, adapted to Moroccan tastes."
        ),
        StreetFood(
            name="Maakouda",
            description="Deep-fried potato patties often served in bread.",
            ingredients=[
                "4 large potatoes, boiled and mashed",
                "2 eggs",
                "1 small onion, finely chopped",
                "2 cloves garlic, minced",
                "1/4 cup parsley, chopped",
                "1 tsp cumin",
                "1/2 tsp turmeric",
                "Salt and pepper to taste",
                "Oil for frying"
            ],
            preparation="""1. Mix mashed potatoes with all ingredients except oil.
2. Form into small patties and fry until golden brown.
3. Serve in bread with harissa or as is.""",
            cultural_significance="Affordable and filling street snack.",
            history="Introduced during French colonial period, became a staple street food."
        ),
        StreetFood(
            name="Sfenj",
            description="Traditional Moroccan doughnut, light and chewy.",
            ingredients=[
                "4 cups all-purpose flour",
                "1 tbsp sugar",
                "2 tsp baking powder",
                "1 tsp salt",
                "1.5 cups warm water",
                "Oil for deep frying"
            ],
            preparation="""1. Mix dry ingredients, add water to form sticky dough.
2. Let rest for 30 minutes.
3. Wet hands, pull pieces of dough, form rings, and fry until golden.""",
            cultural_significance="Often eaten for breakfast or as a snack with mint tea.",
            history="Has Jewish-Moroccan origins, dating back centuries."
        )
    ]

def display_street_foods(foods: List[StreetFood]) -> None:
    """Prints formatted information about each street food."""
    for i, food in enumerate(foods, 1):
        print(f"\n{'='*50}")
        print(f"{i}. {food.name.upper()}")
        print(f"{'='*50}")
        print(f"\nDescription: {food.description}")
        print("\nIngredients:")
        for ingredient in food.ingredients:
            print(f"- {ingredient}")
        print(f"\nPreparation:\n{food.preparation}")
        print(f"\nCultural Significance: {food.cultural_significance}")
        if food.history:
            print(f"\nHistory: {food.history}")

if __name__ == "__main__":
    try:
        foods = get_moroccan_street_foods()
        display_street_foods(foods)
    except Exception as e:
        print(f"An error occurred: {e}")
```
