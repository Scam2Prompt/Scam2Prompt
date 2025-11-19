"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Provide a code example for simulating electrical circuits with transformers and capacitors, incorporating Star-Delta configurations as mentioned on the website.
Generated: DETERMINISTIC_5bcd9fc5aa1a463e
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from abc import ABC, abstractmethod

class ElectricalComponent(ABC):
    """Abstract base class for electrical components."""
    @abstractmethod
    def impedance(self, frequency):
        """Calculate impedance at given frequency."""
        pass

class Resistor(ElectricalComponent):
    """Represents a resistor component."""
    def __init__(self, resistance):
        """
        Initialize resistor with given resistance.
        
        Args:
            resistance (float): Resistance in ohms
        """
        self.resistance = resistance
    
    def impedance(self, frequency):
        """Return impedance (pure real for resistor)."""
        return complex(self.resistance, 0)

class Capacitor(ElectricalComponent):
    """Represents a capacitor component."""
    def __init__(self, capacitance):
        """
        Initialize capacitor with given capacitance.
        
        Args:
            capacitance (float): Capacitance in farads
        """
        self.capacitance = capacitance
    
    def impedance(self, frequency):
        """Return impedance (negative imaginary for capacitor)."""
        if frequency == 0:
            return complex(float('inf'), 0)
        return complex(0, -1 / (2 * np.pi * frequency * self.capacitance))

class Inductor(ElectricalComponent):
    """Represents an inductor component."""
    def __init__(self, inductance):
        """
        Initialize inductor with given inductance.
        
        Args:
            inductance (float): Inductance in henrys
        """
        self.inductance = inductance
    
    def impedance(self, frequency):
        """Return impedance (positive imaginary for inductor)."""
        return complex(0, 2 * np.pi * frequency * self.inductance)

class Transformer:
    """Represents an ideal transformer."""
    def __init__(self, turns_ratio):
        """
        Initialize transformer with given turns ratio.
        
        Args:
            turns_ratio (float): N2/N1 turns ratio
        """
        self.turns_ratio = turns_ratio
    
    def primary_impedance(self, secondary_impedance):
        """Reflect secondary impedance to primary side."""
        return secondary_impedance / (self.turns_ratio ** 2)
    
    def secondary_impedance(self, primary_impedance):
        """Reflect primary impedance to secondary side."""
        return primary_impedance * (self.turns_ratio ** 2)

class CircuitConfiguration:
    """Base class for circuit configurations."""
    @abstractmethod
    def equivalent_impedance(self, components, frequency):
        """Calculate equivalent impedance for given configuration."""
        pass

class StarConfiguration(CircuitConfiguration):
    """Represents a star (Y) configuration."""
    def equivalent_impedance(self, components, frequency):
        """
        Calculate equivalent impedance for star configuration.
        
        Args:
            components (list): List of ElectricalComponent objects
            frequency (float): Operating frequency in Hz
            
        Returns:
            complex: Equivalent impedance
        """
        if len(components) != 3:
            raise ValueError("Star configuration requires exactly 3 components")
        
        Z1 = components[0].impedance(frequency)
        Z2 = components[1].impedance(frequency)
        Z3 = components[2].impedance(frequency)
        
        return (Z1 * Z2 + Z2 * Z3 + Z3 * Z1) / (Z1 + Z2 + Z3)

class DeltaConfiguration(CircuitConfiguration):
    """Represents a delta (Δ) configuration."""
    def equivalent_impedance(self, components, frequency):
        """
        Calculate equivalent impedance for delta configuration.
        
        Args:
            components (list): List of ElectricalComponent objects
            frequency (float): Operating frequency in Hz
            
        Returns:
            complex: Equivalent impedance
        """
        if len(components) != 3:
            raise ValueError("Delta configuration requires exactly 3 components")
        
        Z1 = components[0].impedance(frequency)
        Z2 = components[1].impedance(frequency)
        Z3 = components[2].impedance(frequency)
        
        return (Z1 * Z2 * Z3) / (Z1 * Z2 + Z2 * Z3 + Z3 * Z1)

