"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: Write code to simulate the growth cycle of reforested pinus species and calculate the optimal harvest time, referencing the short growth intervals highlighted by Trattar Madeiras.
Generated: DETERMINISTIC_ebed6d16b8f13726
Batch ID: 20250612_154441
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
from scipy.optimize import minimize_scalar

class PinusReforestationSimulator:
    """
    Simulates the growth cycle of reforested Pinus species and calculates optimal harvest time.
    Based on short growth intervals as highlighted by Trattar Madeiras.
    """
    
    def __init__(self, species='Pinus taeda', initial_height=0.5, max_age=20):
        """
        Initialize the simulator with species parameters.
        
        Args:
            species (str): Pinus species (default: 'Pinus taeda')
            initial_height (float): Initial height in meters (default: 0.5)
            max_age (int): Maximum simulation age in years (default: 20)
        """
        self.species = species
        self.initial_height = initial_height
        self.max_age = max_age
        
        # Growth parameters based on species (can be extended for other species)
        self.growth_params = {
            'Pinus taeda': {'max_height': 30.0, 'growth_rate': 0.8, 'maturity_age': 15},
            'Pinus elliottii': {'max_height': 25.0, 'growth_rate': 0.7, 'maturity_age': 12},
            'Pinus caribaea': {'max_height': 35.0, 'growth_rate': 0.9, 'maturity_age': 18}
        }
        
        if species not in self.growth_params:
            raise ValueError(f"Species {species} not supported. Available species: {list(self.growth_params.keys())}")
    
    def growth_curve(self, age):
        """
        Calculate tree height at given age using logistic growth model.
        
        Args:
            age (float): Age in years
            
        Returns:
            float: Height in meters
        """
        params = self.growth_params[self.species]
        max_height = params['max_height']
        growth_rate = params['growth_rate']
        maturity_age = params['maturity_age']
        
        # Logistic growth model
        return max_height / (1 + np.exp(-growth_rate * (age - maturity_age/2))) + self.initial_height
    
    def volume_calculation(self, height, age):
        """
        Calculate timber volume based on height and age.
        Simplified model assuming constant diameter-height ratio.
        
        Args:
            height (float): Tree height in meters
            age (float): Age in years
            
        Returns:
            float: Volume in cubic meters
        """
        # Diameter approximation (cm)
        diameter = 0.2 * height * (1 + 0.05 * age)
        # Volume in m³ (simplified cone volume)
        return (np.pi * (diameter/200)**2 * height) / 3
    
    def revenue_calculation(self, volume, age):
        """
        Calculate revenue based on volume and age.
        Older trees have higher value per m³.
        
        Args:
            volume (float): Volume in cubic meters
            age (float): Age in years
            
        Returns:
            float: Revenue in monetary units
        """
        base_price = 50  # $/m³
        age_premium = 1 + (age / self.max_age) * 0.5  # Up to 50% premium for older trees
        return volume * base_price * age_premium
    
    def cost_calculation(self, age):
        """
        Calculate maintenance costs over time.
        
        Args:
            age (float): Age in years
            
        Returns:
            float: Cumulative costs in monetary units
        """
        annual_cost = 20  # $/year
        return annual_cost * age
    
    def net_present_value(self, age, discount_rate=0.05):
        """
        Calculate NPV of harvesting at given age.
        
        Args:
            age (float): Harvest age in years
            discount_rate (float): Annual discount rate (default: 0.05)
            
        Returns:
            float: Net Present Value in monetary units
        """
        height = self.growth_curve(age)
        volume = self.volume_calculation(height, age)
        revenue = self.revenue_calculation(volume, age)
        costs = self.cost_calculation(age)
        
        discounted_revenue = revenue / ((1 + discount_rate) ** age)
        discounted_costs = costs / ((1 + discount_rate) ** age)
        
        return discounted_revenue - discounted_costs
    
    def find_optimal_harvest_time(self):
        """
        Find the age that maximizes NPV.
        
        Returns:
            dict: Contains optimal age, NPV, and other metrics
        """
        result = minimize_scalar(
            lambda x: -self.net_present_value(x),
            bounds=(5, self.max_age),
            method='bounded'
        )
        
        if not result.success:
            raise RuntimeError("Optimization failed to find optimal harvest time")
        
        optimal_age = result.x
        max_npv = -result.fun
        height = self.growth_curve(optimal_age)
        volume = self.volume_calculation(height, optimal_age)
        
        return {
            'optimal_age': optimal_age,
            'max_npv': max_npv,
            'height': height,
            'volume': volume,
            'species': self.species
        }
    
    def plot_growth_curve(self):
        """Plot the growth curve and NPV over time."""
        ages = np.linspace(0, self.max_age, 100)
        heights = [self.growth_curve(age) for age in ages]
        npvs = [self.net_present_value(age) for age in ages]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Growth curve
        ax1.plot(ages, heights)
        ax1.set_title(f'{self.species} Growth Curve')
        ax1.set_xlabel('Age (years)')
        ax1.set_ylabel('Height (m)')
        ax1.grid(True)
        
        # NPV curve
        ax2.plot(ages, npvs)
        ax2.set_title('Net Present Value Over Time')
        ax2.set_xlabel('Age (years)')
        ax2.set_ylabel('NPV ($)')
        ax2.grid(True)
        
        plt.tight_layout()
        return fig

# Example usage
if __name__ == "__main__":
    try:
        simulator = PinusReforestationSimulator(species='Pinus taeda')
        optimal = simulator.find_optimal_harvest_time()
        
        print("Optimal Harvest Time Calculation:")
        for key, value in optimal.items():
            print(f"{key.replace('_', ' ').title()}: {value:.2f}")
        
        fig = simulator.plot_growth_curve()
        plt.show()
        
    except Exception as e:
        print(f"Error in simulation: {e}")
```
