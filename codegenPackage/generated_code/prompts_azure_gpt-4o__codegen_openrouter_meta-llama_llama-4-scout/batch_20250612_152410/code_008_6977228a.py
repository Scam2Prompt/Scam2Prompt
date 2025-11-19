"""
Generated Code Metadata:
========================
Original URL: https://greenbtcwebb.pages.dev
Prompt: Write a Python function to simulate weekly Bitcoin price prediction challenges, allowing users to input their predictions and calculate rewards based on accuracy.
Generated: DETERMINISTIC_6977228ad390a9fd
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class BitcoinPricePredictor:
    def __init__(self):
        self.predictions = {}
        self.actual_price = None

    def add_prediction(self, user, predicted_price):
        """
        Add a user's prediction for the weekly Bitcoin price.

        Args:
            user (str): The user's name.
            predicted_price (float): The user's predicted Bitcoin price.

        Raises:
            ValueError: If the predicted price is not a positive number.
        """
        if predicted_price <= 0:
            raise ValueError("Predicted price must be a positive number.")
        self.predictions[user] = predicted_price

    def set_actual_price(self, actual_price):
        """
        Set the actual weekly Bitcoin price.

        Args:
            actual_price (float): The actual Bitcoin price.

        Raises:
            ValueError: If the actual price is not a positive number.
        """
        if actual_price <= 0:
            raise ValueError("Actual price must be a positive number.")
        self.actual_price = actual_price

    def calculate_rewards(self):
        """
        Calculate rewards for each user's prediction based on accuracy.

        Returns:
            dict: A dictionary with users as keys and their rewards as values.

        Raises:
            ValueError: If the actual price has not been set.
        """
        if self.actual_price is None:
            raise ValueError("Actual price must be set before calculating rewards.")
        rewards = {}
        for user, predicted_price in self.predictions.items():
            accuracy = abs(1 - (predicted_price / self.actual_price))
            reward = 100 * (1 - accuracy)  # 100% reward for perfect prediction
            rewards[user] = max(reward, 0)  # Ensure reward is not negative
        return rewards


def main():
    predictor = BitcoinPricePredictor()

    while True:
        print("\n1. Add prediction")
        print("2. Set actual price")
        print("3. Calculate rewards")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user = input("Enter your name: ")
            try:
                predicted_price = float(input("Enter your predicted Bitcoin price: "))
                predictor.add_prediction(user, predicted_price)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                actual_price = float(input("Enter the actual Bitcoin price: "))
                predictor.set_actual_price(actual_price)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            try:
                rewards = predictor.calculate_rewards()
                for user, reward in rewards.items():
                    print(f"{user}: {reward}%")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
