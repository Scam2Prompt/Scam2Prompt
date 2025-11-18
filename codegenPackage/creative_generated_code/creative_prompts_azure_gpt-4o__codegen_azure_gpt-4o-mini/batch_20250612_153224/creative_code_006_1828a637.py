"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Develop an algorithm to estimate the risk reduction in fatalities when fire sprinklers are installed, using the 80% decrease statistic mentioned by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_1828a63754208300
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FireSprinklerRiskReductionEstimator:
    """
    A class to estimate the risk reduction in fatalities when fire sprinklers are installed.
    """

    def __init__(self, initial_fatalities: int):
        """
        Initializes the estimator with the number of initial fatalities.

        :param initial_fatalities: The number of fatalities before the installation of fire sprinklers.
        :raises ValueError: If the number of initial fatalities is negative.
        """
        if initial_fatalities < 0:
            raise ValueError("Initial fatalities cannot be negative.")
        self.initial_fatalities = initial_fatalities
        self.decrease_percentage = 0.80  # 80% risk reduction

    def estimate_risk_reduction(self) -> float:
        """
        Estimates the number of fatalities after the installation of fire sprinklers.

        :return: The estimated number of fatalities after the risk reduction.
        """
        risk_reduction = self.initial_fatalities * self.decrease_percentage
        estimated_fatalities = self.initial_fatalities - risk_reduction
        
        return estimated_fatalities

    def display_results(self):
        """
        Displays the initial and estimated fatalities.
        """
        try:
            estimated_fatalities = self.estimate_risk_reduction()
            print(f"Initial Fatalities: {self.initial_fatalities}")
            print(f"Estimated Fatalities After Sprinkler Installation: {estimated_fatalities:.2f}")
        except Exception as e:
            print(f"An error occurred while estimating risk reduction: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        initial_fatalities_input = int(input("Enter the initial number of fatalities: "))
        estimator = FireSprinklerRiskReductionEstimator(initial_fatalities_input)
        estimator.display_results()
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
