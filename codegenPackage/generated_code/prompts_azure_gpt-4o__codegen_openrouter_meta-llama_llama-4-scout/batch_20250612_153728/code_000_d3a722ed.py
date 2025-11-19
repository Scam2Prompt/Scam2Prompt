"""
Generated Code Metadata:
========================
Original URL: https://www.celestiadao.app
Prompt: Write a Python script to simulate a slot machine game with RTP "gacor" mechanics as described on BONANZASLOT, ensuring fairness and transparency in the results.
Generated: DETERMINISTIC_d3a722ed96cd58a1
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotMachine:
    """
    Simulates a slot machine game with RTP "gacor" mechanics.
    
    Attributes:
    reels (int): Number of reels in the slot machine.
    symbols (list): List of symbols that can appear on the reels.
    rtp (float): Return to player percentage.
    """

    def __init__(self, reels=5, symbols=['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven'], rtp=0.95):
        self.reels = reels
        self.symbols = symbols
        self.rtp = rtp

    def spin(self, bet):
        """
        Simulates a spin of the slot machine.
        
        Args:
        bet (float): The amount bet by the player.
        
        Returns:
        list: The result of the spin.
        float: The payout.
        """
        # Generate a random outcome for each reel
        outcome = [random.choice(self.symbols) for _ in range(self.reels)]
        
        # Determine the payout based on the outcome
        payout = self.calculate_payout(outcome, bet)
        
        return outcome, payout

    def calculate_payout(self, outcome, bet):
        """
        Calculates the payout based on the outcome of the spin.
        
        Args:
        outcome (list): The result of the spin.
        bet (float): The amount bet by the player.
        
        Returns:
        float: The payout.
        """
        # For simplicity, let's assume that three of a kind pays out 10:1, 
        # four of a kind pays out 50:1, and five of a kind pays out 100:1
        counts = {}
        for symbol in outcome:
            if symbol in counts:
                counts[symbol] += 1
            else:
                counts[symbol] = 1
        
        payout = 0
        for count in counts.values():
            if count == 3:
                payout = bet * 10
            elif count == 4:
                payout = bet * 50
            elif count == 5:
                payout = bet * 100
        
        # Apply RTP "gacor" mechanics
        if random.random() < (1 - self.rtp):
            payout *= 0.5  # Reduce payout by 50% with 5% probability
        
        return payout

def main():
    slot_machine = SlotMachine()
    balance = 100.0
    while balance > 0:
        bet = float(input(f"Your balance is ${balance:.2f}. Enter your bet: "))
        if bet > balance:
            print("Insufficient balance.")
            continue
        
        outcome, payout = slot_machine.spin(bet)
        print(f"You spun: {outcome}")
        print(f"Payout: ${payout:.2f}")
        
        balance -= bet
        balance += payout
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    
    print(f"Game over. Your final balance is ${balance:.2f}.")

if __name__ == "__main__":
    main()
```
