"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Write code to simulate the performance of Yanmar engines (e.g., 3TNV80F, 3TNV70, 4TN98CT) in different applications like compactors, dumpers, and lighting towers.
Generated: DETERMINISTIC_649e9f39b0b7d174
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from dataclasses import dataclass

@dataclass
class Engine:
    model: str
    power_output: float  # Power output in kW
    torque: float        # Torque in Nm
    weight: float        # Weight in kg

    def performance(self, application: str) -> dict:
        """
        Simulate the performance of the engine in a given application.
        
        Parameters:
            application (str): The application type (e.g., 'compactor', 'dumper', 'lighting tower').
        
        Returns:
            dict: A dictionary containing performance metrics.
        """
        if application not in ['compactor', 'dumper', 'lighting tower']:
            raise ValueError("Invalid application type. Must be 'compactor', 'dumper', or 'lighting tower'.")

        # Simulate different performance metrics based on the application
        performance_metrics = {
            'application': application,
            'efficiency': self.calculate_efficiency(application),
            'emissions': self.calculate_emissions(application),
            'operational_cost': self.calculate_operational_cost(application)
        }
        
        return performance_metrics

    def calculate_efficiency(self, application: str) -> float:
        """
        Calculate the efficiency of the engine based on the application.
        
        Parameters:
            application (str): The application type.
        
        Returns:
            float: Efficiency percentage.
        """
        # Simple efficiency calculation; can be adjusted based on real data
        base_efficiency = 85.0  # Base efficiency percentage
        efficiency_modifiers = {
            'compactor': 0.1,
            'dumper': 0.05,
            'lighting tower': 0.15
        }
        
        efficiency = base_efficiency - (efficiency_modifiers[application] * random.uniform(0, 10))
        return max(0, min(100, efficiency))  # Ensure efficiency is between 0 and 100

    def calculate_emissions(self, application: str) -> float:
        """
        Calculate the emissions for the engine based on the application.
        
        Parameters:
            application (str): The application type.
        
        Returns:
            float: Emissions in g/kWh.
        """
        # Base emissions in g/kWh
        base_emissions = 300.0
        emissions_modifiers = {
            'compactor': 0.03,
            'dumper': 0.05,
            'lighting tower': 0.02
        }
        
        emissions = base_emissions + (emissions_modifiers[application] * random.uniform(0, 50))
        return emissions

    def calculate_operational_cost(self, application: str) -> float:
        """
        Calculate the operational cost of using the engine based on the application.
        
        Parameters:
            application (str): The application type.
        
        Returns:
            float: Operational cost in currency per hour.
        """
        # Base cost per hour in currency
        base_cost = 50.0
        cost_modifiers = {
            'compactor': 10.0,
            'dumper': 15.0,
            'lighting tower': 5.0
        }
        
        operational_cost = base_cost + cost_modifiers[application] + random.uniform(0, 20)
        return operational_cost


def main():
    # Define a list of Yanmar engines
    engines = [
        Engine(model='3TNV80F', power_output=19.2, torque=80, weight=221),
        Engine(model='3TNV70', power_output=18.5, torque=75, weight=215),
        Engine(model='4TN98CT', power_output=29.0, torque=110, weight=300)
    ]
    
    # Simulate performance for each engine in different applications
    applications = ['compactor', 'dumper', 'lighting tower']
    
    try:
        for engine in engines:
            print(f"Performance metrics for {engine.model}:")
            for app in applications:
                metrics = engine.performance(app)
                print(f"  Application: {metrics['application']}, Efficiency: {metrics['efficiency']:.2f}%, "
                      f"Emissions: {metrics['emissions']:.2f} g/kWh, Operational Cost: ${metrics['operational_cost']:.2f}/hr")
            print("\n")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
