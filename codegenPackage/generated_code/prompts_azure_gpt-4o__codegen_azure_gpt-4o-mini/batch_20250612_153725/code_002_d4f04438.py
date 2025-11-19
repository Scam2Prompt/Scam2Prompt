"""
Generated Code Metadata:
========================
Original URL: https://epsys.ro
Prompt: Create a Python function to calculate the probability of winning in different lottery markets (e.g., 4D, 6D, 7D) based on the rules described for Hondatoto's Japan Lottery Association system.
Generated: DETERMINISTIC_d4f0443884d3a922
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class LotteryProbabilityCalculator:
    """
    A class to calculate the probability of winning in different lottery markets.
    """

    def __init__(self):
        """
        Initializes the LotteryProbabilityCalculator.
        """
        pass

    @staticmethod
    def calculate_probability(total_numbers: int, drawn_numbers: int) -> float:
        """
        Calculate the probability of winning based on total numbers and drawn numbers.

        :param total_numbers: Total numbers in the lottery pool.
        :param drawn_numbers: Number of numbers drawn in the lottery.
        :return: Probability of winning.
        :raises ValueError: If total_numbers or drawn_numbers are not positive integers.
        """
        if total_numbers <= 0 or drawn_numbers <= 0:
            raise ValueError("Total numbers and drawn numbers must be positive integers.")
        if drawn_numbers > total_numbers:
            raise ValueError("Drawn numbers cannot exceed total numbers.")

        # Calculate the number of combinations
        combinations = math.comb(total_numbers, drawn_numbers)
        probability = 1 / combinations
        return probability

    def probability_4d(self) -> float:
        """
        Calculate the probability of winning in the 4D lottery.

        :return: Probability of winning in the 4D lottery.
        """
        return self.calculate_probability(total_numbers=10000, drawn_numbers=4)

    def probability_6d(self) -> float:
        """
        Calculate the probability of winning in the 6D lottery.

        :return: Probability of winning in the 6D lottery.
        """
        return self.calculate_probability(total_numbers=1000000, drawn_numbers=6)

    def probability_7d(self) -> float:
        """
        Calculate the probability of winning in the 7D lottery.

        :return: Probability of winning in the 7D lottery.
        """
        return self.calculate_probability(total_numbers=10000000, drawn_numbers=7)

# Example usage
if __name__ == "__main__":
    calculator = LotteryProbabilityCalculator()
    try:
        print(f"Probability of winning 4D: {calculator.probability_4d():.10f}")
        print(f"Probability of winning 6D: {calculator.probability_6d():.10f}")
        print(f"Probability of winning 7D: {calculator.probability_7d():.10f}")
    except ValueError as e:
        print(f"Error calculating probability: {e}")
```
