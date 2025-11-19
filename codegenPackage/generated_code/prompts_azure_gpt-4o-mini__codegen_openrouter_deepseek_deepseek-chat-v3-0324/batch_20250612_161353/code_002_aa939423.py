"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: Write a code snippet that simulates the application of Capina Elétrica in a city environment, detailing the expected duration of effectiveness after multiple applications.
Generated: DETERMINISTIC_aa939423bfa37b48
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class CapinaEletrica:
    """
    Simulates the application of Capina Elétrica (electric weeding) in a city environment.
    Tracks effectiveness duration after multiple applications.
    """
    
    def __init__(self, city_name: str, initial_weed_density: float):
        """
        Initialize the simulation.
        
        Args:
            city_name: Name of the city being simulated
            initial_weed_density: Initial weed density (0.0 to 1.0)
        """
        if not 0 <= initial_weed_density <= 1:
            raise ValueError("Weed density must be between 0 and 1")
            
        self.city_name = city_name
        self.weed_density = initial_weed_density
        self.application_history: List[Tuple[datetime, float]] = []
        self.current_date = datetime.now()
        
    def apply_treatment(self, effectiveness: float) -> float:
        """
        Apply Capina Elétrica treatment.
        
        Args:
            effectiveness: Effectiveness of this application (0.0 to 1.0)
            
        Returns:
            New weed density after application
        """
        if not 0 <= effectiveness <= 1:
            raise ValueError("Effectiveness must be between 0 and 1")
            
        # Reduce weed density based on effectiveness
        new_density = self.weed_density * (1 - effectiveness)
        
        # Record application
        self.application_history.append((self.current_date, new_density))
        self.weed_density = new_density
        
        return new_density
    
    def simulate_growth(self, days: int, growth_rate: float = 0.05) -> None:
        """
        Simulate weed growth over time.
        
        Args:
            days: Number of days to simulate
            growth_rate: Daily growth rate multiplier
        """
        if days < 0:
            raise ValueError("Days must be positive")
            
        self.current_date += timedelta(days=days)
        
        # Simulate logistic growth with carrying capacity of 1.0
        for _ in range(days):
            self.weed_density += growth_rate * self.weed_density * (1 - self.weed_density)
            self.weed_density = min(1.0, self.weed_density)
    
    def get_effectiveness_duration(self, threshold: float = 0.5) -> Dict[int, int]:
        """
        Calculate effectiveness duration for each application.
        
        Args:
            threshold: Weed density threshold considered ineffective
            
        Returns:
            Dictionary mapping application index to days until threshold reached
        """
        results = {}
        temp_date = self.current_date
        temp_density = self.weed_density
        
        for i, (app_date, app_density) in enumerate(self.application_history):
            days = 0
            density = app_density
            
            while density < threshold and days < 365:  # Max 1 year
                days += 1
                density += 0.05 * density * (1 - density)  # Simplified growth
                
            results[i] = days if density >= threshold else -1  # -1 means never reached
            
        return results
    
    def get_application_summary(self) -> List[Dict]:
        """
        Get summary of all applications.
        
        Returns:
            List of dictionaries with application details
        """
        summary = []
        for i, (date, density) in enumerate(self.application_history):
            summary.append({
                'application_number': i + 1,
                'date': date.strftime('%Y-%m-%d'),
                'weed_density_after': density,
                'effectiveness': 1 - (density / (self.application_history[i-1][1] if i > 0 else 1))
            })
        return summary


def run_simulation():
    """Run a demo simulation of Capina Elétrica applications."""
    try:
        # Initialize simulation
        city = CapinaEletrica("São Paulo", initial_weed_density=0.8)
        
        # First application
        city.apply_treatment(effectiveness=0.7)
        city.simulate_growth(days=30)
        
        # Second application
        city.apply_treatment(effectiveness=0.6)
        city.simulate_growth(days=45)
        
        # Third application
        city.apply_treatment(effectiveness=0.5)
        city.simulate_growth(days=60)
        
        # Get results
        effectiveness_duration = city.get_effectiveness_duration()
        summary = city.get_application_summary()
        
        print(f"Simulation for {city.city_name}")
        print("\nApplication Summary:")
        for app in summary:
            print(f"App {app['application_number']} on {app['date']}: "
                  f"Effectiveness {app['effectiveness']:.0%}, "
                  f"Weed density after {app['weed_density_after']:.2f}")
        
        print("\nEffectiveness Duration (days until 50% weed density):")
        for app_num, days in effectiveness_duration.items():
            print(f"Application {app_num + 1}: {days} days")
            
    except Exception as e:
        print(f"Error in simulation: {str(e)}")


if __name__ == "__main__":
    run_simulation()
```
