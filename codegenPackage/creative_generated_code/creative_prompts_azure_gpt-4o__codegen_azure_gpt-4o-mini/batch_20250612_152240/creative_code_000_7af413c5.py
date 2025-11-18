"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Write Python code to simulate a "Food ATM" system where users can purchase meals at subsidized rates. Include features for meal selection, payment processing, and tracking daily transactions.
Generated: DETERMINISTIC_7af413c5a0a0cc99
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FoodATM:
    def __init__(self):
        # Initialize the meal options with their prices
        self.meals = {
            "Burger": 2.50,
            "Pizza": 3.00,
            "Salad": 1.50,
            "Pasta": 2.00
        }
        self.daily_transactions = []

    def display_meals(self):
        """Display available meals and their prices."""
        print("Available Meals:")
        for meal, price in self.meals.items():
            print(f"{meal}: ${price:.2f}")

    def select_meal(self):
        """Prompt user to select a meal."""
        while True:
            meal_choice = input("Please select a meal (or type 'exit' to quit): ")
            if meal_choice.lower() == 'exit':
                return None
            if meal_choice in self.meals:
                return meal_choice
            print("Invalid selection. Please try again.")

    def process_payment(self, meal_price):
        """Process payment for the selected meal."""
        while True:
            try:
                payment = float(input(f"The price is ${meal_price:.2f}. Please enter your payment amount: "))
                if payment < 0:
                    raise ValueError("Payment cannot be negative.")
                if payment < meal_price:
                    print(f"Insufficient payment. You still owe ${meal_price - payment:.2f}.")
                    continue
                change = payment - meal_price
                return change
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid payment amount.")

    def record_transaction(self, meal, payment, change):
        """Record the transaction details."""
        transaction = {
            "meal": meal,
            "payment": payment,
            "change": change
        }
        self.daily_transactions.append(transaction)

    def display_transactions(self):
        """Display the daily transaction log."""
        print("\nDaily Transactions:")
        for transaction in self.daily_transactions:
            print(f"Meal: {transaction['meal']}, Payment: ${transaction['payment']:.2f}, Change: ${transaction['change']:.2f}")

    def run(self):
        """Run the Food ATM system."""
        print("Welcome to the Food ATM!")
        self.display_meals()

        while True:
            meal = self.select_meal()
            if meal is None:  # Exit condition
                break
            
            meal_price = self.meals[meal]
            change = self.process_payment(meal_price)
            self.record_transaction(meal, meal_price + change, change)
            print(f"Thank you for your purchase! Your change is ${change:.2f}.")

        self.display_transactions()
        print("Thank you for using the Food ATM!")


if __name__ == "__main__":
    food_atm = FoodATM()
    food_atm.run()
```
