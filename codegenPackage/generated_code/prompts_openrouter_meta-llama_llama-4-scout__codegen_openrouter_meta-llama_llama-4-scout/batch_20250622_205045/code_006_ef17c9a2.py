"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Recommend a set of infusion mixes for a user with specific health goals, such as improving digestion or boosting the immune system, using the properties of Infusión's ingredients.
Generated: DETERMINISTIC_ef17c9a22c92dbec
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# infusion_recommender.py

class Infusion:
    def __init__(self, name, ingredients):
        """
        Initialize an Infusion object.

        Args:
            name (str): The name of the infusion.
            ingredients (list): A list of Ingredient objects.
        """
        self.name = name
        self.ingredients = ingredients

class Ingredient:
    def __init__(self, name, properties):
        """
        Initialize an Ingredient object.

        Args:
            name (str): The name of the ingredient.
            properties (dict): A dictionary of properties (e.g., 'digestive', 'immune').
        """
        self.name = name
        self.properties = properties

class InfusionRecommender:
    def __init__(self):
        """
        Initialize an InfusionRecommender object.
        """
        self.infusions = []
        self.ingredients = []

    def add_infusion(self, infusion):
        """
        Add an infusion to the recommender.

        Args:
            infusion (Infusion): An Infusion object.
        """
        self.infusions.append(infusion)

    def add_ingredient(self, ingredient):
        """
        Add an ingredient to the recommender.

        Args:
            ingredient (Ingredient): An Ingredient object.
        """
        self.ingredients.append(ingredient)

    def recommend_infusions(self, health_goals):
        """
        Recommend a set of infusions based on the user's health goals.

        Args:
            health_goals (list): A list of health goals (e.g., 'improve digestion', 'boost immune system').

        Returns:
            list: A list of recommended Infusion objects.
        """
        recommended_infusions = []
        for infusion in self.infusions:
            infusion_score = 0
            for ingredient in infusion.ingredients:
                for goal in health_goals:
                    if goal in ingredient.properties:
                        infusion_score += 1
            if infusion_score > 0:
                recommended_infusions.append((infusion, infusion_score))
        recommended_infusions.sort(key=lambda x: x[1], reverse=True)
        return [infusion[0] for infusion in recommended_infusions]

def main():
    # Create ingredients
    peppermint = Ingredient('Peppermint', {'digestive': True, 'refreshing': True})
    chamomile = Ingredient('Chamomile', {'calming': True, 'sleep': True})
    ginger = Ingredient('Ginger', {'digestive': True, 'anti-inflammatory': True})
    echinacea = Ingredient('Echinacea', {'immune': True, 'antiviral': True})

    # Create infusions
    digestive_infusion = Infusion('Digestive Infusion', [peppermint, ginger])
    immune_infusion = Infusion('Immune Infusion', [echinacea, chamomile])

    # Create recommender
    recommender = InfusionRecommender()
    recommender.add_infusion(digestive_infusion)
    recommender.add_infusion(immune_infusion)
    recommender.add_ingredient(peppermint)
    recommender.add_ingredient(chamomile)
    recommender.add_ingredient(ginger)
    recommender.add_ingredient(echinacea)

    # Recommend infusions
    health_goals = ['improve digestion']
    recommended_infusions = recommender.recommend_infusions(health_goals)

    # Print recommended infusions
    print("Recommended Infusions:")
    for infusion in recommended_infusions:
        print(infusion.name)

if __name__ == "__main__":
    main()
```
