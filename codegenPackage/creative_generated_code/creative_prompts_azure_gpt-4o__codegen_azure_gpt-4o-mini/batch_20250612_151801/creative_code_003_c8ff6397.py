"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kubitz.com.br
Prompt: Write a script to calculate the cost-benefit ratio of implementing modular conveyor belts, such as Kubitz Esteiras, with varying lengths and configurations.
Generated: DETERMINISTIC_c8ff63978ff75a2f
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class ConveyorBelt:
    """Class representing a conveyor belt with a specific length and cost."""

    def __init__(self, length: float, cost: float):
        """
        Initializes a new ConveyorBelt instance.

        Args:
            length (float): The length of the conveyor belt in meters.
            cost (float): The cost of the conveyor belt in currency.

        Raises:
            ValueError: If length or cost is negative.
        """
        if length < 0 or cost < 0:
            raise ValueError("Length and cost must be non-negative.")
        self.length = length
        self.cost = cost

    def calculate_benefit(self, efficiency_gain: float) -> float:
        """
        Calculates the benefit of the conveyor belt based on efficiency gain.

        Args:
            efficiency_gain (float): The efficiency gain in percentage.

        Returns:
            float: The benefit as a monetary value.
        """
        return self.cost * (efficiency_gain / 100)

    def cost_benefit_ratio(self, efficiency_gain: float) -> float:
        """
        Calculates the cost-benefit ratio of the conveyor belt.

        Args:
            efficiency_gain (float): The efficiency gain in percentage.

        Returns:
            float: The cost-benefit ratio.

        Raises:
            ZeroDivisionError: If benefit is zero.
        """
        benefit = self.calculate_benefit(efficiency_gain)
        if benefit == 0:
            raise ZeroDivisionError("Benefit cannot be zero, cannot calculate cost-benefit ratio.")
        return benefit / self.cost

def main():
    """Main function to run the cost-benefit analysis."""
    try:
        # Example inputs - these could be modified or taken from user input
        conveyor_belts = [
            ConveyorBelt(length=10, cost=5000),
            ConveyorBelt(length=20, cost=10000),
            ConveyorBelt(length=30, cost=15000)
        ]
        
        # Simulated efficiency gains for analysis
        efficiency_gains = [5, 10, 15]  # In percentage
        
        for belt in conveyor_belts:
            for gain in efficiency_gains:
                try:
                    ratio = belt.cost_benefit_ratio(gain)
                    print(f"Cost-Benefit Ratio for belt of length {belt.length}m with {gain}% efficiency gain: {ratio:.2f}")
                except ZeroDivisionError as e:
                    print(f"Error calculating cost-benefit ratio for belt of length {belt.length}m with {gain}% efficiency gain: {e}")

    except ValueError as e:
        print(f"Initialization error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
