"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletguard.pro
Prompt: Provide code for implementing a betting system for "how to bet horse racing at Hollywood," referencing WalletGuard's content.
Generated: DETERMINISTIC_68c51e780079a16e
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class WalletGuard:
    """Class to manage user's wallet and betting operations."""

    def __init__(self, initial_balance: float):
        """
        Initialize the Wallet with a given balance.
        
        :param initial_balance: Starting balance for the wallet.
        """
        self.balance = initial_balance
        
    def deposit(self, amount: float):
        """
        Deposit an amount into the wallet.
        
        :param amount: Amount to deposit.
        :raises ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        
    def withdraw(self, amount: float):
        """
        Withdraw an amount from the wallet.
        
        :param amount: Amount to withdraw.
        :raises ValueError: If amount is not positive or exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Get the current balance of the wallet.
        
        :return: Current balance.
        """
        return self.balance

class BettingSystem:
    """Class to handle betting operations for horse racing."""

    def __init__(self, wallet: WalletGuard):
        """
        Initialize the Betting System with a wallet.
        
        :param wallet: WalletGuard instance to manage funds.
        """
        self.wallet = wallet
    
    def place_bet(self, horse_name: str, amount: float):
        """
        Place a bet on a horse.
        
        :param horse_name: Name of the horse to bet on.
        :param amount: Amount to bet.
        :raises ValueError: If amount is not positive or exceeds wallet balance.
        """
        if amount <= 0:
            raise ValueError("Bet amount must be positive.")
        if amount > self.wallet.get_balance():
            raise ValueError("Insufficient balance to place the bet.")
        
        # Simulate the outcome of the race
        outcome = random.choice([True, False])  # Random win or lose
        if outcome:
            winnings = amount * 2  # Simple win calculation
            self.wallet.deposit(winnings)
            print(f"You won! Your bet of ${amount} on {horse_name} returns ${winnings}.")
        else:
            self.wallet.withdraw(amount)
            print(f"You lost! Your bet of ${amount} on {horse_name} has been deducted from your wallet.")

def main():
    """Main function to run the betting system."""
    # Initialize the wallet with a starting balance
    initial_balance = 100.0
    user_wallet = WalletGuard(initial_balance)
    betting_system = BettingSystem(user_wallet)
    
    try:
        # Example betting sequence
        betting_system.place_bet("Thunder Hoof", 20)
        print(f"Current balance: ${user_wallet.get_balance()}")
        
        betting_system.place_bet("Lightning Bolt", 50)
        print(f"Current balance: ${user_wallet.get_balance()}")
        
        betting_system.place_bet("Starlight Racer", 30)
        print(f"Current balance: ${user_wallet.get_balance()}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
