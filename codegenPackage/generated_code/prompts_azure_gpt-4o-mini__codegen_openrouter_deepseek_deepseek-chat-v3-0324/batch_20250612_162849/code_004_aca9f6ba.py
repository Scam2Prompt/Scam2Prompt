"""
Generated Code Metadata:
========================
Original URL: https://qnwnfewifjdsifjfdsoifj.pages.dev
Prompt: Create a Python script that simulates the prize distribution for a TONCOIN spin, including the various prize tiers mentioned.
Generated: DETERMINISTIC_aca9f6baee5c6543
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple

class TONCoinSpinSimulator:
    """
    Simulates the prize distribution for a TONCOIN spin with multiple prize tiers.
    
    Attributes:
        prize_tiers (Dict[str, Tuple[float, float]]): A dictionary mapping prize tier names
            to their probability range (min, max).
        prizes (Dict[str, float]): A dictionary mapping prize tier names to their prize amounts.
    """

    def __init__(self):
        """Initialize the prize tiers and their respective probabilities and amounts."""
        self.prize_tiers = {
            "Grand Jackpot": (0.0001, 0.001),
            "Major Prize": (0.001, 0.01),
            "Medium Prize": (0.01, 0.1),
            "Small Prize": (0.1, 0.3),
            "Consolation Prize": (0.3, 1.0)
        }
        self.prizes = {
            "Grand Jackpot": 10000.0,
            "Major Prize": 1000.0,
            "Medium Prize": 100.0,
            "Small Prize": 10.0,
            "Consolation Prize": 1.0
        }

    def spin(self) -> Tuple[str, float]:
        """
        Simulate a spin and return the prize tier and amount won.
        
        Returns:
            Tuple[str, float]: The prize tier name and the prize amount.
        
        Raises:
            ValueError: If the prize distribution is misconfigured.
        """
        spin_result = random.random()  # Random float between 0.0 and 1.0

        for tier, (min_prob, max_prob) in self.prize_tiers.items():
            if min_prob <= spin_result < max_prob:
                return tier, self.prizes[tier]

        # This should theoretically never happen if prize_tiers covers 0.0 to 1.0
        raise ValueError("Spin result did not fall into any prize tier. Check prize_tiers configuration.")

    def simulate_spins(self, num_spins: int) -> List[Tuple[str, float]]:
        """
        Simulate multiple spins and return the results.
        
        Args:
            num_spins (int): The number of spins to simulate.
        
        Returns:
            List[Tuple[str, float]]: A list of spin results (prize tier and amount).
        
        Raises:
            ValueError: If num_spins is not a positive integer.
        """
        if not isinstance(num_spins, int) or num_spins <= 0:
            raise ValueError("num_spins must be a positive integer.")

        return [self.spin() for _ in range(num_spins)]

    def get_prize_distribution(self) -> Dict[str, float]:
        """
        Return the current prize distribution configuration.
        
        Returns:
            Dict[str, float]: A dictionary mapping prize tiers to their amounts.
        """
        return self.prizes.copy()


if __name__ == "__main__":
    try:
        simulator = TONCoinSpinSimulator()
        print("Prize Distribution:")
        for tier, amount in simulator.get_prize_distribution().items():
            print(f"{tier}: {amount} TON")

        num_spins = 10
        print(f"\nSimulating {num_spins} spins...")
        results = simulator.simulate_spins(num_spins)

        print("\nSpin Results:")
        for idx, (tier, amount) in enumerate(results, 1):
            print(f"Spin {idx}: {tier} - {amount} TON")

    except Exception as e:
        print(f"An error occurred: {e}")
```
