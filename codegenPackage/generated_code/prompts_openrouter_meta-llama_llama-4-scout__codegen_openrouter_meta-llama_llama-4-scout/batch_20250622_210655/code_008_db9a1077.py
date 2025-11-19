"""
Generated Code Metadata:
========================
Original URL: https://fullport.net
Prompt: Recommend a suitable power cable for a computer with a specific power supply unit (PSU).
Generated: DETERMINISTIC_db9a1077274e940d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# power_cable_recommender.py

class PowerSupplyUnit:
    """Represents a Power Supply Unit (PSU) with its specifications."""

    def __init__(self, wattage, connector_type, voltage):
        """
        Initializes a PowerSupplyUnit object.

        Args:
            wattage (int): The wattage of the PSU.
            connector_type (str): The type of connector (e.g., ATX, Micro-ATX, Mini-ITX).
            voltage (int): The voltage supported by the PSU (e.g., 230V, 120V).
        """
        self.wattage = wattage
        self.connector_type = connector_type
        self.voltage = voltage


class PowerCable:
    """Represents a power cable with its specifications."""

    def __init__(self, cable_type, voltage_rating, current_rating):
        """
        Initializes a PowerCable object.

        Args:
            cable_type (str): The type of power cable (e.g., C7, C13, C19).
            voltage_rating (int): The voltage rating of the power cable.
            current_rating (int): The current rating of the power cable.
        """
        self.cable_type = cable_type
        self.voltage_rating = voltage_rating
        self.current_rating = current_rating


def recommend_power_cable(psu):
    """
    Recommends a suitable power cable for a given Power Supply Unit (PSU).

    Args:
        psu (PowerSupplyUnit): The Power Supply Unit object.

    Returns:
        PowerCable: A recommended PowerCable object.

    Raises:
        ValueError: If the PSU's voltage is not supported.
    """
    # Define a mapping of PSU voltages to supported power cable voltage ratings
    voltage_mapping = {
        230: 250,
        120: 125
    }

    # Check if the PSU's voltage is supported
    if psu.voltage not in voltage_mapping:
        raise ValueError(f"Unsupported voltage: {psu.voltage}V")

    # Determine the recommended power cable type based on the PSU's connector type
    if psu.connector_type == "ATX":
        cable_type = "C7"
    elif psu.connector_type in ["Micro-ATX", "Mini-ITX"]:
        cable_type = "C13"
    else:
        raise ValueError(f"Unsupported connector type: {psu.connector_type}")

    # Calculate the recommended current rating based on the PSU's wattage
    current_rating = int(psu.wattage / voltage_mapping[psu.voltage])

    # Create a recommended PowerCable object
    recommended_cable = PowerCable(
        cable_type=cable_type,
        voltage_rating=voltage_mapping[psu.voltage],
        current_rating=current_rating
    )

    return recommended_cable


def main():
    try:
        # Example usage
        psu = PowerSupplyUnit(
            wattage=650,
            connector_type="ATX",
            voltage=230
        )

        recommended_cable = recommend_power_cable(psu)

        print("Recommended Power Cable:")
        print(f"Cable Type: {recommended_cable.cable_type}")
        print(f"Voltage Rating: {recommended_cable.voltage_rating}V")
        print(f"Current Rating: {recommended_cable.current_rating}A")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
