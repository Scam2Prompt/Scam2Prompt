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
from typing import Dict, List, Any

class PredictionChallenge:
    def __init__(self):
        # Initialize a dictionary to hold user predictions
        self.user_predictions: Dict[str, List[Dict[str, Any]]] = {}
        self.challenge_start_date = datetime.datetime.now()
        self.challenge_end_date = self.challenge_start_date + datetime.timedelta(weeks=1)

    def add_prediction(self, username: str, prediction: float) -> None:
        """
        Add a user's prediction to the challenge.

        :param username: The name of the user making the prediction.
        :param prediction: The predicted Bitcoin price.
        :raises ValueError: If the prediction is not a positive number.
        """
        if prediction <= 0:
            raise ValueError("Prediction must be a positive number.")
        
        # Store the prediction along with the timestamp
        prediction_entry = {
            'timestamp': datetime.datetime.now(),
            'prediction': prediction
        }
        
        # Initialize user entry if it doesn't exist
        if username not in self.user_predictions:
            self.user_predictions[username] = []
        
        self.user_predictions[username].append(prediction_entry)

    def get_predictions(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieve all user predictions.

        :return: A dictionary of users and their predictions.
        """
        return self.user_predictions

    def get_challenge_status(self) -> str:
        """
        Determine if the challenge is ongoing, completed, or not started.

        :return: A string representing the current status of the challenge.
        """
        now = datetime.datetime.now()
        if now < self.challenge_start_date:
            return "Challenge not started."
        elif now > self.challenge_end_date:
            return "Challenge completed."
        else:
            return "Challenge ongoing."

# Sample usage
if __name__ == "__main__":
    challenge = PredictionChallenge()
    
    # Simulating user predictions
    try:
        challenge.add_prediction("user1", 60000.0)
        challenge.add_prediction("user2", 61000.5)

        # Output all predictions
        print("User Predictions:", challenge.get_predictions())

        # Check challenge status
        print("Challenge Status:", challenge.get_challenge_status())
    except ValueError as e:
        print("Error occurred:", e)
```
