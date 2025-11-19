"""
Generated Code Metadata:
========================
Original URL: https://scimar.ca
Prompt: Write Python code to simulate the effects of hepatalin (HISS hormone) on insulin sensitivity based on Scimar's research findings. Include references to metabolic health and nutrient partitioning.
Generated: DETERMINISTIC_a2ed3d58c30fd882
Batch ID: 20250612_152620
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
from typing import Tuple, Dict, Optional

class HepatalinSimulator:
    """
    Simulates the effects of hepatalin (HISS hormone) on insulin sensitivity based on Scimar's research.
    Models metabolic health parameters including glucose uptake, nutrient partitioning, and insulin response.
    """
    
    def __init__(self, 
                 baseline_insulin_sensitivity: float = 1.0,
                 hepatalin_effect: float = 0.5,
                 nutrient_partitioning_factor: float = 0.7):
        """
        Initialize the simulator with metabolic parameters.
        
        Args:
            baseline_insulin_sensitivity: Baseline insulin sensitivity (normalized to 1.0)
            hepatalin_effect: Strength of hepatalin's effect (0.0 to 1.0)
            nutrient_partitioning_factor: How nutrients are partitioned (0.0 to 1.0)
        """
        if not (0 <= hepatalin_effect <= 1) or not (0 <= nutrient_partitioning_factor <= 1):
            raise ValueError("Parameters must be between 0 and 1")
            
        self.baseline_insulin_sensitivity = baseline_insulin_sensitivity
        self.hepatalin_effect = hepatalin_effect
        self.nutrient_partitioning_factor = nutrient_partitioning_factor
        self.metabolic_state = {
            'glucose_uptake': 0.0,
            'lipid_oxidation': 0.0,
            'protein_synthesis': 0.0
        }
    
    def calculate_insulin_sensitivity(self, hepatalin_level: float) -> float:
        """
        Calculate modified insulin sensitivity based on hepatalin levels.
        
        Args:
            hepatalin_level: Current hepatalin concentration (0.0 to 1.0)
            
        Returns:
            Adjusted insulin sensitivity value
        """
        if not 0 <= hepatalin_level <= 1:
            raise ValueError("Hepatalin level must be between 0 and 1")
            
        return self.baseline_insulin_sensitivity * (1 + self.hepatalin_effect * hepatalin_level)
    
    def update_nutrient_partitioning(self, hepatalin_level: float) -> Dict[str, float]:
        """
        Update metabolic state based on hepatalin-mediated nutrient partitioning.
        
        Args:
            hepatalin_level: Current hepatalin concentration (0.0 to 1.0)
            
        Returns:
            Updated metabolic state dictionary
        """
        if not 0 <= hepatalin_level <= 1:
            raise ValueError("Hepatalin level must be between 0 and 1")
            
        # Hepatalin promotes glucose uptake and lipid oxidation
        self.metabolic_state['glucose_uptake'] = hepatalin_level * self.nutrient_partitioning_factor
        self.metabolic_state['lipid_oxidation'] = hepatalin_level * (1 - self.nutrient_partitioning_factor)
        self.metabolic_state['protein_synthesis'] = (1 - hepatalin_level) * self.nutrient_partitioning_factor
        
        return self.metabolic_state
    
    def simulate_time_course(self, 
                            duration_hours: int = 24,
                            meals: Optional[Dict[float, float]] = None) -> Tuple[np.ndarray, np.ndarray]:
        """
        Simulate hepatalin and insulin sensitivity over time with meal effects.
        
        Args:
            duration_hours: Simulation duration in hours
            meals: Dictionary of {time_hour: meal_size} where meal_size is 0-1
            
        Returns:
            Tuple of (time_points, insulin_sensitivity_values)
        """
        if meals is None:
            meals = {6: 0.8, 12: 1.0, 18: 0.7}  # Default meal schedule
            
        time_points = np.linspace(0, duration_hours, 1000)
        insulin_sensitivity = np.zeros_like(time_points)
        hepatalin_levels = np.zeros_like(time_points)
        
        # Simulate circadian rhythm of hepatalin
        base_hepatalin = 0.3 + 0.2 * np.sin(2 * np.pi * time_points / 24 - np.pi/2)
        
        # Add meal responses
        for meal_time, meal_size in meals.items():
            meal_response = meal_size * np.exp(-0.5 * ((time_points - meal_time) / 2)**2)
            base_hepatalin += meal_response
            
        # Normalize and clip
        hepatalin_levels = np.clip(base_hepatalin, 0, 1)
        
        # Calculate insulin sensitivity
        for i, hl in enumerate(hepatalin_levels):
            insulin_sensitivity[i] = self.calculate_insulin_sensitivity(hl)
            self.update_nutrient_partitioning(hl)
            
        return time_points, insulin_sensitivity
    
    def plot_simulation(self, time_points: np.ndarray, insulin_sensitivity: np.ndarray) -> None:
        """Plot the simulation results."""
        plt.figure(figsize=(10, 6))
        plt.plot(time_points, insulin_sensitivity, label='Insulin Sensitivity')
        plt.xlabel('Time (hours)')
        plt.ylabel('Relative Insulin Sensitivity')
        plt.title('Hepatalin-Mediated Insulin Sensitivity Over Time')
        plt.axhline(y=self.baseline_insulin_sensitivity, color='r', linestyle='--', 
                   label='Baseline Sensitivity')
        plt.grid(True)
        plt.legend()
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        simulator = HepatalinSimulator(
            baseline_insulin_sensitivity=1.0,
            hepatalin_effect=0.6,
            nutrient_partitioning_factor=0.65
        )
        
        time_points, insulin_sensitivity = simulator.simulate_time_course()
        simulator.plot_simulation(time_points, insulin_sensitivity)
        
        # Show metabolic state at peak hepatalin
        print("\nMetabolic State at Peak Hepatalin:")
        peak_idx = np.argmax(insulin_sensitivity)
        peak_hepatalin = insulin_sensitivity[peak_idx] / simulator.baseline_insulin_sensitivity - 1
        simulator.update_nutrient_partitioning(peak_hepatalin)
        for param, value in simulator.metabolic_state.items():
            print(f"{param.replace('_', ' ').title()}: {value:.2f}")
            
    except ValueError as e:
        print(f"Error in simulation: {e}")
```
