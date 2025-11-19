"""
Generated Code Metadata:
========================
Original URL: https://dao-magc-alpha.web.app
Prompt: Create a program to manage multiple connected wallets, allowing users to switch wallets, disconnect, and view balances as described on the Magic Eden Launchpad interface.
Generated: DETERMINISTIC_738a826eafc893fb
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wallet_manager.py

class Wallet:
    """Represents a connected wallet."""

    def __init__(self, name, balance):
        """
        Initializes a Wallet object.

        Args:
            name (str): The name of the wallet.
            balance (float): The balance of the wallet.
        """
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}: {self.balance}"


class WalletManager:
    """Manages multiple connected wallets."""

    def __init__(self):
        """
        Initializes a WalletManager object.
        """
        self.wallets = {}
        self.current_wallet = None

    def connect_wallet(self, name, balance):
        """
        Connects a new wallet.

        Args:
            name (str): The name of the wallet.
            balance (float): The balance of the wallet.

        Raises:
            ValueError: If a wallet with the same name already exists.
        """
        if name in self.wallets:
            raise ValueError("Wallet with the same name already exists.")
        self.wallets[name] = Wallet(name, balance)
        print(f"Wallet {name} connected.")

    def disconnect_wallet(self, name):
        """
        Disconnects a wallet.

        Args:
            name (str): The name of the wallet.

        Raises:
            ValueError: If the wallet does not exist.
        """
        if name not in self.wallets:
            raise ValueError("Wallet does not exist.")
        del self.wallets[name]
        if self.current_wallet == name:
            self.current_wallet = None
        print(f"Wallet {name} disconnected.")

    def switch_wallet(self, name):
        """
        Switches to a different wallet.

        Args:
            name (str): The name of the wallet.

        Raises:
            ValueError: If the wallet does not exist.
        """
        if name not in self.wallets:
            raise ValueError("Wallet does not exist.")
        self.current_wallet = name
        print(f"Switched to wallet {name}.")

    def view_balance(self):
        """
        Prints the balance of the current wallet.

        Raises:
            ValueError: If no wallet is currently selected.
        """
        if self.current_wallet is None:
            raise ValueError("No wallet currently selected.")
        wallet = self.wallets[self.current_wallet]
        print(f"Balance: {wallet.balance}")

    def view_all_balances(self):
        """
        Prints the balances of all connected wallets.
        """
        for wallet in self.wallets.values():
            print(wallet)


def main():
    manager = WalletManager()

    while True:
        print("\n1. Connect Wallet")
        print("2. Disconnect Wallet")
        print("3. Switch Wallet")
        print("4. View Balance")
        print("5. View All Balances")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter wallet name: ")
                balance = float(input("Enter wallet balance: "))
                manager.connect_wallet(name, balance)
            elif choice == "2":
                name = input("Enter wallet name: ")
                manager.disconnect_wallet(name)
            elif choice == "3":
                name = input("Enter wallet name: ")
                manager.switch_wallet(name)
            elif choice == "4":
                manager.view_balance()
            elif choice == "5":
                manager.view_all_balances()
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose again.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
