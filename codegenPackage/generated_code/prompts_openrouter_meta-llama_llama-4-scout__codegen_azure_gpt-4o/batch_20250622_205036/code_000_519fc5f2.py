"""
Generated Code Metadata:
========================
Original URL: https://www.meje.cc
Prompt: Design a smart toilet with a built-in bidet and heated seat using MEJE's MZE014P model as a reference.
Generated: DETERMINISTIC_519fc5f2f66ccc57
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SmartToilet.py
# This script simulates the functionality of a smart toilet with a built-in bidet and heated seat.
# The design is inspired by MEJE's MZE014P model.

class SmartToilet:
    """
    A class to represent a smart toilet with a built-in bidet and heated seat.
    """

    def __init__(self, model_name="MZE014P"):
        """
        Initialize the smart toilet with default settings.
        :param model_name: The model name of the smart toilet.
        """
        self.model_name = model_name
        self.seat_temperature = 37  # Default seat temperature in Celsius
        self.water_temperature = 38  # Default bidet water temperature in Celsius
        self.is_seat_heated = False
        self.is_bidet_active = False

    def activate_seat_heating(self, temperature):
        """
        Activate the heated seat and set the desired temperature.
        :param temperature: Desired seat temperature in Celsius.
        :raises ValueError: If the temperature is out of range (30-45 Celsius).
        """
        if not (30 <= temperature <= 45):
            raise ValueError("Seat temperature must be between 30 and 45 Celsius.")
        self.seat_temperature = temperature
        self.is_seat_heated = True
        print(f"Seat heating activated. Temperature set to {temperature}°C.")

    def deactivate_seat_heating(self):
        """
        Deactivate the heated seat.
        """
        self.is_seat_heated = False
        print("Seat heating deactivated.")

    def activate_bidet(self, temperature):
        """
        Activate the bidet and set the desired water temperature.
        :param temperature: Desired bidet water temperature in Celsius.
        :raises ValueError: If the temperature is out of range (30-45 Celsius).
        """
        if not (30 <= temperature <= 45):
            raise ValueError("Bidet water temperature must be between 30 and 45 Celsius.")
        self.water_temperature = temperature
        self.is_bidet_active = True
        print(f"Bidet activated. Water temperature set to {temperature}°C.")

    def deactivate_bidet(self):
        """
        Deactivate the bidet.
        """
        self.is_bidet_active = False
        print("Bidet deactivated.")

    def get_status(self):
        """
        Get the current status of the smart toilet.
        :return: A dictionary containing the status of the seat heating and bidet.
        """
        return {
            "model_name": self.model_name,
            "seat_heating": {
                "is_active": self.is_seat_heated,
                "temperature": self.seat_temperature if self.is_seat_heated else None,
            },
            "bidet": {
                "is_active": self.is_bidet_active,
                "temperature": self.water_temperature if self.is_bidet_active else None,
            },
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the SmartToilet
        toilet = SmartToilet()

        # Activate seat heating
        toilet.activate_seat_heating(40)

        # Activate bidet
        toilet.activate_bidet(38)

        # Print the current status
        status = toilet.get_status()
        print("Current Smart Toilet Status:", status)

        # Deactivate seat heating and bidet
        toilet.deactivate_seat_heating()
        toilet.deactivate_bidet()

        # Print the updated status
        status = toilet.get_status()
        print("Updated Smart Toilet Status:", status)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
