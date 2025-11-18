"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epiccoin-miners.ltd
Prompt: Generate a Python script that simulates instant withdrawals and calculates referral bonuses based on the 10% referral program described on epiccoin-miners.ltd.
Generated: DETERMINISTIC_9a072c1fce118dd7
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class WithdrawalError(Exception):
    """Custom exception for withdrawal errors."""
    pass

class ReferralBonusError(Exception):
    """Custom exception for referral bonus errors."""
    pass

class EpicCoinMiners:
    def __init__(self):
        # Initialize the balance and referral bonuses
        self.user_balance = 1000.00  # Example balance in USD
        self.referral_bonus = 0.00
    
    def withdraw(self, amount):
        """
        Simulates an instant withdrawal.

        :param amount: The amount to withdraw (float).
        :raises WithdrawalError: If the withdrawal amount exceeds the user's balance.
        """
        if amount <= 0:
            raise WithdrawalError("Withdrawal amount must be greater than zero.")
        
        if amount > self.user_balance:
            raise WithdrawalError("Insufficient funds for withdrawal.")
        
        self.user_balance -= amount
        print(f"Withdrawal successful. You withdrew ${amount:.2f}.")
        print(f"Remaining balance: ${self.user_balance:.2f}")

    def calculate_referral_bonus(self, referral_amount):
        """
        Calculates the referral bonus based on a 10% referral program.

        :param referral_amount: The amount earned by a referral (float).
        :raises ReferralBonusError: If the referral amount is negative.
        """
        if referral_amount < 0:
            raise ReferralBonusError("Referral amount cannot be negative.")
        
        bonus = referral_amount * 0.10
        self.referral_bonus += bonus
        print(f"Referral bonus of ${bonus:.2f} added.")
        print(f"Total referral bonus: ${self.referral_bonus:.2f}")

def main():
    """
    Main function to demonstrate EpicCoinMiners functionality.
    """
    miner = EpicCoinMiners()

    # Simulate withdrawals
    try:
        print("Attempting withdrawal of $200...")
        miner.withdraw(200)
        
        print("\nAttempting withdrawal of $900...")
        miner.withdraw(900)  # This will raise an exception
        
    except WithdrawalError as e:
        print(f"Error during withdrawal: {e}")
    
    # Simulate referral bonuses
    try:
        print("\nCalculating referral bonus for $500 earned by a referral...")
        miner.calculate_referral_bonus(500)
        
        print("\nCalculating referral bonus for -$100 (invalid referral amount)...")
        miner.calculate_referral_bonus(-100)  # This will raise an exception
        
    except ReferralBonusError as e:
        print(f"Error during referral bonus calculation: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
