"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Generate a Python script to analyze poker game data and calculate RTP (Return to Player) percentages, similar to DominoBet's 99.55% RTP rate.
Generated: DETERMINISTIC_a5bac739bc37a3c1
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class PokerGameAnalyzer:
    """
    A class to analyze poker game data and calculate the Return to Player (RTP) percentage.
    """

    def __init__(self, data):
        """
        Initializes the PokerGameAnalyzer with game data.

        :param data: A pandas DataFrame containing poker game results with 'amount_bet' and 'amount_won' columns.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the input data to ensure it contains the required columns.

        :raises ValueError: If required columns are missing.
        """
        required_columns = ['amount_bet', 'amount_won']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_rtp(self):
        """
        Calculates the RTP (Return to Player) percentage based on the game data.

        :return: The RTP percentage as a float.
        """
        self.validate_data()

        total_bet = self.data['amount_bet'].sum()
        total_won = self.data['amount_won'].sum()

        if total_bet == 0:
            return 0.0  # Avoid division by zero, return 0% RTP

        rtp = (total_won / total_bet) * 100
        return rtp

    def run_analysis(self):
        """
        Executes the analysis and returns the RTP percentage.

        :return: The calculated RTP percentage.
        """
        try:
            rtp = self.calculate_rtp()
            return rtp
        except Exception as e:
            print(f"An error occurred during analysis: {e}")
            return None

def main():
    # Example usage:
    # Create a sample DataFrame with poker game data
    sample_data = {
        'amount_bet': [100, 200, 150, 300, 250],
        'amount_won': [90, 220, 130, 280, 200]
    }
    
    poker_data = pd.DataFrame(sample_data)

    # Initialize the analyzer
    analyzer = PokerGameAnalyzer(poker_data)

    # Run the analysis and print the RTP
    rtp_percentage = analyzer.run_analysis()
    if rtp_percentage is not None:
        print(f"Calculated RTP: {rtp_percentage:.2f}%")

if __name__ == "__main__":
    main()
```
