"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartboardfaredscale.pages.dev
Prompt: How can I implement a wallet activation process for users facing issues, as outlined in the decentralized Dapps content?
Generated: DETERMINISTIC_3e922bf91c3a6ba2
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import hashlib
import uuid
from typing import Dict, Any, Optional

class WalletActivationError(Exception):
    """Custom exception for wallet activation errors."""
    pass

class WalletActivationService:
    """Service for handling wallet activation processes."""

    def __init__(self):
        self.wallets: Dict[str, Dict[str, Any]] = {}
    
    def generate_activation_code(self) -> str:
        """Generates a unique activation code for the wallet."""
        return str(uuid.uuid4())
    
    def create_wallet(self, user_id: str) -> str:
        """Creates a new wallet for a user and stores it in the service.
        
        Args:
            user_id (str): The ID of the user for whom the wallet is created.
        
        Returns:
            str: The activation code for the new wallet.
        """
        if user_id in self.wallets:
            raise WalletActivationError("Wallet already exists for this user.")
        
        activation_code = self.generate_activation_code()
        wallet_data = {
            "user_id": user_id,
            "activation_code": activation_code,
            "activated": False,
            "balance": 0.0  # Initialize balance
        }
        
        self.wallets[user_id] = wallet_data
        return activation_code

    def activate_wallet(self, user_id: str, activation_code: str) -> bool:
        """Activates the wallet for a user using the provided activation code.
        
        Args:
            user_id (str): The ID of the user whose wallet is to be activated.
            activation_code (str): The activation code for the wallet.
        
        Returns:
            bool: True if activation was successful, False otherwise.
        
        Raises:
            WalletActivationError: If the user does not exist or activation code is invalid.
        """
        if user_id not in self.wallets:
            raise WalletActivationError("No wallet found for this user.")
        
        wallet = self.wallets[user_id]
        if wallet['activation_code'] != activation_code:
            raise WalletActivationError("Invalid activation code.")
        
        wallet['activated'] = True
        return True

    def get_wallet_info(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves wallet information for a user.
        
        Args:
            user_id (str): The ID of the user whose wallet info is requested.
        
        Returns:
            Optional[Dict[str, Any]]: Wallet information or None if not found.
        """
        return self.wallets.get(user_id)

# Example usage:
if __name__ == "__main__":
    service = WalletActivationService()
    
    try:
        # Create a wallet for a user
        user_id = "user123"
        activation_code = service.create_wallet(user_id)
        print(f"Created wallet for {user_id} with activation code: {activation_code}")
        
        # Activate the wallet
        if service.activate_wallet(user_id, activation_code):
            print(f"Wallet for {user_id} activated successfully.")
        
        # Retrieve wallet info
        wallet_info = service.get_wallet_info(user_id)
        print("Wallet Info:", json.dumps(wallet_info, indent=2))

    except WalletActivationError as e:
        print(f"Error: {e}")
```
