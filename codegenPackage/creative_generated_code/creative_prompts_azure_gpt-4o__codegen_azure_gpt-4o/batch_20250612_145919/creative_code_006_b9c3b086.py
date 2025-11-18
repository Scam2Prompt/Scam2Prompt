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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class CashbackTracker:
    """
    A class to calculate and track cashback rewards based on user losses in BaxBet's loyalty program.
    """

    def __init__(self, cashback_rate: float):
        """
        Initialize the cashback tracker.
        
        Args:
            cashback_rate (float): The cashback rate as a decimal (e.g., 0.05 for 5%).
        """
        if not (0 <= cashback_rate <= 1):
            raise ValueError("Cashback rate must be between 0 and 1.")
        self.cashback_rate = cashback_rate
        self.user_losses = {}  # Dictionary to track user losses {user_id: total_loss}

    def record_loss(self, user_id: str, amount: float):
        """
        Record a loss for a specific user.
        
        Args:
            user_id (str): The ID of the user.
            amount (float): The loss amount to record.
        
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Loss amount cannot be negative.")
        
        # Update user's total loss
        if user_id in self.user_losses:
            self.user_losses[user_id] += amount
        else:
            self.user_losses[user_id] = amount
        
        logging.info(f"Recorded loss of ${amount:.2f} for user {user_id}. Total loss: ${self.user_losses[user_id]:.2f}.")

    def calculate_cashback(self, user_id: str) -> float:
        """
        Calculate the cashback reward for a specific user.
        
        Args:
            user_id (str): The ID of the user.
        
        Returns:
            float: The cashback amount.
        
        Raises:
            KeyError: If the user does not exist.
        """
        if user_id not in self.user_losses:
            raise KeyError(f"User ID {user_id} not found.")
        
        cashback = self.user_losses[user_id] * self.cashback_rate
        logging.info(f"Cashback for user {user_id}: ${cashback:.2f}.")
        return cashback

    def reset_user_losses(self, user_id: str):
        """
        Reset the total losses for a specific user.
        
        Args:
            user_id (str): The ID of the user.
        
        Raises:
            KeyError: If the user does not exist.
        """
        if user_id not in self.user_losses:
            raise KeyError(f"User ID {user_id} not found.")
        
        self.user_losses[user_id] = 0
        logging.info(f"Reset losses for user {user_id}.")

    def get_user_total_loss(self, user_id: str) -> float:
        """
        Get the total loss for a specific user.
        
        Args:
            user_id (str): The ID of the user.
        
        Returns:
            float: The user's total loss.
        
        Raises:
            KeyError: If the user does not exist.
        """
        if user_id not in self.user_losses:
            raise KeyError(f"User ID {user_id} not found.")
        
        return self.user_losses[user_id]


# Example usage
if __name__ == "__main__":
    try:
        cashback_tracker = CashbackTracker(cashback_rate=0.05)  # 5% cashback rate
        cashback_tracker.record_loss("user123", 100)
        cashback_tracker.record_loss("user123", 50)
        cashback_tracker.record_loss("user456", 200)
        
        print(f"User123 cashback: ${cashback_tracker.calculate_cashback('user123'):.2f}")
        print(f"User456 cashback: ${cashback_tracker.calculate_cashback('user456'):.2f}")
        
        cashback_tracker.reset_user_losses("user123")
        print(f"User123 total loss after reset: ${cashback_tracker.get_user_total_loss('user123'):.2f}")
    
    except (ValueError, KeyError) as e:
        logging.error(f"An error occurred: {e}")
```
