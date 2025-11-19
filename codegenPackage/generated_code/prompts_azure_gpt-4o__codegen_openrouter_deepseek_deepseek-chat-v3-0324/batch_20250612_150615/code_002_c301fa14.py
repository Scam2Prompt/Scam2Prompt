"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Generate Python code to calculate the required passive components (e.g., resistors and capacitors) for a circuit using ATMEGA328P-PU microcontroller.
Generated: DETERMINISTIC_c301fa14d7ccb040
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ATmega328PComponentCalculator:
    """
    Calculator for passive components in ATmega328P-PU microcontroller circuits.
    Handles calculations for oscillator, reset, and decoupling components.
    """
    
    def __init__(self, clock_frequency=16e6, vcc=5.0):
        """
        Initialize calculator with default parameters.
        
        Args:
            clock_frequency (float): Desired clock frequency in Hz (default: 16MHz)
            vcc (float): Operating voltage in volts (default: 5.0V)
        """
        self.clock_frequency = clock_frequency
        self.vcc = vcc
        
    def calculate_crystal_oscillator_components(self, crystal_freq, load_capacitance=22e-12, esr=30):
        """
        Calculate components for crystal oscillator circuit.
        
        Args:
            crystal_freq (float): Crystal frequency in Hz
            load_capacitance (float): Load capacitance in Farads (default: 22pF)
            esr (float): Crystal equivalent series resistance in ohms (default: 30Ω)
            
        Returns:
            dict: Dictionary containing calculated component values
        """
        try:
            # Calculate the required capacitance for each crystal pin
            c1 = c2 = 2 * load_capacitance - 5e-12  # 5pF is typical stray capacitance
            
            # Verify the crystal meets the startup requirements
            gm_crit = 4 * esr * (2 * math.pi * crystal_freq)**2 * (load_capacitance + 5e-12)**2
            gm_atmega = 10e-3  # Typical transconductance for ATmega328P
            
            if gm_atmega < gm_crit:
                raise ValueError("Crystal ESR too high for reliable startup")
                
            return {
                'crystal_frequency': crystal_freq,
                'load_capacitance': load_capacitance,
                'c1': max(c1, 12e-12),  # Minimum recommended is 12pF
                'c2': max(c2, 12e-12),
                'esr': esr,
                'gm_critical': gm_crit,
                'gm_microcontroller': gm_atmega,
                'startup_ok': gm_atmega > gm_crit
            }
            
        except Exception as e:
            raise ValueError(f"Error calculating crystal components: {str(e)}")
    
    def calculate_reset_pullup_resistor(self, reset_current=0.1e-3):
        """
        Calculate reset pull-up resistor value.
        
        Args:
            reset_current (float): Desired reset pin current in Amps (default: 0.1mA)
            
        Returns:
            float: Resistor value in ohms
        """
        try:
            if reset_current <= 0:
                raise ValueError("Reset current must be positive")
                
            # Vcc - 0.5V (reset threshold) / desired current
            r = (self.vcc - 0.5) / reset_current
            
            # Standard resistor value between 4.7kΩ and 10kΩ is typical
            return min(max(r, 4.7e3), 10e3)
            
        except Exception as e:
            raise ValueError(f"Error calculating reset resistor: {str(e)}")
    
    def calculate_decoupling_capacitors(self, num_caps=2):
        """
        Recommend decoupling capacitor values.
        
        Args:
            num_caps (int): Number of capacitors to recommend (default: 2)
            
        Returns:
            list: List of recommended capacitor values in Farads
        """
        try:
            if num_caps < 1:
                raise ValueError("At least one decoupling capacitor is required")
                
            # Typical decoupling scheme: 100nF + 10µF
            standard_values = [100e-9, 10e-6]
            
            # Return the requested number of capacitors
            return standard_values[:num_caps]
            
        except Exception as e:
            raise ValueError(f"Error determining decoupling capacitors: {str(e)}")
    
    def calculate_brown_out_detector_resistor(self, bod_level=2.7):
        """
        Calculate voltage divider for external brown-out detection.
        
        Args:
            bod_level (float): Desired brown-out detection level in volts
            
        Returns:
            dict: Dictionary with R1 and R2 values in ohms
        """
        try:
            if bod_level >= self.vcc:
                raise ValueError("BOD level must be below VCC")
                
            # ATmega328P BOD comparator threshold is ~1.3V
            v_ref = 1.3
            ratio = (self.vcc / v_ref) - 1
            
            # Calculate resistor values (R2 = 10kΩ is typical)
            r2 = 10e3
            r1 = r2 * (ratio - (bod_level / v_ref))
            
            return {
                'bod_level': bod_level,
                'r1': r1,
                'r2': r2,
                'v_ref': v_ref
            }
            
        except Exception as e:
            raise ValueError(f"Error calculating BOD resistors: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        calculator = ATmega328PComponentCalculator(clock_frequency=16e6, vcc=5.0)
        
        # Crystal oscillator components
        crystal = calculator.calculate_crystal_oscillator_components(16e6)
        print("Crystal Oscillator Components:")
        for k, v in crystal.items():
            print(f"{k:15}: {v}")
        
        # Reset pull-up resistor
        reset_r = calculator.calculate_reset_pullup_resistor()
        print(f"\nReset Pull-up Resistor: {reset_r:.0f} Ω")
        
        # Decoupling capacitors
        decoupling = calculator.calculate_decoupling_capacitors()
        print("\nDecoupling Capacitors:")
        for i, cap in enumerate(decoupling, 1):
            print(f"C{i}: {cap * 1e6:.1f} µF")
        
        # Brown-out detector (if needed)
        bod = calculator.calculate_brown_out_detector_resistor(2.7)
        print("\nBrown-out Detector Components:")
        print(f"R1: {bod['r1']:.0f} Ω")
        print(f"R2: {bod['r2']:.0f} Ω")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
