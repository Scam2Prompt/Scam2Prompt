"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-st.pages.dev
Prompt: Describe how to set up a weekly challenge for predicting Bitcoin prices using the Green Bitcoin staking mechanics and provide a sample code for tracking user predictions.
Generated: DETERMINISTIC_3acd9488edc9559b
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class BitcoinChallenge:
    """
    A class to set up and manage a weekly Bitcoin price prediction challenge
    using Green Bitcoin staking mechanics.
    """

    def __init__(self):
        """
        Initializes the challenge with an empty list of user predictions.
        """
        self.user_predictions = []  # List to store user predictions
        self.start_date = datetime.datetime.now()  # Start date of the challenge
        self.end_date = self.start_date + datetime.timedelta(days=7)  # Challenge duration is 7 days

    def add_prediction(self, username, predicted_price):
        """
        Adds a user's prediction to the challenge.

        Args:
            username (str): The name of the user.
            predicted_price (float): The user's predicted Bitcoin price.

        Returns:
            dict: A confirmation message or error response.
        """
        # Validate input types
        if not isinstance(username, str) or not isinstance(predicted_price, (int, float)):
            return {"error": "Invalid input types. Username must be a string and predicted_price must be numeric."}

        # Ensure challenge is still active
        if datetime.datetime.now() > self.end_date:
            return {"error": "The challenge has ended. Predictions are no longer accepted."}

        # Add prediction
        self.user_predictions.append({
            "username": username,
            "predicted_price": predicted_price,
            "timestamp": datetime.datetime.now().isoformat()
        })
        return {"message": f"Prediction added successfully for user {username}."}

    def get_predictions(self):
        """
        Retrieves all user predictions.

        Returns:
            list: A list of all user predictions.
        """
        return self.user_predictions

    def save_predictions_to_file(self, filename="user_predictions.json"):
        """
        Saves all user predictions to a JSON file.

        Args:
            filename (str): The name of the file to save predictions to (default: "user_predictions.json").

        Returns:
            dict: A confirmation message or error response.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.user_predictions, file, indent=4)
            return {"message": f"Predictions successfully saved to {filename}."}
        except Exception as e:
            return {"error": str(e)}

    def get_winner(self, actual_bitcoin_price):
        """
        Determines the winner of the challenge based on the closest prediction to the actual Bitcoin price.

        Args:
            actual_bitcoin_price (float): The actual Bitcoin price at the end of the challenge.

        Returns:
            dict: A dictionary containing the winner's username and their prediction.
        """
        if not self.user_predictions:
            return {"error": "No predictions available to determine a winner."}

        # Find the closest prediction
        winner = min(self.user_predictions, key=lambda p: abs(p["predicted_price"] - actual_bitcoin_price))
        return {
            "winner": winner["username"],
            "predicted_price": winner["predicted_price"],
            "actual_price": actual_bitcoin_price
        }


# Example usage of BitcoinChallenge class
if __name__ == "__main__":
    challenge = BitcoinChallenge()

    # Add some user predictions
    print(challenge.add_prediction("Alice", 50000.5))
    print(challenge.add_prediction("Bob", 48000))
    print(challenge.add_prediction("Charlie", 50500.7))

    # Save predictions to file
    print(challenge.save_predictions_to_file())

    # Get and print all user predictions
    print(challenge.get_predictions())

    # Determine the winner based on the actual Bitcoin price
    actual_price = 50020  # Example actual price
    print(challenge.get_winner(actual_price))
```
