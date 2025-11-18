"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Write Python code to simulate the operation of a Schulz screw compressor (SRP 4000) based on its technical specifications, including pressure and flow rate.
Generated: DETERMINISTIC_a4a43b4191829e60
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SchulzScrewCompressor:
    """
    A class to simulate the operation of a Schulz screw compressor (SRP 4000).
    
    Attributes:
        max_pressure (float): Maximum output pressure of the compressor in bar.
        max_flow_rate (float): Maximum flow rate of the compressor in m³/h.
        current_pressure (float): Current pressure of the compressor in bar.
        current_flow_rate (float): Current flow rate of the compressor in m³/h.
    """

    def __init__(self, max_pressure: float, max_flow_rate: float):
        """
        Initializes the SchulzScrewCompressor with specified maximum pressure and flow rate.

        Args:
            max_pressure (float): Maximum output pressure in bar.
            max_flow_rate (float): Maximum flow rate in m³/h.

        Raises:
            ValueError: If max_pressure or max_flow_rate is negative.
        """
        if max_pressure < 0:
            raise ValueError("Maximum pressure must be non-negative.")
        if max_flow_rate < 0:
            raise ValueError("Maximum flow rate must be non-negative.")
        
        self.max_pressure = max_pressure
        self.max_flow_rate = max_flow_rate
        self.current_pressure = 0.0
        self.current_flow_rate = 0.0

    def start(self):
        """Starts the compressor, initializing current values."""
        self.current_pressure = 0.0
        self.current_flow_rate = 0.0
        print("Compressor started.")

    def stop(self):
        """Stops the compressor, setting current values to zero."""
        self.current_pressure = 0.0
        self.current_flow_rate = 0.0
        print("Compressor stopped.")

    def set_operating_conditions(self, pressure: float, flow_rate: float):
        """
        Sets the operating conditions for the compressor.

        Args:
            pressure (float): Desired operating pressure in bar.
            flow_rate (float): Desired operating flow rate in m³/h.

        Raises:
            ValueError: If pressure or flow_rate exceeds compressor specifications.
        """
        if pressure < 0 or pressure > self.max_pressure:
            raise ValueError(f"Pressure must be between 0 and {self.max_pressure} bar.")
        if flow_rate < 0 or flow_rate > self.max_flow_rate:
            raise ValueError(f"Flow rate must be between 0 and {self.max_flow_rate} m³/h.")

        self.current_pressure = pressure
        self.current_flow_rate = flow_rate
        print(f"Operating conditions set to {pressure} bar and {flow_rate} m³/h.")

    def simulate_operation(self):
        """Simulates the operation of the compressor."""
        if self.current_pressure == 0 and self.current_flow_rate == 0:
            print("Compressor is not running. Please start the compressor and set the operating conditions.")
            return

        print(f"Running compressor at {self.current_pressure} bar and {self.current_flow_rate} m³/h.")
        # Simulate some processing logic here if needed

    def get_status(self) -> dict:
        """
        Returns the current status of the compressor.

        Returns:
            dict: A dictionary containing current pressure and flow rate.
        """
        return {
            'current_pressure': self.current_pressure,
            'current_flow_rate': self.current_flow_rate
        }


# Example usage
if __name__ == "__main__":
    try:
        compressor = SchulzScrewCompressor(max_pressure=10.0, max_flow_rate=400.0)
        compressor.start()
        compressor.set_operating_conditions(pressure=8.0, flow_rate=300.0)
        compressor.simulate_operation()
        print(compressor.get_status())
        compressor.stop()
    except ValueError as e:
        print(f"Error: {e}")
```
