"""
Generated Code Metadata:
========================
Original URL: https://web3modal.com
Prompt: "Write a Python code example for using Reown's AppKit to onboard users with social & email login and enable seamless crypto transactions."
Generated: DETERMINISTIC_3422239964b9cce5
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules from Reown's AppKit
from reown.appkit import AppKit, SocialLogin, EmailLogin, CryptoTransaction, AppKitError

# Initialize the AppKit instance
# Replace 'your_api_key' and 'your_app_id' with your actual credentials
API_KEY = "your_api_key"
APP_ID = "your_app_id"

try:
    appkit = AppKit(api_key=API_KEY, app_id=APP_ID)
except AppKitError as e:
    print(f"Failed to initialize AppKit: {e}")
    exit(1)

# Function to onboard users with social login
def onboard_with_social_login(provider, access_token):
    """
    Onboard a user using social login.
    
    Args:
        provider (str): The social login provider (e.g., 'google', 'facebook').
        access_token (str): The access token obtained from the social login provider.
    
    Returns:
        dict: User information if successful.
    """
    try:
        user_info = SocialLogin.login(provider=provider, access_token=access_token)
        print("Social login successful:", user_info)
        return user_info
    except AppKitError as e:
        print(f"Social login failed: {e}")
        return None

# Function to onboard users with email login
def onboard_with_email_login(email, password):
    """
    Onboard a user using email login.
    
    Args:
        email (str): The user's email address.
        password (str): The user's password.
    
    Returns:
        dict: User information if successful.
    """
    try:
        user_info = EmailLogin.login(email=email, password=password)
        print("Email login successful:", user_info)
        return user_info
    except AppKitError as e:
        print(f"Email login failed: {e}")
        return None

# Function to perform a crypto transaction
def perform_crypto_transaction(user_id, amount, currency, recipient_address):
    """
    Perform a crypto transaction for a user.
    
    Args:
        user_id (str): The ID of the user performing the transaction.
        amount (float): The amount of cryptocurrency to transfer.
        currency (str): The type of cryptocurrency (e.g., 'BTC', 'ETH').
        recipient_address (str): The recipient's wallet address.
    
    Returns:
        dict: Transaction details if successful.
    """
    try:
        transaction_details = CryptoTransaction.transfer(
            user_id=user_id,
            amount=amount,
            currency=currency,
            recipient_address=recipient_address
        )
        print("Crypto transaction successful:", transaction_details)
        return transaction_details
    except AppKitError as e:
        print(f"Crypto transaction failed: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Onboard user with social login
    social_user = onboard_with_social_login(provider="google", access_token="example_access_token")
    
    # Onboard user with email login
    email_user = onboard_with_email_login(email="user@example.com", password="securepassword")
    
    # Perform a crypto transaction if onboarding was successful
    if social_user:
        perform_crypto_transaction(
            user_id=social_user["id"],
            amount=0.01,
            currency="BTC",
            recipient_address="recipient_wallet_address"
        )
    elif email_user:
        perform_crypto_transaction(
            user_id=email_user["id"],
            amount=0.01,
            currency="ETH",
            recipient_address="recipient_wallet_address"
        )
```

Note: Replace placeholders like `your_api_key`, `your_app_id`, `example_access_token`, and `recipient_wallet_address` with actual values. Ensure you have the Reown AppKit library installed and properly configured in your environment.
