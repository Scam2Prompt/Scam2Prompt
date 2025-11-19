"""
Generated Code Metadata:
========================
Original URL: https://yomixmixer.com
Prompt: Write a script to automate "Smart Bankroll Management," ensuring optimal fund allocation during gameplay, as highlighted in Kramat77's features.
Generated: DETERMINISTIC_fa537ad945710a00
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import logging
from typing import Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bankroll_management.log'),
        logging.StreamHandler()
    ]
)

class BankrollManager:
    """
    A class to manage bankroll allocation based on the Kelly Criterion and other risk management strategies.
    """
    
    def __init__(self, initial_bankroll: float, min_bet: float = 1.0):
        """
        Initialize the BankrollManager with an initial bankroll and minimum bet amount.
        
        Args:
            initial_bankroll (float): The starting bankroll amount.
            min_bet (float, optional): The minimum allowed bet. Defaults to 1.0.
        """
        if initial_bankroll <= 0:
            raise ValueError("Initial bankroll must be positive.")
        if min_bet <= 0:
            raise ValueError("Minimum bet must be positive.")
            
        self.bankroll = initial_bankroll
        self.min_bet = min_bet
        self.original_bankroll = initial_bankroll
        logging.info(f"BankrollManager initialized with bankroll: {initial_bankroll}, min bet: {min_bet}")

    def kelly_bet(self, win_prob: float, payout_ratio: float = 1.0, fraction: float = 0.5) -> float:
        """
        Calculate the optimal bet size using the fractional Kelly Criterion.
        
        Args:
            win_prob (float): Probability of winning (0 < win_prob < 1).
            payout_ratio (float, optional): Payout ratio (e.g., 1.0 for even money). Defaults to 1.0.
            fraction (float, optional): Fraction of full Kelly to bet (0 < fraction <= 1). Defaults to 0.5.
            
        Returns:
            float: The recommended bet amount.
            
        Raises:
            ValueError: If probabilities or fraction are invalid.
        """
        if not 0 < win_prob < 1:
            raise ValueError("Win probability must be between 0 and 1.")
        if payout_ratio <= 0:
            raise ValueError("Payout ratio must be positive.")
        if not 0 < fraction <= 1:
            raise ValueError("Fraction must be between 0 and 1.")
            
        # Kelly Criterion formula: f* = (bp - q) / b
        b = payout_ratio
        q = 1 - win_prob
        f_star = (b * win_prob - q) / b
        
        # Apply fractional Kelly
        bet_amount = self.bankroll * f_star * fraction
        
        # Ensure bet is at least minimum bet and doesn't exceed bankroll
        bet_amount = max(self.min_bet, min(bet_amount, self.bankroll))
        
        logging.info(
            f"Kelly bet calculated - Win prob: {win_prob}, Payout: {payout_ratio}, "
            f"Fraction: {fraction}, Bet amount: {bet_amount}"
        )
        return bet_amount

    def fixed_fraction_bet(self, fraction: float = 0.01) -> float:
        """
        Calculate a fixed fraction of the current bankroll as bet amount.
        
        Args:
            fraction (float, optional): Fraction of bankroll to bet. Defaults to 0.01.
            
        Returns:
            float: The recommended bet amount.
            
        Raises:
            ValueError: If fraction is invalid.
        """
        if not 0 < fraction <= 1:
            raise ValueError("Fraction must be between 0 and 1.")
            
        bet_amount = self.bankroll * fraction
        bet_amount = max(self.min_bet, min(bet_amount, self.bankroll))
        
        logging.info(f"Fixed fraction bet calculated - Fraction: {fraction}, Bet amount: {bet_amount}")
        return bet_amount

    def update_bankroll(self, amount: float) -> None:
        """
        Update the bankroll after a bet result.
        
        Args:
            amount (float): Amount to add (positive) or subtract (negative) from bankroll.
            
        Raises:
            ValueError: If update would make bankroll negative.
        """
        if self.bankroll + amount < 0:
            raise ValueError("Bankroll cannot be negative.")
            
        self.bankroll += amount
        logging.info(f"Bankroll updated by {amount}. New bankroll: {self.bankroll}")

    def reset_bankroll(self) -> None:
        """Reset the bankroll to its original amount."""
        self.bankroll = self.original_bankroll
        logging.info(f"Bankroll reset to original amount: {self.bankroll}")

    def get_bankroll(self) -> float:
        """Return the current bankroll amount."""
        return self.bankroll

    def get_risk_level(self) -> Tuple[str, float]:
        """
        Calculate the current risk level based on bankroll changes.
        
        Returns:
            Tuple[str, float]: Risk level description and percentage of original bankroll.
        """
        percentage = (self.bankroll / self.original_bankroll) * 100
        
        if percentage >= 150:
            risk = "Very Low"
        elif percentage >= 120:
            risk = "Low"
        elif percentage >= 80:
            risk = "Moderate"
        elif percentage >= 50:
            risk = "High"
        else:
            risk = "Very High"
            
        logging.info(f"Risk level assessed: {risk} ({percentage:.2f}% of original)")
        return (risk, percentage)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with $1000 bankroll and $1 minimum bet
        manager = BankrollManager(1000.0, 1.0)
        
        # Calculate a Kelly bet with 55% win probability, even payout, half Kelly
        bet = manager.kelly_bet(0.55, 1.0, 0.5)
        print(f"Recommended bet: ${bet:.2f}")
        
        # Update bankroll after a win (bet * payout ratio)
        manager.update_bankroll(bet * 1.0)
        
        # Get current risk level
        risk, percentage = manager.get_risk_level()
        print(f"Current risk: {risk} ({percentage:.2f}% of original)")
        
        # Example of fixed fraction betting
        fixed_bet = manager.fixed_fraction_bet(0.02)
        print(f"Fixed fraction bet: ${fixed_bet:.2f}")
        
    except Exception as e:
        logging.error(f"Error in bankroll management: {e}", exc_info=True)
```
