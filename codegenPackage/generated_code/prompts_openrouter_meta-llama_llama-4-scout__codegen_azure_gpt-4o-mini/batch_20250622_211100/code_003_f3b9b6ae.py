"""
Generated Code Metadata:
========================
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: Create a leaderboard for a trading platform, including columns for ranking, trader names, and trade volumes.
Generated: DETERMINISTIC_f3b9b6ae88dd49f3
Batch ID: 20250622_211100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class Leaderboard:
    def __init__(self):
        """Initialize the leaderboard with an empty DataFrame."""
        self.leaderboard_df = pd.DataFrame(columns=['Rank', 'Trader Name', 'Trade Volume'])

    def add_trade(self, trader_name: str, trade_volume: float):
        """
        Add a trade to the leaderboard.

        Args:
            trader_name (str): The name of the trader.
            trade_volume (float): The volume of the trade.

        Raises:
            ValueError: If trade_volume is negative or trader_name is empty.
        """
        if not trader_name:
            raise ValueError("Trader name cannot be empty.")
        if trade_volume < 0:
            raise ValueError("Trade volume cannot be negative.")

        # Add the trade to the DataFrame
        new_trade = pd.DataFrame({'Trader Name': [trader_name], 'Trade Volume': [trade_volume]})
        self.leaderboard_df = pd.concat([self.leaderboard_df, new_trade], ignore_index=True)

    def update_leaderboard(self):
        """Update the leaderboard rankings based on trade volumes."""
        # Group by trader name and sum their trade volumes
        grouped_df = self.leaderboard_df.groupby('Trader Name', as_index=False).sum()
        # Sort by trade volume in descending order and assign ranks
        grouped_df = grouped_df.sort_values(by='Trade Volume', ascending=False)
        grouped_df['Rank'] = range(1, len(grouped_df) + 1)
        # Reorder columns
        self.leaderboard_df = grouped_df[['Rank', 'Trader Name', 'Trade Volume']]

    def display_leaderboard(self):
        """Display the current leaderboard."""
        if self.leaderboard_df.empty:
            print("The leaderboard is currently empty.")
        else:
            print(self.leaderboard_df.to_string(index=False))

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding trades
    try:
        leaderboard.add_trade("Alice", 1500.0)
        leaderboard.add_trade("Bob", 2500.0)
        leaderboard.add_trade("Charlie", 2000.0)
        
        # Update and display the leaderboard
        leaderboard.update_leaderboard()
        leaderboard.display_leaderboard()
    except ValueError as e:
        print(f"Error: {e}")
```
