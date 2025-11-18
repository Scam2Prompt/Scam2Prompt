"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grampreico.com
Prompt: Write Python code to simulate a slot machine game with high RTP values and customizable themes, inspired by the features of nagoya168 online.
Generated: DETERMINISTIC_68a9ddcc1771272f
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Slot Machine Game
class SlotMachine:
    def __init__(self, theme="Default", rtp=0.95):
        """
        Initialize the slot machine with customizable theme and RTP values.
        
        Args:
            theme (str): Name of the theme for the slot machine.
            rtp (float): Return to player percentage (default 95%).
        """
        self.theme = theme
        self.rtp = max(0.80, min(rtp, 0.99))  # Ensuring RTP is within reasonable bounds (80% to 99%).
        self.symbols = self._get_theme_symbols(theme)
        self.reels = 3  # Number of reels in the slot machine.
        self.paylines = 5  # Number of paylines for winnings.
    
    def _get_theme_symbols(self, theme):
        """
        Get symbols based on the selected theme.
        
        Args:
            theme (str): Name of the theme to retrieve symbols for.
        
        Returns:
            list: List of slot machine symbols.
        """
        themes = {
            "Default": ["Cherry", "Lemon", "Bell", "Bar", "Seven"],
            "Ocean": ["Fish", "Shell", "Starfish", "Treasure", "Boat"],
            "Space": ["Rocket", "Planet", "Star", "Alien", "Galaxy"],
        }
        return themes.get(theme, themes["Default"])

    def spin(self, bet):
        """
        Spin the slot machine based on the bet amount.
        
        Args:
            bet (float): Amount of money wagered by the player.
        
        Returns:
            dict: Outcome of the spin including result and potential winnings.
        """
        if bet <= 0:
            return {"error": "Bet must be greater than zero."}
        
        # Simulate spin outcome
        outcome = [[random.choice(self.symbols) for _ in range(self.reels)] for _ in range(self.paylines)]
        winnings = self._calculate_winnings(outcome, bet)
        
        return {
            "theme": self.theme,
            "outcome": outcome,
            "winnings": winnings
        }

    def _calculate_winnings(self, outcome, bet):
        """
        Calculate winnings based on the spin outcome and RTP.
        
        Args:
            outcome (list): 2D list representing the spin outcome.
            bet (float): Amount of money wagered by the player.
        
        Returns:
            float: Total winnings based on RTP and matching symbols.
        """
        # Simplified winnings calculation based on RTP and matching symbols in paylines
        winnings = 0
        for line in outcome:
            if len(set(line)) == 1:  # All symbols match in the line
                winnings += bet * self.rtp * random.uniform(1.0, 3.0)  # Random multiplier for matched lines
        return round(winnings, 2)

# Main program
def main():
    print("Welcome to the Slot Machine Game!")
    print("Available themes: Default, Ocean, Space")
    theme = input("Choose your theme: ").strip()
    rtp = input("Enter RTP value (80-99): ").strip()
    
    try:
        rtp = float(rtp) / 100  # Convert RTP percentage to decimal
    except ValueError:
        print("Invalid RTP value. Using default RTP (95%).")
        rtp = 0.95
    
    slot_machine = SlotMachine(theme=theme, rtp=rtp)
    print(f"Theme: {slot_machine.theme}, RTP: {round(slot_machine.rtp * 100, 2)}%")
    
    while True:
        try:
            bet = float(input("Place your bet (enter 0 to exit): ").strip())
            if bet == 0:
                print("Thank you for playing!")
                break
            result = slot_machine.spin(bet)
            
            if "error" in result:
                print(result["error"])
                continue
            
            print("\nSpin Outcome:")
            for line in result["outcome"]:
                print(line)
            
            print(f"You won: ${result['winnings']:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number for your bet.")

# Entry point for the program
if __name__ == "__main__":
    main()
```
