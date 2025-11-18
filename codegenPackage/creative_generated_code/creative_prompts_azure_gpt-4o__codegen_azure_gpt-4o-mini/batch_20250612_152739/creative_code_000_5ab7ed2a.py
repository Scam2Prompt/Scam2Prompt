"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herramientasharo.shop
Prompt: Write Python code to calculate the power output (in watts) for a Predator generator model listed on the Haro Outlet website, given its maximum start wattage and running wattage.
Generated: DETERMINISTIC_5ab7ed2a55c80492
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PredatorGenerator:
    """
    A class to represent a Predator generator.

    Attributes:
        max_start_wattage (float): The maximum starting wattage of the generator.
        running_wattage (float): The running wattage of the generator.
    """

    def __init__(self, max_start_wattage: float, running_wattage: float):
        """
        Initializes the PredatorGenerator with maximum start wattage and running wattage.

        Parameters:
            max_start_wattage (float): The maximum starting wattage of the generator.
            running_wattage (float): The running wattage of the generator.
        """
        if max_start_wattage <= 0 or running_wattage <= 0:
            raise ValueError("Wattages must be positive numbers.")

        self.max_start_wattage = max_start_wattage
        self.running_wattage = running_wattage

    def calculate_power_output(self) -> float:
        """
        Calculates the effective power output of the generator.

        Returns:
            float: The calculated power output in watts.

        Raises:
            ValueError: If running wattage exceeds maximum starting wattage.
        """
        if self.running_wattage > self.max_start_wattage:
            raise ValueError("Running wattage cannot exceed maximum starting wattage.")

        # The power output for the generator can be considered as the running wattage
        return self.running_wattage

def main():
    """
    The main function to create a PredatorGenerator instance and calculate power output.
    """
    try:
        # Example values for the generator's wattages
        max_start_wattage = 4000.0  # Maximum starting wattage in watts
        running_wattage = 3500.0      # Running wattage in watts

        # Create an instance of PredatorGenerator
        generator = PredatorGenerator(max_start_wattage, running_wattage)

        # Calculate and print the power output
        power_output = generator.calculate_power_output()
        print(f"The power output of the Predator generator is: {power_output:.2f} watts")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
