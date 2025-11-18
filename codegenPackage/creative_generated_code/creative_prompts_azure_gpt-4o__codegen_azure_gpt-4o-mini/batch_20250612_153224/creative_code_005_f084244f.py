"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Write code to model the impact of small hydroelectric plants on biodiversity, referencing the environmental advocacy efforts of "Čuvari Šare."
Generated: DETERMINISTIC_f084244fb04681c1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class HydroImpactModel:
    """
    A class to model the impact of small hydroelectric plants on biodiversity.
    
    Attributes:
        years (np.ndarray): The range of years to simulate the impact over.
        biodiversity_index (np.ndarray): The simulated biodiversity index over the years.
    """

    def __init__(self, start_year: int, end_year: int):
        """
        Initializes the model with a range of years.
        
        Args:
            start_year (int): The starting year for the simulation.
            end_year (int): The ending year for the simulation.
        """
        self.years = np.arange(start_year, end_year + 1)
        self.biodiversity_index = np.zeros(len(self.years))
        
    def simulate_biodiversity(self, plant_count: int, advocacy_effect: float):
        """
        Simulates the impact on biodiversity based on the number of hydro plants
        and the effect of advocacy efforts.
        
        Args:
            plant_count (int): The number of hydroelectric plants.
            advocacy_effect (float): The effectiveness of advocacy efforts (0 to 1).
        """
        # Check for valid input values
        if plant_count < 0:
            raise ValueError("Number of hydroelectric plants must be non-negative.")
        if not (0 <= advocacy_effect <= 1):
            raise ValueError("Advocacy effect must be between 0 and 1.")
        
        for i, year in enumerate(self.years):
            # Simulate biodiversity decrease due to hydro plants
            self.biodiversity_index[i] = max(0, 1 - (plant_count * 0.02))
            # Adjust based on advocacy efforts
            self.biodiversity_index[i] += advocacy_effect * 0.1
            
    def plot_biodiversity(self):
        """Plots the biodiversity index over the years."""
        plt.figure(figsize=(10, 5))
        plt.plot(self.years, self.biodiversity_index, marker='o', color='green')
        plt.title('Impact of Small Hydroelectric Plants on Biodiversity')
        plt.xlabel('Year')
        plt.ylabel('Biodiversity Index (0 to 1)')
        plt.ylim(0, 1)
        plt.grid()
        plt.axhline(y=0.5, color='red', linestyle='--', label='Critical Biodiversity Level')
        plt.legend()
        plt.show()

def main():
    """Main function to run the biodiversity impact model."""
    try:
        # Initialize model for years 2020 to 2030
        model = HydroImpactModel(start_year=2020, end_year=2030)
        
        # Simulate the impact with hypothetical parameters
        model.simulate_biodiversity(plant_count=5, advocacy_effect=0.8)
        
        # Plot the results
        model.plot_biodiversity()
        
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
