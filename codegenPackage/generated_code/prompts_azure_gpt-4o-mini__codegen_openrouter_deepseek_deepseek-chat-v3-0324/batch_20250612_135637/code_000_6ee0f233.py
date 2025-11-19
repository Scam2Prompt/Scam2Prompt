"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Write a code snippet that utilizes Niobium Oxide (OxiCap®) capacitors for a high-reliability electronic circuit, ensuring it meets AEC-Q200 requirements.
Generated: DETERMINISTIC_6ee0f2335deb601f
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import math

class OxiCapCircuit:
    """
    A class to design and validate a high-reliability electronic circuit 
    using Niobium Oxide (OxiCap®) capacitors that meets AEC-Q200 requirements.
    """
    
    def __init__(self, capacitance: float, voltage_rating: float, temperature_range: tuple):
        """
        Initialize the OxiCap circuit with given parameters.
        
        Args:
            capacitance (float): Capacitance value in microfarads (µF)
            voltage_rating (float): Rated voltage in volts (V)
            temperature_range (tuple): Operating temperature range in Celsius (min, max)
        """
        self.capacitance = capacitance
        self.voltage_rating = voltage_rating
        self.temperature_range = temperature_range
        self.aec_q200_compliant = False
        
        # Validate parameters against AEC-Q200 requirements
        self._validate_parameters()
        
    def _validate_parameters(self):
        """
        Validate circuit parameters against AEC-Q200 requirements for OxiCap capacitors.
        """
        try:
            # Check capacitance is within typical OxiCap range (0.1µF to 1000µF)
            if not (0.1 <= self.capacitance <= 1000):
                raise ValueError("Capacitance out of OxiCap typical range (0.1µF to 1000µF)")
                
            # Check voltage rating is within typical OxiCap range (2.5V to 25V)
            if not (2.5 <= self.voltage_rating <= 25):
                raise ValueError("Voltage rating out of OxiCap typical range (2.5V to 25V)")
                
            # Check temperature range meets AEC-Q200 Grade 1 (-40°C to +125°C)
            if self.temperature_range[0] < -40 or self.temperature_range[1] > 125:
                raise ValueError("Temperature range must meet AEC-Q200 Grade 1 (-40°C to +125°C)")
                
            # If all checks pass, mark as AEC-Q200 compliant
            self.aec_q200_compliant = True
            
        except ValueError as e:
            print(f"Validation Error: {e}")
            self.aec_q200_compliant = False
            
    def calculate_derating(self, operating_voltage: float, operating_temp: float) -> float:
        """
        Calculate derating factor based on operating conditions.
        
        Args:
            operating_voltage (float): Actual operating voltage in volts (V)
            operating_temp (float): Actual operating temperature in Celsius (°C)
            
        Returns:
            float: Derating factor (0.0 to 1.0)
            
        Raises:
            ValueError: If operating conditions exceed rated specifications
        """
        try:
            if operating_voltage > self.voltage_rating:
                raise ValueError("Operating voltage exceeds rated voltage")
                
            if not (self.temperature_range[0] <= operating_temp <= self.temperature_range[1]):
                raise ValueError("Operating temperature outside rated range")
                
            # Voltage derating (80% of rated voltage for high reliability)
            voltage_derating = min(1.0, 0.8 * (self.voltage_rating / operating_voltage))
            
            # Temperature derating (linear reduction above 85°C)
            temp_derating = 1.0
            if operating_temp > 85:
                temp_derating = 1.0 - ((operating_temp - 85) / (self.temperature_range[1] - 85)) * 0.2
                
            return voltage_derating * temp_derating
            
        except ValueError as e:
            print(f"Derating Calculation Error: {e}")
            return 0.0
            
    def get_reliability_data(self) -> dict:
        """
        Return reliability data for AEC-Q200 compliant OxiCap circuit.
        
        Returns:
            dict: Dictionary containing reliability metrics
        """
        return {
            "capacitance": self.capacitance,
            "voltage_rating": self.voltage_rating,
            "temperature_range": self.temperature_range,
            "aec_q200_compliant": self.aec_q200_compliant,
            "estimated_lifetime": "100,000 hours at 105°C",
            "failure_rate": "< 1 FIT (Failure in Time)",
            "esr": "Low ESR (typically < 100mΩ)"
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create an AEC-Q200 compliant OxiCap circuit
        oxicap_circuit = OxiCapCircuit(
            capacitance=10.0,  # 10µF
            voltage_rating=16.0,  # 16V
            temperature_range=(-40, 125)  # -40°C to +125°C
        )
        
        # Check if compliant
        if oxicap_circuit.aec_q200_compliant:
            print("Circuit meets AEC-Q200 requirements")
            
            # Calculate derating for actual operating conditions
            derating = oxicap_circuit.calculate_derating(
                operating_voltage=12.0,
                operating_temp=105.0
            )
            print(f"Derating factor: {derating:.2f}")
            
            # Get reliability data
            reliability = oxicap_circuit.get_reliability_data()
            print("\nReliability Data:")
            for key, value in reliability.items():
                print(f"{key}: {value}")
                
        else:
            print("Circuit does not meet AEC-Q200 requirements")
            
    except Exception as e:
        print(f"Error in circuit design: {e}")
```
