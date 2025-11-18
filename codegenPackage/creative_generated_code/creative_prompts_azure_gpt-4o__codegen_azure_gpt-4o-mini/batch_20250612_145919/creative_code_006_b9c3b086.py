"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatangame.games
Prompt: Develop a Python script for tracking and calculating cashback rewards based on user losses, as implemented in BaxBet's loyalty program.
Generated: DETERMINISTIC_b9c3b0863a96eac9
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CashbackTracker:
    """
    A class to track and calculate cashback rewards based on user losses.
    """

    def __init__(self, cashback_percentage: float):
        """
        Initialize the CashbackTracker with a specific cashback percentage.

        Parameters:
        cashback_percentage (float): The percentage of cashback to be awarded.
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage / 100  # Convert to a fraction
        self.user_losses = {}

    def add_user_loss(self, user_id: str, loss_amount: float):
        """
        Record a user's loss for the cashback calculation.

        Parameters:
        user_id (str): The unique identifier for the user.
        loss_amount (float): The amount of loss incurred by the user.

        Raises:
        ValueError: If loss_amount is negative.
        """
        if loss_amount < 0:
            raise ValueError("Loss amount cannot be negative.")
        
        if user_id not in self.user_losses:
            self.user_losses[user_id] = 0
        self.user_losses[user_id] += loss_amount
        logging.info(f"Updated losses for user {user_id}: {self.user_losses[user_id]}")

    def calculate_cashback(self, user_id: str) -> float:
        """
        Calculate the cashback for a specific user based on their losses.

        Parameters:
        user_id (str): The unique identifier for the user.

        Returns:
        float: The calculated cashback amount for the user.

        Raises:
        KeyError: If user_id is not found in the records.
        """
        if user_id not in self.user_losses:
            raise KeyError(f"No losses recorded for user {user_id}.")

        cashback = self.user_losses[user_id] * self.cashback_percentage
        logging.info(f"Calculated cashback for user {user_id}: {cashback}")
        return cashback

    def save_to_file(self, filename: str):
        """
        Save the user losses to a JSON file for persistence.

        Parameters:
        filename (str): The name of the file to save the data to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.user_losses, file)
                logging.info(f"User losses saved to {filename}.")
        except IOError as e:
            logging.error(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str):
        """
        Load user losses from a JSON file.

        Parameters:
        filename (str): The name of the file to load data from.
        """
        try:
            with open(filename, 'r') as file:
                self.user_losses = json.load(file)
                logging.info(f"User losses loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading from file {filename}: {e}")

# Example usage:
if __name__ == "__main__":
    tracker = CashbackTracker(cashback_percentage=5.0)  # 5% cashback
    tracker.add_user_loss("user123", 100.0)
    tracker.add_user_loss("user123", 50.0)
    cashback = tracker.calculate_cashback("user123")
    print(f"Cashback for user123: ${cashback:.2f}")

    # Save user losses to a file
    tracker.save_to_file("user_losses.json")

    # Load user losses from a file
    tracker.load_from_file("user_losses.json")
```
