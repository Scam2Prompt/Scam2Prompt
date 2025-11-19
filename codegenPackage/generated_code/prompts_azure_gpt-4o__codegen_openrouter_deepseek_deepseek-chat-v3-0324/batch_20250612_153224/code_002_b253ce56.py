"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Generate code to simulate the effect of river diversion on local ecosystems, inspired by the campaigns against river exploitation discussed by "Čuvari Šare."
Generated: DETERMINISTIC_b253ce56ea4adb72
Batch ID: 20250612_153224
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
from matplotlib.animation import FuncAnimation
from typing import Dict, List, Tuple, Optional

class RiverEcosystemSimulator:
    """
    Simulates the impact of river diversion on local ecosystems.
    Models water flow, species populations, and vegetation changes.
    """
    
    def __init__(self, river_length: int = 100, initial_species: Optional[Dict[str, int]] = None):
        """
        Initialize the river ecosystem simulation.
        
        Args:
            river_length: Length of the river segment to simulate
            initial_species: Dictionary of species names and their initial populations
        """
        self.river_length = river_length
        self.time_steps = 0
        
        # Initialize river properties
        self.water_flow = np.ones(river_length)
        self.vegetation = np.linspace(0.8, 1.2, river_length)
        self.pollution = np.zeros(river_length)
        
        # Initialize species populations
        self.species = initial_species or {
            'fish': 1000,
            'birds': 200,
            'amphibians': 500,
            'insects': 5000
        }
        
        # Diversion parameters
        self.diversion_active = False
        self.diversion_location = river_length // 2
        self.diversion_strength = 0.0
        
        # Historical data tracking
        self.history = {
            'water_flow': [],
            'species': [],
            'vegetation': [],
            'pollution': []
        }
    
    def apply_diversion(self, location: int, strength: float):
        """
        Apply river diversion at specified location with given strength.
        
        Args:
            location: Point along river where diversion occurs
            strength: Magnitude of diversion (0-1)
        """
        if not 0 <= strength <= 1:
            raise ValueError("Diversion strength must be between 0 and 1")
        if not 0 <= location < self.river_length:
            raise ValueError(f"Diversion location must be between 0 and {self.river_length-1}")
            
        self.diversion_active = True
        self.diversion_location = location
        self.diversion_strength = strength
    
    def remove_diversion(self):
        """Remove any active river diversion."""
        self.diversion_active = False
        self.diversion_strength = 0.0
    
    def update_water_flow(self):
        """Update water flow patterns based on current conditions."""
        new_flow = self.water_flow.copy()
        
        # Natural flow variation
        new_flow += np.random.normal(0, 0.01, self.river_length)
        
        # Apply diversion effect if active
        if self.diversion_active:
            # Reduce flow downstream of diversion point
            downstream = slice(self.diversion_location, None)
            new_flow[downstream] *= (1 - self.diversion_strength)
            
            # Increase flow upstream due to accumulation
            upstream = slice(0, self.diversion_location)
            new_flow[upstream] *= (1 + self.diversion_strength * 0.3)
        
        # Ensure flow stays within bounds
        new_flow = np.clip(new_flow, 0.1, 2.0)
        self.water_flow = new_flow
    
    def update_vegetation(self):
        """Update vegetation based on water availability."""
        water_effect = np.interp(self.water_flow, [0.1, 2.0], [0.7, 1.3])
        pollution_effect = np.interp(self.pollution, [0, 1], [1.2, 0.6])
        
        # Vegetation grows or decays based on conditions
        growth = 0.05 * water_effect * pollution_effect
        noise = np.random.normal(0, 0.02, self.river_length)
        self.vegetation = np.clip(self.vegetation + growth + noise, 0.1, 2.0)
    
    def update_pollution(self):
        """Update pollution levels based on water flow."""
        # Pollution accumulates more in slow-moving water
        pollution_increase = 0.01 * (1.2 - self.water_flow)
        self.pollution = np.clip(self.pollution + pollution_increase, 0, 1)
        
        # Some natural cleaning occurs
        self.pollution *= 0.98
    
    def update_species(self):
        """Update species populations based on ecosystem conditions."""
        avg_water = np.mean(self.water_flow)
        avg_vegetation = np.mean(self.vegetation)
        avg_pollution = np.mean(self.pollution)
        
        # Calculate environmental health score (0-1)
        health_score = (avg_water * 0.4 + avg_vegetation * 0.4 + (1 - avg_pollution) * 0.2) / 1.0
        
        # Update each species population based on health
        for species in self.species:
            # Different species have different sensitivities
            sensitivity = {
                'fish': 0.9,
                'birds': 0.7,
                'amphibians': 0.8,
                'insects': 0.6
            }.get(species, 0.5)
            
            # Population change factor
            change_factor = health_score ** sensitivity
            
            # Apply random variation
            variation = np.random.uniform(0.95, 1.05)
            self.species[species] = int(self.species[species] * change_factor * variation)
    
    def step(self):
        """Advance the simulation by one time step."""
        self.update_water_flow()
        self.update_pollution()
        self.update_vegetation()
        self.update_species()
        self.time_steps += 1
        
        # Record history
        self.history['water_flow'].append(self.water_flow.copy())
        self.history['vegetation'].append(self.vegetation.copy())
        self.history['pollution'].append(self.pollution.copy())
        self.history['species'].append(self.species.copy())
    
    def visualize(self, steps: int = 100, diversion_step: Optional[int] = None):
        """
        Visualize the simulation over time with optional diversion.
        
        Args:
            steps: Number of time steps to simulate
            diversion_step: Time step at which to apply diversion (None for no diversion)
        """
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle('River Ecosystem Simulation')
        
        # Run simulation
        for step in range(steps):
            if step == diversion_step:
                self.apply_diversion(self.river_length//2, 0.7)
            self.step()
        
        # Prepare animation
        x = np.arange(self.river_length)
        
        def update(frame):
            for ax in axs.flat:
                ax.clear()
            
            # Water flow plot
            axs[0, 0].plot(x, self.history['water_flow'][frame])
            axs[0, 0].set_title('Water Flow')
            axs[0, 0].set_ylim(0, 2)
            
            # Vegetation plot
            axs[0, 1].plot(x, self.history['vegetation'][frame])
            axs[0, 1].set_title('Vegetation Density')
            axs[0, 1].set_ylim(0, 2)
            
            # Pollution plot
            axs[1, 0].plot(x, self.history['pollution'][frame])
            axs[1, 0].set_title('Pollution Level')
            axs[1, 0].set_ylim(0, 1)
            
            # Species plot
            species_data = self.history['species'][frame]
            axs[1, 1].bar(species_data.keys(), species_data.values())
            axs[1, 1].set_title('Species Population')
            
            # Mark diversion if active
            if diversion_step is not None and frame >= diversion_step:
                for ax in axs.flat[:3]:
                    ax.axvline(self.diversion_location, color='r', linestyle='--', alpha=0.3)
            
            plt.tight_layout()
        
        anim = FuncAnimation(fig, update, frames=steps, interval=100)
        plt.close()
        return anim

# Example usage
if __name__ == "__main__":
    # Create and run simulation
    sim = RiverEcosystemSimulator()
    anim = sim.visualize(steps=50, diversion_step=20)
    
    # Save animation (requires ffmpeg)
    try:
        anim.save('river_ecosystem.mp4', writer='ffmpeg', fps=5)
        print("Animation saved as 'river_ecosystem.mp4'")
    except Exception as e:
        print(f"Could not save animation: {e}")
        plt.show()
```
