"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Develop a script to calculate the aromatic intensity of mint oils in food applications, using YSC's description of mint oil as a flavoring agent.
Generated: DETERMINISTIC_9585828a82f8707c
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class MintOilAromaticIntensityCalculator:
    """
    A class to calculate the aromatic intensity of mint oils in food applications.

    Attributes:
        flavor_profiles (pd.DataFrame): DataFrame containing flavor profile data of mint oils.
    """

    def __init__(self, flavor_profiles):
        """
        Initializes the MintOilAromaticIntensityCalculator with flavor profile data.

        Args:
            flavor_profiles (pd.DataFrame): DataFrame with columns 'compound' and 'intensity'.
        """
        if not isinstance(flavor_profiles, pd.DataFrame):
            raise ValueError("flavor_profiles must be a pandas DataFrame.")
        self.flavor_profiles = flavor_profiles

    def calculate_intensity(self):
        """
        Calculates the total aromatic intensity of mint oils.

        Returns:
            float: The total aromatic intensity.
        """
        try:
            total_intensity = self.flavor_profiles['intensity'].sum()
            return total_intensity
        except KeyError as e:
            raise KeyError(f"Missing expected column in DataFrame: {e}")

    def plot_intensity_distribution(self):
        """
        Plots the distribution of aromatic intensity for each compound in mint oil.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(self.flavor_profiles['compound'], self.flavor_profiles['intensity'], color='green')
            plt.title('Aromatic Intensity of Mint Oil Compounds')
            plt.xlabel('Compound')
            plt.ylabel('Intensity')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise RuntimeError(f"Failed to plot intensity distribution: {e}")

def main():
    # Sample data for mint oil flavor profiles
    data = {
        'compound': ['Menthol', 'Menthone', 'Isomenthone', 'Menthyl Acetate'],
        'intensity': [8.5, 6.2, 4.1, 5.0]
    }

    # Create DataFrame
    flavor_profiles = pd.DataFrame(data)

    # Initialize the calculator
    mint_calculator = MintOilAromaticIntensityCalculator(flavor_profiles)

    # Calculate total aromatic intensity
    try:
        total_intensity = mint_calculator.calculate_intensity()
        print(f"Total aromatic intensity of mint oils: {total_intensity:.2f}")
    except Exception as e:
        print(f"Error calculating intensity: {e}")

    # Plot intensity distribution
    try:
        mint_calculator.plot_intensity_distribution()
    except Exception as e:
        print(f"Error while plotting intensity distribution: {e}")

if __name__ == "__main__":
    main()
```
