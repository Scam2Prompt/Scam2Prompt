"""
Generated Code Metadata:
========================
Original URL: https://bscbhn.com
Prompt: "Generate code for a simple digital wallet transaction system that allows users to recargar, retirar, and transferir funds."
Generated: DETERMINISTIC_d7e6e9f7643f3070
Batch ID: 20250622_212115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_wallet.py

class DigitalWallet:
    """
    A simple digital wallet system that allows users to:
    - Recargar (add funds)
    - Retirar (withdraw funds)
    - Transferir (transfer funds to another wallet)
    """

    def __init__(self, owner_name):
        """
        Initialize the wallet with an owner and a balance of 0.
        :param owner_name: Name of the wallet owner.
        """
        self.owner_name = owner_name
        self.balance = 0.0

    def recargar(self, amount):
        """
        Add funds to the wallet.
        :param amount: Amount to add (must be positive).
        :raises ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Amount to recargar must be positive.")
        self.balance += amount
        print(f"{amount:.2f} added to {self.owner_name}'s wallet. New balance: {self.balance:.2f}")

    def retirar(self, amount):
        """
        Withdraw funds from the wallet.
        :param amount: Amount to withdraw (must be positive and <= balance).
        :raises ValueError: If the amount is not positive or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError("Amount to retirar must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds to retirar.")
        self.balance -= amount
        print(f"{amount:.2f} withdrawn from {self.owner_name}'s wallet. New balance: {self.balance:.2f}")

    def transferir(self, recipient_wallet, amount):
        """
        Transfer funds to another wallet.
        :param recipient_wallet: The wallet to transfer funds to (must be a DigitalWallet instance).
        :param amount: Amount to transfer (must be positive and <= balance).
        :raises ValueError: If the amount is not positive or exceeds the balance.
        :raises TypeError: If the recipient_wallet is not a DigitalWallet instance.
        """
        if not isinstance(recipient_wallet, DigitalWallet):
            raise TypeError("Recipient wallet must be a DigitalWallet instance.")
        if amount <= 0:
            raise ValueError("Amount to transferir must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds to transferir.")
        self.balance -= amount
        recipient_wallet.recargar(amount)  # Use recargar to add funds to recipient
        print(f"{amount:.2f} transferred from {self.owner_name}'s wallet to {recipient_wallet.owner_name}'s wallet.")

# Example usage
if __name__ == "__main__":
    try:
        # Create wallets
        wallet1 = DigitalWallet("Alice")
        wallet2 = DigitalWallet("Bob")

        # Perform transactions
        wallet1.recargar(100.0)  # Add funds to Alice's wallet
        wallet1.retirar(30.0)    # Withdraw funds from Alice's wallet
        wallet1.transferir(wallet2, 50.0)  # Transfer funds from Alice to Bob

        # Check final balances
        print(f"Alice's final balance: {wallet1.balance:.2f}")
        print(f"Bob's final balance: {wallet2.balance:.2f}")

    except Exception as e:
        print(f"Error: {e}")
```
