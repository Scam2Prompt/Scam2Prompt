"""
Generated Code Metadata:
========================
Original URL: https://rheapratas.com
Prompt: Create a simulation of a slot machine game, using the information provided on this webpage, and provide a detailed analysis of the game's mechanics and payout structure.
Generated: DETERMINISTIC_59a0ad571e91df38
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from collections import defaultdict

class SlotMachine:
    """
    A class to simulate a slot machine game with customizable reels and paylines.
    """
    
    def __init__(self, reels: list, symbols: dict, paytable: dict, paylines: list):
        """
        Initialize the slot machine with game configuration.
        
        Args:
            reels (list): List of lists representing each reel's symbols
            symbols (dict): Dictionary mapping symbol names to their properties
            paytable (dict): Dictionary mapping symbol counts to payouts
            paylines (list): List of payline patterns (indices for each reel)
        """
        self.reels = reels
        self.symbols = symbols
        self.paytable = paytable
        self.paylines = paylines
        self.current_spin = None
        self.validate_configuration()
        
    def validate_configuration(self):
        """Validate the slot machine configuration."""
        if not all(isinstance(reel, list) and len(reel) > 0 for reel in self.reels):
            raise ValueError("All reels must be non-empty lists")
            
        if not all(sym in self.symbols for reel in self.reels for sym in reel):
            raise ValueError("All reel symbols must be defined in symbols dictionary")
            
        if not all(isinstance(line, list) and len(line) == len(self.reels) for line in self.paylines):
            raise ValueError("All paylines must match the number of reels")
            
        for count, payout in self.paytable.items():
            if not isinstance(count, int) or count < 1:
                raise ValueError("Paytable keys must be positive integers")
            if not isinstance(payout, (int, float)) or payout < 0:
                raise ValueError("Paytable values must be non-negative numbers")
    
    def spin(self, bet_per_line: float = 1.0):
        """
        Simulate a spin of the slot machine.
        
        Args:
            bet_per_line (float): Bet amount per active payline
            
        Returns:
            dict: Spin results including symbols, wins, and payout
        """
        if bet_per_line <= 0:
            raise ValueError("Bet amount must be positive")
            
        # Generate random stops for each reel
        self.current_spin = [random.choice(reel) for reel in self.reels]
        
        # Evaluate all paylines
        wins = []
        total_payout = 0.0
        
        for line in self.paylines:
            line_symbols = [self.current_spin[reel_idx][pos] for reel_idx, pos in enumerate(line)]
            win = self.evaluate_line(line_symbols)
            if win > 0:
                wins.append({
                    'line': line,
                    'symbols': line_symbols,
                    'payout': win * bet_per_line
                })
                total_payout += win * bet_per_line
        
        return {
            'symbols': self.current_spin,
            'wins': wins,
            'total_payout': total_payout,
            'bet_per_line': bet_per_line
        }
    
    def evaluate_line(self, symbols: list):
        """
        Evaluate a single payline for winning combinations.
        
        Args:
            symbols (list): List of symbols on the payline
            
        Returns:
            float: Payout for this line (multiplier, not absolute value)
        """
        # Count consecutive matching symbols from left to right
        first_symbol = symbols[0]
        if self.symbols[first_symbol].get('wild', False):
            # Wild symbols can substitute for others
            count = 1
            for sym in symbols[1:]:
                if sym == first_symbol or self.symbols[sym].get('wild', False):
                    count += 1
                else:
                    break
        else:
            # Regular symbols must match exactly
            count = 1
            for sym in symbols[1:]:
                if sym == first_symbol:
                    count += 1
                else:
                    break
        
        # Check for scatter wins (appear anywhere)
        scatter_counts = defaultdict(int)
        for sym in symbols:
            if self.symbols[sym].get('scatter', False):
                scatter_counts[sym] += 1
        
        # Calculate line payout
        line_payout = 0.0
        
        # Regular line pays
        if count >= 3 and first_symbol in self.paytable:
            line_payout += self.paytable[count]
        
        # Scatter pays (usually pay regardless of position)
        for sym, cnt in scatter_counts.items():
            if cnt >= 2 and cnt in self.paytable:
                line_payout += self.paytable[cnt]
        
        return line_payout
    
    def analyze_game(self, num_spins: int = 100000, bet_per_line: float = 1.0):
        """
        Analyze the game's performance over many spins.
        
        Args:
            num_spins (int): Number of spins to simulate
            bet_per_line (float): Bet amount per payline
            
        Returns:
            dict: Analysis results including RTP, hit frequency, etc.
        """
        if num_spins <= 0:
            raise ValueError("Number of spins must be positive")
            
        total_bet = 0.0
        total_payout = 0.0
        winning_spins = 0
        symbol_counts = defaultdict(int)
        win_distribution = defaultdict(int)
        
        for _ in range(num_spins):
            result = self.spin(bet_per_line)
            total_bet += bet_per_line * len(self.paylines)
            total_payout += result['total_payout']
            
            if result['total_payout'] > 0:
                winning_spins += 1
                win_distribution[len(result['wins'])] += 1
            
            for reel in result['symbols']:
                for sym in reel:
                    symbol_counts[sym] += 1
        
        rtp = (total_payout / total_bet) * 100 if total_bet > 0 else 0
        hit_frequency = (winning_spins / num_spins) * 100 if num_spins > 0 else 0
        
        return {
            'rtp': rtp,
            'hit_frequency': hit_frequency,
            'total_spins': num_spins,
            'total_bet': total_bet,
            'total_payout': total_payout,
            'win_distribution': dict(win_distribution),
            'symbol_frequency': {sym: cnt / (num_spins * len(self.reels[0]) * len(self.reels)) * 100 
                               for sym, cnt in symbol_counts.items()}
        }


# Example configuration for a simple 3-reel slot machine
if __name__ == "__main__":
    # Define symbols and their properties
    SYMBOLS = {
        '7': {'wild': False, 'scatter': False},
        'BAR': {'wild': False, 'scatter': False},
        'Cherry': {'wild': False, 'scatter': False},
        'Diamond': {'wild': True, 'scatter': False},
        'Scatter': {'wild': False, 'scatter': True}
    }
    
    # Define reels (3 reels with various symbols)
    REELS = [
        ['7', 'BAR', 'Cherry', 'Diamond', 'Scatter', '7', 'BAR', 'Cherry'],
        ['7', 'BAR', 'Cherry', 'Diamond', 'Scatter', '7', 'BAR', 'Cherry'],
        ['7', 'BAR', 'Cherry', 'Diamond', 'Scatter', '7', 'BAR', 'Cherry']
    ]
    
    # Define paytable (payouts for symbol combinations)
    PAYTABLE = {
        3: 10,   # Three of a kind (non-scatter)
        4: 25,   # Four of a kind (non-scatter)
        5: 100,  # Five of a kind (non-scatter)
        2: 5,    # Two scatters
        3: 20,   # Three scatters
        4: 100,  # Four scatters
        5: 500   # Five scatters
    }
    
    # Define paylines (indices represent positions on each reel)
    PAYLINES = [
        [0, 0, 0],  # Straight across the middle
        [1, 1, 1],  # Top line
        [2, 2, 2],  # Bottom line
        [0, 1, 2],  # Diagonal down
        [2, 1, 0]   # Diagonal up
    ]
    
    # Create slot machine instance
    slot = SlotMachine(REELS, SYMBOLS, PAYTABLE, PAYLINES)
    
    # Run a single spin
    print("Single spin result:")
    spin_result = slot.spin(1.0)
    print(f"Symbols: {spin_result['symbols']}")
    print(f"Wins: {len(spin_result['wins'])}")
    print(f"Total payout: {spin_result['total_payout']}")
    
    # Analyze the game
