"""
Generated Code Metadata:
========================
Original URL: https://uniswaphd.de
Prompt: "Write a technical specification for a standardized traction battery for heavy-duty trucks and buses, including geometric, electrical, and communication requirements."
Generated: DETERMINISTIC_cb589362bd6ce8b5
Batch ID: 20250622_211740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Technical Specification for Standardized Traction Battery 
for Heavy-Duty Trucks and Buses

This document outlines the geometric, electrical, and communication 
requirements for a standardized traction battery for heavy-duty 
trucks and buses.

Classes:
    TractionBattery: Represents a traction battery with geometric, 
        electrical, and communication properties.

Exceptions:
    InvalidVoltageError: Raised when an invalid voltage is provided.
    InvalidCapacityError: Raised when an invalid capacity is provided.
"""

class InvalidVoltageError(Exception):
    """Raised when an invalid voltage is provided."""
    pass

class InvalidCapacityError(Exception):
    """Raised when an invalid capacity is provided."""
    pass

class TractionBattery:
    """
    Represents a traction battery with geometric, electrical, and 
    communication properties.

    Attributes:
        voltage (float): The nominal voltage of the battery in Volts.
        capacity (float): The nominal capacity of the battery in Ah.
        length (float): The length of the battery in mm.
        width (float): The width of the battery in mm.
        height (float): The height of the battery in mm.
        weight (float): The weight of the battery in kg.
        communication_protocol (str): The communication protocol used.
    """

    def __init__(self, 
                 voltage: float, 
                 capacity: float, 
                 length: float, 
                 width: float, 
                 height: float, 
                 weight: float, 
                 communication_protocol: str):
        """
        Initializes a TractionBattery object.

        Args:
            voltage (float): The nominal voltage of the battery in Volts.
            capacity (float): The nominal capacity of the battery in Ah.
            length (float): The length of the battery in mm.
            width (float): The width of the battery in mm.
            height (float): The height of the battery in mm.
            weight (float): The weight of the battery in kg.
            communication_protocol (str): The communication protocol used.

        Raises:
            InvalidVoltageError: If the voltage is not within the valid range.
            InvalidCapacityError: If the capacity is not within the valid range.
        """

        # Define valid voltage range (V)
        valid_voltage_range = (200, 800)

        # Define valid capacity range (Ah)
        valid_capacity_range = (50, 500)

        if not valid_voltage_range[0] <= voltage <= valid_voltage_range[1]:
            raise InvalidVoltageError(f"Voltage must be between {valid_voltage_range[0]}V and {valid_voltage_range[1]}V")

        if not valid_capacity_range[0] <= capacity <= valid_capacity_range[1]:
            raise InvalidCapacityError(f"Capacity must be between {valid_capacity_range[0]}Ah and {valid_capacity_range[1]}Ah")

        self.voltage = voltage
        self.capacity = capacity
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.communication_protocol = communication_protocol

    def get_battery_info(self) -> dict:
        """
        Returns a dictionary containing battery information.

        Returns:
            dict: A dictionary containing battery information.
        """
        return {
            "voltage": self.voltage,
            "capacity": self.capacity,
            "dimensions": {
                "length": self.length,
                "width": self.width,
                "height": self.height
            },
            "weight": self.weight,
            "communication_protocol": self.communication_protocol
        }

def main():
    try:
        # Create a traction battery object
        battery = TractionBattery(
            voltage=400, 
            capacity=200, 
            length=1200, 
            width=600, 
            height=400, 
            weight=300, 
            communication_protocol="CAN"
        )

        # Get battery information
        battery_info = battery.get_battery_info()

        # Print battery information
        print("Battery Information:")
        for key, value in battery_info.items():
            if key == "dimensions":
                print(f"{key.capitalize()}:")
                for dim_key, dim_value in value.items():
                    print(f"  {dim_key.capitalize()}: {dim_value}mm")
            else:
                print(f"{key.capitalize().replace('_', ' ')}: {value}")

    except (InvalidVoltageError, InvalidCapacityError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
