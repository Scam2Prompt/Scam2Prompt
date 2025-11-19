"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Write a Python script to calculate the cost of building a home studio like Eric Navarro's, considering the prices of equipment such as the Cad E100s microphone and SSL 2 audio interface.
Generated: DETERMINISTIC_9dd6a6ec67d5654c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# home_studio_cost_calculator.py

class Equipment:
    """Represents a piece of equipment with a name and price."""

    def __init__(self, name: str, price: float):
        """
        Initializes an Equipment object.

        Args:
            name (str): The name of the equipment.
            price (float): The price of the equipment.
        """
        self.name = name
        self.price = price


class HomeStudio:
    """Represents a home studio with a list of equipment."""

    def __init__(self):
        """Initializes a HomeStudio object with an empty list of equipment."""
        self.equipment = []

    def add_equipment(self, equipment: Equipment):
        """
        Adds a piece of equipment to the home studio.

        Args:
            equipment (Equipment): The equipment to add.
        """
        self.equipment.append(equipment)

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the home studio.

        Returns:
            float: The total cost of the home studio.
        """
        return sum(equipment.price for equipment in self.equipment)


def main():
    try:
        # Define equipment prices
        cad_e100s_microphone = Equipment("Cad E100s Microphone", 99.99)
        ssl2_audio_interface = Equipment("SSL2 Audio Interface", 499.99)
        acoustic_treatment = Equipment("Acoustic Treatment", 200.00)
        desk_and_chair = Equipment("Desk and Chair", 300.00)
        headphones = Equipment("Headphones", 150.00)

        # Create a home studio
        home_studio = HomeStudio()

        # Add equipment to the home studio
        home_studio.add_equipment(cad_e100s_microphone)
        home_studio.add_equipment(ssl2_audio_interface)
        home_studio.add_equipment(acoustic_treatment)
        home_studio.add_equipment(desk_and_chair)
        home_studio.add_equipment(headphones)

        # Calculate and print the total cost
        total_cost = home_studio.calculate_total_cost()
        print(f"Total cost of building a home studio like Eric Navarro's: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
