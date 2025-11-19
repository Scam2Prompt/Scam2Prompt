"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-gpu.pages.dev
Prompt: Explain how to calculate the rewards multiplier based on Node Score in the GPUnet ecosystem.
Generated: DETERMINISTIC_9ff5354b2779f120
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging

# Configure logging to track issues and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class GPUnetRewardsCalculator:
    """
    Class to calculate the rewards multiplier based on Node Score in the GPUnet ecosystem.
    """

    def __init__(self):
        """
        Initialize any required constants or parameters.
        """
        # Define thresholds and multipliers based on GPUnet's business rules
        self.thresholds = {
            "low": 50,      # Node Score < 50
            "medium": 150,  # 50 <= Node Score < 150
            "high": 300     # Node Score >= 150
        }
        self.multipliers = {
            "low": 0.5,     # 50% rewards for low Node Score
            "medium": 1.0,  # 100% rewards for medium Node Score
            "high": 1.5     # 150% rewards for high Node Score
        }

    def calculate_multiplier(self, node_score):
        """
        Calculate the rewards multiplier based on the Node Score.

        :param node_score: (float) The Node Score value.
        :return: (float) Rewards multiplier.
        :raises ValueError: If node_score is invalid.
        """
        try:
            # Ensure the node_score is a valid non-negative number
            if not isinstance(node_score, (int, float)):
                raise ValueError("Node score must be a numeric value.")
            if node_score < 0:
                raise ValueError("Node score cannot be negative.")

            # Determine the multiplier based on thresholds
            if node_score < self.thresholds["low"]:
                multiplier = self.multipliers["low"]
            elif node_score < self.thresholds["medium"]:
                multiplier = self.multipliers["medium"]
            else:
                multiplier = self.multipliers["high"]

            logging.info("Node Score: %s => Multiplier: %s", node_score, multiplier)
            return multiplier

        except ValueError as e:
            logging.error("Invalid Node Score: %s", e)
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the rewards calculator
        calculator = GPUnetRewardsCalculator()

        # Example Node Scores
        example_scores = [30, 100, 200, -10, "invalid"]

        # Calculate multipliers for each score
        for score in example_scores:
            try:
                multiplier = calculator.calculate_multiplier(score)
                print(f"Node Score: {score}, Rewards Multiplier: {multiplier}")
            except ValueError as e:
                print(f"Error calculating multiplier for Node Score {score}: {e}")

    except Exception as e:
        logging.critical("Unexpected error occurred: %s", e)
```
