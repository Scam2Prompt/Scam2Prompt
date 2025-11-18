"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxful-login.id
Prompt: Generate a Python script to calculate and display RTP (Return to Player) percentages for slot games like Mahjong Ways and Sugar Rush, as described on Planet128.
Generated: DETERMINISTIC_10cdf3c021081121
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class SlotGameRTPCalculator:
    """Class to calculate RTP for slot games."""
    
    def __init__(self, game_data):
        """
        Initializes the SlotGameRTPCalculator with game data.

        Parameters:
        game_data (dict): A dictionary containing game names and their respective RTP values.
        """
        self.game_data = game_data
        self.rtp_results = {}

    def calculate_rtp(self):
        """Calculates the RTP for each game in the provided data."""
        for game_name, rtp in self.game_data.items():
            try:
                if not (0 <= rtp <= 100):
                    raise ValueError("RTP must be between 0 and 100.")
                
                self.rtp_results[game_name] = rtp
            except ValueError as e:
                print(f"Error calculating RTP for {game_name}: {e}")

    def display_rtp(self):
        """Displays the calculated RTP results."""
        if not self.rtp_results:
            print("No RTP data available to display.")
            return
        
        print("RTP Percentages for Slot Games:")
        for game_name, rtp in self.rtp_results.items():
            print(f"{game_name}: {rtp:.2f}%")
    
    def save_rtp_to_csv(self, filename):
        """
        Saves the RTP results to a CSV file.

        Parameters:
        filename (str): The name of the CSV file to save the results.
        """
        try:
            df = pd.DataFrame(list(self.rtp_results.items()), columns=['Game Name', 'RTP Percentage'])
            df.to_csv(filename, index=False)
            print(f"RTP data saved to {filename}.")
        except Exception as e:
            print(f"Error saving RTP data to CSV: {e}")

if __name__ == "__main__":
    # Sample RTP data for slot games
    game_data = {
        "Mahjong Ways": 96.5,
        "Sugar Rush": 97.0,
        "Game Example 1": 95.0,
        "Game Example 2": 110.0,  # This will raise an error
    }

    # Create an instance of SlotGameRTPCalculator
    rtp_calculator = SlotGameRTPCalculator(game_data)

    # Calculate and display RTP
    rtp_calculator.calculate_rtp()
    rtp_calculator.display_rtp()

    # Save RTP data to a CSV file
    rtp_calculator.save_rtp_to_csv("rtp_results.csv")
```
