"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur-nft-marketplace.org
Prompt: Generate code for tracking and calculating RTP values for a gambling platform, similar to the RTP monitoring system mentioned on PAIZA99.
Generated: DETERMINISTIC_22b6375dec834300
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RTPTracker:
    """
    Class to track and calculate Return to Player (RTP) values for a gambling platform.
    """
    
    def __init__(self):
        """
        Initializes the RTPTracker with an empty records list.
        """
        self.records: List[Dict[str, float]] = []

    def add_game_result(self, game_name: str, bet_amount: float, payout_amount: float) -> None:
        """
        Adds a game result to the records.

        Args:
            game_name (str): The name of the game played.
            bet_amount (float): The amount of money bet on the game.
            payout_amount (float): The amount of money won from the game.

        Raises:
            ValueError: If bet_amount is negative or payout_amount is negative.
        """
        if bet_amount < 0:
            logging.error("Bet amount cannot be negative.")
            raise ValueError("Bet amount cannot be negative.")
        if payout_amount < 0:
            logging.error("Payout amount cannot be negative.")
            raise ValueError("Payout amount cannot be negative.")
        
        self.records.append({
            'game_name': game_name,
            'bet_amount': bet_amount,
            'payout_amount': payout_amount
        })
        logging.info(f"Added game result: {game_name}, Bet: {bet_amount}, Payout: {payout_amount}")

    def calculate_rtp(self) -> Dict[str, float]:
        """
        Calculates the RTP for each game and overall RTP.

        Returns:
            Dict[str, float]: A dictionary with game names as keys and their RTP values, 
                              along with an overall RTP value.
        """
        rtp_values: Dict[str, float] = {}
        total_bets = 0.0
        total_payouts = 0.0

        for record in self.records:
            total_bets += record['bet_amount']
            total_payouts += record['payout_amount']
            if record['game_name'] not in rtp_values:
                rtp_values[record['game_name']] = {'total_bets': 0.0, 'total_payouts': 0.0}
            rtp_values[record['game_name']]['total_bets'] += record['bet_amount']
            rtp_values[record['game_name']]['total_payouts'] += record['payout_amount']

        # Calculate individual RTP values
        for game_name, values in rtp_values.items():
            if values['total_bets'] > 0:
                rtp_values[game_name] = (values['total_payouts'] / values['total_bets']) * 100
            else:
                rtp_values[game_name] = 0.0

        # Calculate overall RTP
        overall_rtp = (total_payouts / total_bets) * 100 if total_bets > 0 else 0.0
        rtp_values['overall_rtp'] = overall_rtp

        logging.info(f"Calculated RTP values: {rtp_values}")
        return rtp_values

# Example usage:
if __name__ == "__main__":
    tracker = RTPTracker()
    try:
        tracker.add_game_result("Slot Machine", 100.0, 90.0)
        tracker.add_game_result("Roulette", 200.0, 220.0)
        tracker.add_game_result("Blackjack", 150.0, 0.0)
        
        rtp = tracker.calculate_rtp()
        print(f"RTP values: {rtp}")
    except ValueError as e:
        logging.error(f"Error occurred: {e}")
```
