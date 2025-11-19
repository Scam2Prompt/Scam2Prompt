"""
Generated Code Metadata:
========================
Original URL: https://lanimal443331.github.io
Prompt: Generate code to simulate the high-to-low pricing mechanism used in Fjord Foundry's LBPs for community-driven price discovery.
Generated: DETERMINISTIC_973241b1f0c69876
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class FjordFoundryLBP:
    """
    Simulates the high-to-low pricing mechanism used in Fjord Foundry's LBPs for community-driven price discovery.
    """

    def __init__(self, 
                 initial_weight: float, 
                 final_weight: float, 
                 initial_supply: float, 
                 final_supply: float, 
                 start_time: int, 
                 end_time: int, 
                 total_time: int):
        """
        Initializes the Fjord Foundry LBP simulator.

        Args:
        - initial_weight (float): The initial weight of the LBP.
        - final_weight (float): The final weight of the LBP.
        - initial_supply (float): The initial supply of the token.
        - final_supply (float): The final supply of the token.
        - start_time (int): The start time of the LBP in seconds.
        - end_time (int): The end time of the LBP in seconds.
        - total_time (int): The total duration of the LBP in seconds.
        """

        self.initial_weight = initial_weight
        self.final_weight = final_weight
        self.initial_supply = initial_supply
        self.final_supply = final_supply
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = total_time

        # Validate inputs
        if self.initial_weight <= 0 or self.final_weight <= 0:
            raise ValueError("Weights must be greater than zero.")
        if self.initial_supply < 0 or self.final_supply < 0:
            raise ValueError("Supplies must be non-negative.")
        if self.start_time < 0 or self.end_time < 0 or self.total_time < 0:
            raise ValueError("Times must be non-negative.")
        if self.start_time >= self.end_time:
            raise ValueError("Start time must be less than end time.")

    def _calculate_weight(self, time_elapsed: int) -> float:
        """
        Calculates the current weight based on the time elapsed.

        Args:
        - time_elapsed (int): The time elapsed since the start of the LBP in seconds.

        Returns:
        - float: The current weight of the LBP.
        """

        # Calculate the weight using the formula: w = w0 * (wf / w0)^(t / T)
        # where w0 is the initial weight, wf is the final weight, t is the time elapsed, and T is the total time
        weight = self.initial_weight * (self.final_weight / self.initial_weight)**(time_elapsed / self.total_time)
        return weight

    def _calculate_supply(self, time_elapsed: int) -> float:
        """
        Calculates the current supply based on the time elapsed.

        Args:
        - time_elapsed (int): The time elapsed since the start of the LBP in seconds.

        Returns:
        - float: The current supply of the token.
        """

        # Calculate the supply using the formula: s = s0 + (sf - s0) * (t / T)
        # where s0 is the initial supply, sf is the final supply, t is the time elapsed, and T is the total time
        supply = self.initial_supply + (self.final_supply - self.initial_supply) * (time_elapsed / self.total_time)
        return supply

    def _calculate_price(self, time_elapsed: int) -> float:
        """
        Calculates the current price based on the time elapsed.

        Args:
        - time_elapsed (int): The time elapsed since the start of the LBP in seconds.

        Returns:
        - float: The current price of the token.
        """

        weight = self._calculate_weight(time_elapsed)
        supply = self._calculate_supply(time_elapsed)

        # Calculate the price using the formula: p = w / s
        if supply <= 0:
            raise ValueError("Supply cannot be zero or negative.")
        price = weight / supply
        return price

    def simulate(self, time_points: list) -> dict:
        """
        Simulates the LBP at multiple time points.

        Args:
        - time_points (list): A list of time points to simulate.

        Returns:
        - dict: A dictionary with time points as keys and corresponding prices as values.
        """

        # Validate time points
        for time_point in time_points:
            if time_point < self.start_time or time_point > self.end_time:
                raise ValueError("Time points must be within the LBP duration.")

        # Simulate the LBP at each time point
        results = {}
        for time_point in time_points:
            time_elapsed = time_point - self.start_time
            price = self._calculate_price(time_elapsed)
            results[time_point] = price

        return results


# Example usage:
if __name__ == "__main__":
    lbp = FjordFoundryLBP(
        initial_weight=1000.0,
        final_weight=500.0,
        initial_supply=1000.0,
        final_supply=2000.0,
        start_time=0,
        end_time=86400,  # 1 day
        total_time=86400  # 1 day
    )

    time_points = [0, 43200, 86400]  # simulate at start, middle, and end of LBP
    results = lbp.simulate(time_points)
    print(results)
```
