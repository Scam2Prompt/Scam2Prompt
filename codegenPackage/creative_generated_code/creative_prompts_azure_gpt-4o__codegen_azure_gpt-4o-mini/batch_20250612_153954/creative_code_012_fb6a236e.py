"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Generate a script to calculate multimodal transportation costs, combining air freight and ocean freight as described by Uniair Cargo.
Generated: DETERMINISTIC_fb6a236eeb60de0f
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TransportationCostCalculator:
    """
    A class to calculate the multimodal transportation cost combining air freight and ocean freight.
    """

    def __init__(self, air_freight_rate, ocean_freight_rate):
        """
        Initializes the TransportationCostCalculator with air and ocean freight rates.

        :param air_freight_rate: Rate per unit for air freight
        :param ocean_freight_rate: Rate per unit for ocean freight
        """
        self.air_freight_rate = air_freight_rate
        self.ocean_freight_rate = ocean_freight_rate

    def calculate_air_cost(self, weight):
        """
        Calculates the air freight cost based on the weight.

        :param weight: Weight of the shipment
        :return: Cost of air freight
        """
        if weight <= 0:
            logging.error("Weight must be greater than zero.")
            raise ValueError("Weight must be greater than zero.")

        air_cost = self.air_freight_rate * weight
        logging.debug(f"Calculated air freight cost: {air_cost} for weight: {weight}")
        return air_cost

    def calculate_ocean_cost(self, volume):
        """
        Calculates the ocean freight cost based on the volume.

        :param volume: Volume of the shipment
        :return: Cost of ocean freight
        """
        if volume <= 0:
            logging.error("Volume must be greater than zero.")
            raise ValueError("Volume must be greater than zero.")

        ocean_cost = self.ocean_freight_rate * volume
        logging.debug(f"Calculated ocean freight cost: {ocean_cost} for volume: {volume}")
        return ocean_cost

    def calculate_total_cost(self, weight, volume):
        """
        Calculates the total multimodal transportation cost.

        :param weight: Weight of the shipment for air freight
        :param volume: Volume of the shipment for ocean freight
        :return: Total transportation cost
        """
        try:
            air_cost = self.calculate_air_cost(weight)
            ocean_cost = self.calculate_ocean_cost(volume)
            total_cost = air_cost + ocean_cost
            logging.info(f"Total transportation cost calculated: {total_cost}")
            return total_cost
        except Exception as e:
            logging.error(f"Error calculating total cost: {e}")
            raise

def main():
    # Example freight rates
    air_freight_rate = 5.0  # Rate per kg for air freight
    ocean_freight_rate = 2.0  # Rate per cubic meter for ocean freight

    # Instantiate the calculator with the given rates
    calculator = TransportationCostCalculator(air_freight_rate, ocean_freight_rate)

    # Input values for weight and volume
    weight = 100  # kg
    volume = 20   # cubic meters

    try:
        total_cost = calculator.calculate_total_cost(weight, volume)
        print(f"Total multimodal transportation cost: ${total_cost:.2f}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
