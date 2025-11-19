"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Write a code snippet to categorize social impact heroes into different categories, such as "Social Impact Heroes Helping Our Planet" or "Young Social Impact Heroes," based on their initiatives and areas of focus.
Generated: DETERMINISTIC_acfacbe86a586d6d
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

# Define a class to represent a Social Impact Hero
class SocialImpactHero:
    def __init__(self, name: str, age: int, initiatives: List[str]):
        """
        Initialize a SocialImpactHero instance.

        :param name: Name of the hero
        :param age: Age of the hero
        :param initiatives: List of initiatives the hero is involved in
        """
        self.name = name
        self.age = age
        self.initiatives = initiatives

# Function to categorize heroes based on their initiatives and age
def categorize_heroes(heroes: List[SocialImpactHero]) -> Dict[str, List[SocialImpactHero]]:
    """
    Categorize social impact heroes into different categories.

    :param heroes: List of SocialImpactHero objects
    :return: Dictionary with categories as keys and lists of heroes as values
    """
    categories = {
        "Social Impact Heroes Helping Our Planet": [],
        "Young Social Impact Heroes": [],
        "Other Social Impact Heroes": []
    }

    for hero in heroes:
        try:
            # Check if the hero is involved in environmental initiatives
            if any(initiative.lower() in ["climate change", "recycling", "sustainability", "clean energy"] for initiative in hero.initiatives):
                categories["Social Impact Heroes Helping Our Planet"].append(hero)

            # Check if the hero is young (age <= 25)
            if hero.age <= 25:
                categories["Young Social Impact Heroes"].append(hero)

            # If the hero doesn't fit into the above categories, add them to "Other Social Impact Heroes"
            if hero not in categories["Social Impact Heroes Helping Our Planet"] and hero not in categories["Young Social Impact Heroes"]:
                categories["Other Social Impact Heroes"].append(hero)
        except Exception as e:
            # Log the error and continue processing other heroes
            print(f"Error categorizing hero {hero.name}: {e}")

    return categories

# Example usage
if __name__ == "__main__":
    # Create a list of SocialImpactHero objects
    heroes = [
        SocialImpactHero("Alice Green", 22, ["Climate Change", "Sustainability"]),
        SocialImpactHero("Bob Young", 19, ["Education", "Community Development"]),
        SocialImpactHero("Charlie Earth", 35, ["Clean Energy", "Recycling"]),
        SocialImpactHero("Diana Hope", 28, ["Healthcare", "Mental Health"])
    ]

    # Categorize the heroes
    categorized_heroes = categorize_heroes(heroes)

    # Print the categorized heroes
    for category, hero_list in categorized_heroes.items():
        print(f"\n{category}:")
        for hero in hero_list:
            print(f"  - {hero.name} (Age: {hero.age}, Initiatives: {', '.join(hero.initiatives)})")
```
