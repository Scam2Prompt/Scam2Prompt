"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infusionperu.com
Prompt: Write a code snippet that simulates a drink selection system for Infusion Peru, allowing users to choose mixes based on health benefits like digestion and relaxation.
Generated: DETERMINISTIC_7c3097625a5837c3
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Drink:
    """Represents a drink with a name, ingredients, and health benefits."""
    
    def __init__(self, name, ingredients, benefits):
        self.name = name
        self.ingredients = ingredients
        self.benefits = benefits

    def __str__(self):
        return f"{self.name} - Ingredients: {', '.join(self.ingredients)} | Benefits: {', '.join(self.benefits)}"


class DrinkSelectionSystem:
    """A system to manage and select drinks based on health benefits."""
    
    def __init__(self):
        self.drinks = []
        self.populate_drinks()

    def populate_drinks(self):
        """Populate the drink selection with predefined drinks."""
        self.drinks.append(Drink("Digestive Herbal Tea", ["Peppermint", "Ginger", "Fennel"], ["Digestion", "Nausea Relief"]))
        self.drinks.append(Drink("Relaxing Chamomile Blend", ["Chamomile", "Lavender", "Honey"], ["Relaxation", "Sleep Aid"]))
        self.drinks.append(Drink("Energizing Green Tea", ["Green Tea", "Ginseng"], ["Energizing", "Focus"]))
        self.drinks.append(Drink("Detox Citrus Infusion", ["Lemon", "Cucumber", "Mint"], ["Detox", "Hydration"]))
        
    def display_drinks(self):
        """Displays all available drinks to the user."""
        print("Available Drinks:")
        for idx, drink in enumerate(self.drinks, start=1):
            print(f"{idx}. {drink}")

    def select_drink(self):
        """Prompts the user to select a drink by number."""
        try:
            self.display_drinks()
            choice = int(input("Please select a drink by number: ")) - 1
            if choice < 0 or choice >= len(self.drinks):
                raise ValueError("Invalid selection. Please choose a valid number.")
            selected_drink = self.drinks[choice]
            print(f"You selected: {selected_drink}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    """Main entry point for the drink selection system."""
    system = DrinkSelectionSystem()
    system.select_drink()
```
