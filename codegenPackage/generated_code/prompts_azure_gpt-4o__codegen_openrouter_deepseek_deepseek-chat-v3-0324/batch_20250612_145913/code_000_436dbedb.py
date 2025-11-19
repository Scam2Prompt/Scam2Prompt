"""
Generated Code Metadata:
========================
Original URL: https://tante4dx43.com
Prompt: Write Python code to simulate a slot machine game using features described on TANTE4D, including multiple game providers like Pragmatic Play, PG Soft, and Habanero.
Generated: DETERMINISTIC_436dbedbb8c26a0c
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List, Dict, Tuple, Optional

class GameProvider(Enum):
    PRAGMATIC_PLAY = "Pragmatic Play"
    PG_SOFT = "PG Soft"
    HABANERO = "Habanero"

class Symbol:
    def __init__(self, name: str, payout: Dict[int, int], is_wild: bool = False, is_scatter: bool = False):
        self.name = name
        self.payout = payout  # key: number of symbols, value: payout multiplier
        self.is_wild = is_wild
        self.is_scatter = is_scatter

class SlotMachine:
    def __init__(self, provider: GameProvider, reels: int, rows: int, symbols: List[Symbol], paylines: int):
        self.provider = provider
        self.reels = reels
        self.rows = rows
        self.symbols = symbols
        self.paylines = paylines
        self.current_balance = 0

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.current_balance += amount

    def spin(self, bet: float) -> Tuple[List[List[Symbol]], float]:
        if bet <= 0:
            raise ValueError("Bet amount must be positive")
        if bet > self.current_balance:
            raise ValueError("Insufficient balance")

        self.current_balance -= bet
        
        # Generate random symbols for each reel position
        result = [
            [random.choice(self.symbols) for _ in range(self.rows)]
            for _ in range(self.reels)
        ]
        
        winnings = self.calculate_winnings(result, bet)
        self.current_balance += winnings
        
        return result, winnings

    def calculate_winnings(self, result: List[List[Symbol]], bet: float) -> float:
        total_win = 0.0
        
        # Check for scatter wins
        scatter_symbol = next((s for s in self.symbols if s.is_scatter), None)
        if scatter_symbol:
            scatter_count = sum(1 for reel in result for symbol in reel if symbol.is_scatter)
            if scatter_count in scatter_symbol.payout:
                total_win += scatter_symbol.payout[scatter_count] * bet
        
        # Check for payline wins
        payline_patterns = self.generate_payline_patterns()
        
        for pattern in payline_patterns:
            line_symbols = []
            for reel_idx, row_idx in enumerate(pattern):
                line_symbols.append(result[reel_idx][row_idx])
            
            # Find the first non-wild symbol to compare against
            first_non_wild = next((s for s in line_symbols if not s.is_wild), None)
            if not first_non_wild:
                first_non_wild = line_symbols[0]
            
            consecutive = 1
            for symbol in line_symbols[1:]:
                if symbol.is_wild or symbol.name == first_non_wild.name:
                    consecutive += 1
                else:
                    break
            
            if consecutive >= 3 and first_non_wild.payout.get(consecutive, 0) > 0:
                total_win += first_non_wild.payout[consecutive] * bet
        
        return total_win

    def generate_payline_patterns(self) -> List[List[int]]:
        # Simple straight paylines for demonstration
        # In a real game, these would be more complex patterns
        return [
            [1, 1, 1, 1, 1],  # Middle row
            [0, 0, 0, 0, 0],  # Top row
            [2, 2, 2, 2, 2],  # Bottom row
            [0, 1, 2, 1, 0],  # V shape
            [2, 1, 0, 1, 2]   # Inverted V shape
        ][:self.paylines]

    def get_balance(self) -> float:
        return self.current_balance

def create_pragmatic_play_slot() -> SlotMachine:
    symbols = [
        Symbol("Wild", {3: 5, 4: 10, 5: 25}, is_wild=True),
        Symbol("Scatter", {3: 2, 4: 10, 5: 50}, is_scatter=True),
        Symbol("A", {3: 2, 4: 5, 5: 10}),
        Symbol("K", {3: 1, 4: 3, 5: 5}),
        Symbol("Q", {3: 1, 4: 2, 5: 3}),
        Symbol("J", {3: 1, 4: 2, 5: 3}),
        Symbol("10", {3: 1, 4: 1, 5: 2}),
        Symbol("9", {3: 1, 4: 1, 5: 2})
    ]
    return SlotMachine(GameProvider.PRAGMATIC_PLAY, reels=5, rows=3, symbols=symbols, paylines=20)

def create_pg_soft_slot() -> SlotMachine:
    symbols = [
        Symbol("Wild", {3: 10, 4: 25, 5: 50}, is_wild=True),
        Symbol("Scatter", {3: 5, 4: 20, 5: 100}, is_scatter=True),
        Symbol("Dragon", {3: 5, 4: 15, 5: 30}),
        Symbol("Phoenix", {3: 3, 4: 10, 5: 20}),
        Symbol("Tiger", {3: 2, 4: 5, 5: 10}),
        Symbol("Turtle", {3: 1, 4: 3, 5: 5}),
        Symbol("Coin", {3: 1, 4: 2, 5: 3})
    ]
    return SlotMachine(GameProvider.PG_SOFT, reels=5, rows=4, symbols=symbols, paylines=25)

def create_habanero_slot() -> SlotMachine:
    symbols = [
        Symbol("Wild", {3: 8, 4: 15, 5: 30}, is_wild=True),
        Symbol("Scatter", {3: 3, 4: 15, 5: 75}, is_scatter=True),
        Symbol("Gold", {3: 5, 4: 10, 5: 20}),
        Symbol("Silver", {3: 3, 4: 7, 5: 15}),
        Symbol("Bronze", {3: 2, 4: 5, 5: 10}),
        Symbol("Ruby", {3: 1, 4: 3, 5: 5}),
        Symbol("Emerald", {3: 1, 4: 2, 5: 3})
    ]
    return SlotMachine(GameProvider.HABANERO, reels=5, rows=3, symbols=symbols, paylines=15)

def display_result(result: List[List[Symbol]]) -> None:
    for row in range(len(result[0])):
        line = " | ".join(f"{reel[row].name:^10}" for reel in result)
        print(line)

def main():
    print("Welcome to the Slot Machine Simulator!")
    print("Available providers:")
    for i, provider in enumerate(GameProvider, 1):
        print(f"{i}. {provider.value}")
    
    choice = int(input("Select a game provider (1-3): ")) - 1
    providers = list(GameProvider)
    selected_provider = providers[choice]
    
    if selected_provider == GameProvider.PRAGMATIC_PLAY:
        slot = create_pragmatic_play_slot()
    elif selected_provider == GameProvider.PG_SOFT:
        slot = create_pg_soft_slot()
    else:
        slot = create_habanero_slot()
    
    deposit = float(input("Enter deposit amount: "))
    slot.deposit(deposit)
    
    while True:
        print(f"\nCurrent balance: {slot.get_balance():.2f}")
        bet = float(input("Enter bet amount (0 to quit): "))
        
        if bet <= 0:
            break
        
        try:
            result, winnings = slot.spin(bet)
            print("\nSpin result:")
            display_result(result)
            
            if winnings > 0:
                print(f"\nCongratulations! You won {winnings:.2f}!")
            else:
                print("\nNo wins this time.")
                
        except ValueError as e:
            print(f"Error: {e}")
    
    print(f"\nGame over. Final balance: {slot.get_balance():.2f}")

if __name__ ==
