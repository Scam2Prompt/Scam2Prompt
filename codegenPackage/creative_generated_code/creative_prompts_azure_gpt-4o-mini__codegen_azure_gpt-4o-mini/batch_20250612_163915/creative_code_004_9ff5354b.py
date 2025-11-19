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
class GPUNetRewardCalculator:
    """
    A class to calculate the rewards multiplier based on the Node Score in the GPUnet ecosystem.
    """

    def __init__(self, base_multiplier: float = 1.0):
        """
        Initializes the reward calculator with a base multiplier.

        Args:
            base_multiplier (float): The base multiplier for the calculations.
        """
        if base_multiplier <= 0:
            raise ValueError("Base multiplier must be greater than 0.")
        self.base_multiplier = base_multiplier

    def calculate_multiplier(self, node_score: float) -> float:
        """
        Calculates the rewards multiplier based on the given Node Score.

        Args:
            node_score (float): The score of the node, which affects the rewards multiplier.

        Returns:
            float: The calculated rewards multiplier.

        Raises:
            ValueError: If node_score is negative.
        """
        if node_score < 0:
            raise ValueError("Node Score cannot be negative.")
        
        # Define threshold values and multipliers
        if node_score < 50:
            multiplier = 0.5  # Low score, low multiplier
        elif 50 <= node_score < 100:
            multiplier = 1.0  # Medium score, base multiplier
        elif 100 <= node_score < 150:
            multiplier = 1.5  # High score, higher multiplier
        else:
            multiplier = 2.0  # Very high score, maximum multiplier
        
        # Calculate the final rewards multiplier
        final_multiplier = self.base_multiplier * multiplier
        return final_multiplier

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the reward calculator
        reward_calculator = GPUNetRewardCalculator(base_multiplier=1.0)

        # Example Node Scores
        scores = [30, 75, 120, 200]

        # Calculate and print multipliers for each score
        for score in scores:
            multiplier = reward_calculator.calculate_multiplier(score)
            print(f"Node Score: {score}, Rewards Multiplier: {multiplier:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
