"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.vercel.app
Prompt: Create a function using the PolyMarket codebase to simulate market outcomes based on user-provided probabilities.
Generated: DETERMINISTIC_6e1bc0e024d6cd79
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import Dict, Any, Tuple

class MarketSimulator:
    """
    A class to simulate market outcomes based on user-provided probabilities.

    Attributes:
        probabilities (Dict[str, float]): A dictionary where keys are outcome names
                                            and values are their associated probabilities.
    """

    def __init__(self, probabilities: Dict[str, float]):
        """
        Initializes the MarketSimulator with the provided probabilities.

        Args:
            probabilities (Dict[str, float]): A dictionary of probabilities.

        Raises:
            ValueError: If probabilities do not sum to 1 or any probability is out of range [0, 1].
        """
        self.validate_probabilities(probabilities)
        self.probabilities = probabilities

    @staticmethod
    def validate_probabilities(probabilities: Dict[str, float]):
        """
        Validates that the provided probabilities are correct.

        Args:
            probabilities (Dict[str, float]): A dictionary of probabilities.

        Raises:
            ValueError: If probabilities do not sum to 1 or any probability is out of range [0, 1].
        """
        total = sum(probabilities.values())
        if not all(0 <= prob <= 1 for prob in probabilities.values()):
            raise ValueError("All probabilities must be in the range [0, 1].")
        if abs(total - 1.0) > 1e-6:
            raise ValueError("Probabilities must sum to 1.")

    def simulate_outcome(self) -> str:
        """
        Simulates an outcome based on the defined probabilities.

        Returns:
            str: The outcome that was simulated.
        """
        # Create a cumulative distribution for the given probabilities
        cumulative_distribution: List[Tuple[str, float]] = []
        cumulative_sum = 0.0

        for outcome, probability in self.probabilities.items():
            cumulative_sum += probability
            cumulative_distribution.append((outcome, cumulative_sum))

        # Generate a random number and find the corresponding outcome
        random_value = random.random()
        for outcome, cumulative_prob in cumulative_distribution:
            if random_value < cumulative_prob:
                return outcome

        return None  # Fallback, should never hit this due to validation

# Example of how to use the MarketSimulator
if __name__ == "__main__":
    try:
        # Define probabilities for outcomes
        outcomes = {
            "Outcome A": 0.5,
            "Outcome B": 0.3,
            "Outcome C": 0.2
        }

        # Create a MarketSimulator instance
        market_simulator = MarketSimulator(outcomes)

        # Simulate and print the outcome
        result = market_simulator.simulate_outcome()
        print(f"Simulated Outcome: {result}")
        
    except ValueError as e:
        print(f"Error occurred: {e}")
```
