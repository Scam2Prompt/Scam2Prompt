"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gnosis-safe.io
Prompt: Write a code example to integrate Safe Smart Accounts with third-party apps using out-of-the-box integrations from the Safe{CORE} SDK.
Generated: DETERMINISTIC_e7310073ac151a50
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import safe_core_sdk
from safe_core_sdk import SafeAccount, IntegrationManager, ApiError

# Initialize the Safe Core SDK
def initialize_sdk(api_key: str):
    """Initialize the Safe Core SDK with the provided API key."""
    try:
        safe_core_sdk.init(api_key)
        print("Safe Core SDK initialized successfully.")
    except ApiError as e:
        print(f"Failed to initialize SDK: {e}")
        raise

# Create a Safe Account
def create_safe_account(account_name: str) -> SafeAccount:
    """Create a new Safe Account."""
    try:
        account = SafeAccount.create(account_name)
        print(f"Safe Account '{account_name}' created successfully.")
        return account
    except ApiError as e:
        print(f"Error creating Safe Account: {e}")
        raise

# Integrate Safe Account with a third-party app
def integrate_with_third_party(account: SafeAccount, app_id: str):
    """Integrate the Safe Account with a third-party application."""
    try:
        integration_manager = IntegrationManager(account)
        integration_manager.add_integration(app_id)
        print(f"Integrated Safe Account with app: {app_id}")
    except ApiError as e:
        print(f"Integration failed: {e}")
        raise

# Main function to demonstrate the integration
if __name__ == "__main__":
    # Define constants
    API_KEY = "YOUR_API_KEY"
    ACCOUNT_NAME = "MySafeAccount"
    APP_ID = "ThirdPartyApp"

    # Execute the process
    try:
        initialize_sdk(API_KEY)
        safe_account = create_safe_account(ACCOUNT_NAME)
        integrate_with_third_party(safe_account, APP_ID)
    except Exception as e:
        print(f"An error occurred: {e}")
```
