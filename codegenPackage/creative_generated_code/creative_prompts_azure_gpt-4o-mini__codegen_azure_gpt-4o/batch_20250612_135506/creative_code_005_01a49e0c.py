"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premiertradeoptions.com
Prompt: What are the steps to create a referral program for a trading platform, inspired by the referral earnings structure of Premier Trade Options?
Generated: DETERMINISTIC_01a49e0c8db0b712
Batch ID: 20250612_135506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program for a Trading Platform
This script implements a referral program inspired by Premier Trade Options.
It includes user account creation, referral code generation, earnings calculation, and error handling.
"""

import uuid
import logging

# Configure logging for error handling and monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='referral_program.log'
)

class ReferralProgram:
    """
    Main class for handling the referral program logic.
    """
    def __init__(self):
        # Dictionary to store user data (in a real app, replace this with a database)
        self.users = {}

    def create_user(self, name, email):
        """
        Create a new user with a unique referral code.
        :param name: str - Name of the user
        :param email: str - Email of the user
        :return: dict - User details
        """
        try:
            if email in self.users:
                raise ValueError("User with this email already exists.")

            referral_code = str(uuid.uuid4())[:8]  # Generate a short, unique referral code
            user = {
                'name': name,
                'email': email,
                'referral_code': referral_code,
                'referred_users': [],
                'earnings': 0.0  # User's earnings from referrals
            }
            self.users[email] = user
            logging.info(f"User created: {email} with referral code: {referral_code}")
            return user
        except Exception as e:
            logging.error(f"Error creating user: {e}")
            raise

    def refer_user(self, referrer_email, referred_name, referred_email):
        """
        Refer a new user and link them to the referrer.
        :param referrer_email: str - Email of the referrer
        :param referred_name: str - Name of the referred user
        :param referred_email: str - Email of the referred user
        :return: dict - Referred user details
        """
        try:
            if referrer_email not in self.users:
                raise ValueError("Referrer does not exist.")
            if referred_email in self.users:
                raise ValueError("User with this email already exists.")

            # Create the referred user
            referred_user = self.create_user(referred_name, referred_email)

            # Link the referred user to the referrer
            self.users[referrer_email]['referred_users'].append(referred_email)

            # Update earnings for the referrer (example: $10 per referral)
            self.users[referrer_email]['earnings'] += 10.0

            logging.info(f"Referral successful: {referrer_email} referred {referred_email}")
            return referred_user
        except Exception as e:
            logging.error(f"Error referring user: {e}")
            raise

    def get_user_details(self, email):
        """
        Get user details by email.
        :param email: str - Email of the user
        :return: dict - User details
        """
        try:
            if email not in self.users:
                raise ValueError("User does not exist.")
            return self.users[email]
        except Exception as e:
            logging.error(f"Error retrieving user details: {e}")
            raise

    def calculate_total_earnings(self):
        """
        Calculate the total earnings from all users in the system.
        :return: float - Total earnings
        """
        try:
            total_earnings = sum(user['earnings'] for user in self.users.values())
            return total_earnings
        except Exception as e:
            logging.error(f"Error calculating total earnings: {e}")
            raise


# Example usage of the ReferralProgram class
if __name__ == "__main__":
    try:
        # Instantiate the referral program
        program = ReferralProgram()

        # Create initial users
        user1 = program.create_user("Alice Johnson", "alice@example.com")
        user2 = program.create_user("Bob Smith", "bob@example.com")

        # Refer new users
        program.refer_user("alice@example.com", "Charlie Brown", "charlie@example.com")
        program.refer_user("bob@example.com", "Dana White", "dana@example.com")

        # Get user details
        alice_details = program.get_user_details("alice@example.com")
        bob_details = program.get_user_details("bob@example.com")

        # Calculate total earnings
        total_earnings = program.calculate_total_earnings()

        # Print results
        print("Alice's Details:", alice_details)
        print("Bob's Details:", bob_details)
        print("Total Earnings:", total_earnings)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
