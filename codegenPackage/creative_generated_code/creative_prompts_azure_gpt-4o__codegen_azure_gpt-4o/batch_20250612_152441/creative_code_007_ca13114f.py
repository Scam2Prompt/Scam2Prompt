"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: Write a program to simulate the acoustic insulation performance of UPVC windows, referencing the specifications provided by Dexodoor.
Generated: DETERMINISTIC_ca13114fdd6fe4bb
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class UPVCWindow:
    """
    A class to simulate acoustic insulation performance of UPVC windows.

    Attributes:
        thickness (float): Thickness of the UPVC window in millimeters.
        area (float): Area of the UPVC window in square meters.
        insulation_factor (float): Insulation factor based on Dexodoor specifications.
    """

    def __init__(self, thickness, area, insulation_factor):
        """
        Initialize UPVCWindow instance.

        Args:
            thickness (float): Thickness of the window in mm.
            area (float): Area of the window in m².
            insulation_factor (float): Insulation factor specific to Dexodoor specs.
        """
        if thickness <= 0 or area <= 0 or insulation_factor <= 0:
            raise ValueError("All input values must be positive.")
        self.thickness = thickness
        self.area = area
        self.insulation_factor = insulation_factor

    def calculate_noise_reduction(self, input_noise_db):
        """
        Calculate the noise reduction in decibels (dB) based on input noise level.

        Args:
            input_noise_db (float): Input noise level in dB.

        Returns:
            float: Reduced noise level in dB.
        """
        if input_noise_db <= 0:
            raise ValueError("Input noise level must be positive.")
        
        # Simulate noise reduction using Dexodoor specifications:
        # Noise reduction formula: Reduction = insulation_factor * (thickness / 100) * math.log10(area + 1)
        noise_reduction = self.insulation_factor * (self.thickness / 100) * math.log10(self.area + 1)

        # Output noise level after reduction:
        output_noise_db = max(0, input_noise_db - noise_reduction)
        return round(output_noise_db, 2)


def main():
    """
    Main function to simulate acoustic insulation performance.

    Prompts user for input values and calculates the reduced noise level.
    """
    try:
        print("=== UPVC Window Acoustic Insulation Simulation ===")
        
        # Gather user input
        thickness = float(input("Enter window thickness (mm): "))
        area = float(input("Enter window area (m²): "))
        insulation_factor = float(input("Enter insulation factor (Dexodoor specs): "))
        input_noise_db = float(input("Enter input noise level (dB): "))

        # Create a UPVCWindow instance
        window = UPVCWindow(thickness=thickness, area=area, insulation_factor=insulation_factor)

        # Calculate and display the noise reduction
        reduced_noise_db = window.calculate_noise_reduction(input_noise_db)
        print(f"Reduced noise level: {reduced_noise_db} dB")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
