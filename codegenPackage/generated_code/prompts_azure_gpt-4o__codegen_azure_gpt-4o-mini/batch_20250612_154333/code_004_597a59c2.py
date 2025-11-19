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
class HydraulicSystem:
    """
    A class to simulate the hydraulic system of an excavator.
    This system is compatible with various attachments like hydraulic breakers and pulverizers.
    """

    def __init__(self, pressure: float = 0.0):
        """
        Initializes the hydraulic system with a given pressure.

        :param pressure: Initial pressure of the hydraulic system in Pascals.
        """
        self.pressure = pressure
        self.attachments = []
        self.is_active = False

    def add_attachment(self, attachment: str):
        """
        Adds an attachment to the hydraulic system.

        :param attachment: The name of the attachment to be added.
        """
        if attachment not in self.attachments:
            self.attachments.append(attachment)
            print(f"Attachment '{attachment}' added to the hydraulic system.")
        else:
            print(f"Attachment '{attachment}' is already added.")

    def remove_attachment(self, attachment: str):
        """
        Removes an attachment from the hydraulic system.

        :param attachment: The name of the attachment to be removed.
        """
        try:
            self.attachments.remove(attachment)
            print(f"Attachment '{attachment}' removed from the hydraulic system.")
        except ValueError:
            print(f"Attachment '{attachment}' not found in the system.")

    def activate_system(self):
        """
        Activates the hydraulic system, setting it to an operational state.
        """
        if not self.is_active:
            self.is_active = True
            print("Hydraulic system activated.")
        else:
            print("Hydraulic system is already active.")

    def deactivate_system(self):
        """
        Deactivates the hydraulic system, setting it to a non-operational state.
        """
        if self.is_active:
            self.is_active = False
            print("Hydraulic system deactivated.")
        else:
            print("Hydraulic system is already inactive.")

    def set_pressure(self, pressure: float):
        """
        Sets the pressure of the hydraulic system.

        :param pressure: Pressure to be set in Pascals.
        :raises ValueError: If the pressure is negative.
        """
        if pressure < 0:
            raise ValueError("Pressure cannot be negative.")
        self.pressure = pressure
        print(f"Hydraulic system pressure set to {self.pressure} Pascals.")

    def operate_attachment(self, attachment: str):
        """
        Operates the specified attachment if the system is active.

        :param attachment: The name of the attachment to operate.
        :raises RuntimeError: If the hydraulic system is not active.
        :raises ValueError: If the attachment is not found.
        """
        if not self.is_active:
            raise RuntimeError("Cannot operate attachment. Hydraulic system is not active.")
        if attachment not in self.attachments:
            raise ValueError(f"Attachment '{attachment}' not found in the system.")
        
        print(f"Operating attachment '{attachment}' at {self.pressure} Pascals.")

# Example usage
if __name__ == "__main__":
    try:
        hydraulic_system = HydraulicSystem()
        hydraulic_system.add_attachment("Hydraulic Breaker")
        hydraulic_system.add_attachment("Pulverizer")
        hydraulic_system.set_pressure(200000)  # Set pressure to 200,000 Pascals
        hydraulic_system.activate_system()
        hydraulic_system.operate_attachment("Hydraulic Breaker")
        hydraulic_system.deactivate_system()
    except Exception as e:
        print(f"An error occurred: {e}")
```
