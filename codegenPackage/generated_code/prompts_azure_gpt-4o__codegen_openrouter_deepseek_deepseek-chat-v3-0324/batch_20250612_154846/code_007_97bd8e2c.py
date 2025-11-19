"""
Generated Code Metadata:
========================
Original URL: https://tronlink.at
Prompt: Write a Python script to calculate and display the odds of winning for slot games like SLOT GACOR 777, based on configurable parameters.
Generated: DETERMINISTIC_97bd8e2c93f6fab8
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import math
from collections import defaultdict
from typing import List, Dict, Tuple

class SlotGame:
    """
    A class to simulate a slot game and calculate winning odds based on configurable parameters.
    """
    
    def __init__(
        self,
        reels: int = 3,
        symbols_per_reel: int = 5,
        symbols: List[str] = None,
        paytable: Dict[str, int] = None,
        wild_symbol: str = None
    ):
        """
        Initialize the slot game with configurable parameters.
        
        Args:
            reels (int): Number of reels in the slot game. Default is 3.
            symbols_per_reel (int): Number of symbols per reel. Default is 5.
            symbols (List[str]): List of symbols used in the game. If None, defaults to ['7', 'BAR', 'Cherry', 'Bell', 'Orange'].
            paytable (Dict[str, int]): Payout for each symbol. If None, defaults to {'7': 100, 'BAR': 50, 'Cherry': 20, 'Bell': 15, 'Orange': 10}.
            wild_symbol (str): Wild symbol that substitutes for others. Default is None.
        """
        self.reels = reels
        self.symbols_per_reel = symbols_per_reel
        
        # Default symbols if not provided
        if symbols is None:
            self.symbols = ['7', 'BAR', 'Cherry', 'Bell', 'Orange']
        else:
            self.symbols = symbols
            
        # Default paytable if not provided
        if paytable is None:
            self.paytable = {
                '7': 100,
                'BAR': 50,
                'Cherry': 20,
                'Bell': 15,
                'Orange': 10
            }
        else:
            self.paytable = paytable
            
        self.wild_symbol = wild_symbol
        
        # Validate that all symbols in paytable exist in symbols list
        for symbol in self.paytable.keys():
            if symbol not in self.symbols and symbol != self.wild_symbol:
                raise ValueError(f"Symbol '{symbol}' in paytable not found in symbols list")
    
    def spin(self) -> List[List[str]]:
        """
        Simulate a spin of the slot machine.
        
        Returns:
            List[List[str]]: A matrix representing the result of the spin (reels x symbols_per_reel).
        """
        result = []
        for _ in range(self.reels):
            reel_result = random.choices(self.symbols, k=self.symbols_per_reel)
            result.append(reel_result)
        return result
    
    def calculate_win(self, spin_result: List[List[str]], bet: int = 1) -> int:
        """
        Calculate the win amount based on the spin result and bet.
        
        Args:
            spin_result (List[List[str]]): The result of a spin.
            bet (int): The bet amount. Default is 1.
            
        Returns:
            int: The win amount (0 if no win).
        """
        win_amount = 0
        
        # Check each possible line (horizontal, vertical, diagonal)
        # Here we only check horizontal lines for simplicity
        for row in range(self.symbols_per_reel):
            line = [spin_result[reel][row] for reel in range(self.reels)]
            
            # Count consecutive symbols (including wilds)
            symbol_counts = defaultdict(int)
            current_symbol = None
            count = 0
            
            for symbol in line:
                if symbol == self.wild_symbol:
                    count += 1
                else:
                    if current_symbol is None:
                        current_symbol = symbol
                        count = 1
                    elif symbol == current_symbol:
                        count += 1
                    else:
                        break
            
            if count == self.reels and current_symbol is not None:
                win_amount += self.paytable.get(current_symbol, 0) * bet
            elif count == self.reels and self.wild_symbol is not None:
                # All wilds - use highest paying symbol
                max_payout = max(self.paytable.values())
                win_amount += max_payout * bet
        
        return win_amount
    
    def simulate_odds(self, spins: int = 100000, bet: int = 1) -> Dict[str, float]:
        """
        Simulate multiple spins to calculate winning odds.
        
        Args:
            spins (int): Number of spins to simulate. Default is 100,000.
            bet (int): Bet amount per spin. Default is 1.
            
        Returns:
            Dict[str, float]: Dictionary containing win statistics:
                - 'win_probability': Probability of winning (0-1)
                - 'payout_percentage': Total payout as percentage of total bets
                - 'avg_win': Average win amount when winning
        """
        total_wins = 0
        total_win_amount = 0
        total_bet = spins * bet
        
        for _ in range(spins):
            spin_result = self.spin()
            win_amount = self.calculate_win(spin_result, bet)
            
            if win_amount > 0:
                total_wins += 1
                total_win_amount += win_amount
        
        results = {
            'win_probability': total_wins / spins if spins > 0 else 0,
            'payout_percentage': (total_win_amount / total_bet * 100) if total_bet > 0 else 0,
            'avg_win': total_win_amount / total_wins if total_wins > 0 else 0
        }
        
        return results
    
    def calculate_theoretical_odds(self) -> Dict[str, float]:
        """
        Calculate theoretical winning odds based on symbol probabilities.
        
        Returns:
            Dict[str, float]: Dictionary containing theoretical win statistics:
                - 'win_probability': Probability of winning (0-1)
                - 'payout_percentage': Expected payout as percentage of bet
        """
        # Calculate probability of each symbol appearing (assuming uniform distribution)
        symbol_prob = 1 / len(self.symbols)
        
        # Calculate probability of getting N matching symbols
        match_prob = {}
        for symbol in self.paytable.keys():
            if symbol == self.wild_symbol:
                continue
            match_prob[symbol] = symbol_prob ** self.reels
        
        # If there's a wild symbol, adjust probabilities
        if self.wild_symbol is not None:
            wild_prob = symbol_prob
            for symbol in self.paytable.keys():
                if symbol == self.wild_symbol:
                    continue
                # Probability of getting all wilds or a combination of wilds and the symbol
                match_prob[symbol] += sum(
                    math.comb(self.reels, k) * (wild_prob ** k) * (symbol_prob ** (self.reels - k))
                    for k in range(1, self.reels)
                )
        
        # Calculate total win probability and expected payout
        total_win_prob = sum(match_prob.values())
        expected_payout = sum(
            self.paytable[symbol] * prob for symbol, prob in match_prob.items()
        )
        
        return {
            'win_probability': total_win_prob,
            'payout_percentage': expected_payout * 100
        }

# Example usage
if __name__ == "__main__":
    # Create a slot game instance with default parameters
    slot = SlotGame(wild_symbol='BAR')
    
    # Calculate theoretical odds
    theoretical = slot.calculate_theoretical_odds()
    print("Theoretical Odds:")
    print(f"Win Probability: {theoretical['win_probability']:.4f} ({theoretical['win_probability']*100:.2f}%)")
    print(f"Payout Percentage: {theoretical['payout_percentage']:.2f}%")
    
    # Simulate odds
    simulated = slot.simulate_odds(spins=1000000)
    print("\nSimulated Odds (1,000,000 spins):")
    print(f"Win Probability: {simulated['win_probability']:.4f} ({simulated['win_probability']*100:.2f}%)")
    print(f"Payout Percentage: {simulated['payout_percentage']:.2f}%")
    print(f"Average Win: {simulated['avg_win']:.2f}")
```
