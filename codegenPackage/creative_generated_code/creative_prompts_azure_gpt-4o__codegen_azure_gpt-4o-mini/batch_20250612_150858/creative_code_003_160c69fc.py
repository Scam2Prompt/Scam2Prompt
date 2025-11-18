"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debank.lu
Prompt: Write code to model the electrical connections for a Honda Fourtrax 300 ATV wiring diagram, incorporating the wiring details available on https://debank.lu.
Generated: DETERMINISTIC_160c69fc2976de6a
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Wire:
    def __init__(self, color, gauge, length):
        """
        Initializes a wire with the specified color, gauge, and length.
        
        :param color: str - The color of the wire.
        :param gauge: int - The gauge of the wire.
        :param length: float - The length of the wire in meters.
        """
        self.color = color
        self.gauge = gauge
        self.length = length

    def __str__(self):
        return f"Wire(color={self.color}, gauge={self.gauge}, length={self.length})"


class Connection:
    def __init__(self, wire1, wire2, connector_type):
        """
        Initializes a connection between two wires.

        :param wire1: Wire - The first wire in the connection.
        :param wire2: Wire - The second wire in the connection.
        :param connector_type: str - The type of connector used.
        """
        if not isinstance(wire1, Wire) or not isinstance(wire2, Wire):
            raise ValueError("Both connections must be Wire instances.")
        
        self.wire1 = wire1
        self.wire2 = wire2
        self.connector_type = connector_type

    def __str__(self):
        return f"Connection({self.wire1} <-> {self.wire2}, connector={self.connector_type})"


class ATVElectricalSystem:
    def __init__(self):
        """
        Initializes the ATV electrical system with a list of wires and connections.
        """
        self.wires = []
        self.connections = []

    def add_wire(self, wire):
        """
        Adds a wire to the electrical system.
        
        :param wire: Wire - The wire to be added.
        """
        if not isinstance(wire, Wire):
            raise ValueError("Only Wire instances can be added.")
        self.wires.append(wire)

    def add_connection(self, wire1, wire2, connector_type):
        """
        Creates and adds a connection between two wires.
        
        :param wire1: Wire - The first wire in the connection.
        :param wire2: Wire - The second wire in the connection.
        :param connector_type: str - The type of connector used.
        """
        connection = Connection(wire1, wire2, connector_type)
        self.connections.append(connection)

    def display_system(self):
        """
        Displays the current state of the ATV electrical system, including all wires and connections.
        """
        print("Wires:")
        for wire in self.wires:
            print(f" - {wire}")

        print("Connections:")
        for connection in self.connections:
            print(f" - {connection}")


# Example usage:
if __name__ == "__main__":
    try:
        atv_system = ATVElectricalSystem()

        # Adding wires
        wire1 = Wire(color="Red", gauge=16, length=2.5)
        wire2 = Wire(color="Black", gauge=16, length=3.0)
        atv_system.add_wire(wire1)
        atv_system.add_wire(wire2)

        # Adding connections
        atv_system.add_connection(wire1, wire2, connector_type="Splice")

        # Display the ATV electrical system
        atv_system.display_system()
    
    except ValueError as e:
        print(f"Error: {e}")
```
