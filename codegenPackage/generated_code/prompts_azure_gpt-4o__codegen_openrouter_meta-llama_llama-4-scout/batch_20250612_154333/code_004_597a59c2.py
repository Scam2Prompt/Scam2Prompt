"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Create a program that simulates the hydraulic system of an excavator equipped with a piping kit, ensuring compatibility with attachments like hydraulic breakers and pulverizers as detailed by PT. Fuji Metal Teknik.
Generated: DETERMINISTIC_597a59c2ffcc6c4f
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hydraulic_system.py

class HydraulicSystem:
    """
    Simulates the hydraulic system of an excavator equipped with a piping kit.
    """

    def __init__(self, max_pressure, max_flow_rate):
        """
        Initializes the hydraulic system.

        Args:
            max_pressure (float): The maximum pressure of the system in bar.
            max_flow_rate (float): The maximum flow rate of the system in l/min.
        """
        self.max_pressure = max_pressure
        self.max_flow_rate = max_flow_rate
        self.current_pressure = 0
        self.current_flow_rate = 0
        self.attachments = []

    def add_attachment(self, attachment):
        """
        Adds an attachment to the hydraulic system.

        Args:
            attachment (Attachment): The attachment to add.

        Raises:
            ValueError: If the attachment is not compatible with the system.
        """
        if not attachment.is_compatible(self.max_pressure, self.max_flow_rate):
            raise ValueError("Attachment is not compatible with the system")
        self.attachments.append(attachment)

    def remove_attachment(self, attachment):
        """
        Removes an attachment from the hydraulic system.

        Args:
            attachment (Attachment): The attachment to remove.

        Raises:
            ValueError: If the attachment is not found in the system.
        """
        if attachment not in self.attachments:
            raise ValueError("Attachment not found in the system")
        self.attachments.remove(attachment)

    def update_pressure(self, pressure):
        """
        Updates the current pressure of the system.

        Args:
            pressure (float): The new pressure in bar.

        Raises:
            ValueError: If the pressure exceeds the maximum pressure.
        """
        if pressure > self.max_pressure:
            raise ValueError("Pressure exceeds the maximum pressure")
        self.current_pressure = pressure

    def update_flow_rate(self, flow_rate):
        """
        Updates the current flow rate of the system.

        Args:
            flow_rate (float): The new flow rate in l/min.

        Raises:
            ValueError: If the flow rate exceeds the maximum flow rate.
        """
        if flow_rate > self.max_flow_rate:
            raise ValueError("Flow rate exceeds the maximum flow rate")
        self.current_flow_rate = flow_rate

    def get_status(self):
        """
        Returns the current status of the hydraulic system.

        Returns:
            dict: A dictionary containing the current pressure, flow rate, and attachments.
        """
        return {
            "pressure": self.current_pressure,
            "flow_rate": self.current_flow_rate,
            "attachments": [attachment.name for attachment in self.attachments],
        }


class Attachment:
    """
    Represents an attachment for the hydraulic system.
    """

    def __init__(self, name, min_pressure, max_pressure, min_flow_rate, max_flow_rate):
        """
        Initializes the attachment.

        Args:
            name (str): The name of the attachment.
            min_pressure (float): The minimum pressure required by the attachment in bar.
            max_pressure (float): The maximum pressure supported by the attachment in bar.
            min_flow_rate (float): The minimum flow rate required by the attachment in l/min.
            max_flow_rate (float): The maximum flow rate supported by the attachment in l/min.
        """
        self.name = name
        self.min_pressure = min_pressure
        self.max_pressure = max_pressure
        self.min_flow_rate = min_flow_rate
        self.max_flow_rate = max_flow_rate

    def is_compatible(self, max_pressure, max_flow_rate):
        """
        Checks if the attachment is compatible with the hydraulic system.

        Args:
            max_pressure (float): The maximum pressure of the system in bar.
            max_flow_rate (float): The maximum flow rate of the system in l/min.

        Returns:
            bool: True if the attachment is compatible, False otherwise.
        """
        return (
            self.min_pressure <= max_pressure
            and self.max_pressure <= max_pressure
            and self.min_flow_rate <= max_flow_rate
            and self.max_flow_rate <= max_flow_rate
        )


class HydraulicBreaker(Attachment):
    """
    Represents a hydraulic breaker attachment.
    """

    def __init__(self):
        """
        Initializes the hydraulic breaker attachment.
        """
        super().__init__("Hydraulic Breaker", 100, 150, 20, 50)


class Pulverizer(Attachment):
    """
    Represents a pulverizer attachment.
    """

    def __init__(self):
        """
        Initializes the pulverizer attachment.
        """
        super().__init__("Pulverizer", 120, 180, 30, 60)


def main():
    # Create a hydraulic system with a maximum pressure of 200 bar and a maximum flow rate of 100 l/min
    system = HydraulicSystem(200, 100)

    # Create a hydraulic breaker and a pulverizer
    breaker = HydraulicBreaker()
    pulverizer = Pulverizer()

    # Add the hydraulic breaker to the system
    system.add_attachment(breaker)

    # Update the pressure and flow rate of the system
    system.update_pressure(120)
    system.update_flow_rate(40)

    # Get the status of the system
    status = system.get_status()
    print(status)

    # Remove the hydraulic breaker and add the pulverizer
    system.remove_attachment(breaker)
    system.add_attachment(pulverizer)

    # Update the pressure and flow rate of the system
    system.update_pressure(150)
    system.update_flow_rate(50)

    # Get the status of the system
    status = system.get_status()
    print(status)


if __name__ == "__main__":
    main()
```
