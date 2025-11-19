"""
Generated Code Metadata:
========================
Original URL: https://gadgetexa.com
Prompt: Write Python code to simulate the lamination process for ID cards, including tips and tricks from Gadgetexa's beginner's guide.
Generated: DETERMINISTIC_eb1e575c8488527c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulates the lamination process for ID cards.

This script follows the guidelines from Gadgetexa's beginner's guide
to ensure a smooth and efficient lamination process.

Author: [Your Name]
Date: [Today's Date]
"""

import time

class LaminationMachine:
    """
    Simulates a lamination machine.

    Attributes:
        temperature (int): The current temperature of the machine.
        laminating (bool): Whether the machine is currently laminating.
    """

    def __init__(self):
        self.temperature = 0
        self.laminating = False

    def heat_up(self, temperature):
        """
        Heats up the machine to the specified temperature.

        Args:
            temperature (int): The desired temperature.

        Raises:
            ValueError: If the temperature is not within the valid range.
        """
        if temperature < 100 or temperature > 200:
            raise ValueError("Temperature must be between 100 and 200")

        self.temperature = temperature
        print(f"Heating up to {temperature}°C...")
        time.sleep(2)  # Simulate heating up time
        print("Machine is ready.")

    def start_lamination(self):
        """
        Starts the lamination process.

        Raises:
            RuntimeError: If the machine is not heated up or is already laminating.
        """
        if self.temperature == 0:
            raise RuntimeError("Machine is not heated up.")
        if self.laminating:
            raise RuntimeError("Machine is already laminating.")

        self.laminating = True
        print("Starting lamination process...")
        time.sleep(5)  # Simulate lamination time
        print("Lamination complete.")

    def cool_down(self):
        """
        Cools down the machine.

        Raises:
            RuntimeError: If the machine is still laminating.
        """
        if self.laminating:
            raise RuntimeError("Machine is still laminating.")

        print("Cooling down...")
        time.sleep(2)  # Simulate cooling down time
        print("Machine is cooled down.")
        self.temperature = 0


def laminate_id_card(machine, card):
    """
    Simulates laminating an ID card.

    Args:
        machine (LaminationMachine): The lamination machine.
        card (str): The ID card to laminate.

    Raises:
        Exception: If any error occurs during the lamination process.
    """
    try:
        machine.heat_up(150)
        machine.start_lamination()
        print(f"Laminating {card}...")
        machine.cool_down()
    except Exception as e:
        print(f"Error laminating {card}: {str(e)}")


if __name__ == "__main__":
    machine = LaminationMachine()
    id_card = "ID-12345"

    laminate_id_card(machine, id_card)
```
