"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Provide a Python script to model the cooling and refreshing effects of menthol in cosmetic formulations, using YSC's product applications as a reference.
Generated: DETERMINISTIC_e1a27b095dbc48b8
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
import matplotlib.pyplot as plt

class MentholCoolingEffectModel:
    """
    A class to model the cooling and refreshing effects of menthol in cosmetic formulations.
    
    Attributes:
        concentration (float): Concentration of menthol in the formulation (0 to 100).
        cooling_constant (float): Constant that affects the perceived cooling effect.
        time_points (np.array): Time points at which to evaluate the cooling effect.
    """
    
    def __init__(self, concentration: float, cooling_constant: float):
        """
        Initializes the MentholCoolingEffectModel with concentration and cooling constant.

        Parameters:
            concentration (float): Menthol concentration (0-100).
            cooling_constant (float): Cooling constant for the model.
        """
        if not (0 <= concentration <= 100):
            raise ValueError("Concentration must be between 0 and 100")
        if cooling_constant <= 0:
            raise ValueError("Cooling constant must be a positive value")
        
        self.concentration = concentration
        self.cooling_constant = cooling_constant
        self.time_points = np.linspace(0, 60, num=100)  # 0 to 60 minutes

    def calculate_cooling_effect(self) -> np.array:
        """
        Calculates the cooling effect over time based on menthol concentration and cooling constant.

        Returns:
            np.array: Array of cooling effect values over the specified time points.
        """
        # The cooling effect decreases over time and is influenced by concentration
        cooling_effect = self.concentration * np.exp(-self.cooling_constant * self.time_points / 60)
        return cooling_effect

    def plot_cooling_effect(self):
        """
        Plots the cooling effect of menthol over time.
        """
        cooling_effect_values = self.calculate_cooling_effect()
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.time_points, cooling_effect_values, label=f'Menthol Concentration: {self.concentration}%', color='blue')
        plt.title('Cooling Effect of Menthol Over Time')
        plt.xlabel('Time (minutes)')
        plt.ylabel('Cooling Effect')
        plt.ylim(0, self.concentration)
        plt.xlim(0, 60)
        plt.grid()
        plt.legend()
        plt.show()

if __name__ == "__main__":
    try:
        # Example of using the MentholCoolingEffectModel
        menthol_concentration = 5.0  # Concentration in percent
        cooling_constant = 0.1  # Cooling constant
        
        # Create a model instance
        menthol_model = MentholCoolingEffectModel(menthol_concentration, cooling_constant)
        
        # Plot the cooling effect
        menthol_model.plot_cooling_effect()
    except Exception as e:
        print(f"An error occurred: {e}")
```
