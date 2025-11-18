"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://authorization-b6o.pages.dev
Prompt: Write code to calculate a 10% service commission after successfully matching seed phrases to wallets with a balance, as described in the SeedAim service model.
Generated: DETERMINISTIC_d6bd8b0d56f2849d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SeedAimService:
    """
    A service to calculate a 10% commission based on matched seed phrases 
    to wallets that have a balance.
    """

    def __init__(self):
        self.wallets = {}  # Store wallet addresses and their balances

    def add_wallet(self, address: str, balance: float) -> None:
        """
        Add a wallet to the service with a specified balance.

        :param address: The wallet address.
        :param balance: The initial balance of the wallet.
        :raises ValueError: If the balance is negative.
        """
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        
        self.wallets[address] = balance

    def calculate_commission(self, matched_wallets: list) -> float:
        """
        Calculate the total service commission for matched wallets.

        :param matched_wallets: A list of wallet addresses that matched seed phrases.
        :return: The total commission calculated as 10% of the total balance of matched wallets.
        :raises ValueError: If no wallets are provided.
        """
        if not matched_wallets:
            raise ValueError("No matched wallets provided.")

        total_balance = 0.0

        for wallet in matched_wallets:
            if wallet in self.wallets:
                total_balance += self.wallets[wallet]
            else:
                raise ValueError(f"Wallet {wallet} not found in the service.")
        
        commission = total_balance * 0.10
        return commission

# Example usage
if __name__ == "__main__":
    service = SeedAimService()
    
    # Adding wallets
    service.add_wallet("wallet_1", 100.0)
    service.add_wallet("wallet_2", 200.0)
    
    # List of matched wallets
    matched_wallets = ["wallet_1", "wallet_2"]

    try:
        commission = service.calculate_commission(matched_wallets)
        print(f"Total service commission: ${commission:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
