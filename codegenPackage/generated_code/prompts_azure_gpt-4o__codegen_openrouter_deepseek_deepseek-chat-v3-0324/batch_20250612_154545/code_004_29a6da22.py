"""
Generated Code Metadata:
========================
Original URL: https://plf3108.com
Prompt: Develop a Python program to calculate potential winnings for multi-sport bets, including football and basketball, based on the diverse betting markets highlighted on the 868 platform.
Generated: DETERMINISTIC_29a6da221aae97f8
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Union, Optional

class BetCalculator:
    """
    A class to calculate potential winnings for multi-sport bets (football and basketball).
    Supports various betting markets including moneyline, point spread, and totals (over/under).
    """
    
    def __init__(self):
        self.sports_data = {
            'football': {
                'moneyline': {'commission': 0.05},
                'point_spread': {'commission': 0.05, 'point_value': 1.0},
                'totals': {'commission': 0.05, 'point_value': 0.5}
            },
            'basketball': {
                'moneyline': {'commission': 0.05},
                'point_spread': {'commission': 0.05, 'point_value': 1.0},
                'totals': {'commission': 0.05, 'point_value': 0.5}
            }
        }
    
    def calculate_single_bet(self, sport: str, market: str, odds: float, stake: float) -> float:
        """
        Calculate winnings for a single bet.
        
        Args:
            sport: Sport type ('football' or 'basketball')
            market: Betting market ('moneyline', 'point_spread', 'totals')
            odds: Decimal odds for the bet
            stake: Amount wagered
            
        Returns:
            Potential winnings (including stake)
            
        Raises:
            ValueError: If invalid sport, market, odds, or stake is provided
        """
        if sport not in self.sports_data:
            raise ValueError(f"Invalid sport. Must be one of: {list(self.sports_data.keys())}")
        
        if market not in self.sports_data[sport]:
            raise ValueError(f"Invalid market for {sport}. Must be one of: {list(self.sports_data[sport].keys())}")
        
        if odds <= 1.0:
            raise ValueError("Odds must be greater than 1.0")
        
        if stake <= 0:
            raise ValueError("Stake must be positive")
        
        commission = self.sports_data[sport][market]['commission']
        gross_winnings = stake * odds
        net_winnings = gross_winnings * (1 - commission)
        
        return round(net_winnings, 2)
    
    def calculate_parlay(self, bets: List[Dict[str, Union[str, float]]]) -> float:
        """
        Calculate winnings for a parlay bet (all bets must win).
        
        Args:
            bets: List of bet dictionaries with keys: 'sport', 'market', 'odds'
            
        Returns:
            Potential parlay winnings (including stake)
            
        Raises:
            ValueError: If any bet is invalid or empty list provided
        """
        if not bets:
            raise ValueError("At least one bet is required for a parlay")
        
        total_odds = 1.0
        stake = bets[0].get('stake', 0)
        
        for bet in bets:
            if bet.get('stake', 0) != stake:
                raise ValueError("All bets in a parlay must have the same stake")
            
            sport = bet.get('sport')
            market = bet.get('market')
            odds = bet.get('odds', 0)
            
            if not all([sport, market, odds]):
                raise ValueError("Each bet must have 'sport', 'market', and 'odds'")
            
            # Validate the single bet (will raise ValueError if invalid)
            self.calculate_single_bet(sport, market, odds, 1.0)
            
            total_odds *= odds
        
        commission = 0.05  # Standard commission for parlays
        gross_winnings = stake * total_odds
        net_winnings = gross_winnings * (1 - commission)
        
        return round(net_winnings, 2)
    
    def calculate_round_robin(self, bets: List[Dict[str, Union[str, float]]], combination_size: int = 2) -> Dict[str, float]:
        """
        Calculate winnings for a round robin bet (multiple smaller parlays).
        
        Args:
            bets: List of bet dictionaries with keys: 'sport', 'market', 'odds'
            combination_size: Number of bets in each parlay (default 2)
            
        Returns:
            Dictionary with 'total_winnings' and breakdown of each parlay
            
        Raises:
            ValueError: If invalid combination_size or not enough bets
        """
        from itertools import combinations
        
        if combination_size < 2:
            raise ValueError("Combination size must be at least 2")
        
        if len(bets) < combination_size:
            raise ValueError(f"Need at least {combination_size} bets for round robin")
        
        stake = bets[0].get('stake', 0)
        parlays = list(combinations(bets, combination_size))
        results = {}
        total_winnings = 0.0
        
        for i, parlay in enumerate(parlays, 1):
            try:
                winnings = self.calculate_parlay(list(parlay))
                results[f'parlay_{i}'] = winnings
                total_winnings += winnings
            except ValueError as e:
                results[f'parlay_{i}'] = f"Invalid: {str(e)}"
        
        results['total_winnings'] = round(total_winnings, 2)
        return results
    
    def save_calculation(self, filename: str, data: Dict) -> None:
        """
        Save calculation results to a JSON file.
        
        Args:
            filename: Name of the file to save
            data: Data to save
            
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save calculation: {str(e)}")

# Example usage
if __name__ == "__main__":
    calculator = BetCalculator()
    
    # Single bet example
    try:
        winnings = calculator.calculate_single_bet(
            sport='football',
            market='moneyline',
            odds=2.5,
            stake=100.0
        )
        print(f"Single bet winnings: ${winnings:.2f}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    
    # Parlay example
    try:
        parlay_bets = [
            {'sport': 'football', 'market': 'moneyline', 'odds': 1.8, 'stake': 50},
            {'sport': 'basketball', 'market': 'point_spread', 'odds': 1.9, 'stake': 50}
        ]
        parlay_winnings = calculator.calculate_parlay(parlay_bets)
        print(f"Parlay winnings: ${parlay_winnings:.2f}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    
    # Round robin example
    try:
        rr_bets = [
            {'sport': 'football', 'market': 'moneyline', 'odds': 1.8, 'stake': 20},
            {'sport': 'basketball', 'market': 'point_spread', 'odds': 1.9, 'stake': 20},
            {'sport': 'football', 'market': 'totals', 'odds': 2.1, 'stake': 20}
        ]
        rr_results = calculator.calculate_round_robin(rr_bets, combination_size=2)
        print("Round robin results:")
        for k, v in rr_results.items():
            print(f"{k}: ${v:.2f}" if isinstance(v, float) else f"{k}: {v}")
        
        # Save results
        calculator.save_calculation('bet_results.json', rr_results)
    except ValueError as e:
        print(f"Error: {str(e)}")
```
