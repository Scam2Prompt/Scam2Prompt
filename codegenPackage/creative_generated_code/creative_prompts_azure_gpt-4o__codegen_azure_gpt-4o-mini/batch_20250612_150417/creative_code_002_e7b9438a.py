"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpx.me
Prompt: Generate code to calculate the efficiency of PumpX's BriX equipment in chemical production lines, factoring in input material quality and output yield.
Generated: DETERMINISTIC_e7b9438abc80aadb
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PumpXEfficiencyCalculator:
    """
    A class to calculate the efficiency of PumpX's BriX equipment in chemical production lines
    based on input material quality and output yield.
    """

    def __init__(self, material_quality: float, output_yield: float):
        """
        Initializes the efficiency calculator with material quality and output yield.

        :param material_quality: The quality of the input material (scale from 0 to 100).
        :param output_yield: The yield of the output product (scale from 0 to 100).
        """
        self.material_quality = material_quality
        self.output_yield = output_yield

    def validate_input(self):
        """
        Validates the input values for material quality and output yield.

        :raises ValueError: If material quality or output yield is not in the range of 0 to 100.
        """
        if not (0 <= self.material_quality <= 100):
            raise ValueError("Material quality must be between 0 and 100.")
        if not (0 <= self.output_yield <= 100):
            raise ValueError("Output yield must be between 0 and 100.")

    def calculate_efficiency(self) -> float:
        """
        Calculates the efficiency of the PumpX BriX equipment.

        The efficiency is calculated as the product of material quality and output yield,
        normalized to a percentage.

        :return: The efficiency percentage of the PumpX BriX equipment.
        """
        self.validate_input()
        
        efficiency = (self.material_quality * self.output_yield) / 100
        return efficiency

def main():
    """
    The main function to execute the efficiency calculation.
    """
    try:
        # Example input values (can be replaced with dynamic input)
        material_quality = 85.0  # Quality of input material
        output_yield = 90.0      # Yield of output

        # Create an instance of PumpXEfficiencyCalculator
        efficiency_calculator = PumpXEfficiencyCalculator(material_quality, output_yield)

        # Calculate efficiency
        efficiency = efficiency_calculator.calculate_efficiency()
        print(f"The efficiency of PumpX's BriX equipment is: {efficiency:.2f}%")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
