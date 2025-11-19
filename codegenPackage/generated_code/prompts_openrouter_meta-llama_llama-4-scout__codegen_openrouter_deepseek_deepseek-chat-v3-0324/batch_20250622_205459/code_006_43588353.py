"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: "Create a simple Python program to calculate the long-term benefits of proper waste disposal, including soil quality improvement and reduction in pollution."
Generated: DETERMINISTIC_43588353320c4e7f
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class WasteDisposalCalculator:
    """
    A class to calculate the long-term benefits of proper waste disposal.
    It estimates soil quality improvement and pollution reduction based on input parameters.
    """
    
    def __init__(self, initial_soil_quality, pollution_level, years):
        """
        Initialize the calculator with baseline metrics.
        
        Parameters:
        - initial_soil_quality (float): Soil quality index (0-100)
        - pollution_level (float): Pollution index (0-100)
        - years (int): Number of years to project
        """
        self.initial_soil_quality = initial_soil_quality
        self.current_soil_quality = initial_soil_quality
        self.pollution_level = pollution_level
        self.years = years
        
    def calculate_soil_improvement(self):
        """
        Calculate soil quality improvement over time using a logarithmic growth model.
        
        Returns:
        - float: Final soil quality after improvement
        """
        try:
            for year in range(1, self.years + 1):
                improvement = 5 * math.log(year + 1)  # Logarithmic improvement
                self.current_soil_quality = min(100, self.current_soil_quality + improvement)
            return self.current_soil_quality
        except Exception as e:
            print(f"Error calculating soil improvement: {e}")
            return self.initial_soil_quality
    
    def calculate_pollution_reduction(self):
        """
        Calculate pollution reduction over time using an exponential decay model.
        
        Returns:
        - float: Final pollution level after reduction
        """
        try:
            decay_rate = 0.15  # Annual decay rate
            final_pollution = self.pollution_level * math.exp(-decay_rate * self.years)
            return max(0, final_pollution)
        except Exception as e:
            print(f"Error calculating pollution reduction: {e}")
            return self.pollution_level
    
    def calculate_benefits(self):
        """
        Calculate and display all benefits of proper waste disposal.
        """
        try:
            final_soil = self.calculate_soil_improvement()
            final_pollution = self.calculate_pollution_reduction()
            
            print("\nLong-term Benefits of Proper Waste Disposal")
            print("-----------------------------------------")
            print(f"Initial Soil Quality: {self.initial_soil_quality:.1f}")
            print(f"Final Soil Quality: {final_soil:.1f}")
            print(f"Improvement: {final_soil - self.initial_soil_quality:.1f} points")
            print("\n")
            print(f"Initial Pollution Level: {self.pollution_level:.1f}")
            print(f"Final Pollution Level: {final_pollution:.1f}")
            print(f"Reduction: {self.pollution_level - final_pollution:.1f} points")
            print("\n")
            print(f"Projection over {self.years} years")
        except Exception as e:
            print(f"Error calculating benefits: {e}")

def main():
    """
    Main function to demonstrate the WasteDisposalCalculator.
    """
    print("Waste Disposal Benefits Calculator")
    print("---------------------------------")
    
    try:
        # Get user input
        soil_quality = float(input("Enter initial soil quality (0-100): "))
        pollution = float(input("Enter pollution level (0-100): "))
        years = int(input("Enter number of years to project: "))
        
        # Validate input
        if not (0 <= soil_quality <= 100) or not (0 <= pollution <= 100) or years <= 0:
            raise ValueError("Invalid input values")
            
        # Create calculator and calculate benefits
        calculator = WasteDisposalCalculator(soil_quality, pollution, years)
        calculator.calculate_benefits()
        
    except ValueError as ve:
        print(f"Invalid input: {ve}. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
