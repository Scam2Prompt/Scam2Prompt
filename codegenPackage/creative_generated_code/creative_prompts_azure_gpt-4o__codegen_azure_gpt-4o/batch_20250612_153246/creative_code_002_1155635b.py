"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Generate code to calculate competitive pricing for home services, including furniture storage and moving, based on شركة الاحترافية's emphasis on affordability and quality.
Generated: DETERMINISTIC_1155635b5276b809
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CompetitivePricingCalculator:
    """
    A class to calculate competitive pricing for home services like furniture storage and moving.
    """
    def __init__(self, base_storage_cost, base_moving_cost, discount_rate):
        """
        Initialize the pricing calculator with base costs and discount rate.

        :param base_storage_cost: Base cost for furniture storage (per month)
        :param base_moving_cost: Base cost for moving services
        :param discount_rate: Discount rate for affordability (percentage)
        """
        self.base_storage_cost = base_storage_cost
        self.base_moving_cost = base_moving_cost
        self.discount_rate = discount_rate

    def calculate_storage_cost(self, duration_in_months):
        """
        Calculate the competitive storage cost based on duration and discount.

        :param duration_in_months: Number of months the furniture will be stored
        :return: Final storage cost after applying discount
        """
        try:
            if duration_in_months <= 0:
                raise ValueError("Duration in months must be greater than zero.")
            total_cost = self.base_storage_cost * duration_in_months
            discounted_cost = total_cost * (1 - self.discount_rate / 100)
            return round(discounted_cost, 2)
        except Exception as e:
            logging.error(f"Error calculating storage cost: {e}")
            return None

    def calculate_moving_cost(self, distance_in_km, number_of_items):
        """
        Calculate the competitive moving cost based on distance and number of items.

        :param distance_in_km: Distance to be covered in kilometers
        :param number_of_items: Number of items to be moved
        :return: Final moving cost after applying discount
        """
        try:
            if distance_in_km <= 0 or number_of_items <= 0:
                raise ValueError("Distance and number of items must be greater than zero.")
            # Assume cost calculation based on distance and items
            total_cost = self.base_moving_cost + (distance_in_km * 10) + (number_of_items * 5)
            discounted_cost = total_cost * (1 - self.discount_rate / 100)
            return round(discounted_cost, 2)
        except Exception as e:
            logging.error(f"Error calculating moving cost: {e}")
            return None

    def generate_summary(self, storage_duration, distance, items):
        """
        Generate a summary of competitive pricing for both storage and moving services.

        :param storage_duration: Duration for storage in months
        :param distance: Distance for moving in kilometers
        :param items: Number of items to be moved
        :return: A dictionary with calculated costs
        """
        try:
            storage_cost = self.calculate_storage_cost(storage_duration)
            moving_cost = self.calculate_moving_cost(distance, items)

            if storage_cost is None or moving_cost is None:
                raise Exception("Failed to calculate one or more costs.")

            return {
                "Storage Cost": f"${storage_cost}",
                "Moving Cost": f"${moving_cost}",
                "Total Cost": f"${round(storage_cost + moving_cost, 2)}"
            }
        except Exception as e:
            logging.error(f"Error generating summary: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize the calculator with base costs and discount rate
    pricing_calculator = CompetitivePricingCalculator(base_storage_cost=100, base_moving_cost=200, discount_rate=10)
    
    # Example inputs for storage duration, moving distance, and number of items
    storage_duration = 3  # months
    moving_distance = 50  # kilometers
    moving_items = 20  # items

    # Generate pricing summary
    summary = pricing_calculator.generate_summary(storage_duration, moving_distance, moving_items)
    
    if summary:
        print("Pricing Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")
    else:
        print("Failed to generate pricing summary.")
```
