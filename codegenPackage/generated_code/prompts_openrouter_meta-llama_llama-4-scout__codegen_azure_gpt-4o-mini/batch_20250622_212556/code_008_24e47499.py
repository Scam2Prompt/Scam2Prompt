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
import json

# Define a class to represent a street food item
class StreetFood:
    def __init__(self, name, recipe, cultural_significance, history):
        """
        Initialize a StreetFood object.

        :param name: Name of the street food
        :param recipe: Recipe for the street food
        :param cultural_significance: Cultural significance of the street food
        :param history: Historical background of the street food
        """
        self.name = name
        self.recipe = recipe
        self.cultural_significance = cultural_significance
        self.history = history

    def to_dict(self):
        """
        Convert the StreetFood object to a dictionary.

        :return: Dictionary representation of the StreetFood object
        """
        return {
            "name": self.name,
            "recipe": self.recipe,
            "cultural_significance": self.cultural_significance,
            "history": self.history
        }

# Function to generate a list of popular Moroccan street foods
def generate_moroccan_street_foods():
    """
    Generate a list of popular Moroccan street foods with their recipes,
    cultural significance, and history.

    :return: List of StreetFood objects
    """
    street_foods = []

    # Example street food items
    street_foods.append(StreetFood(
        name="Tajine",
        recipe="Cook meat and vegetables slowly in a conical pot.",
        cultural_significance="Tajine is a staple of Moroccan cuisine, symbolizing hospitality.",
        history="Originated from Berber culture, it has evolved over centuries."
    ))

    street_foods.append(StreetFood(
        name="Briouat",
        recipe="Fill pastry with meat or almond paste, then fry or bake.",
        cultural_significance="Often served during celebrations and weddings.",
        history="A traditional dish with roots in Andalusian cuisine."
    ))

    street_foods.append(StreetFood(
        name="Msemen",
        recipe="Layered flatbread, cooked on a griddle, often served with honey.",
        cultural_significance="Commonly enjoyed for breakfast or as a snack.",
        history="Msemen has been a part of Moroccan culture for centuries."
    ))

    street_foods.append(StreetFood(
        name="Harira",
        recipe="A soup made with tomatoes, lentils, chickpeas, and spices.",
        cultural_significance="Traditionally eaten during Ramadan to break the fast.",
        history="Harira has been a staple in Moroccan households for generations."
    ))

    return street_foods

# Function to save street food data to a JSON file
def save_street_foods_to_json(file_path):
    """
    Save the list of Moroccan street foods to a JSON file.

    :param file_path: Path to the JSON file
    """
    try:
        street_foods = generate_moroccan_street_foods()
        street_foods_dict = [food.to_dict() for food in street_foods]

        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(street_foods_dict, json_file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving to JSON: {e}")

# Main execution
if __name__ == "__main__":
    # Specify the output JSON file path
    output_file_path = "moroccan_street_foods.json"
    save_street_foods_to_json(output_file_path)
```
