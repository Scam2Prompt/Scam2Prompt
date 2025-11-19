"""
Generated Code Metadata:
========================
Original URL: https://metis2020.com
Prompt: Write a Python code snippet to implement a simple slot machine game using the QRIS payment method, considering the RTP and transaction ease mentioned on Satria4D.
Generated: DETERMINISTIC_76678623b41f4935
Batch ID: 20250622_210316
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
    def __init__(self, rtp=0.95):
        """
        Initializes the SlotMachine with a specified Return to Player (RTP) percentage.
        
        :param rtp: float, the RTP percentage (default is 0.95)
        """
        self.rtp = rtp
        self.symbols = ['🍒', '🍋', '🍊', '🍉', '🍇', '🔔', '⭐']
        self.reels = 3  # Number of reels in the slot machine

    def spin(self):
        """
        Simulates a spin of the slot machine.
        
        :return: list of symbols representing the outcome of the spin
        """
        return [random.choice(self.symbols) for _ in range(self.reels)]

    def calculate_payout(self, spin_result):
        """
        Calculates the payout based on the spin result.
        
        :param spin_result: list of symbols from the spin
        :return: int, payout multiplier based on the result
        """
        if len(set(spin_result)) == 1:  # All symbols are the same
            return 10  # Example payout for three of a kind
        elif len(set(spin_result)) == 2:  # Two symbols are the same
            return 5  # Example payout for two of a kind
        return 0  # No payout

    def play(self, bet_amount):
        """
        Plays a round of the slot machine with a specified bet amount.
        
        :param bet_amount: float, the amount to bet
        :return: float, net gain or loss from the round
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")
        
        spin_result = self.spin()
        payout_multiplier = self.calculate_payout(spin_result)
        payout = payout_multiplier * bet_amount
        
        # Calculate net gain/loss
        net_result = payout - bet_amount
        return net_result, spin_result

def main():
    """
    Main function to run the slot machine game.
    """
    print("Welcome to the Slot Machine Game!")
    rtp = 0.95  # Set RTP
    slot_machine = SlotMachine(rtp)

    while True:
        try:
            bet_amount = float(input("Enter your bet amount (or type 'exit' to quit): "))
            net_result, spin_result = slot_machine.play(bet_amount)
            print(f"Spin result: {spin_result}")
            if net_result > 0:
                print(f"You won! Net gain: {net_result:.2f}")
            else:
                print(f"You lost! Net loss: {abs(net_result):.2f}")
        except ValueError as e:
            if str(e) == "could not convert string to float: 'exit'":
                print("Thank you for playing!")
                break
            else:
                print(f"Error: {e}. Please enter a valid bet amount.")

if __name__ == "__main__":
    main()
```
