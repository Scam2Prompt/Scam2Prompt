"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxful-login.id
Prompt: Write code to simulate a slot machine game with high RTP settings, inspired by the games listed on Planet128, such as Gates of Olympus or Sweet Bonanza.
Generated: DETERMINISTIC_183dd97ff1cfc5e3
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SlotMachineGame:
    """
    A class to simulate a slot machine game.

    Attributes:
        symbols (list): List of symbols appearing on the reels.
        high_rtp (float): High Return-To-Player percentage (e.g., 0.96 for 96% RTP).
    """
    def __init__(self, symbols=None, high_rtp=0.96):
        """
        Initializes the SlotMachineGame with symbols and RTP settings.

        Args:
            symbols (list): Optional list of symbols. Defaults to predefined symbols.
            high_rtp (float): RTP percentage for the game. Defaults to 0.96.
        """
        self.symbols = symbols or ["🍒", "🍋", "🍊", "🍇", "🍓", "💎", "⭐", "🥇"]
        self.high_rtp = high_rtp

    def spin(self):
        """
        Simulates spinning the slot machine.

        Returns:
            dict: Result of the spin including the reels and potential payout.
        """
        try:
            # Generate random reel results
            reel1 = random.choice(self.symbols)
            reel2 = random.choice(self.symbols)
            reel3 = random.choice(self.symbols)
            
            reels = [reel1, reel2, reel3]
            
            # RTP logic: chance of payout is based on high RTP percentage
            payout = 0
            if random.random() < self.high_rtp:
                if reel1 == reel2 == reel3:  # Jackpot condition
                    payout = 100  # Jackpot payout
                elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
                    payout = 20  # Moderate payout for 2 matching symbols
                else:
                    payout = 10  # Small payout for participation
            
            return {
                "reels": reels,
                "payout": payout
            }
        
        except Exception as e:
            # Handle unexpected errors during spin
            return {
                "error": str(e)
            }

def main():
    """
    Main function to run the slot machine simulation.
    """
    print("Welcome to the Slot Machine Game!")
    print("Spin the reels and test your luck!\n")
    
    game = SlotMachineGame()

    while True:
        user_input = input("\nPress Enter to spin (or type 'exit' to quit): ").strip().lower()
        
        if user_input == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        
        result = game.spin()
        
        # Display reel results
        if "error" in result:
            print(f"An error occurred during the spin: {result['error']}")
        else:
            print(f"\nReels: {' | '.join(result['reels'])}")
            print(f"Payout: {result['payout']} coins")

if __name__ == "__main__":
    main()
```
