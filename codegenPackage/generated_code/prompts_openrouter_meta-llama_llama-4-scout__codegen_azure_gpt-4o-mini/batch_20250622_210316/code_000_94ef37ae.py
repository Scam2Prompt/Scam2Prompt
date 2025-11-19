"""
Generated Code Metadata:
========================
Original URL: https://mollinari.com.pl
Prompt: Write a Python script to create a restaurant menu like Mollinari's, including pizza and cocktail options, with prices and daily operating hours.
Generated: DETERMINISTIC_94ef37ae2ad452e6
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MenuItem:
    """Class to represent a menu item with a name, price, and description."""
    
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} - {self.description}"


class RestaurantMenu:
    """Class to represent a restaurant menu containing pizza and cocktail options."""
    
    def __init__(self):
        self.pizzas = []
        self.cocktails = []
        self.operating_hours = "11:00 AM - 11:00 PM"

    def add_pizza(self, name: str, price: float, description: str):
        """Add a pizza to the menu."""
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.pizzas.append(MenuItem(name, price, description))

    def add_cocktail(self, name: str, price: float, description: str):
        """Add a cocktail to the menu."""
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.cocktails.append(MenuItem(name, price, description))

    def display_menu(self):
        """Display the full menu including pizzas and cocktails."""
        print("Welcome to Mollinari's Restaurant Menu")
        print("Operating Hours:", self.operating_hours)
        print("\nPizzas:")
        for pizza in self.pizzas:
            print(pizza)
        
        print("\nCocktails:")
        for cocktail in self.cocktails:
            print(cocktail)


def main():
    """Main function to create and display the restaurant menu."""
    try:
        menu = RestaurantMenu()

        # Adding pizza options
        menu.add_pizza("Margherita", 12.99, "Classic pizza with fresh mozzarella and basil.")
        menu.add_pizza("Pepperoni", 14.99, "Topped with pepperoni and mozzarella cheese.")
        menu.add_pizza("Vegetarian", 13.99, "Loaded with seasonal vegetables and mozzarella.")

        # Adding cocktail options
        menu.add_cocktail("Margarita", 8.50, "Tequila, lime juice, and triple sec.")
        menu.add_cocktail("Mojito", 7.50, "Rum, mint, lime, and soda water.")
        menu.add_cocktail("Old Fashioned", 9.00, "Bourbon, sugar, bitters, and an orange twist.")

        # Display the menu
        menu.display_menu()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
