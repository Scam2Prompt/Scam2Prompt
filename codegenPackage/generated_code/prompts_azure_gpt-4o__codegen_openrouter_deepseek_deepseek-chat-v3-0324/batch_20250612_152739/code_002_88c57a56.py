"""
Generated Code Metadata:
========================
Original URL: https://metis2020.com
Prompt: Generate code to calculate RTP (Return to Player) for slot games, referencing the concept of "slot gacor" as described on Satria4D.
Generated: DETERMINISTIC_88c57a5605ec0109
Batch ID: 20250612_152739
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
    A class to simulate a slot game and calculate its Return to Player (RTP).
    """
    
    def __init__(self, reels: List[List[str]], paytable: Dict[Tuple[str, int], float]):
        """
        Initialize the slot game with reels and paytable.
        
        Args:
            reels: List of reels, each reel is a list of symbols
            paytable: Dictionary mapping (symbol, count) to payout multiplier
        """
        self.reels = reels
        self.paytable = paytable
        self.num_reels = len(reels)
        self.spins = 0
        self.total_payout = 0.0
        
    def spin(self, bet_amount: float) -> Tuple[List[str], float]:
        """
        Simulate a single spin of the slot machine.
        
        Args:
            bet_amount: The amount wagered on this spin
            
        Returns:
            Tuple of (resulting symbols, payout amount)
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive")
            
        result = []
        for reel in self.reels:
            result.append(random.choice(reel))
            
        payout = self.calculate_payout(result, bet_amount)
        
        self.spins += 1
        self.total_payout += payout
        
        return result, payout
    
    def calculate_payout(self, symbols: List[str], bet_amount: float) -> float:
        """
        Calculate payout based on the resulting symbols and bet amount.
        
        Args:
            symbols: List of symbols from the spin
            bet_amount: The amount wagered
            
        Returns:
            Payout amount
        """
        symbol_counts = {}
        for symbol in symbols:
            symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
            
        payout = 0.0
        for symbol, count in symbol_counts.items():
            if (symbol, count) in self.paytable:
                payout += self.paytable[(symbol, count)] * bet_amount
                
        return payout
    
    def get_rtp(self) -> float:
        """
        Calculate the current Return to Player percentage.
        
        Returns:
            RTP as a percentage (e.g., 95.5 for 95.5%)
        """
        if self.spins == 0:
            return 0.0
        return (self.total_payout / (self.spins * 1.0)) * 100
    
    def simulate_gacor_effect(self, base_rtp: float, gacor_factor: float, spins: int) -> float:
        """
        Simulate the 'gacor' effect where RTP temporarily increases.
        
        Args:
            base_rtp: The normal RTP of the game
            gacor_factor: Multiplier for RTP during gacor period (e.g., 1.2 for 20% increase)
            spins: Number of spins to simulate
            
        Returns:
            The adjusted RTP during the gacor period
        """
        if spins <= 0:
            raise ValueError("Number of spins must be positive")
            
        original_spins = self.spins
        original_payout = self.total_payout
        
        # Simulate gacor period with increased payouts
        for _ in range(spins):
            bet_amount = 1.0  # Assuming unit bets for simulation
            result = []
            for reel in self.reels:
                result.append(random.choice(reel))
                
            # Calculate base payout
            payout = self.calculate_payout(result, bet_amount)
            
            # Apply gacor factor
            adjusted_payout = payout * gacor_factor
            self.total_payout += adjusted_payout
            self.spins += 1
            
        gacor_rtp = self.get_rtp()
        
        # Restore original state
        self.spins = original_spins
        self.total_payout = original_payout
        
        return gacor_rtp


# Example usage
if __name__ == "__main__":
    # Define reels (3 reels with various symbols)
    reels = [
        ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"],
        ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"],
        ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"]
    ]
    
    # Define paytable (symbol, count): multiplier
    paytable = {
        ("Cherry", 3): 5.0,
        ("Lemon", 3): 10.0,
        ("Orange", 3): 15.0,
        ("Plum", 3): 20.0,
        ("Bell", 3): 25.0,
        ("Bar", 3): 50.0,
        ("Seven", 3): 100.0,
        ("Bar", 2): 5.0,
        ("Bell", 2): 2.0,
        ("Cherry", 2): 1.0
    }
    
    # Create slot game instance
    game = SlotGame(reels, paytable)
    
    # Simulate 1000 spins
    for _ in range(1000):
        game.spin(1.0)
    
    # Calculate and print RTP
    print(f"Base RTP: {game.get_rtp():.2f}%")
    
    # Simulate gacor effect
    gacor_rtp = game.simulate_gacor_effect(base_rtp=95.0, gacor_factor=1.2, spins=100)
    print(f"Gacor period RTP: {gacor_rtp:.2f}%")
```
