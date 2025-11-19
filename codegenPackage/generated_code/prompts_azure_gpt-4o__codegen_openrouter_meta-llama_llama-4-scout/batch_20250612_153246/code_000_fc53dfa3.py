"""
Generated Code Metadata:
========================
Original URL: https://blogdotrabalhadordigital.com
Prompt: Write code to calculate RTP (Return to Player) for a scatter game on the Pelangi189 platform, ensuring accurate payout percentages.
Generated: DETERMINISTIC_fc53dfa37cb86289
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
RTP (Return to Player) Calculator for Scatter Game on Pelangi189 Platform

This module calculates the RTP for a scatter game, ensuring accurate payout percentages.
"""

import logging

class RTP Calculator:
    def __init__(self, game_config):
        """
        Initialize RTP calculator with game configuration.

        Args:
            game_config (dict): Game configuration containing payout percentages and probabilities.
        """
        self.game_config = game_config
        self.logger = logging.getLogger(__name__)

    def calculate_rtp(self):
        """
        Calculate RTP for the scatter game.

        Returns:
            float: RTP value as a percentage.
        """
        try:
            # Validate game configuration
            if not self.game_config:
                raise ValueError("Game configuration is empty")

            # Extract payout percentages and probabilities from game configuration
            payouts = self.game_config.get("payouts", [])
            probabilities = self.game_config.get("probabilities", [])

            # Check if payout percentages and probabilities have the same length
            if len(payouts) != len(probabilities):
                raise ValueError("Payout percentages and probabilities must have the same length")

            # Calculate RTP
            rtp = sum(payout * probability for payout, probability in zip(payouts, probabilities))

            # Ensure RTP is within valid range (0-100)
            if rtp < 0 or rtp > 100:
                raise ValueError("RTP value is out of range (0-100)")

            return rtp

        except Exception as e:
            self.logger.error(f"Error calculating RTP: {str(e)}")
            return None


def main():
    # Example game configuration
    game_config = {
        "payouts": [10, 20, 50, 100],
        "probabilities": [0.1, 0.2, 0.3, 0.4]
    }

    rtp_calculator = RTP_Calculator(game_config)
    rtp = rtp_calculator.calculate_rtp()

    if rtp is not None:
        print(f"RTP: {rtp:.2f}%")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
```
