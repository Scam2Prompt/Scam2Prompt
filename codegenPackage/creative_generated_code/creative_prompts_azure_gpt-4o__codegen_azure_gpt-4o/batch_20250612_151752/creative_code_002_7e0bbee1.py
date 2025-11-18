"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealvsmetamask.com
Prompt: Create a script to calculate cashback rewards for purchases using Zeal Wallet, factoring in the user's GNO token holdings to determine the rate (0-4%).
Generated: DETERMINISTIC_7e0bbee18c85b542
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CashbackCalculator:
    """
    A class to calculate cashback rewards based on purchases
    and GNO token holdings in Zeal Wallet.
    """
    
    def __init__(self, gno_balance):
        """
        Initialize the cashback calculator with the user's GNO token balance.
        
        Args:
            gno_balance (float): The user's GNO token balance.
        """
        self.gno_balance = gno_balance
        self.cashback_rate = self._determine_cashback_rate()
    
    def _determine_cashback_rate(self):
        """
        Determine the cashback rate based on the GNO balance.
        
        Returns:
            float: The cashback rate (0-4%).
        """
        if self.gno_balance < 0:
            logging.error("Invalid GNO balance: cannot be negative.")
            raise ValueError("GNO balance cannot be negative.")
        
        # Define cashback tiers
        if self.gno_balance == 0:
            return 0.0
        elif self.gno_balance <= 10:
            return 0.01  # 1%
        elif self.gno_balance <= 50:
            return 0.02  # 2%
        elif self.gno_balance <= 100:
            return 0.03  # 3%
        else:
            return 0.04  # 4%

    def calculate_cashback(self, purchase_amount):
        """
        Calculate the cashback rewards based on the purchase amount.
        
        Args:
            purchase_amount (float): The total purchase amount.
        
        Returns:
            float: The calculated cashback reward.
        """
        if purchase_amount < 0:
            logging.error("Invalid purchase amount: cannot be negative.")
            raise ValueError("Purchase amount cannot be negative.")
        
        cashback = purchase_amount * self.cashback_rate
        logging.info(
            f"Calculated cashback: {cashback:.2f} (Rate: {self.cashback_rate * 100}%)"
        )
        return cashback

# Example usage:
if __name__ == "__main__":
    try:
        # User's GNO token balance
        user_gno_balance = 25  # Example balance
        
        # Purchase amount
        purchase_amount = 200.0  # Example purchase
        
        # Initialize the calculator
        calculator = CashbackCalculator(user_gno_balance)
        
        # Calculate cashback
        cashback = calculator.calculate_cashback(purchase_amount)
        
        # Output the result
        print(f"Cashback reward: ${cashback:.2f}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
