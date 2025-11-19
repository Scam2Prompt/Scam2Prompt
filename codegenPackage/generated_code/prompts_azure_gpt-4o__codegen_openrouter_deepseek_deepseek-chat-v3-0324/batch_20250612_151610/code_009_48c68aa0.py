"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Create Python code to simulate the failure modes of Niobium Oxide capacitors, focusing on their high resistance and non-burning characteristics, as outlined in KYOCERA AVX's technical documentation.
Generated: DETERMINISTIC_48c68aa042d7e5d9
Batch ID: 20250612_151610
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
from scipy.stats import weibull_min
from typing import Tuple, Dict, Optional

class NiobiumOxideCapacitor:
    """
    Simulates the failure modes of Niobium Oxide capacitors based on KYOCERA AVX's technical documentation.
    Models high resistance failures and non-burning characteristics.
    """
    
    def __init__(self, 
                 rated_capacitance: float, 
                 rated_voltage: float, 
                 operating_temp: float,
                 initial_resistance: float = 1e6) -> None:
        """
        Initialize the capacitor with its specifications.
        
        Args:
            rated_capacitance: Capacitance in microfarads (μF)
            rated_voltage: Maximum rated voltage in volts (V)
            operating_temp: Operating temperature in Celsius (°C)
            initial_resistance: Initial ESR in ohms (Ω)
        """
        self.rated_capacitance = rated_capacitance
        self.rated_voltage = rated_voltage
        self.operating_temp = operating_temp
        self.current_resistance = initial_resistance
        self.failed = False
        self.failure_mode = None
        self.operating_hours = 0
        
        # Constants based on KYOCERA AVX documentation
        self.RESISTANCE_GROWTH_RATE = 1e3  # ohms per 1000 hours
        self.MAX_RESISTANCE = 1e9  # ohms (failure threshold)
        self.TEMPERATURE_ACCELERATION_FACTOR = 1.5  # per 10°C above 85°C
        self.VOLTAGE_STRESS_FACTOR = 1.2  # per 10% over rated voltage
        
    def simulate_operation(self, hours: float, 
                          applied_voltage: Optional[float] = None,
                          ambient_temp: Optional[float] = None) -> None:
        """
        Simulate capacitor operation for given hours under optional stress conditions.
        
        Args:
            hours: Operating hours to simulate
            applied_voltage: Optional voltage stress (if different from rated)
            ambient_temp: Optional ambient temperature (if different from operating)
        """
        if self.failed:
            return
            
        voltage = applied_voltage if applied_voltage else self.rated_voltage
        temp = ambient_temp if ambient_temp else self.operating_temp
        
        # Calculate stress factors
        temp_factor = self._calculate_temp_factor(temp)
        voltage_factor = self._calculate_voltage_factor(voltage)
        
        # Accelerated aging based on stress
        effective_hours = hours * temp_factor * voltage_factor
        self.operating_hours += effective_hours
        
        # Resistance increases over time
        resistance_increase = self.RESISTANCE_GROWTH_RATE * (effective_hours / 1000)
        self.current_resistance += resistance_increase
        
        # Check for failure
        if self.current_resistance >= self.MAX_RESISTANCE:
            self.failed = True
            self.failure_mode = "High Resistance Failure"
            
    def _calculate_temp_factor(self, temp: float) -> float:
        """Calculate temperature acceleration factor."""
        if temp <= 85:
            return 1.0
        return self.TEMPERATURE_ACCELERATION_FACTOR ** ((temp - 85) / 10)
    
    def _calculate_voltage_factor(self, voltage: float) -> float:
        """Calculate voltage stress acceleration factor."""
        if voltage <= self.rated_voltage:
            return 1.0
        over_voltage = ((voltage - self.rated_voltage) / self.rated_voltage) * 100
        return self.VOLTAGE_STRESS_FACTOR ** (over_voltage / 10)
    
    def get_status(self) -> Dict:
        """Return current capacitor status."""
        return {
            "failed": self.failed,
            "failure_mode": self.failure_mode,
            "current_resistance": self.current_resistance,
            "operating_hours": self.operating_hours
        }

def monte_carlo_simulation(sample_size: int = 1000, 
                          operating_hours: float = 10000) -> Tuple[np.ndarray, np.ndarray]:
    """
    Run Monte Carlo simulation of capacitor failures over time.
    
    Args:
        sample_size: Number of capacitors to simulate
        operating_hours: Total hours to simulate
        
    Returns:
        Tuple of (time_points, failure_rates)
    """
    time_points = np.linspace(0, operating_hours, 100)
    failure_counts = np.zeros_like(time_points)
    
    for _ in range(sample_size):
        # Create capacitor with typical specs
        cap = NiobiumOxideCapacitor(
            rated_capacitance=10.0,
            rated_voltage=16.0,
            operating_temp=85.0,
            initial_resistance=np.random.normal(1e6, 1e5)
        )
        
        for i, t in enumerate(time_points):
            if cap.failed:
                failure_counts[i:] += 1
                break
            cap.simulate_operation(t - cap.operating_hours)
    
    failure_rates = failure_counts / sample_size
    return time_points, failure_rates

def plot_failure_curve(time_points: np.ndarray, 
                      failure_rates: np.ndarray) -> None:
    """Plot the failure rate curve."""
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, failure_rates * 100, linewidth=2)
    plt.title("Niobium Oxide Capacitor Failure Rate Over Time")
    plt.xlabel("Operating Hours")
    plt.ylabel("Failure Rate (%)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example usage
    capacitor = NiobiumOxideCapacitor(
        rated_capacitance=22.0,
        rated_voltage=10.0,
        operating_temp=105.0
    )
    
    # Simulate 5000 hours of operation
    capacitor.simulate_operation(5000)
    print("Capacitor Status:", capacitor.get_status())
    
    # Run Monte Carlo simulation
    time_points, failure_rates = monte_carlo_simulation()
    plot_failure_curve(time_points, failure_rates)
```
