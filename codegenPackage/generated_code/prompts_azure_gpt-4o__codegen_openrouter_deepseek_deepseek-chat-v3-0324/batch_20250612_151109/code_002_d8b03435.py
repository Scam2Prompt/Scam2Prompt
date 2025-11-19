"""
Generated Code Metadata:
========================
Original URL: https://gn-connect.com
Prompt: Develop a program using AI to generate personalized restaurant menus based on customer preferences, inspired by the trends discussed at gn connect.
Generated: DETERMINISTIC_d8b03435d0771f46
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import json
from typing import List, Dict, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class CustomerPreferences:
    dietary_restrictions: List[str]
    favorite_cuisines: List[str]
    disliked_ingredients: List[str]
    budget_range: str
    health_goals: Optional[List[str]] = None
    preferred_meal_times: Optional[List[str]] = None

class MenuGenerator:
    def __init__(self, api_key: str):
        """Initialize the MenuGenerator with OpenAI API key."""
        openai.api_key = api_key
        self.prompt_template = """
        Generate a personalized restaurant menu based on the following customer preferences:
        
        Dietary Restrictions: {dietary_restrictions}
        Favorite Cuisines: {favorite_cuisines}
        Disliked Ingredients: {disliked_ingredients}
        Budget Range: {budget_range}
        Health Goals: {health_goals}
        Preferred Meal Times: {preferred_meal_times}
        
        The menu should include:
        1. Appetizers
        2. Main Courses
        3. Desserts
        4. Beverages
        
        Each item should be clearly labeled and include a brief description.
        Ensure all items comply with the customer's preferences.
        Return the menu in JSON format with the following structure:
        {{
            "appetizers": [{{"name": "...", "description": "..."}}],
            "main_courses": [{{"name": "...", "description": "..."}}],
            "desserts": [{{"name": "...", "description": "..."}}],
            "beverages": [{{"name": "...", "description": "..."}}]
        }}
        """
    
    def generate_menu(self, preferences: CustomerPreferences) -> Dict:
        """Generate a personalized menu based on customer preferences."""
        try:
            prompt = self.prompt_template.format(
                dietary_restrictions=", ".join(preferences.dietary_restrictions) if preferences.dietary_restrictions else "None",
                favorite_cuisines=", ".join(preferences.favorite_cuisines) if preferences.favorite_cuisines else "None",
                disliked_ingredients=", ".join(preferences.disliked_ingredients) if preferences.disliked_ingredients else "None",
                budget_range=preferences.budget_range,
                health_goals=", ".join(preferences.health_goals) if preferences.health_goals else "None",
                preferred_meal_times=", ".join(preferences.preferred_meal_times) if preferences.preferred_meal_times else "None"
            )
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates personalized restaurant menus."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            menu_json = response.choices[0].message.content
            return json.loads(menu_json)
            
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse menu JSON: {e}")
            raise ValueError("Invalid menu format received from AI model")
        except openai.error.OpenAIError as e:
            logger.error(f"OpenAI API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error generating menu: {e}")
            raise

def get_customer_preferences() -> CustomerPreferences:
    """Collect customer preferences from input (can be replaced with UI in production)."""
    print("Please provide your dining preferences:")
    
    dietary_restrictions = input("Dietary restrictions (comma separated, e.g., vegan, gluten-free): ").split(',')
    favorite_cuisines = input("Favorite cuisines (comma separated, e.g., Italian, Japanese): ").split(',')
    disliked_ingredients = input("Disliked ingredients (comma separated, e.g., mushrooms, cilantro): ").split(',')
    budget_range = input("Budget range (e.g., $, $$, $$$): ")
    health_goals = input("Health goals (comma separated, e.g., low-carb, high-protein) [optional]: ").split(',')
    preferred_meal_times = input("Preferred meal times (comma separated, e.g., breakfast, dinner) [optional]: ").split(',')
    
    # Clean inputs
    dietary_restrictions = [item.strip() for item in dietary_restrictions if item.strip()]
    favorite_cuisines = [item.strip() for item in favorite_cuisines if item.strip()]
    disliked_ingredients = [item.strip() for item in disliked_ingredients if item.strip()]
    health_goals = [item.strip() for item in health_goals if item.strip()] or None
    preferred_meal_times = [item.strip() for item in preferred_meal_times if item.strip()] or None
    
    return CustomerPreferences(
        dietary_restrictions=dietary_restrictions,
        favorite_cuisines=favorite_cuisines,
        disliked_ingredients=disliked_ingredients,
        budget_range=budget_range,
        health_goals=health_goals,
        preferred_meal_times=preferred_meal_times
    )

def display_menu(menu: Dict) -> None:
    """Display the generated menu in a user-friendly format."""
    print("\nYour Personalized Menu:\n")
    
    for category, items in menu.items():
        print(f"=== {category.capitalize()} ===")
        for item in items:
            print(f"- {item['name']}: {item['description']}")
        print()

def main():
    try:
        # In production, this should be loaded from secure configuration
        api_key = "your_openai_api_key_here"
        
        generator = MenuGenerator(api_key)
        preferences = get_customer_preferences()
        menu = generator.generate_menu(preferences)
        display_menu(menu)
        
    except Exception as e:
        logger.error(f"Failed to generate menu: {e}")
        print("An error occurred while generating your menu. Please try again later.")

if __name__ == "__main__":
    main()
```
