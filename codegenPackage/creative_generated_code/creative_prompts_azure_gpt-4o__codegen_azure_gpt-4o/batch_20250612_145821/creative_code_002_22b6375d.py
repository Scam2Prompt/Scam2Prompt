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

# Configure logging to track application flow and errors
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("rtp_calculator.log"), logging.StreamHandler()]
)

class RTPTracker:
    """
    Class to track and calculate RTP (Return to Player) values for a gambling platform.
    """

    def __init__(self):
        # A dictionary to store game data: {game_id: {'total_bets': float, 'total_payouts': float}}
        self.games_data: Dict[str, Dict[str, float]] = {}

    def record_bet(self, game_id: str, amount: float) -> None:
        """
        Records a bet for a specific game.
        :param game_id: Unique identifier of the game.
        :param amount: Bet amount.
        """
        if game_id not in self.games_data:
            self.games_data[game_id] = {'total_bets': 0.0, 'total_payouts': 0.0}
        # Update the total bets
        self.games_data[game_id]['total_bets'] += amount
        logging.info(f"Recorded bet: Game ID {game_id}, Amount {amount}")

    def record_payout(self, game_id: str, amount: float) -> None:
        """
        Records a payout for a specific game.
        :param game_id: Unique identifier of the game.
        :param amount: Payout amount.
        """
        if game_id not in self.games_data:
            self.games_data[game_id] = {'total_bets': 0.0, 'total_payouts': 0.0}
        # Update the total payouts
        self.games_data[game_id]['total_payouts'] += amount
        logging.info(f"Recorded payout: Game ID {game_id}, Amount {amount}")

    def calculate_rtp(self, game_id: str) -> float:
        """
        Calculates the RTP (Return to Player) for a specific game.
        :param game_id: Unique identifier of the game.
        :return: RTP value as a percentage.
        """
        if game_id not in self.games_data:
            logging.error(f"Game ID {game_id} not found.")
            raise ValueError(f"Game ID {game_id} not found.")
        game_data = self.games_data[game_id]
        total_bets = game_data['total_bets']
        total_payouts = game_data['total_payouts']

        if total_bets == 0:
            logging.warning(f"Total bets for Game ID {game_id} is zero. Cannot calculate RTP.")
            return 0.0  # Return 0% RTP if no bets have been placed.

        # Calculate RTP as (Total Payouts / Total Bets) * 100
        rtp = (total_payouts / total_bets) * 100
        logging.info(f"Calculated RTP for Game ID {game_id}: {rtp:.2f}%")
        return rtp

    def get_summary(self) -> List[Dict[str, float]]:
        """
        Provides a summary of all games with their RTP values.
        :return: A list of dictionaries containing game summaries.
        """
        summary = []
        for game_id, data in self.games_data.items():
            rtp = self.calculate_rtp(game_id)
            summary.append({
                'game_id': game_id,
                'total_bets': data['total_bets'],
                'total_payouts': data['total_payouts'],
                'rtp': rtp
            })
        logging.info("Generated summary for all games.")
        return summary


if __name__ == "__main__":
    # Example usage of the RTPTracker class

    # Initialize the tracker
    tracker = RTPTracker()

    # Record some bets and payouts
    try:
        tracker.record_bet("game_1", 100.0)
        tracker.record_payout("game_1", 95.0)
        tracker.record_bet("game_1", 50.0)
        tracker.record_payout("game_1", 25.0)
        tracker.record_bet("game_2", 200.0)
        tracker.record_payout("game_2", 180.0)

        # Calculate RTP for individual games
        print(f"RTP for game_1: {tracker.calculate_rtp('game_1'):.2f}%")
        print(f"RTP for game_2: {tracker.calculate_rtp('game_2'):.2f}%")

        # Generate a summary of all games
        summary = tracker.get_summary()
        print("Game Summary:")
        for game in summary:
            print(game)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
