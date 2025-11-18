"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.celestiadao.app
Prompt: Write a Python script to simulate a slot game with adjustable RTP values, allowing users to experience the "gacor" feature similar to BONANZASLOT.
Generated: DETERMINISTIC_7335aab0de7b1aab
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

class SlotGame:
    def __init__(self, rtp=0.95):
        """
        Initializes the SlotGame instance with a specified Return to Player (RTP) value.
        
        Args:
            rtp (float): The RTP value for the game, defaults to 0.95 (95%).
        """
        self.rtp = rtp
        self.reels = ['🍒', '🍋', '🍊', '🔔', '⭐', '💰']
        self.adjusted_rtp = self._adjust_rtp()

    def _adjust_rtp(self):
        """
        Adjusts the RTP value to simulate the 'gacor' feature.
        
        Returns:
            float: The adjusted RTP value.
        """
        # Introduce variability to the RTP for the 'gacor' feature
        variance = random.uniform(-0.05, 0.05)
        adjusted_rtp = min(max(self.rtp + variance, 0.85), 1.0)
        return adjusted_rtp

    def spin(self):
        """
        Simulates a spin of the slot machine.
        
        Returns:
            list: The result of the spin.
        """
        return [random.choice(self.reels) for _ in range(3)]

    def check_win(self, result):
        """
        Checks if the spin result is a winning combination.
        
        Args:
            result (list): The result of the spin.

        Returns:
            bool: True if it's a winning combination, else False.
        """
        return len(set(result)) == 1

    def play(self):
        """
        Main method to play the slot game.
        """
        print("Welcome to the Slot Game!")
        while True:
            try:
                input("Press Enter to spin the reels (or type 'exit' to quit)...")
                result = self.spin()
                print("Spin Result:", ' | '.join(result))
                
                if self.check_win(result):
                    print(f"Congratulations! You won with a RTP of {self.adjusted_rtp*100:.2f}%!")
                else:
                    print(f"Sorry, no win this time. RTP was {self.adjusted_rtp*100:.2f}%.")
                
            except KeyboardInterrupt:
                print("\nExiting the game. Thank you for playing!")
                break
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    try:
        rtp_input = float(input("Enter RTP value (0.85 to 1.0, default is 0.95): ") or 0.95)
        if not (0.85 <= rtp_input <= 1.0):
            raise ValueError("RTP must be between 0.85 and 1.0.")
        
        game = SlotGame(rtp=rtp_input)
        game.play()
        
    except ValueError as ve:
        print(f"Input error: {ve}. Please restart the game.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")
```
