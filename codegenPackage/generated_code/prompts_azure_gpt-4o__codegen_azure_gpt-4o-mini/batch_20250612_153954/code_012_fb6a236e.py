"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Generate a script to calculate multimodal transportation costs, combining air freight and ocean freight as described by Uniair Cargo.
Generated: DETERMINISTIC_fb6a236eeb60de0f
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TransportationCostCalculator:
    """
    A class to calculate multimodal transportation costs combining air freight and ocean freight.
    """

    def __init__(self, air_freight_rate, ocean_freight_rate):
        """
        Initializes the TransportationCostCalculator with air and ocean freight rates.

        :param air_freight_rate: Cost per unit weight for air freight
        :param ocean_freight_rate: Cost per unit weight for ocean freight
        """
        self.air_freight_rate = air_freight_rate
        self.ocean_freight_rate = ocean_freight_rate

    def calculate_air_freight_cost(self, weight):
        """
        Calculates the air freight cost based on weight.

        :param weight: Weight of the cargo in kilograms
        :return: Air freight cost
        """
        if weight < 0:
            logging.error("Weight cannot be negative.")
            raise ValueError("Weight must be a non-negative value.")
        cost = self.air_freight_rate * weight
        logging.info(f"Calculated air freight cost: {cost} for weight: {weight}")
        return cost

    def calculate_ocean_freight_cost(self, weight):
        """
        Calculates the ocean freight cost based on weight.

        :param weight: Weight of the cargo in kilograms
        :return: Ocean freight cost
        """
        if weight < 0:
            logging.error("Weight cannot be negative.")
            raise ValueError("Weight must be a non-negative value.")
        cost = self.ocean_freight_rate * weight
        logging.info(f"Calculated ocean freight cost: {cost} for weight: {weight}")
        return cost

    def calculate_total_cost(self, weight, mode='air'):
        """
        Calculates the total transportation cost based on the selected mode.

        :param weight: Weight of the cargo in kilograms
        :param mode: Mode of transportation ('air' or 'ocean')
        :return: Total transportation cost
        """
        if mode not in ['air', 'ocean']:
            logging.error("Invalid mode selected. Choose 'air' or 'ocean'.")
            raise ValueError("Mode must be either 'air' or 'ocean'.")

        if mode == 'air':
            return self.calculate_air_freight_cost(weight)
        else:
            return self.calculate_ocean_freight_cost(weight)

def main():
    """
    Main function to execute the transportation cost calculation.
    """
    try:
        # Example rates (these should be set according to actual rates)
        air_freight_rate = 5.0  # Cost per kg for air freight
        ocean_freight_rate = 2.0  # Cost per kg for ocean freight

        # Create an instance of the calculator
        calculator = TransportationCostCalculator(air_freight_rate, ocean_freight_rate)

        # Example weight
        weight = 100  # Weight in kg

        # Calculate costs
        air_cost = calculator.calculate_total_cost(weight, mode='air')
        ocean_cost = calculator.calculate_total_cost(weight, mode='ocean')

        # Output results
        logging.info(f"Total air freight cost for {weight} kg: {air_cost}")
        logging.info(f"Total ocean freight cost for {weight} kg: {ocean_cost}")

    except ValueError as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
