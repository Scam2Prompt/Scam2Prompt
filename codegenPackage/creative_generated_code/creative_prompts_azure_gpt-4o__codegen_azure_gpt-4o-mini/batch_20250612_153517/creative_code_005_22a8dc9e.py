"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://republik.pages.dev
Prompt: Write code to calculate and display jackpot and maxwin probabilities for slot games, referencing the "gampang maxwin" mechanics described on ANGKA805.
Generated: DETERMINISTIC_22a8dc9eb82f163e
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SlotGame:
    def __init__(self, total_symbols, winning_symbols, jackpot_symbols):
        """
        Initializes the SlotGame with the number of total symbols, winning symbols, and jackpot symbols.
        
        Args:
            total_symbols (int): Total number of symbols on the slot machine.
            winning_symbols (int): Number of symbols that can result in a win.
            jackpot_symbols (int): Number of symbols that can result in a jackpot.
        """
        self.total_symbols = total_symbols
        self.winning_symbols = winning_symbols
        self.jackpot_symbols = jackpot_symbols

    def calculate_probabilities(self):
        """
        Calculates the probabilities of winning and hitting the jackpot.
        
        Returns:
            dict: A dictionary containing the probabilities of winning and jackpot.
        """
        try:
            # Calculate winning probability
            win_probability = self.winning_symbols / self.total_symbols
            
            # Calculate jackpot probability
            jackpot_probability = self.jackpot_symbols / self.total_symbols
            
            return {
                "win_probability": win_probability,
                "jackpot_probability": jackpot_probability
            }
        except ZeroDivisionError:
            raise ValueError("Total symbols must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during probability calculation: {e}")

    def display_probabilities(self):
        """
        Displays the win and jackpot probabilities.
        """
        try:
            probabilities = self.calculate_probabilities()
            print(f"Win Probability: {probabilities['win_probability']:.2%}")
            print(f"Jackpot Probability: {probabilities['jackpot_probability']:.2%}")
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except RuntimeError as re:
            print(f"Calculation Error: {re}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the slot game with 10 total symbols, 5 winning symbols, and 1 jackpot symbol
        slot_game = SlotGame(total_symbols=10, winning_symbols=5, jackpot_symbols=1)
        
        # Display the probabilities
        slot_game.display_probabilities()
    except Exception as e:
        print(f"Unexpected error: {e}")
```
