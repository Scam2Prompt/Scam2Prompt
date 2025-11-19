"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wieneraidog.pages.dev
Prompt: What are the best practices for launching a presale for an AI-based token like WienerAI?
Generated: DETERMINISTIC_538b9a33b38186f1
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PresaleManager:
    def __init__(self, token_name, presale_start, presale_end, target_amount, min_investment):
        """
        Initializes the PresaleManager with relevant parameters.
        
        :param token_name: Name of the token
        :param presale_start: Start datetime of the presale
        :param presale_end: End datetime of the presale
        :param target_amount: Target amount to raise in the presale
        :param min_investment: Minimum investment allowed per participant
        """
        self.token_name = token_name
        self.presale_start = presale_start
        self.presale_end = presale_end
        self.target_amount = target_amount
        self.min_investment = min_investment
        self.total_raised = 0
        self.participants = {}

    def validate_investment(self, amount):
        """
        Validates the investment amount.
        
        :param amount: Amount to invest
        :raises ValueError: If amount is less than minimum investment
        """
        if amount < self.min_investment:
            raise ValueError(f"Investment must be at least {self.min_investment}.")

    def participate(self, participant_id, amount):
        """
        Processes a participation in the presale.
        
        :param participant_id: Identifier of the participant
        :param amount: Amount to invest
        """
        # Check if presale is active
        current_time = datetime.now()
        if not self.presale_start <= current_time <= self.presale_end:
            logging.error("Presale is not active.")
            raise Exception("Presale is not active.")

        # Validate investment
        try:
            self.validate_investment(amount)
        except ValueError as ve:
            logging.error(f"Validation error: {ve}")
            raise

        # Update total raised and participant record
        self.total_raised += amount
        self.participants[participant_id] = self.participants.get(participant_id, 0) + amount
        logging.info(f"Participant {participant_id} invested {amount}. Total raised: {self.total_raised}")

        # Check if target has been reached
        if self.total_raised >= self.target_amount:
            logging.info("Target amount reached! Presale is now closed.")
            self.close_presale()

    def close_presale(self):
        """
        Closes the presale and logs the final details.
        """
        logging.info(f"Presale for {self.token_name} has ended. Total raised: {self.total_raised}. Participants: {len(self.participants)}")

# Example usage
if __name__ == "__main__":
    presale_start = datetime.now() + timedelta(seconds=10)  # Presale starts in 10 seconds
    presale_end = presale_start + timedelta(minutes=30)     # Presale lasts for 30 minutes
    target_amount = 1000000  # Target amount to raise
    min_investment = 100     # Minimum investment per participant

    presale_manager = PresaleManager("WienerAI", presale_start, presale_end, target_amount, min_investment)

    # Simulate investments (in a real application, these would come from user input)
    try:
        presale_manager.participate("user1", 150)
        presale_manager.participate("user2", 200)
        presale_manager.participate("user3", 50)  # Will raise validation error
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
