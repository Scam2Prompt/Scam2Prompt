"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltokenburner.com
Prompt: Provide a step-by-step guide to implement a feature that allows users to switch between wallets when using SOLTOKENBURNER.
Generated: DETERMINISTIC_ec194116bf4c7db3
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# wallet_switcher.py

import logging

class WalletSwitcher:
    """
    A class to handle switching between different wallets for the SOLTOKENBURNER application.
    """

    def __init__(self):
        """Initializes the WalletSwitcher with an empty wallet list and no active wallet."""
        self.wallets = []  # List to store user wallets
        self.active_wallet = None  # Currently active wallet

    def add_wallet(self, wallet_address: str) -> None:
        """
        Adds a new wallet to the list of wallets.

        Args:
            wallet_address (str): The address of the wallet to be added.

        Raises:
            ValueError: If the wallet address is already in the list.
        """
        if wallet_address in self.wallets:
            logging.error(f"Wallet {wallet_address} already exists.")
            raise ValueError("Wallet address already exists.")
        
        self.wallets.append(wallet_address)
        logging.info(f"Wallet {wallet_address} added successfully.")

    def remove_wallet(self, wallet_address: str) -> None:
        """
        Removes a wallet from the list of wallets.

        Args:
            wallet_address (str): The address of the wallet to be removed.

        Raises:
            ValueError: If the wallet address is not found in the list.
        """
        try:
            self.wallets.remove(wallet_address)
            logging.info(f"Wallet {wallet_address} removed successfully.")
        except ValueError:
            logging.error(f"Wallet {wallet_address} not found.")
            raise ValueError("Wallet address not found.")

    def switch_wallet(self, wallet_address: str) -> None:
        """
        Switches the active wallet to the specified wallet address.

        Args:
            wallet_address (str): The address of the wallet to switch to.

        Raises:
            ValueError: If the wallet address is not found in the list.
        """
        if wallet_address not in self.wallets:
            logging.error(f"Wallet {wallet_address} not found.")
            raise ValueError("Wallet address not found in the list.")

        self.active_wallet = wallet_address
        logging.info(f"Switched to wallet {wallet_address}.")

    def get_active_wallet(self) -> str:
        """
        Returns the currently active wallet.

        Returns:
            str: The address of the currently active wallet.
        
        Raises:
            RuntimeError: If no active wallet has been set.
        """
        if self.active_wallet is None:
            logging.error("No active wallet set.")
            raise RuntimeError("No active wallet set.")
        
        return self.active_wallet

    def get_wallets(self) -> list:
        """
        Returns the list of all wallets.

        Returns:
            list: A list of wallet addresses.
        """
        return self.wallets


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Example usage of the WalletSwitcher class
    wallet_switcher = WalletSwitcher()

    # Adding wallets
    try:
        wallet_switcher.add_wallet("wallet1")
        wallet_switcher.add_wallet("wallet2")
    except ValueError as e:
        logging.error(e)

    # Switching wallets
    try:
        wallet_switcher.switch_wallet("wallet1")
        active_wallet = wallet_switcher.get_active_wallet()
        logging.info(f"Active wallet is: {active_wallet}")
    except ValueError as e:
        logging.error(e)
    except RuntimeError as e:
        logging.error(e)

    # Removing a wallet
    try:
        wallet_switcher.remove_wallet("wallet2")
    except ValueError as e:
        logging.error(e)

    # Check remaining wallets
    logging.info(f"Remaining wallets: {wallet_switcher.get_wallets()}")
```