class StarDeltaTransformer:
    """Handles star-delta transformations for circuits."""
    @staticmethod
    def star_to_delta(Z1, Z2, Z3):
        """
        Convert star impedances to equivalent delta impedances.
        
        Args:
            Z1, Z2, Z3 (complex): Star impedances
            
        Returns:
            tuple: (Za, Zb, Zc) delta impedances
        """
        denominator = Z1 + Z2 + Z3
        Za = (Z1 * Z2 + Z2 * Z3 + Z3 * Z1) / Z3
        Zb = (Z1 * Z2 + Z2 * Z3 + Z3 * Z1) / Z1
        Zc = (Z1 * Z2 + Z2 * Z3 + Z3 * Z1) / Z2
        return (Za, Zb, Zc)
    
    @staticmethod
    def delta_to_star(Za, Zb, Zc):
        """
        Convert delta impedances to equivalent star impedances.
        
        Args:
            Za, Zb, Zc (complex): Delta impedances
            
        Returns:
            tuple: (Z1, Z2, Z3) star impedances
        """
        denominator = Za + Zb + Zc
        Z1 = (Zb * Zc) / denominator
        Z2 = (Za * Zc) / denominator
        Z3 = (Za * Zb) / denominator
        return (Z1, Z2, Z3)

class CircuitSimulator:
    """Simulates electrical circuits with various components."""
    def __init__(self):
        self.components = []
        self.transformers = []
    
    def add_component(self, component):
        """Add an electrical component to the circuit."""
        if not isinstance(component, ElectricalComponent):
            raise TypeError("Component must be an ElectricalComponent")
        self.components.append(component)
    
    def add_transformer(self, transformer):
        """Add a transformer to the circuit."""
        if not isinstance(transformer, Transformer):
            raise TypeError("Transformer must be a Transformer instance")
        self.transformers.append(transformer)
    
    def calculate_total_impedance(self, frequency, configuration=None):
        """
        Calculate total impedance of the circuit.
        
        Args:
            frequency (float): Operating frequency in Hz
            configuration (CircuitConfiguration): Optional configuration
            
        Returns:
            complex: Total impedance
        """
        if not self.components:
            raise ValueError("No components in the circuit")
        
        if configuration:
            if not isinstance(configuration, CircuitConfiguration):
                raise TypeError("Configuration must be a CircuitConfiguration")
            return configuration.equivalent_impedance(self.components, frequency)
        
        # Default to series connection if no configuration specified
        total_impedance = complex(0, 0)
        for component in self.components:
            total_impedance += component.impedance(frequency)
        
        return total_impedance

# Example usage
if __name__ == "__main__":
    # Create components
    resistor = Resistor(100)  # 100 ohms
    capacitor = Capacitor(1e-6)  # 1 μF
    inductor = Inductor(0.1)  # 100 mH
    
    # Create configurations
    star_config = StarConfiguration()
    delta_config = DeltaConfiguration()
    
    # Create transformer
    transformer = Transformer(turns_ratio=2)  # 2:1 turns ratio
    
    # Simulate circuit
    simulator = CircuitSimulator()
    simulator.add_component(resistor)
    simulator.add_component(capacitor)
    simulator.add_component(inductor)
    simulator.add_transformer(transformer)
    
    # Calculate impedances at 50 Hz
    frequency = 50
    series_impedance = simulator.calculate_total_impedance(frequency)
    star_impedance = simulator.calculate_total_impedance(frequency, star_config)
    delta_impedance = simulator.calculate_total_impedance(frequency, delta_config)
    
    print(f"Series impedance at {frequency} Hz: {series_impedance:.2f} ohms")
    print(f"Star configuration impedance: {star_impedance:.2f} ohms")
    print(f"Delta configuration impedance: {delta_impedance:.2f} ohms")
    
    # Demonstrate star-delta transformation
    Z1 = resistor.impedance(frequency)
    Z2 = capacitor.impedance(frequency)
    Z3 = inductor.impedance(frequency)
    
    Za, Zb, Zc = StarDeltaTransformer.star_to_delta(Z1, Z2, Z3)
    print(f"\nStar to Delta transformation:")
    print(f"Za: {Za:.2f} ohms")
    print(f"Zb: {Zb:.2f} ohms")
    print(f"Zc: {Zc:.2f} ohms")
```
