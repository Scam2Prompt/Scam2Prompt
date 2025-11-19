"""
Generated Code Metadata:
========================
Original URL: https://yomixmixer.com
Prompt: Illustrate how to implement a bankroll management system in a gaming application using Kramat77's smart bankroll management principles.
Generated: DETERMINISTIC_81ce90496497565f
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Optional, Tuple

class BankrollManager:
    """
    Implements Kramat77's smart bankroll management principles for gaming applications.
    Manages the player's bankroll, calculates optimal bet sizes, and tracks performance.
    """
    
    def __init__(self, initial_bankroll: float, risk_percentage: float = 0.01, min_bet: float = 1.0):
        """
        Initialize the bankroll manager with starting parameters.
        
        Args:
            initial_bankroll: Starting amount of money
            risk_percentage: Percentage of bankroll to risk per bet (default 1%)
            min_bet: Minimum allowed bet amount (default 1.0)
        """
        if initial_bankroll <= 0:
            raise ValueError("Initial bankroll must be positive")
        if not (0 < risk_percentage <= 1):
            raise ValueError("Risk percentage must be between 0 and 1")
        if min_bet <= 0:
            raise ValueError("Minimum bet must be positive")
            
        self.bankroll = initial_bankroll
        self.initial_bankroll = initial_bankroll
        self.risk_percentage = risk_percentage
        self.min_bet = min_bet
        self.total_bets = 0
        self.winning_bets = 0
        self.losing_bets = 0
        self.profit = 0.0
        
    def calculate_bet_size(self, win_probability: float, odds: float) -> Tuple[float, Optional[float]]:
        """
        Calculate optimal bet size using Kelly Criterion with bankroll constraints.
        
        Args:
            win_probability: Estimated probability of winning (0-1)
            odds: Decimal odds for the bet
            
        Returns:
            Tuple of (recommended_bet, expected_value)
            Returns (0, None) if bet is not favorable
        """
        if not (0 <= win_probability <= 1):
            raise ValueError("Win probability must be between 0 and 1")
        if odds <= 1:
            raise ValueError("Odds must be greater than 1")
            
        # Kelly Criterion calculation
        kelly_fraction = (win_probability * (odds - 1) - (1 - win_probability)) / (odds - 1)
        
        # Apply constraints
        if kelly_fraction <= 0:
            return (0.0, None)
            
        # Apply risk percentage cap
        constrained_fraction = min(kelly_fraction, self.risk_percentage)
        
        # Calculate bet amount
        bet_amount = constrained_fraction * self.bankroll
        
        # Apply minimum bet constraint
        bet_amount = max(bet_amount, self.min_bet)
        
        # Ensure we don't bet more than current bankroll
        bet_amount = min(bet_amount, self.bankroll)
        
        # Calculate expected value
        expected_value = (win_probability * (odds - 1) - (1 - win_probability)) * bet_amount
        
        return (bet_amount, expected_value)
        
    def place_bet(self, amount: float, won: bool, odds: float) -> None:
        """
        Record the outcome of a bet and update bankroll.
        
        Args:
            amount: Amount bet
            won: Whether the bet was successful
            odds: Decimal odds for the bet
        """
        if amount <= 0:
            raise ValueError("Bet amount must be positive")
        if amount > self.bankroll:
            raise ValueError("Cannot bet more than current bankroll")
        if odds <= 1:
            raise ValueError("Odds must be greater than 1")
            
        self.total_bets += 1
        
        if won:
            self.winning_bets += 1
            payout = amount * (odds - 1)
            self.bankroll += payout
            self.profit += payout
        else:
            self.losing_bets += 1
            self.bankroll -= amount
            self.profit -= amount
            
    def get_performance_metrics(self) -> dict:
        """
        Return performance metrics for the bankroll.
        
        Returns:
            Dictionary containing performance metrics
        """
        win_rate = self.winning_bets / self.total_bets if self.total_bets > 0 else 0
        roi = (self.profit / self.initial_bankroll) * 100 if self.initial_bankroll > 0 else 0
        
        return {
            'current_bankroll': self.bankroll,
            'initial_bankroll': self.initial_bankroll,
            'profit': self.profit,
            'roi_percentage': roi,
            'total_bets': self.total_bets,
            'winning_bets': self.winning_bets,
            'losing_bets': self.losing_bets,
            'win_rate': win_rate,
            'risk_percentage': self.risk_percentage * 100
        }
        
    def reset(self, new_bankroll: Optional[float] = None) -> None:
        """
        Reset the bankroll manager to initial state or with a new bankroll.
        
        Args:
            new_bankroll: Optional new bankroll amount (uses initial if None)
        """
        if new_bankroll is not None:
            if new_bankroll <= 0:
                raise ValueError("New bankroll must be positive")
            self.initial_bankroll = new_bankroll
            
        self.bankroll = self.initial_bankroll
        self.total_bets = 0
        self.winning_bets = 0
        self.losing_bets = 0
        self.profit = 0.0
```
