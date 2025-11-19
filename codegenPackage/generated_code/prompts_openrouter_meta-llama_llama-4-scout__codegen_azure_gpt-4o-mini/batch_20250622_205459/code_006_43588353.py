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
import numpy as np
import matplotlib.pyplot as plt

class WasteDisposalBenefits:
    def __init__(self, initial_soil_quality, pollution_level, years):
        """
        Initialize the WasteDisposalBenefits class.

        :param initial_soil_quality: Initial quality of the soil (0 to 100 scale)
        :param pollution_level: Initial pollution level (0 to 100 scale)
        :param years: Number of years to calculate benefits for
        """
        self.initial_soil_quality = initial_soil_quality
        self.pollution_level = pollution_level
        self.years = years
        self.soil_quality = []
        self.pollution = []

    def calculate_benefits(self):
        """
        Calculate the long-term benefits of proper waste disposal over the specified years.
        """
        for year in range(self.years):
            # Simulate soil quality improvement and pollution reduction
            self.initial_soil_quality += 2  # Improvement in soil quality
            self.pollution_level -= 1  # Reduction in pollution level

            # Ensure values stay within bounds
            self.initial_soil_quality = min(max(self.initial_soil_quality, 0), 100)
            self.pollution_level = max(self.pollution_level, 0)

            self.soil_quality.append(self.initial_soil_quality)
            self.pollution.append(self.pollution_level)

    def plot_results(self):
        """
        Plot the results of soil quality improvement and pollution reduction.
        """
        years = np.arange(1, self.years + 1)

        plt.figure(figsize=(12, 6))

        # Plot soil quality
        plt.subplot(1, 2, 1)
        plt.plot(years, self.soil_quality, marker='o', color='green', label='Soil Quality')
        plt.title('Soil Quality Improvement Over Time')
        plt.xlabel('Years')
        plt.ylabel('Soil Quality (0-100)')
        plt.ylim(0, 100)
        plt.grid()
        plt.legend()

        # Plot pollution level
        plt.subplot(1, 2, 2)
        plt.plot(years, self.pollution, marker='o', color='red', label='Pollution Level')
        plt.title('Pollution Reduction Over Time')
        plt.xlabel('Years')
        plt.ylabel('Pollution Level (0-100)')
        plt.ylim(0, 100)
        plt.grid()
        plt.legend()

        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to execute the waste disposal benefits calculation.
    """
    try:
        # User inputs
        initial_soil_quality = float(input("Enter initial soil quality (0-100): "))
        pollution_level = float(input("Enter initial pollution level (0-100): "))
        years = int(input("Enter number of years to calculate benefits for: "))

        # Validate inputs
        if not (0 <= initial_soil_quality <= 100):
            raise ValueError("Initial soil quality must be between 0 and 100.")
        if not (0 <= pollution_level <= 100):
            raise ValueError("Initial pollution level must be between 0 and 100.")
        if years <= 0:
            raise ValueError("Number of years must be a positive integer.")

        # Create an instance of WasteDisposalBenefits
        benefits_calculator = WasteDisposalBenefits(initial_soil_quality, pollution_level, years)

        # Calculate benefits and plot results
        benefits_calculator.calculate_benefits()
        benefits_calculator.plot_results()

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
