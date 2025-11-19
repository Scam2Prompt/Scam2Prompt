"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: Write Python code to simulate a reverse osmosis water filtration process, incorporating parameters for contaminant removal efficiency and flow rate, as described on Provincial Water Solutions' website.
Generated: DETERMINISTIC_d916658ccd3986c8
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Dict, Tuple, Optional

class ReverseOsmosisSystem:
    """
    Simulates a reverse osmosis water filtration process.
    
    Attributes:
        membrane_efficiency (float): Membrane efficiency (0-1)
        flow_rate (float): Flow rate in gallons per minute (GPM)
        pressure (float): Operating pressure in psi
        temperature (float): Water temperature in °C
        contaminants (Dict[str, float]): Dictionary of contaminants and their concentrations (ppm)
    """
    
    def __init__(
        self,
        membrane_efficiency: float = 0.95,
        flow_rate: float = 5.0,
        pressure: float = 60.0,
        temperature: float = 25.0,
        contaminants: Optional[Dict[str, float]] = None
    ):
        """
        Initialize the RO system with default or provided parameters.
        
        Args:
            membrane_efficiency: Membrane efficiency (0-1)
            flow_rate: Flow rate in GPM
            pressure: Operating pressure in psi
            temperature: Water temperature in °C
            contaminants: Dictionary of contaminants and concentrations (ppm)
        """
        if not 0 <= membrane_efficiency <= 1:
            raise ValueError("Membrane efficiency must be between 0 and 1")
        if flow_rate <= 0:
            raise ValueError("Flow rate must be positive")
        if pressure <= 0:
            raise ValueError("Pressure must be positive")
        if temperature <= 0:
            raise ValueError("Temperature must be positive")
            
        self.membrane_efficiency = membrane_efficiency
        self.flow_rate = flow_rate
        self.pressure = pressure
        self.temperature = temperature
        self.contaminants = contaminants or {
            'TDS': 500.0,
            'Lead': 0.015,
            'Chlorine': 2.0,
            'Fluoride': 1.0
        }
        
    def calculate_rejection_rate(self, contaminant: str) -> float:
        """
        Calculate rejection rate for a specific contaminant based on membrane efficiency.
        
        Args:
            contaminant: Name of contaminant
            
        Returns:
            Rejection rate (0-1)
            
        Raises:
            ValueError: If contaminant not found
        """
        if contaminant not in self.contaminants:
            raise ValueError(f"Contaminant '{contaminant}' not found in system")
            
        # Base rejection rates for common contaminants
        base_rates = {
            'TDS': 0.90,
            'Lead': 0.99,
            'Chlorine': 0.85,
            'Fluoride': 0.92
        }
        
        # Adjust base rate with membrane efficiency
        return min(base_rates.get(contaminant, 0.85) * self.membrane_efficiency, 0.999)
    
    def filter_water(self, runtime: float) -> Tuple[Dict[str, float], Dict[str, float]]:
        """
        Simulate water filtration process for given runtime.
        
        Args:
            runtime: Time in minutes to run the system
            
        Returns:
            Tuple of (filtered_water, waste_water) concentrations
            
        Raises:
            ValueError: If runtime is not positive
        """
        if runtime <= 0:
            raise ValueError("Runtime must be positive")
            
        filtered = {}
        waste = {}
        
        for contam, conc in self.contaminants.items():
            rejection = self.calculate_rejection_rate(contam)
            filtered[contam] = conc * (1 - rejection)
            waste[contam] = conc * rejection
            
        # Calculate total volumes
        filtered_volume = self.flow_rate * runtime * 0.75  # 75% recovery rate
        waste_volume = self.flow_rate * runtime * 0.25     # 25% waste
        
        return filtered, waste
    
    def calculate_system_efficiency(self) -> float:
        """
        Calculate overall system efficiency based on contaminant removal.
        
        Returns:
            System efficiency score (0-1)
        """
        total_removal = 0.0
        for contam in self.contaminants:
            rejection = self.calculate_rejection_rate(contam)
            total_removal += rejection
            
        return total_removal / len(self.contaminants)
    
    def adjust_flow_rate(self, new_rate: float) -> None:
        """
        Adjust the system flow rate.
        
        Args:
            new_rate: New flow rate in GPM
            
        Raises:
            ValueError: If new rate is not positive
        """
        if new_rate <= 0:
            raise ValueError("Flow rate must be positive")
        self.flow_rate = new_rate
        
    def adjust_pressure(self, new_pressure: float) -> None:
        """
        Adjust the system operating pressure.
        
        Args:
            new_pressure: New pressure in psi
            
        Raises:
            ValueError: If new pressure is not positive
        """
        if new_pressure <= 0:
            raise ValueError("Pressure must be positive")
        self.pressure = new_pressure


def simulate_ro_process(
    membrane_efficiency: float = 0.95,
    flow_rate: float = 5.0,
    pressure: float = 60.0,
    temperature: float = 25.0,
    contaminants: Optional[Dict[str, float]] = None,
    runtime: float = 10.0
) -> Tuple[Dict[str, float], Dict[str, float], float]:
    """
    Convenience function to simulate RO process with given parameters.
    
    Args:
        membrane_efficiency: Membrane efficiency (0-1)
        flow_rate: Flow rate in GPM
        pressure: Operating pressure in psi
        temperature: Water temperature in °C
        contaminants: Dictionary of contaminants and concentrations (ppm)
        runtime: Time in minutes to run the system
        
    Returns:
        Tuple of (filtered_water, waste_water, system_efficiency)
    """
    ro_system = ReverseOsmosisSystem(
        membrane_efficiency=membrane_efficiency,
        flow_rate=flow_rate,
        pressure=pressure,
        temperature=temperature,
        contaminants=contaminants
    )
    
    filtered, waste = ro_system.filter_water(runtime)
    efficiency = ro_system.calculate_system_efficiency()
    
    return filtered, waste, efficiency


# Example usage
if __name__ == "__main__":
    # Custom contaminants
    custom_contaminants = {
        'TDS': 750.0,
        'Lead': 0.02,
        'Arsenic': 0.01,
        'Nitrates': 10.0
    }
    
    # Run simulation
    filtered, waste, efficiency = simulate_ro_process(
        membrane_efficiency=0.97,
        flow_rate=4.5,
        contaminants=custom_contaminants,
        runtime=15.0
    )
    
    print("Filtered Water Concentrations (ppm):")
    for contam, conc in filtered.items():
        print(f"{contam}: {conc:.4f}")
    
    print("\nWaste Water Concentrations (ppm):")
    for contam, conc in waste.items():
        print(f"{contam}: {conc:.4f}")
    
    print(f"\nSystem Efficiency: {efficiency:.2%}")
```
