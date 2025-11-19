"""
Generated Code Metadata:
========================
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Write code to simulate weekly Bitcoin price prediction challenges, incorporating reward distribution logic based on user accuracy, as described in the Green Bitcoin gamification system.
Generated: DETERMINISTIC_811c2b14d86dc0c5
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class User:
    """Represents a user participating in the Green Bitcoin gamification system."""
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.predictions = []
        self.balance = 0

    def make_prediction(self, predicted_price):
        """Records a user's prediction for the weekly Bitcoin price."""
        self.predictions.append(predicted_price)

class GreenBitcoin:
    """Simulates the Green Bitcoin gamification system."""
    def __init__(self):
        self.users = []
        self.actual_price = 0
        self.total_reward = 0

    def add_user(self, user):
        """Adds a user to the system."""
        self.users.append(user)

    def set_actual_price(self, price):
        """Sets the actual weekly Bitcoin price."""
        self.actual_price = price

    def calculate_accuracy(self, predicted_price):
        """Calculates the accuracy of a prediction."""
        if self.actual_price == 0:
            raise ValueError("Actual price has not been set.")
        return abs((predicted_price - self.actual_price) / self.actual_price)

    def distribute_rewards(self):
        """Distributes rewards to users based on their prediction accuracy."""
        if not self.users:
            raise ValueError("No users in the system.")

        total_accuracy = sum(1 - self.calculate_accuracy(user.predictions[-1]) for user in self.users if user.predictions)
        if total_accuracy == 0:
            return  # No rewards if all predictions are inaccurate

        for user in self.users:
            if user.predictions:
                accuracy = 1 - self.calculate_accuracy(user.predictions[-1])
                user_share = (accuracy / total_accuracy) * self.total_reward
                user.balance += user_share
                print(f"User {user.name} earned {user_share} reward.")

    def run_challenge(self, total_reward):
        """Runs a weekly Bitcoin price prediction challenge."""
        self.total_reward = total_reward
        # Simulate users making predictions
        for user in self.users:
            predicted_price = random.uniform(0, 100000)  # Simulate a random prediction
            user.make_prediction(predicted_price)
            print(f"User {user.name} predicted: {predicted_price}")

        # Set the actual Bitcoin price
        self.set_actual_price(random.uniform(0, 100000))

        print(f"Actual Bitcoin price: {self.actual_price}")
        self.distribute_rewards()

def main():
    try:
        gb = GreenBitcoin()
        user1 = User(1, "Alice")
        user2 = User(2, "Bob")

        gb.add_user(user1)
        gb.add_user(user2)

        gb.run_challenge(1000)
        print(f"Alice's balance: {user1.balance}")
        print(f"Bob's balance: {user2.balance}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
