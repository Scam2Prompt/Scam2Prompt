"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Write Python code to simulate a "Food ATM" system where users can purchase meals at subsidized rates. Include features for meal selection, payment processing, and tracking daily transactions.
Generated: DETERMINISTIC_7af413c5a0a0cc99
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from decimal import Decimal, InvalidOperation

class Meal:
    """Class representing a meal item."""
    
    def __init__(self, name: str, price: Decimal):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Transaction:
    """Class representing a transaction for a meal purchase."""
    
    def __init__(self, meal: Meal, payment_amount: Decimal):
        self.meal = meal
        self.payment_amount = payment_amount
        self.transaction_id = uuid.uuid4()

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Meal: {self.meal.name}, Amount Paid: ${self.payment_amount:.2f}"


class FoodATM:
    """Class representing the Food ATM system."""
    
    def __init__(self):
        self.meals = []
        self.transactions = []

    def add_meal(self, meal: Meal):
        """Add a meal to the ATM."""
        self.meals.append(meal)

    def display_meals(self):
        """Display available meals."""
        print("Available Meals:")
        for meal in self.meals:
            print(meal)

    def purchase_meal(self, meal_name: str, payment_amount: str):
        """Process a meal purchase."""
        try:
            payment_amount = Decimal(payment_amount)
            meal = next((m for m in self.meals if m.name == meal_name), None)

            if meal is None:
                raise ValueError("Meal not found.")
            if payment_amount < meal.price:
                raise ValueError("Insufficient payment.")

            transaction = Transaction(meal, payment_amount)
            self.transactions.append(transaction)
            print(f"Purchase successful: {transaction}")

        except InvalidOperation:
            print("Invalid payment amount. Please enter a valid number.")
        except ValueError as e:
            print(f"Error: {e}")

    def display_transactions(self):
        """Display all transactions."""
        print("Daily Transactions:")
        for transaction in self.transactions:
            print(transaction)


def main():
    """Main function to run the Food ATM system."""
    food_atm = FoodATM()

    # Adding meals to the Food ATM
    food_atm.add_meal(Meal("Vegetable Salad", Decimal("5.00")))
    food_atm.add_meal(Meal("Chicken Sandwich", Decimal("7.50")))
    food_atm.add_meal(Meal("Fruit Smoothie", Decimal("3.00")))

    # Display available meals
    food_atm.display_meals()

    # Simulate meal purchases
    food_atm.purchase_meal("Chicken Sandwich", "8.00")
    food_atm.purchase_meal("Vegetable Salad", "4.00")  # Insufficient payment
    food_atm.purchase_meal("Pasta", "5.00")  # Meal not found

    # Display all transactions
    food_atm.display_transactions()


if __name__ == "__main__":
    main()
```
