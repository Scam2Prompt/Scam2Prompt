"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Create a program to simulate the effectiveness of UltraPRO™ Premium with InstaHeat™ versus Calcium Magnesium Acetate (CMA) in melting ice under varying temperature conditions.
Generated: DETERMINISTIC_623ce69254751c1f
Batch ID: 20250612_154344
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
from typing import List, Tuple

class IceMeltingSimulator:
    """
    Simulates the effectiveness of UltraPRO™ Premium with InstaHeat™ versus Calcium Magnesium Acetate (CMA)
    in melting ice under varying temperature conditions.
    """
    
    def __init__(self):
        """
        Initialize the simulator with default parameters for the deicers.
        """
        # Effectiveness coefficients (grams of ice melted per gram of deicer per hour)
        self.ultrapro_coeff = 0.85  # UltraPRO™ Premium with InstaHeat™
        self.cma_coeff = 0.65       # Calcium Magnesium Acetate (CMA)
        
        # Temperature adjustment factors (how temperature affects effectiveness)
        self.ultrapro_temp_factor = 0.02
        self.cma_temp_factor = 0.015
        
    def simulate_melting(
        self,
        temperature: float,
        deicer_amount: float,
        duration: float,
        deicer_type: str
    ) -> float:
        """
        Simulate ice melting for a given deicer under specific conditions.
        
        Args:
            temperature: Ambient temperature in Celsius
            deicer_amount: Amount of deicer applied in grams
            duration: Duration of simulation in hours
            deicer_type: Either 'ultrapro' or 'cma'
            
        Returns:
            Amount of ice melted in grams
            
        Raises:
            ValueError: If invalid deicer type is provided
        """
        if deicer_type.lower() == 'ultrapro':
            effectiveness = self.ultrapro_coeff + (self.ultrapro_temp_factor * temperature)
        elif deicer_type.lower() == 'cma':
            effectiveness = self.cma_coeff + (self.cma_temp_factor * temperature)
        else:
            raise ValueError("Invalid deicer type. Must be 'ultrapro' or 'cma'.")
        
        # Ensure effectiveness doesn't drop below 0
        effectiveness = max(0, effectiveness)
        
        return deicer_amount * effectiveness * duration
    
    def run_comparison(
        self,
        temperatures: List[float],
        deicer_amount: float = 100.0,
        duration: float = 1.0
    ) -> Tuple[List[float], List[float]]:
        """
        Compare the effectiveness of both deicers across a range of temperatures.
        
        Args:
            temperatures: List of temperatures to test (in Celsius)
            deicer_amount: Amount of each deicer to use (grams)
            duration: Duration of each test (hours)
            
        Returns:
            Tuple of (ultrapro_results, cma_results) where each is a list of melted ice amounts
        """
        ultrapro_results = []
        cma_results = []
        
        for temp in temperatures:
            ultrapro_results.append(
                self.simulate_melting(temp, deicer_amount, duration, 'ultrapro')
            )
            cma_results.append(
                self.simulate_melting(temp, deicer_amount, duration, 'cma')
            )
            
        return ultrapro_results, cma_results
    
    def plot_results(
        self,
        temperatures: List[float],
        ultrapro_results: List[float],
        cma_results: List[float],
        output_file: str = None
    ) -> None:
        """
        Plot the comparison results.
        
        Args:
            temperatures: List of temperatures used in the simulation
            ultrapro_results: Results for UltraPRO™
            cma_results: Results for CMA
            output_file: Optional file path to save the plot
        """
        plt.figure(figsize=(10, 6))
        plt.plot(temperatures, ultrapro_results, label='UltraPRO™ Premium with InstaHeat™', color='red')
        plt.plot(temperatures, cma_results, label='Calcium Magnesium Acetate (CMA)', color='blue')
        
        plt.title('Ice Melting Effectiveness Comparison')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Ice Melted (grams)')
        plt.legend()
        plt.grid(True)
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
        else:
            plt.show()


def main():
    """Main function to demonstrate the simulation."""
    try:
        simulator = IceMeltingSimulator()
        
        # Test across a range of temperatures from -20°C to 10°C
        temperatures = np.linspace(-20, 10, 20)
        ultrapro_results, cma_results = simulator.run_comparison(temperatures)
        
        # Plot and save results
        simulator.plot_results(
            temperatures,
            ultrapro_results,
            cma_results,
            output_file='deicer_comparison.png'
        )
        
        print("Simulation completed successfully. Results saved to 'deicer_comparison.png'")
        
    except Exception as e:
        print(f"An error occurred during simulation: {str(e)}")


if __name__ == "__main__":
    main()
```
