"""
Generated Code Metadata:
========================
Original URL: https://locinews.com
Prompt: Write code to implement a fraud detection system for a betting platform, inspired by Bet88's warnings about fraudulent websites.
Generated: DETERMINISTIC_f8f6ae329805fd90
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fraud_detection_system.py

import logging
import re
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FraudDetectionSystem:
    """
    A system to detect potential fraudulent activities on a betting platform.
    """

    def __init__(self, suspicious_keywords: List[str], max_bet_amount: float):
        """
        Initialize the fraud detection system.

        Args:
        - suspicious_keywords (List[str]): A list of keywords that may indicate fraudulent activity.
        - max_bet_amount (float): The maximum allowed bet amount.
        """
        self.suspicious_keywords = suspicious_keywords
        self.max_bet_amount = max_bet_amount

    def check_for_suspicious_activity(self, user_data: Dict[str, str]) -> bool:
        """
        Check if a user's activity is suspicious.

        Args:
        - user_data (Dict[str, str]): A dictionary containing user data, including their username, email, and bet details.

        Returns:
        - bool: True if the user's activity is suspicious, False otherwise.
        """
        # Check for suspicious keywords in user data
        for keyword in self.suspicious_keywords:
            if re.search(keyword, user_data['username'] + user_data['email'] + user_data['bet_details']):
                logger.warning("Suspicious keyword detected in user data.")
                return True

        # Check for excessive bet amounts
        try:
            bet_amount = float(user_data['bet_amount'])
            if bet_amount > self.max_bet_amount:
                logger.warning("Excessive bet amount detected.")
                return True
        except ValueError:
            logger.error("Invalid bet amount.")

        return False

    def validate_user_input(self, user_data: Dict[str, str]) -> bool:
        """
        Validate user input data.

        Args:
        - user_data (Dict[str, str]): A dictionary containing user data.

        Returns:
        - bool: True if the user input is valid, False otherwise.
        """
        required_fields = ['username', 'email', 'bet_details', 'bet_amount']
        for field in required_fields:
            if field not in user_data:
                logger.error("Missing required field: %s", field)
                return False

        # Validate email format
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, user_data['email']):
            logger.error("Invalid email format.")
            return False

        return True


def main():
    suspicious_keywords = ['suspicious', 'fraudulent', 'malicious']
    max_bet_amount = 1000.0

    fraud_detection_system = FraudDetectionSystem(suspicious_keywords, max_bet_amount)

    # Example user data
    user_data = {
        'username': 'john_doe',
        'email': 'john.doe@example.com',
        'bet_details': 'bet on match 1',
        'bet_amount': '500.0'
    }

    if fraud_detection_system.validate_user_input(user_data):
        if fraud_detection_system.check_for_suspicious_activity(user_data):
            print("Suspicious activity detected.")
        else:
            print("User activity appears to be legitimate.")
    else:
        print("Invalid user input.")


if __name__ == "__main__":
    main()
```
