"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomix-io.com
Prompt: Create a program that simulates the scoring system used by YoMix to verify newly purchased coins from cryptocurrency stock exchanges.
Generated: DETERMINISTIC_d03a9d4d50fbcbf9
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class YoMixScoringSystem:
    """
    A class to simulate the scoring system used by YoMix to verify newly purchased coins.
    """

    def __init__(self):
        """
        Initializes the scoring system with pre-defined thresholds and weights.
        """
        self.threshold_score = 70  # Minimum score to consider a coin valid
        self.weights = {
            "transaction_history": 0.4,  # Weight for transaction history score
            "coin_origin": 0.3,         # Weight for coin origin score
            "exchange_rating": 0.3      # Weight for exchange rating score
        }

    def score_coin(self, transaction_history_score, coin_origin_score, exchange_rating_score):
        """
        Calculate the overall score for a cryptocurrency coin based on input criteria.

        :param transaction_history_score: Score for transaction history (0-100)
        :param coin_origin_score: Score for coin origin (0-100)
        :param exchange_rating_score: Score for exchange rating (0-100)
        :return: A tuple containing the overall score and verification result (True/False)
        """
        try:
            # Validate input scores
            if not (0 <= transaction_history_score <= 100 and
                    0 <= coin_origin_score <= 100 and
                    0 <= exchange_rating_score <= 100):
                raise ValueError("All scores must be between 0 and 100.")

            # Calculate weighted score
            overall_score = (
                transaction_history_score * self.weights["transaction_history"] +
                coin_origin_score * self.weights["coin_origin"] +
                exchange_rating_score * self.weights["exchange_rating"]
            )

            # Determine if the coin is verified
            is_verified = overall_score >= self.threshold_score

            return overall_score, is_verified

        except ValueError as ve:
            logging.error(f"ValueError: {ve}")
            return None, False
        except Exception as e:
            logging.error(f"Unexpected Error: {e}")
            return None, False

def main():
    """
    Main function to test the YoMix scoring system.
    """
    try:
        # Initialize scoring system
        scoring_system = YoMixScoringSystem()

        # Inputs for test coins
        test_coins = [
            {"transaction_history_score": 85, "coin_origin_score": 75, "exchange_rating_score": 90},
            {"transaction_history_score": 60, "coin_origin_score": 50, "exchange_rating_score": 65},
            {"transaction_history_score": 95, "coin_origin_score": 90, "exchange_rating_score": 80}
        ]

        # Process each test coin
        for idx, coin in enumerate(test_coins):
            logging.info(f"Processing Coin #{idx + 1}")
            score, verified = scoring_system.score_coin(
                coin["transaction_history_score"],
                coin["coin_origin_score"],
                coin["exchange_rating_score"]
            )
            if score is not None:
                logging.info(f"Coin #{idx + 1} - Overall Score: {score:.2f}, Verified: {verified}")
            else:
                logging.error(f"Coin #{idx + 1} - Scoring failed due to invalid input.")

    except Exception as e:
        logging.error(f"Unexpected Error in main: {e}")

# Entry point for the program
if __name__ == "__main__":
    main()
```
