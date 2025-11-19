"""
Generated Code Metadata:
========================
Original URL: https://alltecskateparks.com
Prompt: Generate a code snippet for implementing a slot game feature similar to Lucky Neko from PG Soft, focusing on RTP mechanics and bonus features like wilds and free spins.
Generated: DETERMINISTIC_6f78aa007d8be76c
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple

class SlotGame:
    """
    A slot game implementation with RTP mechanics, wild symbols, and free spins.
    """
    
    def __init__(self, reels: int = 5, rows: int = 3, symbols: Dict[str, Dict[int, float]] = None):
        """
        Initialize the slot game with reels, rows, and symbols configuration.
        
        Args:
            reels (int): Number of reels in the game (default: 5)
            rows (int): Number of rows in the game (default: 3)
            symbols (Dict): Dictionary of symbols with their payouts and weights
        """
        self.reels = reels
        self.rows = rows
        self.symbols = symbols or self._default_symbols()
        self.wild_symbol = "WILD"
        self.scatter_symbol = "SCATTER"
        self.free_spins_trigger = 3  # Number of scatters needed for free spins
        self.free_spins_awarded = 10  # Number of free spins awarded
        self.rtp = 0.96  # Return to Player percentage
        
    def _default_symbols(self) -> Dict[str, Dict[int, float]]:
        """
        Default symbols configuration with weights and payouts.
        
        Returns:
            Dict: Default symbols configuration
        """
        return {
            "9": {3: 0.5, 4: 1, 5: 2},
            "10": {3: 0.75, 4: 1.5, 5: 3},
            "J": {3: 1, 4: 2, 5: 4},
            "Q": {3: 1.25, 4: 2.5, 5: 5},
            "K": {3: 1.5, 4: 3, 5: 6},
            "A": {3: 2, 4: 4, 5: 8},
            "WILD": {3: 5, 4: 10, 5: 20},
            "SCATTER": {3: 0, 4: 0, 5: 0}  # Scatter pays are handled separately
        }
    
    def _weighted_random_choice(self, weights: Dict[str, float]) -> str:
        """
        Select a symbol based on weighted probability.
        
        Args:
            weights (Dict): Dictionary of symbols and their weights
            
        Returns:
            str: Selected symbol
        """
        total = sum(weights.values())
        r = random.uniform(0, total)
        upto = 0
        for symbol, weight in weights.items():
            if upto + weight >= r:
                return symbol
            upto += weight
        return list(weights.keys())[-1]
    
    def _generate_reel_strip(self) -> List[List[str]]:
        """
        Generate a random reel strip based on symbol weights.
        
        Returns:
            List[List[str]]: Generated reel strip
        """
        reel_strip = []
        symbol_weights = {sym: 1.0 for sym in self.symbols.keys()}  # Equal weights for demo
        
        for _ in range(self.reels):
            reel = []
            for _ in range(self.rows):
                reel.append(self._weighted_random_choice(symbol_weights))
            reel_strip.append(reel)
            
        return reel_strip
    
    def _calculate_line_payout(self, line: List[str]) -> Tuple[float, bool]:
        """
        Calculate payout for a single payline.
        
        Args:
            line (List[str]): Symbols on the payline
            
        Returns:
            Tuple[float, bool]: Payout amount and whether wild was used
        """
        # Count consecutive matching symbols from left
        first_symbol = line[0]
        if first_symbol == self.scatter_symbol:
            return 0, False  # Scatters handled separately
            
        count = 1
        wild_used = False
        
        for symbol in line[1:]:
            if symbol == first_symbol or symbol == self.wild_symbol:
                count += 1
                if symbol == self.wild_symbol:
                    wild_used = True
            else:
                break
                
        # Get payout from symbol configuration
        if count >= 3 and first_symbol in self.symbols:
            payout_table = self.symbols[first_symbol]
            max_count = max(payout_table.keys())
            actual_count = min(count, max_count)
            return payout_table[actual_count], wild_used
            
        return 0, False
    
    def _calculate_scatter_payout(self, reel_strip: List[List[str]]) -> Tuple[float, int]:
        """
        Calculate scatter symbol payouts and count.
        
        Args:
            reel_strip (List[List[str]]): Current reel strip
            
        Returns:
            Tuple[float, int]: Scatter payout and count
        """
        scatter_count = 0
        for reel in reel_strip:
            for symbol in reel:
                if symbol == self.scatter_symbol:
                    scatter_count += 1
                    
        # In this implementation, scatters only trigger free spins
        return 0, scatter_count
    
    def spin(self, bet_amount: float = 1.0) -> Dict:
        """
        Execute a single spin and return results.
        
        Args:
            bet_amount (float): Amount bet on this spin
            
        Returns:
            Dict: Spin results including payout, free spins, and reel strip
        """
        # Adjust for RTP
        adjusted_bet = bet_amount * self.rtp
        
        reel_strip = self._generate_reel_strip()
        total_payout = 0.0
        free_spins = 0
        
        # Check for scatter wins (free spins)
        scatter_payout, scatter_count = self._calculate_scatter_payout(reel_strip)
        if scatter_count >= self.free_spins_trigger:
            free_spins = self.free_spins_awarded
            
        # Calculate line payouts (simplified - checking all possible lines)
        for row in range(self.rows):
            line = [reel[row] for reel in reel_strip]
            payout, _ = self._calculate_line_payout(line)
            total_payout += payout * adjusted_bet
            
        return {
            "reel_strip": reel_strip,
            "payout": total_payout,
            "free_spins": free_spins,
            "scatter_count": scatter_count
        }
    
    def free_spin(self, bet_amount: float = 1.0) -> Dict:
        """
        Execute a free spin (similar to regular spin but with potential multipliers).
        
        Args:
            bet_amount (float): Original bet amount
            
        Returns:
            Dict: Free spin results
        """
        # Free spins often have multipliers or special features
        result = self.spin(bet_amount)
        result["payout"] *= 2  # Example: 2x multiplier during free spins
        return result


# Example usage
if __name__ == "__main__":
    game = SlotGame()
    
    # Regular spin
    result = game.spin(1.0)
    print("Regular Spin Result:")
    print(f"Reel Strip: {result['reel_strip']}")
    print(f"Payout: {result['payout']}")
    print(f"Free Spins Awarded: {result['free_spins']}")
    
    # Free spin (if awarded)
    if result["free_spins"] > 0:
        free_result = game.free_spin(1.0)
        print("\nFree Spin Result:")
        print(f"Reel Strip: {free_result['reel_strip']}")
        print(f"Payout: {free_result['payout']}")
```
