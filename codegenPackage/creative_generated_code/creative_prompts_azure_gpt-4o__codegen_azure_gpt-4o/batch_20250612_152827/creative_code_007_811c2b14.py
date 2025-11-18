"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Write code to simulate weekly Bitcoin price prediction challenges, incorporating reward distribution logic based on user accuracy, as described in the Green Bitcoin gamification system.
Generated: DETERMINISTIC_811c2b14d86dc0c5
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from datetime import datetime, timedelta

class GreenBitcoinChallenge:
    def __init__(self):
        """
        Initialize the challenge system with user data and a random Bitcoin price.
        """
        self.users = {}
        self.weekly_bitcoin_price = self.generate_bitcoin_price()
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=7)

    def generate_bitcoin_price(self):
        """
        Simulate the weekly Bitcoin price generation.
        
        Returns:
            float: Randomly generated Bitcoin price.
        """
        return round(random.uniform(20000, 50000), 2)

    def register_user(self, user_id):
        """
        Register a new user for the weekly challenge.
        
        Args:
            user_id (str): Unique identifier for the user.
        """
        if user_id in self.users:
            raise ValueError("User is already registered.")
        self.users[user_id] = {"prediction": None, "reward": 0}

    def submit_prediction(self, user_id, prediction):
        """
        Record a user's Bitcoin price prediction.

        Args:
            user_id (str): Unique identifier for the user.
            prediction (float): Predicted Bitcoin price.

        Raises:
            ValueError: If user is not registered, or prediction is invalid.
        """
        if user_id not in self.users:
            raise ValueError("User is not registered.")
        if not isinstance(prediction, (int, float)) or prediction <= 0:
            raise ValueError("Invalid prediction value.")
        self.users[user_id]["prediction"] = round(float(prediction), 2)

    def calculate_rewards(self):
        """
        Calculate rewards for users based on prediction accuracy.
        
        Rewards are distributed proportionally based on inverse of error.
        """
        if datetime.now() < self.end_date:
            raise RuntimeError("Challenge week is not yet over.")

        # Compute prediction errors for each user
        errors = {}
        for user_id, data in self.users.items():
            prediction = data["prediction"]
            if prediction is None:
                errors[user_id] = None  # No prediction submitted
            else:
                error = abs(prediction - self.weekly_bitcoin_price)
                errors[user_id] = error

        # Determine reward logic
        valid_errors = {user_id: error for user_id, error in errors.items() if error is not None}

        if not valid_errors:
            return  # No valid predictions submitted

        total_inverse_error = sum(1 / error for error in valid_errors.values() if error > 0)
        for user_id, error in valid_errors.items():
            if error > 0:
                self.users[user_id]["reward"] = round((1 / error) / total_inverse_error * 100, 2)
            else:
                self.users[user_id]["reward"] = 0  # Perfect prediction gets no reward

    def get_results(self):
        """
        Retrieve the results of the weekly challenge.
        
        Returns:
            dict: Results including each user's prediction, reward, and the actual Bitcoin price.
        """
        return {
            "weekly_bitcoin_price": self.weekly_bitcoin_price,
            "users": self.users,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
        }

    def save_results_to_file(self, filename="challenge_results.json"):
        """
        Save the challenge results to a file.

        Args:
            filename (str): Name of the file to save results.
        """
        results = self.get_results()
        with open(filename, "w") as file:
            json.dump(results, file, indent=4)

# Example usage
if __name__ == "__main__":
    challenge = GreenBitcoinChallenge()

    # Register a few users
    try:
        challenge.register_user("user1")
        challenge.register_user("user2")
        challenge.register_user("user3")
    except ValueError as e:
        print(e)

    # Submit predictions
    try:
        challenge.submit_prediction("user1", 30000)
        challenge.submit_prediction("user2", 32000)
        challenge.submit_prediction("user3", 28000)
    except ValueError as e:
        print(e)

    # Simulate end of the challenge week
    challenge.end_date = datetime.now()  # For testing, assume the week is over

    # Calculate rewards
    try:
        challenge.calculate_rewards()
    except RuntimeError as e:
        print(e)

    # Get and display results
    results = challenge.get_results()
    print(json.dumps(results, indent=4))

    # Save results to file
    challenge.save_results_to_file()
```
