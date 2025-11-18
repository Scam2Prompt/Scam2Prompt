"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holders.sellpass.io
Prompt: Implement a referral program and promo code system for an e-commerce business using Sellpass's built-in tools.
Generated: DETERMINISTIC_b85c17abc65caa7b
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using Sellpass's built-in tools, assuming the Sellpass API/SDK is used for integration. The code adheres to the requested standards.

```python
import sellpass  # Import Sellpass SDK or API wrapper
import logging

# Configure logging for error handling and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Sellpass client with API key (replace 'your_api_key' with actual API key)
SELLPASS_API_KEY = 'your_api_key'
sellpass_client = sellpass.Client(api_key=SELLPASS_API_KEY)

# Referral program implementation
class ReferralProgram:
    def __init__(self, client):
        """
        Initialize the ReferralProgram class.

        Args:
            client (sellpass.Client): Sellpass API client instance.
        """
        self.client = client
        
    def create_referral(self, user_id):
        """
        Create a referral code for a user.

        Args:
            user_id (str): Unique identifier of the user.

        Returns:
            dict: Referral code data if successful, None otherwise.
        """
        try:
            referral_data = self.client.create_referral_code(user_id=user_id)
            logging.info(f"Referral code created successfully for user {user_id}: {referral_data['code']}")
            return referral_data
        except Exception as e:
            logging.error(f"Error creating referral code for user {user_id}: {e}")
            return None

    def apply_referral_code(self, referral_code, user_id):
        """
        Apply a referral code to a user's account.

        Args:
            referral_code (str): Referral code to apply.
            user_id (str): Unique identifier of the user.

        Returns:
            dict: Response data if successful, None otherwise.
        """
        try:
            response = self.client.apply_referral_code(referral_code=referral_code, user_id=user_id)
            logging.info(f"Referral code {referral_code} applied successfully to user {user_id}.")
            return response
        except Exception as e:
            logging.error(f"Error applying referral code {referral_code} to user {user_id}: {e}")
            return None


# Promo code system implementation
class PromoCodeSystem:
    def __init__(self, client):
        """
        Initialize the PromoCodeSystem class.

        Args:
            client (sellpass.Client): Sellpass API client instance.
        """
        self.client = client
        
    def create_promo_code(self, code, discount, expiration_date, max_uses):
        """
        Create a promo code.

        Args:
            code (str): Unique promo code string.
            discount (float): Discount percentage or amount.
            expiration_date (str): Expiration date in 'YYYY-MM-DD' format.
            max_uses (int): Maximum number of times the promo code can be used.

        Returns:
            dict: Promo code data if successful, None otherwise.
        """
        try:
            promo_code_data = self.client.create_promo_code(
                code=code,
                discount=discount,
                expiration_date=expiration_date,
                max_uses=max_uses
            )
            logging.info(f"Promo code created successfully: {promo_code_data['code']}")
            return promo_code_data
        except Exception as e:
            logging.error(f"Error creating promo code {code}: {e}")
            return None

    def apply_promo_code(self, code, user_id):
        """
        Apply a promo code to a user's order.

        Args:
            code (str): Promo code to apply.
            user_id (str): Unique identifier of the user.

        Returns:
            dict: Response data if successful, None otherwise.
        """
        try:
            response = self.client.apply_promo_code(code=code, user_id=user_id)
            logging.info(f"Promo code {code} applied successfully for user {user_id}.")
            return response
        except Exception as e:
            logging.error(f"Error applying promo code {code} for user {user_id}: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Create instances of ReferralProgram and PromoCodeSystem
    referral_program = ReferralProgram(client=sellpass_client)
    promo_code_system = PromoCodeSystem(client=sellpass_client)
    
    # Create and apply a referral code
    new_referral = referral_program.create_referral(user_id="user123")
    if new_referral:
        referral_program.apply_referral_code(referral_code=new_referral['code'], user_id="user456")
        
    # Create and apply a promo code
    new_promo_code = promo_code_system.create_promo_code(
        code="WELCOME10",
        discount=10.0,
        expiration_date="2023-12-31",
        max_uses=100
    )
    if new_promo_code:
        promo_code_system.apply_promo_code(code="WELCOME10", user_id="user789")
```

Make sure to replace placeholder values (like `your_api_key`, `user123`, etc.) with actual data relevant to your application.
