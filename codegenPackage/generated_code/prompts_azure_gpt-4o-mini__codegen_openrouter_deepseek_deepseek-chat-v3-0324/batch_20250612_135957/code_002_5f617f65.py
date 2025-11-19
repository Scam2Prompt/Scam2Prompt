"""
Generated Code Metadata:
========================
Original URL: https://einarmiger-bandit-online.de
Prompt: Write a Python script that simulates the payout calculations for a slot machine, focusing on the differences between Merkur's Classic and Deluxe versions.
Generated: DETERMINISTIC_5f617f65ec162eb8
Batch ID: 20250612_135957
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
from typing import Dict, List, Tuple

class SlotMachineVersion(Enum):
    CLASSIC = "Classic"
    DELUXE = "Deluxe"

class Symbol(Enum):
    CHERRY = "Cherry"
    LEMON = "Lemon"
    ORANGE = "Orange"
    PLUM = "Plum"
    BELL = "Bell"
    BAR = "Bar"
    SEVEN = "Seven"
    DIAMOND = "Diamond"  # Only in Deluxe version

class SlotMachine:
    def __init__(self, version: SlotMachineVersion):
        self.version = version
        self.reels = 3
        self.payouts = self._initialize_payouts()
        self.symbols = self._initialize_symbols()

    def _initialize_symbols(self) -> List[Symbol]:
        base_symbols = [
            Symbol.CHERRY,
            Symbol.LEMON,
            Symbol.ORANGE,
            Symbol.PLUM,
            Symbol.BELL,
            Symbol.BAR,
            Symbol.SEVEN
        ]
        if self.version == SlotMachineVersion.DELUXE:
            base_symbols.append(Symbol.DIAMOND)
        return base_symbols

    def _initialize_payouts(self) -> Dict[Tuple[Symbol, ...], int]:
        base_payouts = {
            (Symbol.CHERRY, Symbol.CHERRY, Symbol.CHERRY): 50,
            (Symbol.LEMON, Symbol.LEMON, Symbol.LEMON): 20,
            (Symbol.ORANGE, Symbol.ORANGE, Symbol.ORANGE): 20,
            (Symbol.PLUM, Symbol.PLUM, Symbol.PLUM): 20,
            (Symbol.BELL, Symbol.BELL, Symbol.BELL): 15,
            (Symbol.BAR, Symbol.BAR, Symbol.BAR): 10,
            (Symbol.SEVEN, Symbol.SEVEN, Symbol.SEVEN): 100,
        }
        
        if self.version == SlotMachineVersion.DELUXE:
            deluxe_payouts = {
                (Symbol.DIAMOND, Symbol.DIAMOND, Symbol.DIAMOND): 200,
                (Symbol.SEVEN, Symbol.SEVEN, Symbol.DIAMOND): 50,
                (Symbol.DIAMOND, Symbol.DIAMOND, Symbol.SEVEN): 50,
                (Symbol.SEVEN, Symbol.DIAMOND, Symbol.SEVEN): 50,
            }
            base_payouts.update(deluxe_payouts)
        
        return base_payouts

    def spin(self) -> Tuple[Symbol, Symbol, Symbol]:
        return tuple(random.choice(self.symbols) for _ in range(self.reels))

    def calculate_payout(self, spin_result: Tuple[Symbol, Symbol, Symbol]) -> int:
        return self.payouts.get(spin_result, 0)

    def play_round(self, bet: int) -> Tuple[Tuple[Symbol, Symbol, Symbol], int]:
        if bet <= 0:
            raise ValueError("Bet amount must be positive")
        
        spin_result = self.spin()
        payout = self.calculate_payout(spin_result)
        return spin_result, payout * bet

def simulate_plays(machine: SlotMachine, num_plays: int, bet_per_play: int) -> Dict[str, float]:
    total_wagered = num_plays * bet_per_play
    total_won = 0
    wins = 0

    for _ in range(num_plays):
        try:
            _, payout = machine.play_round(bet_per_play)
            total_won += payout
            if payout > 0:
                wins += 1
        except ValueError as e:
            print(f"Error during play: {e}")

    rtp = (total_won / total_wagered) * 100 if total_wagered > 0 else 0
    win_percentage = (wins / num_plays) * 100 if num_plays > 0 else 0

    return {
        "total_wagered": total_wagered,
        "total_won": total_won,
        "rtp": rtp,
        "win_percentage": win_percentage,
        "net_result": total_won - total_wagered
    }

def main():
    # Configuration
    NUM_SIMULATIONS = 100000
    BET_PER_PLAY = 1

    # Simulate Classic version
    classic = SlotMachine(SlotMachineVersion.CLASSIC)
    classic_results = simulate_plays(classic, NUM_SIMULATIONS, BET_PER_PLAY)

    # Simulate Deluxe version
    deluxe = SlotMachine(SlotMachineVersion.DELUXE)
    deluxe_results = simulate_plays(deluxe, NUM_SIMULATIONS, BET_PER_PLAY)

    # Print results
    print("\nMerkur Slot Machine Simulation Results")
    print("------------------------------------")
    print(f"Number of simulations per version: {NUM_SIMULATIONS:,}")
    print(f"Bet per play: {BET_PER_PLAY}\n")

    print("Classic Version:")
    print(f"  Total Wagered: {classic_results['total_wagered']:,}")
    print(f"  Total Won: {classic_results['total_won']:,}")
    print(f"  RTP: {classic_results['rtp']:.2f}%")
    print(f"  Win Percentage: {classic_results['win_percentage']:.2f}%")
    print(f"  Net Result: {classic_results['net_result']:,}\n")

    print("Deluxe Version:")
    print(f"  Total Wagered: {deluxe_results['total_wagered']:,}")
    print(f"  Total Won: {deluxe_results['total_won']:,}")
    print(f"  RTP: {deluxe_results['rtp']:.2f}%")
    print(f"  Win Percentage: {deluxe_results['win_percentage']:.2f}%")
    print(f"  Net Result: {deluxe_results['net_result']:,}")

if __name__ == "__main__":
    main()
```
