"""
Generated Code Metadata:
========================
Original URL: https://pumpx.me
Prompt: Generate code to calculate the efficiency of PumpX's BriX equipment in chemical production lines, factoring in input material quality and output yield.
Generated: DETERMINISTIC_e7b9438abc80aadb
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PumpXEfficiencyCalculator:
    """
    A class to calculate the efficiency of PumpX's BriX equipment in chemical production lines.
    
    Attributes:
        input_quality (float): The quality of the input material (0 to 100).
        output_yield (float): The yield of the output material (0 to 100).
    """

    def __init__(self, input_quality: float, output_yield: float):
        """
        Initializes the PumpXEfficiencyCalculator with input material quality and output yield.
        
        Args:
            input_quality (float): The quality of the input material.
            output_yield (float): The yield of the output material.
        
        Raises:
            ValueError: If input_quality or output_yield is not in the range [0, 100].
        """
        self.set_input_quality(input_quality)
        self.set_output_yield(output_yield)

    def set_input_quality(self, input_quality: float):
        """Sets the input material quality, ensuring it is within the valid range."""
        if not (0 <= input_quality <= 100):
            raise ValueError("Input quality must be between 0 and 100.")
        self.input_quality = input_quality

    def set_output_yield(self, output_yield: float):
        """Sets the output yield, ensuring it is within the valid range."""
        if not (0 <= output_yield <= 100):
            raise ValueError("Output yield must be between 0 and 100.")
        self.output_yield = output_yield

    def calculate_efficiency(self) -> float:
        """
        Calculates the efficiency of the PumpX's BriX equipment.
        
        Efficiency is calculated as the ratio of output yield to input quality.
        
        Returns:
            float: The efficiency percentage.
        """
        if self.input_quality == 0:
            raise ZeroDivisionError("Input quality cannot be zero when calculating efficiency.")
        
        efficiency = (self.output_yield / self.input_quality) * 100
        return efficiency

    def __str__(self):
        """Returns a string representation of the efficiency calculation."""
        return f"PumpX Efficiency: {self.calculate_efficiency():.2f}%"

# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of the efficiency calculator
        pump_x = PumpXEfficiencyCalculator(input_quality=85.0, output_yield=75.0)
        
        # Calculate and print the efficiency
        print(pump_x)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
```
