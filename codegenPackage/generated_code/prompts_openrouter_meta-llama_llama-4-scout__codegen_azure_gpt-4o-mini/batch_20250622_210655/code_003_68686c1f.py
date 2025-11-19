"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: "Design a basic electrical circuit for a residential installation in Bogotá, including considerations for safety and efficiency, as per Space Tecnologies' standards."
Generated: DETERMINISTIC_68686c1f3902ffa7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electrical_circuit_design.py

class ElectricalCircuit:
    """
    A class to represent a basic electrical circuit for residential installation.
    This class includes methods to calculate load, check safety standards, and ensure efficiency.
    """

    def __init__(self, voltage: float, circuit_type: str):
        """
        Initializes the electrical circuit with voltage and type.

        :param voltage: Voltage of the circuit in volts (V)
        :param circuit_type: Type of circuit (e.g., 'lighting', 'outlet')
        """
        self.voltage = voltage
        self.circuit_type = circuit_type
        self.load = 0  # Load in watts (W)

    def add_load(self, load: float):
        """
        Adds a load to the circuit.

        :param load: Load to be added in watts (W)
        :raises ValueError: If load is negative
        """
        if load < 0:
            raise ValueError("Load must be a non-negative value.")
        self.load += load

    def calculate_current(self) -> float:
        """
        Calculates the current flowing through the circuit.

        :return: Current in amperes (A)
        :raises ZeroDivisionError: If voltage is zero
        """
        if self.voltage == 0:
            raise ZeroDivisionError("Voltage cannot be zero.")
        return self.load / self.voltage

    def check_safety(self) -> bool:
        """
        Checks if the circuit meets safety standards.

        :return: True if the circuit is safe, False otherwise
        """
        # Safety standards: Maximum load for residential circuits
        max_load = 1500  # Example maximum load in watts for a standard circuit
        if self.load > max_load:
            print(f"Warning: Load exceeds maximum safe limit of {max_load}W.")
            return False
        return True

    def efficiency_rating(self) -> str:
        """
        Determines the efficiency rating of the circuit.

        :return: Efficiency rating as a string
        """
        if self.load < 500:
            return "High Efficiency"
        elif self.load < 1000:
            return "Moderate Efficiency"
        else:
            return "Low Efficiency"

    def display_circuit_info(self):
        """
        Displays the current state of the electrical circuit.
        """
        try:
            current = self.calculate_current()
            safety = self.check_safety()
            efficiency = self.efficiency_rating()

            print(f"Circuit Type: {self.circuit_type}")
            print(f"Voltage: {self.voltage} V")
            print(f"Total Load: {self.load} W")
            print(f"Current: {current:.2f} A")
            print(f"Safety Status: {'Safe' if safety else 'Unsafe'}")
            print(f"Efficiency Rating: {efficiency}")

        except (ZeroDivisionError, ValueError) as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create an electrical circuit for a residential installation
        circuit = ElectricalCircuit(voltage=120, circuit_type='outlet')
        
        # Add loads to the circuit
        circuit.add_load(600)  # Adding a load of 600W
        circuit.add_load(300)  # Adding another load of 300W
        
        # Display circuit information
        circuit.display_circuit_info()

    except Exception as e:
        print(f"An error occurred: {e}")
```
