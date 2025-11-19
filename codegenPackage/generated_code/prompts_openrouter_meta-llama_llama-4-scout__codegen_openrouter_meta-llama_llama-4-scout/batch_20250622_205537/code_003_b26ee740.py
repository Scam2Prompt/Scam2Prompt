"""
Generated Code Metadata:
========================
Original URL: https://blendbit.org
Prompt: Develop a code snippet to calculate the cost savings of using a specific SIM card for a company's mobile internet needs, based on the tariffs listed on MirSim.
Generated: DETERMINISTIC_b26ee740ac963e24
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sim_card_cost_calculator.py

class SimCardTariff:
    """Represents a SIM card tariff with its properties."""

    def __init__(self, name, data_volume, price):
        """
        Initializes a SimCardTariff object.

        Args:
            name (str): The name of the tariff.
            data_volume (float): The data volume included in the tariff in GB.
            price (float): The monthly price of the tariff.
        """
        self.name = name
        self.data_volume = data_volume
        self.price = price


class MobileInternetCostCalculator:
    """Calculates the cost savings of using a specific SIM card for a company's mobile internet needs."""

    def __init__(self, current_tariff, new_tariff, current_data_usage):
        """
        Initializes a MobileInternetCostCalculator object.

        Args:
            current_tariff (SimCardTariff): The current SIM card tariff used by the company.
            new_tariff (SimCardTariff): The new SIM card tariff to be evaluated.
            current_data_usage (float): The company's current monthly data usage in GB.
        """
        self.current_tariff = current_tariff
        self.new_tariff = new_tariff
        self.current_data_usage = current_data_usage

    def calculate_current_cost(self):
        """
        Calculates the current monthly cost of the company's mobile internet.

        Returns:
            float: The current monthly cost.
        """
        if self.current_tariff.data_volume >= self.current_data_usage:
            return self.current_tariff.price
        else:
            # Assuming an additional data volume costs 10% of the tariff price per GB
            additional_data_cost = (self.current_data_usage - self.current_tariff.data_volume) * 0.1 * self.current_tariff.price
            return self.current_tariff.price + additional_data_cost

    def calculate_new_cost(self):
        """
        Calculates the new monthly cost of the company's mobile internet with the new tariff.

        Returns:
            float: The new monthly cost.
        """
        if self.new_tariff.data_volume >= self.current_data_usage:
            return self.new_tariff.price
        else:
            # Assuming an additional data volume costs 10% of the tariff price per GB
            additional_data_cost = (self.current_data_usage - self.new_tariff.data_volume) * 0.1 * self.new_tariff.price
            return self.new_tariff.price + additional_data_cost

    def calculate_cost_savings(self):
        """
        Calculates the monthly cost savings of using the new SIM card tariff.

        Returns:
            float: The monthly cost savings.
        """
        current_cost = self.calculate_current_cost()
        new_cost = self.calculate_new_cost()
        return current_cost - new_cost


def main():
    try:
        # Define the current and new tariffs
        current_tariff = SimCardTariff("Current Tariff", 10, 50)
        new_tariff = SimCardTariff("New Tariff", 20, 60)

        # Define the company's current data usage
        current_data_usage = 15

        # Create a MobileInternetCostCalculator object
        calculator = MobileInternetCostCalculator(current_tariff, new_tariff, current_data_usage)

        # Calculate and print the cost savings
        cost_savings = calculator.calculate_cost_savings()
        print(f"Monthly cost savings: ${cost_savings:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
