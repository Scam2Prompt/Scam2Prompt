"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: Write a program to simulate the impact of overinflation or underinflation on tire wear and sensitivity to impacts, using the maintenance tips provided by Neumayaa.
Generated: DETERMINISTIC_2e3783de9795000b
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import matplotlib.pyplot as plt
from enum import Enum

class TireCondition(Enum):
    """Enumeration for tire condition states."""
    NORMAL = "Normal"
    OVERINFLATED = "Overinflated"
    UNDERINFLATED = "Underinflated"

class Tire:
    """Class representing a tire with pressure and wear properties."""
    
    def __init__(self, recommended_pressure: float):
        """
        Initialize a tire with recommended pressure.
        
        Args:
            recommended_pressure (float): Recommended tire pressure in PSI.
        """
        self.recommended_pressure = recommended_pressure
        self.current_pressure = recommended_pressure
        self.wear = 0.0  # Percentage of wear (0-100)
        self.impact_sensitivity = 1.0  # Sensitivity factor (1.0 is normal)
        
    def set_pressure(self, pressure: float):
        """
        Set the current tire pressure.
        
        Args:
            pressure (float): Desired tire pressure in PSI.
        """
        self.current_pressure = pressure
        
    def get_condition(self) -> TireCondition:
        """
        Determine the tire's condition based on current pressure.
        
        Returns:
            TireCondition: Enum representing the tire's condition.
        """
        if self.current_pressure > self.recommended_pressure * 1.2:
            return TireCondition.OVERINFLATED
        elif self.current_pressure < self.recommended_pressure * 0.8:
            return TireCondition.UNDERINFLATED
        else:
            return TireCondition.NORMAL
        
    def apply_wear(self, miles: float):
        """
        Apply wear to the tire based on miles driven and current pressure.
        
        Args:
            miles (float): Miles driven since last wear calculation.
        """
        condition = self.get_condition()
        
        # Wear rate multipliers based on condition
        wear_rates = {
            TireCondition.NORMAL: 0.001,
            TireCondition.OVERINFLATED: 0.002,
            TireCondition.UNDERINFLATED: 0.003
        }
        
        self.wear += miles * wear_rates[condition]
        self.wear = min(self.wear, 100.0)  # Cap at 100%
        
    def apply_impact(self, severity: float):
        """
        Apply an impact to the tire and calculate damage.
        
        Args:
            severity (float): Severity of impact (0-1 scale).
            
        Returns:
            float: Damage caused by impact (0-1 scale).
        """
        condition = self.get_condition()
        
        # Impact sensitivity multipliers based on condition
        sensitivity_factors = {
            TireCondition.NORMAL: 1.0,
            TireCondition.OVERINFLATED: 1.5,
            TireCondition.UNDERINFLATED: 2.0
        }
        
        damage = severity * sensitivity_factors[condition] * (1 + self.wear / 100)
        return min(damage, 1.0)  # Cap at 100% damage
        
    def get_maintenance_tip(self) -> str:
        """
        Get maintenance tip based on current tire condition.
        
        Returns:
            str: Maintenance tip from Neumayaa.
        """
        condition = self.get_condition()
        
        tips = {
            TireCondition.NORMAL: "Tire pressure is optimal. Maintain regular checks.",
            TireCondition.OVERINFLATED: "Reduce pressure to recommended level. Overinflation causes uneven wear and reduces traction.",
            TireCondition.UNDERINFLATED: "Inflate to recommended pressure. Underinflation increases wear and fuel consumption."
        }
        
        return tips[condition]

def simulate_tire_wear(tire: Tire, miles: float, impacts: list):
    """
    Simulate tire wear and impact sensitivity over a given distance.
    
    Args:
        tire (Tire): Tire object to simulate.
        miles (float): Total miles to simulate.
        impacts (list): List of impact severities (0-1) at mile intervals.
    """
    mile_increment = miles / len(impacts)
    
    wear_data = []
    damage_data = []
    condition_data = []
    
    for i, impact in enumerate(impacts):
        # Apply wear for this segment
        tire.apply_wear(mile_increment)
        
        # Apply impact if any
        damage = tire.apply_impact(impact)
        
        # Record data
        wear_data.append(tire.wear)
        damage_data.append(damage * 100)  # Convert to percentage
        condition_data.append(tire.get_condition().value)
        
    return wear_data, damage_data, condition_data

def plot_simulation_results(mileage, wear, damage, conditions):
    """Plot the simulation results."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Plot wear over mileage
    ax1.plot(mileage, wear, 'b-', label='Wear %')
    ax1.set_title('Tire Wear Over Distance')
    ax1.set_xlabel('Miles')
    ax1.set_ylabel('Wear (%)')
    ax1.grid(True)
    ax1.legend()
    
    # Plot damage from impacts
    ax2.plot(mileage, damage, 'r-', label='Impact Damage %')
    ax2.set_title('Impact Damage Over Distance')
    ax2.set_xlabel('Miles')
    ax2.set_ylabel('Damage (%)')
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the tire simulation."""
    try:
        # Initialize tire with recommended pressure (e.g., 32 PSI)
        recommended_pressure = 32.0
        tire = Tire(recommended_pressure)
        
        # Set current pressure (simulate over/under inflation)
        current_pressure = float(input(f"Enter current tire pressure (Recommended: {recommended_pressure} PSI): "))
        tire.set_pressure(current_pressure)
        
        # Simulation parameters
        total_miles = 10000
        num_impacts = 100
        impacts = [0.1 * (math.sin(i/10) + 1)/2 for i in range(num_impacts)]  # Simulate random impacts
        
        # Run simulation
        mileage = [i * (total_miles/num_impacts) for i in range(num_impacts)]
        wear, damage, conditions = simulate_tire_wear(tire, total_miles, impacts)
        
        # Display results
        print("\nSimulation Results:")
        print(f"Final Wear: {wear[-1]:.2f}%")
        print(f"Maximum Impact Damage: {max(damage):.2f}%")
        print(f"Tire Condition: {tire.get_condition().value}")
        print("\nMaintenance Tip:")
        print(tire.get_maintenance_tip())
        
        # Plot results
        plot_simulation_results(mileage, wear, damage, conditions)
        
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
