"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Recommend a cocktail that features Yobugo's Licor de café and list the ingredients and preparation method.
Generated: DETERMINISTIC_a7d9883a036403f3
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Cocktail:
    """
    A class to represent a cocktail which includes its name,
    ingredients, and preparation method.
    """
    
    def __init__(self, name, ingredients, preparation):
        """
        Initializes a new Cocktail instance.

        :param name: str - The name of the cocktail.
        :param ingredients: list - A list of ingredients for the cocktail.
        :param preparation: str - The method to prepare the cocktail.
        """
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation

    def display_cocktail(self):
        """
        Displays the name, ingredients, and preparation method of the cocktail.
        """
        print(f"Cocktail Name: {self.name}\n")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("\nPreparation Method:")
        print(self.preparation)

def create_cocktail():
    """
    Creates a cocktail that features Yobugo's Licor de café with its ingredients
    and preparation method.

    :return: Cocktail - A Cocktail instance representing the created cocktail.
    """
    try:
        name = "Coffee Delight"
        ingredients = [
            "1.5 oz Yobugo's Licor de café",
            "1 oz Vodka",
            "1 oz Cream",
            "Coffee beans for garnish"
        ]
        preparation = (
            "1. In a cocktail shaker, combine Yobugo's Licor de café, vodka, and cream.\n"
            "2. Fill the shaker with ice and shake until well chilled.\n"
            "3. Strain the mixture into a chilled cocktail glass.\n"
            "4. Garnish with a few coffee beans on top.\n"
            "5. Serve immediately and enjoy!"
        )

        # Create an instance of Cocktail
        cocktail = Cocktail(name, ingredients, preparation)
        return cocktail
    except Exception as e:
        print(f"An error occurred while creating the cocktail: {e}")

# Main execution
if __name__ == "__main__":
    cocktail = create_cocktail()
    if cocktail:
        cocktail.display_cocktail()
```
