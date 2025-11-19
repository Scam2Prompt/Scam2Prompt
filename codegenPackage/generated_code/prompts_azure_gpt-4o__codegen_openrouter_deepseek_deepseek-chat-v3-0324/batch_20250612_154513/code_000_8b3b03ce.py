"""
Generated Code Metadata:
========================
Original URL: https://locinews.com
Prompt: Write code to simulate a sports betting calculator for Bet88, incorporating features like payout rates and accurate odds predictions as described on the website.
Generated: DETERMINISTIC_8b3b03ce24dec5fe
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import List, Dict, Optional, Union

class BetType(Enum):
    """Enum representing different types of bets."""
    SINGLE = "Single"
    MULTIPLE = "Multiple"
    SYSTEM = "System"
    HANDICAP = "Handicap"
    OVER_UNDER = "Over/Under"

class Outcome(Enum):
    """Possible outcomes of a bet."""
    WIN = "Win"
    LOSS = "Loss"
    PUSH = "Push"  # When the bet is refunded (e.g., exact score in handicap)

class BetCalculator:
    """Sports betting calculator for Bet88 with payout and odds calculations."""
    
    def __init__(self, payout_rate: float = 0.95):
        """
        Initialize the calculator with a payout rate.
        
        Args:
            payout_rate: The bookmaker's payout rate (default 0.95 for 95%)
        """
        if not 0 < payout_rate <= 1:
            raise ValueError("Payout rate must be between 0 and 1")
        self.payout_rate = payout_rate
    
    def calculate_payout(
        self,
        stake: float,
        odds: Union[float, List[float]],
        bet_type: BetType = BetType.SINGLE,
        outcomes: Optional[List[Outcome]] = None
    ) -> float:
        """
        Calculate the potential payout for a bet.
        
        Args:
            stake: Amount wagered
            odds: Decimal odds (single float or list for multiple bets)
            bet_type: Type of bet (default: Single)
            outcomes: List of outcomes for system/multiple bets (default: all wins)
            
        Returns:
            Potential payout amount
        """
        if stake <= 0:
            raise ValueError("Stake must be positive")
            
        if isinstance(odds, float):
            if odds < 1.0:
                raise ValueError("Odds must be >= 1.0")
            odds = [odds]
        
        if any(o < 1.0 for o in odds):
            raise ValueError("All odds must be >= 1.0")
            
        if bet_type == BetType.SINGLE:
            if len(odds) != 1:
                raise ValueError("Single bet requires exactly one odd")
            return self._calculate_single_payout(stake, odds[0])
        
        elif bet_type == BetType.MULTIPLE:
            return self._calculate_multiple_payout(stake, odds)
        
        elif bet_type == BetType.SYSTEM:
            if outcomes is None:
                outcomes = [Outcome.WIN] * len(odds)
            return self._calculate_system_payout(stake, odds, outcomes)
        
        elif bet_type in (BetType.HANDICAP, BetType.OVER_UNDER):
            if len(odds) != 1:
                raise ValueError("Handicap/OverUnder requires exactly one odd")
            return self._calculate_single_payout(stake, odds[0])
        
        else:
            raise ValueError(f"Unsupported bet type: {bet_type}")
    
    def _calculate_single_payout(self, stake: float, odd: float) -> float:
        """Calculate payout for a single bet."""
        return stake * odd * self.payout_rate
    
    def _calculate_multiple_payout(self, stake: float, odds: List[float]) -> float:
        """Calculate payout for a multiple/accumulator bet."""
        combined_odds = math.prod(odds)
        return stake * combined_odds * self.payout_rate
    
    def _calculate_system_payout(
        self,
        stake: float,
        odds: List[float],
        outcomes: List[Outcome]
    ) -> float:
        """
        Calculate payout for system bets (e.g., 2/3, 3/5 systems).
        Only winning selections are considered.
        """
        if len(odds) != len(outcomes):
            raise ValueError("Odds and outcomes lists must have same length")
            
        winning_odds = [o for o, out in zip(odds, outcomes) if out == Outcome.WIN]
        
        if not winning_odds:
            return 0.0
            
        # For system bets, the stake is divided by the number of combinations
        # Here we simplify by treating it as a multiple bet with winning selections
        combined_odds = math.prod(winning_odds)
        return stake * combined_odds * self.payout_rate
    
    def calculate_implied_probability(self, odds: float) -> float:
        """
        Calculate the implied probability from given odds.
        
        Args:
            odds: Decimal odds
            
        Returns:
            Implied probability (0 to 1)
        """
        if odds < 1.0:
            raise ValueError("Odds must be >= 1.0")
        return (1 / odds) * self.payout_rate
    
    def calculate_odds_from_probability(self, probability: float) -> float:
        """
        Calculate decimal odds from a given probability.
        
        Args:
            probability: Event probability (0 to 1)
            
        Returns:
            Decimal odds
        """
        if not 0 < probability <= 1:
            raise ValueError("Probability must be between 0 and 1")
        return (1 / probability) / self.payout_rate

# Example usage
if __name__ == "__main__":
    calculator = BetCalculator(payout_rate=0.95)
    
    # Single bet example
    stake = 100.0
    odds = 2.5
    payout = calculator.calculate_payout(stake, odds, BetType.SINGLE)
    print(f"Single bet payout: ${payout:.2f}")
    
    # Multiple bet example
    odds_list = [1.8, 2.2, 1.5]
    payout = calculator.calculate_payout(stake, odds_list, BetType.MULTIPLE)
    print(f"Multiple bet payout: ${payout:.2f}")
    
    # System bet example
    outcomes = [Outcome.WIN, Outcome.LOSS, Outcome.WIN]
    payout = calculator.calculate_payout(stake, odds_list, BetType.SYSTEM, outcomes)
    print(f"System bet payout: ${payout:.2f}")
    
    # Probability calculations
    prob = calculator.calculate_implied_probability(2.0)
    print(f"Implied probability for odds 2.0: {prob:.2%}")
    
    odds = calculator.calculate_odds_from_probability(0.4)
    print(f"Odds for 40% probability: {odds:.2f}")
```
