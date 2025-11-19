"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Create a Python script to calculate the total cooking capacity (in kg) for a combination of Caja China, Cilindro, and Parrilla products purchased from Meat Master.
Generated: DETERMINISTIC_643aed0a83a08320
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# meat_master_capacity_calculator.py

class CookingDevice:
    """
    A class to represent a cooking device with its capacity.
    """

    def __init__(self, name: str, capacity_kg: float):
        """
        Initializes a CookingDevice instance.

        :param name: The name of the cooking device.
        :param capacity_kg: The cooking capacity in kilograms.
        """
        self.name = name
        self.capacity_kg = capacity_kg

    def __str__(self):
        return f"{self.name}: {self.capacity_kg} kg"


class MeatMaster:
    """
    A class to calculate the total cooking capacity of various devices.
    """

    def __init__(self):
        """
        Initializes the MeatMaster instance with an empty list of devices.
        """
        self.devices = []

    def add_device(self, device: CookingDevice):
        """
        Adds a cooking device to the list.

        :param device: An instance of CookingDevice to be added.
        """
        if not isinstance(device, CookingDevice):
            raise ValueError("Only instances of CookingDevice can be added.")
        self.devices.append(device)

    def total_capacity(self) -> float:
        """
        Calculates the total cooking capacity of all devices.

        :return: Total cooking capacity in kilograms.
        """
        return sum(device.capacity_kg for device in self.devices)


def main():
    """
    Main function to execute the cooking capacity calculation.
    """
    try:
        # Create instances of cooking devices
        caja_china = CookingDevice("Caja China", 50.0)
        cilindro = CookingDevice("Cilindro", 30.0)
        parrilla = CookingDevice("Parrilla", 20.0)

        # Initialize MeatMaster and add devices
        meat_master = MeatMaster()
        meat_master.add_device(caja_china)
        meat_master.add_device(cilindro)
        meat_master.add_device(parrilla)

        # Calculate and display total cooking capacity
        total_capacity = meat_master.total_capacity()
        print(f"Total Cooking Capacity: {total_capacity} kg")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
