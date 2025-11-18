"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchainairdrop1.pages.dev
Prompt: Create a Python script to calculate token rewards for nodes contributing AI computations (e.g., model training or optimization) under Lightchain AI’s Proof-of-Intelligence mechanism.
Generated: DETERMINISTIC_99f54c774afdd7ae
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal, InvalidOperation

class TokenRewardCalculator:
    """
    A class to calculate token rewards for nodes contributing AI computations under Lightchain AI’s Proof-of-Intelligence mechanism.
    """

    def __init__(self, base_reward: Decimal, performance_factor: Decimal):
        """
        Initializes the TokenRewardCalculator with a base reward and performance factor.

        :param base_reward: The base reward for contributing computations.
        :param performance_factor: The multiplier based on the node's performance.
        """
        if base_reward < 0 or performance_factor < 0:
            raise ValueError("Base reward and performance factor must be non-negative.")
        
        self.base_reward = base_reward
        self.performance_factor = performance_factor

    def calculate_reward(self, computation_time: Decimal, quality_score: Decimal) -> Decimal:
        """
        Calculates the token reward based on computation time and quality score.

        :param computation_time: The time spent on computations in hours.
        :param quality_score: A score indicating the quality of computations (0 to 1).
        :return: The calculated token reward.
        """
        if computation_time < 0:
            raise ValueError("Computation time must be non-negative.")
        if not (0 <= quality_score <= 1):
            raise ValueError("Quality score must be between 0 and 1.")
        
        # Reward calculation
        reward = self.base_reward * computation_time * (self.performance_factor * quality_score)
        return reward

    def to_json(self) -> str:
        """
        Converts the current state of the calculator to a JSON string.

        :return: JSON string representation of the current state.
        """
        return json.dumps({
            'base_reward': str(self.base_reward),
            'performance_factor': str(self.performance_factor)
        })

def main():
    """
    Main function to demonstrate the token reward calculation.
    """
    try:
        # Example initialization
        base_reward = Decimal('10.0')  # Base reward in tokens
        performance_factor = Decimal('1.5')  # Performance multiplier
        calculator = TokenRewardCalculator(base_reward, performance_factor)

        # Example computation inputs
        computation_time = Decimal('5.0')  # Hours
        quality_score = Decimal('0.8')  # Quality score between 0 and 1

        # Calculate the reward
        reward = calculator.calculate_reward(computation_time, quality_score)

        # Output the results
        print(f"Token Reward: {reward:.2f} tokens")
        print("Calculator State (JSON):", calculator.to_json())

    except (ValueError, InvalidOperation) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
