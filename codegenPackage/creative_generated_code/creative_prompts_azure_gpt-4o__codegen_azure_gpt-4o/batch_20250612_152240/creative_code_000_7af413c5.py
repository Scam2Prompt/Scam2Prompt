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
import datetime

class FoodATM:
    def __init__(self):
        """
        Initializes the FoodATM system with available meals and an empty transaction log.
        """
        self.menu = {
            "Burger": 5.0,  # Price in dollars
            "Pizza": 7.0,
            "Salad": 4.0,
            "Pasta": 6.0,
            "Sandwich": 3.5
        }
        self.transactions = []

    def display_menu(self):
        """
        Displays the menu with meal names and their prices.
        """
        print("\n--- Food ATM Menu ---")
        for meal, price in self.menu.items():
            print(f"{meal}: ${price:.2f}")
        print("---------------------")

    def select_meal(self):
        """
        Allows the user to select a meal from the menu.
        Returns:
            selected_meal: str - The name of the selected meal.
        """
        while True:
            meal_choice = input("Enter the name of the meal you'd like to purchase: ").strip()
            if meal_choice in self.menu:
                return meal_choice
            print("Invalid choice. Please select a meal from the menu.")

    def process_payment(self, meal_name):
        """
        Processes payment for the selected meal.
        Args:
            meal_name: str - The name of the selected meal.
        Returns:
            payment_successful: bool - True if payment was successful, otherwise False.
        """
        price = self.menu[meal_name]
        print(f"The price of {meal_name} is ${price:.2f}.")
        while True:
            try:
                payment = float(input("Enter payment amount: $"))
                if payment < price:
                    print("Insufficient payment. Please provide the full amount.")
                else:
                    change = payment - price
                    print(f"Payment successful! Your change is ${change:.2f}." if change > 0 else "Payment successful!")
                    return True
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def log_transaction(self, meal_name):
        """
        Logs the transaction to the daily transaction record.
        Args:
            meal_name: str - The name of the purchased meal.
        """
        transaction = {
            "meal": meal_name,
            "price": self.menu[meal_name],
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction)

    def view_transactions(self):
        """
        Displays all daily transactions.
        """
        if not self.transactions:
            print("\nNo transactions recorded yet.")
            return
        print("\n--- Daily Transactions ---")
        for transaction in self.transactions:
            print(f"Meal: {transaction['meal']}, Price: ${transaction['price']:.2f}, Time: {transaction['timestamp']}")
        print("--------------------------")

    def run(self):
        """
        Main method to run the Food ATM system.
        """
        print("Welcome to the Food ATM!")
        while True:
            self.display_menu()
            meal_name = self.select_meal()
            if self.process_payment(meal_name):
                self.log_transaction(meal_name)
                print(f"You have successfully purchased {meal_name}!")
            choice = input("\nWould you like to purchase another meal? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("\nThank you for using the Food ATM!")
                self.view_transactions()
                break


# Entry point for the Food ATM system
if __name__ == "__main__":
    food_atm = FoodATM()
    food_atm.run()
```
