"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autobux.top
Prompt: What are the best practices for creating a referral system with 70% commission like the one on AUTOBUX?
Generated: DETERMINISTIC_a489a2a4445ef6ed
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, production-ready implementation of a referral system with a 70% commission model in Python. It follows best practices, includes error handling, and is syntactically correct.

```python
import uuid
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReferralSystem:
    """
    A class to represent a referral system with a 70% commission model.
    """

    def __init__(self):
        """
        Initializes the referral system with an empty user and referral database.
        """
        self.users = {}  # Stores user details as {user_id: {'balance': 0, 'referred_users': []}}
        self.referrals = {}  # Maps referral codes to user IDs

    def create_user(self):
        """
        Creates a new user and assigns a unique referral code.
        
        Returns:
            dict: Information about the newly created user (user_id and referral_code).
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        referral_code = str(uuid.uuid4())[:8]  # Generate a short unique referral code
        
        # Initialize the user in the database
        self.users[user_id] = {
            'balance': 0,
            'referred_users': []
        }
        self.referrals[referral_code] = user_id

        logging.info(f"User created with ID: {user_id} and Referral Code: {referral_code}")
        
        return {'user_id': user_id, 'referral_code': referral_code}

    def refer_user(self, referral_code):
        """
        Refers a new user using the provided referral code.
        If the referral code is valid, the referrer earns a commission.

        Args:
            referral_code (str): The referral code of the referring user.

        Returns:
            dict: Information about the newly referred user.
        """
        if referral_code not in self.referrals:
            logging.error("Invalid referral code provided.")
            raise ValueError("Invalid referral code. Please check and try again.")

        # Create the new user
        new_user = self.create_user()
        referrer_id = self.referrals[referral_code]

        # Update the referrer's data
        self.users[referrer_id]['referred_users'].append(new_user['user_id'])
        self.users[referrer_id]['balance'] += self.calculate_commission()

        logging.info(f"Referral successful. Referrer ID: {referrer_id} earned commission.")
        
        return new_user

    def calculate_commission(self):
        """
        Calculates the commission for a referral.
        
        Returns:
            float: The commission amount (70% of a fixed $100 for simplicity).
        """
        FIXED_AMOUNT = 100.00
        COMMISSION_RATE = 0.70
        return FIXED_AMOUNT * COMMISSION_RATE

    def get_user_details(self, user_id):
        """
        Retrieves the details of a user by their user ID.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            dict: The user's details (balance and referred users).
        """
        if user_id not in self.users:
            logging.error("User ID not found.")
            raise ValueError("User ID not found. Please check and try again.")

        return self.users[user_id]


# Example usage
if __name__ == "__main__":
    try:
        referral_system = ReferralSystem()

        # Create a main user
        main_user = referral_system.create_user()
        print("Main User:", main_user)

        # Refer new users using the main user's referral code
        referred_user_1 = referral_system.refer_user(main_user['referral_code'])
        print("Referred User 1:", referred_user_1)

        referred_user_2 = referral_system.refer_user(main_user['referral_code'])
        print("Referred User 2:", referred_user_2)

        # Get main user's details after earning commissions
        main_user_details = referral_system.get_user_details(main_user['user_id'])
        print("Main User Details:", main_user_details)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

This Python script implements a simple referral system, ensuring clean code design, error handling, and adherence to best practices. You can extend or customize this code to fit specific requirements.
