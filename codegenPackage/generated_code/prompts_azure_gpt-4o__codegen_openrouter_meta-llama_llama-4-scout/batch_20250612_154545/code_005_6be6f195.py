"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Create a Python program to recommend nail art accessories, such as UV/LED lamps, tweezers, and stamping templates, based on user input and AirstyleArt's product catalog.
Generated: DETERMINISTIC_6be6f195e5cb5423
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nail_art_recommender.py

class NailArtAccessory:
    def __init__(self, name, category, price):
        """
        Initialize a NailArtAccessory object.

        Args:
            name (str): Name of the accessory.
            category (str): Category of the accessory (e.g., lamp, tweezers, stamping_template).
            price (float): Price of the accessory.
        """
        self.name = name
        self.category = category
        self.price = price

class AirstyleArtCatalog:
    def __init__(self):
        """
        Initialize an AirstyleArtCatalog object with a list of nail art accessories.
        """
        self.accessories = [
            NailArtAccessory("UV Lamp", "lamp", 50.0),
            NailArtAccessory("LED Lamp", "lamp", 70.0),
            NailArtAccessory("Precision Tweezers", "tweezers", 10.0),
            NailArtAccessory("Stamping Template Set", "stamping_template", 20.0),
            # Add more accessories here...
        ]

    def get_accessories_by_category(self, category):
        """
        Get a list of accessories by category.

        Args:
            category (str): Category of the accessories to retrieve.

        Returns:
            list[NailArtAccessory]: List of accessories in the specified category.
        """
        return [a for a in self.accessories if a.category == category]

class NailArtRecommender:
    def __init__(self, catalog):
        """
        Initialize a NailArtRecommender object with an AirstyleArtCatalog.

        Args:
            catalog (AirstyleArtCatalog): Catalog of nail art accessories.
        """
        self.catalog = catalog

    def recommend_lamp(self, budget):
        """
        Recommend a UV/LED lamp based on the user's budget.

        Args:
            budget (float): User's budget for the lamp.

        Returns:
            NailArtAccessory: Recommended lamp, or None if no lamp is within budget.
        """
        lamps = self.catalog.get_accessories_by_category("lamp")
        affordable_lamps = [l for l in lamps if l.price <= budget]
        if affordable_lamps:
            return min(affordable_lamps, key=lambda l: l.price)
        return None

    def recommend_tweezers(self):
        """
        Recommend tweezers.

        Returns:
            NailArtAccessory: Recommended tweezers.
        """
        tweezers = self.catalog.get_accessories_by_category("tweezers")
        if tweezers:
            return tweezers[0]
        return None

    def recommend_stamping_template(self, budget):
        """
        Recommend a stamping template set based on the user's budget.

        Args:
            budget (float): User's budget for the stamping template.

        Returns:
            NailArtAccessory: Recommended stamping template, or None if no template is within budget.
        """
        templates = self.catalog.get_accessories_by_category("stamping_template")
        affordable_templates = [t for t in templates if t.price <= budget]
        if affordable_templates:
            return min(affordable_templates, key=lambda t: t.price)
        return None

def main():
    catalog = AirstyleArtCatalog()
    recommender = NailArtRecommender(catalog)

    print("Nail Art Accessory Recommender")
    print("--------------------------------")

    budget = float(input("Enter your budget: $"))

    lamp = recommender.recommend_lamp(budget)
    if lamp:
        print(f"Recommended lamp: {lamp.name} (${lamp.price:.2f})")
    else:
        print("No lamps found within your budget.")

    tweezers = recommender.recommend_tweezers()
    if tweezers:
        print(f"Recommended tweezers: {tweezers.name} (${tweezers.price:.2f})")

    template_budget = float(input("Enter your budget for stamping templates: $"))
    template = recommender.recommend_stamping_template(template_budget)
    if template:
        print(f"Recommended stamping template: {template.name} (${template.price:.2f})")
    else:
        print("No stamping templates found within your budget.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
