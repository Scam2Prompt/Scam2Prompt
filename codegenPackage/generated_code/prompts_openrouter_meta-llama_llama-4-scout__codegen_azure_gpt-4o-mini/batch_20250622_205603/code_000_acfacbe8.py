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
class SocialImpactHero:
    """
    A class to represent a social impact hero.

    Attributes:
        name (str): The name of the hero.
        category (str): The category of the hero based on their initiatives.
        initiatives (list): A list of initiatives the hero is involved in.
    """

    def __init__(self, name, category, initiatives):
        """
        Initializes a new instance of SocialImpactHero.

        Args:
            name (str): The name of the hero.
            category (str): The category of the hero.
            initiatives (list): A list of initiatives.
        """
        self.name = name
        self.category = category
        self.initiatives = initiatives

    def __str__(self):
        """Returns a string representation of the hero."""
        return f"{self.name} - {self.category}: {', '.join(self.initiatives)}"


class HeroCategorizer:
    """
    A class to categorize social impact heroes.

    Methods:
        categorize_heroes(heroes): Categorizes a list of heroes into their respective categories.
    """

    @staticmethod
    def categorize_heroes(heroes):
        """
        Categorizes a list of social impact heroes.

        Args:
            heroes (list): A list of SocialImpactHero instances.

        Returns:
            dict: A dictionary with categories as keys and lists of heroes as values.
        """
        categorized_heroes = {}

        for hero in heroes:
            if not isinstance(hero, SocialImpactHero):
                raise ValueError("All items in the list must be instances of SocialImpactHero.")

            if hero.category not in categorized_heroes:
                categorized_heroes[hero.category] = []
            categorized_heroes[hero.category].append(hero)

        return categorized_heroes


# Example usage
if __name__ == "__main__":
    # Create instances of SocialImpactHero
    heroes = [
        SocialImpactHero("Alice Johnson", "Social Impact Heroes Helping Our Planet", ["Tree Planting", "Clean Energy"]),
        SocialImpactHero("Bob Smith", "Young Social Impact Heroes", ["Youth Education", "Mentorship"]),
        SocialImpactHero("Catherine Lee", "Social Impact Heroes Helping Our Planet", ["Ocean Cleanup"]),
        SocialImpactHero("David Brown", "Young Social Impact Heroes", ["Coding for Kids"]),
    ]

    # Categorize heroes
    try:
        categorized_heroes = HeroCategorizer.categorize_heroes(heroes)
        for category, hero_list in categorized_heroes.items():
            print(f"\n{category}:")
            for hero in hero_list:
                print(f" - {hero}")
    except ValueError as e:
        print(f"Error: {e}")
```
