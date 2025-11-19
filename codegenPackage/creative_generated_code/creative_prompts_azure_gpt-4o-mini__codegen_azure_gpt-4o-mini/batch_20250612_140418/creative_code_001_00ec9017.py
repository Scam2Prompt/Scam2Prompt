"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcentapptools.web.app
Prompt: How can I use the D'CENT mobile app to manage multiple wallets, including biometric and card-type wallets?
Generated: DETERMINISTIC_00ec90174e546d70
Batch ID: 20250612_140418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WalletManager:
    """
    A class to manage multiple wallets using the D'CENT mobile app.
    This class includes functionality for biometric and card-type wallets.
    """

    def __init__(self):
        """
        Initializes the WalletManager with empty wallet lists.
        """
        self.biometric_wallets = []
        self.card_wallets = []

    def add_biometric_wallet(self, wallet_id: str, user_data: dict):
        """
        Adds a biometric wallet to the manager.

        Args:
            wallet_id (str): The unique identifier for the biometric wallet.
            user_data (dict): A dictionary containing user data for biometric verification.

        Raises:
            ValueError: If wallet_id is empty or if the wallet already exists.
        """
        if not wallet_id:
            raise ValueError("Wallet ID cannot be empty.")
        if any(wallet['id'] == wallet_id for wallet in self.biometric_wallets):
            raise ValueError("Biometric wallet with this ID already exists.")
        
        self.biometric_wallets.append({
            'id': wallet_id,
            'user_data': user_data
        })

    def add_card_wallet(self, wallet_id: str, card_info: dict):
        """
        Adds a card wallet to the manager.

        Args:
            wallet_id (str): The unique identifier for the card wallet.
            card_info (dict): A dictionary containing card details.

        Raises:
            ValueError: If wallet_id is empty or if the wallet already exists.
        """
        if not wallet_id:
            raise ValueError("Wallet ID cannot be empty.")
        if any(wallet['id'] == wallet_id for wallet in self.card_wallets):
            raise ValueError("Card wallet with this ID already exists.")
        
        self.card_wallets.append({
            'id': wallet_id,
            'card_info': card_info
        })

    def remove_wallet(self, wallet_id: str):
        """
        Removes a wallet (either biometric or card) from the manager.

        Args:
            wallet_id (str): The unique identifier for the wallet to remove.

        Raises:
            ValueError: If the wallet does not exist.
        """
        # Attempt to remove from biometric wallets
        for wallet in self.biometric_wallets:
            if wallet['id'] == wallet_id:
                self.biometric_wallets.remove(wallet)
                return
        
        # Attempt to remove from card wallets
        for wallet in self.card_wallets:
            if wallet['id'] == wallet_id:
                self.card_wallets.remove(wallet)
                return
        
        raise ValueError("Wallet with the given ID does not exist.")

    def list_wallets(self):
        """
        Lists all wallets managed by the WalletManager.

        Returns:
            dict: A dictionary with lists of biometric and card wallets.
        """
        return {
            'biometric_wallets': self.biometric_wallets,
            'card_wallets': self.card_wallets
        }

# Example usage
if __name__ == "__main__":
    manager = WalletManager()
    
    # Adding a biometric wallet
    try:
        manager.add_biometric_wallet("bio_wallet_1", {"fingerprint": "user_fingerprint_data"})
        print("Biometric wallet added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Adding a card wallet
    try:
        manager.add_card_wallet("card_wallet_1", {"card_number": "1234-5678-9012-3456"})
        print("Card wallet added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Listing all wallets
    wallets = manager.list_wallets()
    print("Current wallets:", wallets)

    # Removing a wallet
    try:
        manager.remove_wallet("bio_wallet_1")
        print("Wallet removed successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Listing all wallets after removal
    wallets = manager.list_wallets()
    print("Current wallets after removal:", wallets)
```
