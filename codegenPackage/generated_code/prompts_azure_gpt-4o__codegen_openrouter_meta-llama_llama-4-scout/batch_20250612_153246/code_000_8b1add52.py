"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Write a Python script to create a pricing calculator for Jacuzzi® hot tubs, incorporating features like hydrotherapy jets, ergonomic seats, and energy-saving technology as described on the Oasis Hot Tubs website.
Generated: DETERMINISTIC_8b1add520ccb7ce6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# jacuzzi_pricing_calculator.py

class JacuzziHotTub:
    def __init__(self, model, jets, seats, energy_saving_technology):
        """
        Initialize a Jacuzzi hot tub with its features.

        Args:
            model (str): The model of the hot tub.
            jets (int): The number of hydrotherapy jets.
            seats (int): The number of ergonomic seats.
            energy_saving_technology (bool): Whether the hot tub has energy-saving technology.
        """
        self.model = model
        self.jets = jets
        self.seats = seats
        self.energy_saving_technology = energy_saving_technology

    def calculate_base_price(self):
        """
        Calculate the base price of the hot tub based on its model.

        Returns:
            float: The base price of the hot tub.
        """
        base_prices = {
            "Oasis": 9999.99,
            "Paradise": 12999.99,
            "Bliss": 14999.99
        }
        return base_prices.get(self.model, 0)

    def calculate_jet_upgrade_price(self):
        """
        Calculate the price upgrade for additional hydrotherapy jets.

        Returns:
            float: The price upgrade for additional hydrotherapy jets.
        """
        jet_upgrade_price = 200.00
        if self.jets > 10:
            return jet_upgrade_price * (self.jets - 10)
        return 0

    def calculate_seat_upgrade_price(self):
        """
        Calculate the price upgrade for additional ergonomic seats.

        Returns:
            float: The price upgrade for additional ergonomic seats.
        """
        seat_upgrade_price = 500.00
        if self.seats > 4:
            return seat_upgrade_price * (self.seats - 4)
        return 0

    def calculate_energy_saving_upgrade_price(self):
        """
        Calculate the price upgrade for energy-saving technology.

        Returns:
            float: The price upgrade for energy-saving technology.
        """
        energy_saving_upgrade_price = 1000.00
        return energy_saving_upgrade_price if self.energy_saving_technology else 0

    def calculate_total_price(self):
        """
        Calculate the total price of the hot tub.

        Returns:
            float: The total price of the hot tub.
        """
        base_price = self.calculate_base_price()
        jet_upgrade_price = self.calculate_jet_upgrade_price()
        seat_upgrade_price = self.calculate_seat_upgrade_price()
        energy_saving_upgrade_price = self.calculate_energy_saving_upgrade_price()
        return base_price + jet_upgrade_price + seat_upgrade_price + energy_saving_upgrade_price


def main():
    try:
        model = input("Enter the model of the hot tub (Oasis, Paradise, Bliss): ")
        jets = int(input("Enter the number of hydrotherapy jets: "))
        seats = int(input("Enter the number of ergonomic seats: "))
        energy_saving_technology = input("Does the hot tub have energy-saving technology? (yes/no): ").lower() == "yes"

        hot_tub = JacuzziHotTub(model, jets, seats, energy_saving_technology)
        total_price = hot_tub.calculate_total_price()

        print(f"Model: {hot_tub.model}")
        print(f"Hydrotherapy Jets: {hot_tub.jets}")
        print(f"Ergonomic Seats: {hot_tub.seats}")
        print(f"Energy-Saving Technology: {'Yes' if hot_tub.energy_saving_technology else 'No'}")
        print(f"Total Price: ${total_price:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
