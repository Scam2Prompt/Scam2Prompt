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
# Program to calculate the efficiency of PumpX's BriX equipment
# in chemical production lines based on input material quality and output yield.

class PumpXEfficiencyCalculator:
    """
    A class to calculate the efficiency of PumpX's BriX equipment.
    """

    def __init__(self, input_quality: float, output_yield: float):
        """
        Initializes the Calculator with input material quality and output yield.
        
        :param input_quality: A float representing the quality of input material (0.0 to 1.0).
        :param output_yield: A float representing the yield of output material (0.0 to 1.0).
        """
        self.input_quality = input_quality
        self.output_yield = output_yield

    def validate_inputs(self):
        """
        Validates the input parameters to ensure they are within the correct range.
        
        :raises ValueError: If input_quality or output_yield is not in the range [0.0, 1.0].
        """
        if not (0.0 <= self.input_quality <= 1.0):
            raise ValueError("Input material quality must be between 0.0 and 1.0.")
        if not (0.0 <= self.output_yield <= 1.0):
            raise ValueError("Output yield must be between 0.0 and 1.0.")

    def calculate_efficiency(self) -> float:
        """
        Calculates the efficiency of the equipment.
        
        Efficiency is defined as the product of input quality and output yield,
        scaled to a percentage.
        
        :return: A float representing the efficiency in percentage.
        """
        # Ensure input values are valid
        self.validate_inputs()
        
        # Calculate the efficiency
        efficiency = self.input_quality * self.output_yield * 100
        return efficiency


def main():
    """
    Main function to handle user input and output the calculated efficiency.
    """
    print("PumpX BriX Efficiency Calculator")
    print("Enter values between 0.0 and 1.0 for the input quality and output yield.")
    
    try:
        # Get user input for input quality
        input_quality = float(input("Enter input material quality (0.0 to 1.0): "))
        
        # Get user input for output yield
        output_yield = float(input("Enter output yield (0.0 to 1.0): "))
        
        # Instantiate the calculator with user inputs
        calculator = PumpXEfficiencyCalculator(input_quality, output_yield)
        
        # Calculate efficiency
        efficiency = calculator.calculate_efficiency()
        print(f"\nThe efficiency of PumpX's BriX equipment is: {efficiency:.2f}%")
    
    except ValueError as e:
        # Handle invalid input or calculation errors
        print(f"Error: {e}")
    except Exception as e:
        # Catch-all for other unforeseen errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
