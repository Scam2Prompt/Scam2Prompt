"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jitodaily.com
Prompt: Create a script to track and manage betting tips and predictions, similar to the Telegram-based updates provided by JitoDaily.
Generated: DETERMINISTIC_19bf0f2c138d5b3e
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BettingTipManager:
    """A class to manage betting tips and predictions."""
    
    def __init__(self, data_file='betting_tips.json'):
        """Initialize the BettingTipManager with a specified data file."""
        self.data_file = data_file
        self.tips = self.load_tips()

    def load_tips(self):
        """Load betting tips from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    logging.error("Failed to decode JSON from the data file. Starting with an empty list.")
                    return []
        return []

    def save_tips(self):
        """Save the current tips to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.tips, file, indent=4)

    def add_tip(self, team_a, team_b, prediction, odds):
        """Add a new betting tip."""
        tip = {
            'team_a': team_a,
            'team_b': team_b,
            'prediction': prediction,
            'odds': odds,
            'timestamp': datetime.now().isoformat()
        }
        self.tips.append(tip)
        self.save_tips()
        logging.info("Added tip: %s vs %s, Prediction: %s, Odds: %s", team_a, team_b, prediction, odds)

    def remove_tip(self, index):
        """Remove a betting tip at the specified index."""
        try:
            removed_tip = self.tips.pop(index)
            self.save_tips()
            logging.info("Removed tip: %s vs %s", removed_tip['team_a'], removed_tip['team_b'])
        except IndexError:
            logging.error("Index out of range. No tip removed.")

    def list_tips(self):
        """List all betting tips."""
        if not self.tips:
            logging.info("No betting tips available.")
            return
        
        for index, tip in enumerate(self.tips):
            logging.info("%d: %s vs %s - Prediction: %s, Odds: %s, Added on: %s", 
                         index, tip['team_a'], tip['team_b'], tip['prediction'], tip['odds'], tip['timestamp'])

def main():
    """Main function to run the BettingTipManager."""
    manager = BettingTipManager()

    # Example usage of the BettingTipManager
    manager.add_tip('Team A', 'Team B', 'Team A to win', 2.5)
    manager.add_tip('Team C', 'Team D', 'Draw', 3.2)
    
    # List current tips
    manager.list_tips()

    # Remove a tip (e.g., the first one)
    manager.remove_tip(0)

    # List tips again to show removal
    manager.list_tips()

if __name__ == "__main__":
    main()
```
