"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.celestiadao.app
Prompt: Write a Python script to simulate a slot machine game with RTP "gacor" mechanics as described on BONANZASLOT, ensuring fairness and transparency in the results.
Generated: DETERMINISTIC_d3a722ed96cd58a1
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SlotMachine:
    def __init__(self, symbols, payouts, rtp):
        """
        Initialize a SlotMachine instance.

        :param symbols: List of symbols on the slot machine.
        :param payouts: Dictionary mapping symbols to their payout values.
        :param rtp: Return to player percentage (0 < rtp < 100).
        """
        if not (0 < rtp < 100):
            raise ValueError("RTP must be between 0 and 100.")
        
        self.symbols = symbols
        self.payouts = payouts
        self.rtp = rtp

    def spin(self):
        """
        Simulate a spin of the slot machine.

        :return: A tuple of symbols that appeared on the spin.
        """
        return tuple(random.choices(self.symbols, k=3))

    def calculate_payout(self, spin_result):
        """
        Calculate the payout based on the spin results.

        :param spin_result: Tuple of symbols from the spin.
        :return: Payout amount.
        """
        payout = 0
        if len(set(spin_result)) == 1:  # All symbols are the same
            symbol = spin_result[0]
            payout = self.payouts.get(symbol, 0)
        return payout

    def play(self, bet):
        """
        Play a round of the slot machine.

        :param bet: The amount of money wagered.
        :return: A tuple containing the spin result and the payout.
        """
        if bet <= 0:
            raise ValueError("Bet must be greater than zero.")

        spin_result = self.spin()
        payout = self.calculate_payout(spin_result)
        
        # Apply RTP mechanics
        expected_loss = bet * (1 - self.rtp / 100)
        actual_payout = payout - expected_loss

        return spin_result, max(actual_payout, 0)  # Ensure no negative payout

def main():
    # Define symbols and their corresponding payouts
    symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']
    payouts = {
        'Cherry': 10,
        'Lemon': 20,
        'Orange': 30,
        'Plum': 40,
        'Bell': 50,
        'Bar': 100,
        'Seven': 200
    }

    # Initialize the slot machine with a 95% RTP
    slot_machine = SlotMachine(symbols, payouts, rtp=95)

    # Example of playing the game
    try:
        while True:
            bet = float(input("Enter your bet (0 to quit): "))
            if bet == 0:
                print("Thank you for playing!")
                break
            spin_result, payout = slot_machine.play(bet)
            print(f"Spin result: {spin_result}, Payout: {payout}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
