"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinotg.pages.dev
Prompt: Write a program to calculate the rewards for players participating in TG.Casino's seasonal airdrops based on their wagering activity.
Generated: DETERMINISTIC_90b090a420e136a6
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class RewardCalculator:
    """
    A class to calculate rewards for players based on their wagering activity.
    """

    def __init__(self, wager_data: pd.DataFrame):
        """
        Initializes the RewardCalculator with wager data.
        
        Args:
            wager_data (pd.DataFrame): DataFrame containing player wager data with columns 'player_id' and 'wager_amount'.
        """
        if not isinstance(wager_data, pd.DataFrame):
            raise ValueError("Wager data must be a pandas DataFrame.")
        if 'player_id' not in wager_data.columns or 'wager_amount' not in wager_data.columns:
            raise ValueError("Wager data must contain 'player_id' and 'wager_amount' columns.")
        
        self.wager_data = wager_data

    def calculate_rewards(self) -> pd.DataFrame:
        """
        Calculates the rewards for each player based on their total wager amounts.
        
        Returns:
            pd.DataFrame: A DataFrame with player_id and corresponding reward.
        """
        # Group by player_id and sum the wager amounts
        total_wagers = self.wager_data.groupby('player_id')['wager_amount'].sum().reset_index()
        
        # Calculate rewards based on a simple policy:
        # Reward 1% of the wager amount, capped at a maximum of 100 per player
        total_wagers['reward'] = total_wagers['wager_amount'] * 0.01
        total_wagers['reward'] = total_wagers['reward'].clip(upper=100)  # Cap rewards at 100
        
        return total_wagers[['player_id', 'reward']]

def main():
    # Sample wager data for demonstration
    data = {
        'player_id': ['player1', 'player2', 'player1', 'player3', 'player2'],
        'wager_amount': [500, 800, 700, 300, 1500]
    }
    
    wager_df = pd.DataFrame(data)
    
    try:
        # Initialize the RewardCalculator
        reward_calculator = RewardCalculator(wager_df)
        
        # Calculate rewards
        rewards = reward_calculator.calculate_rewards()
        print("Calculated Rewards:")
        print(rewards)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
