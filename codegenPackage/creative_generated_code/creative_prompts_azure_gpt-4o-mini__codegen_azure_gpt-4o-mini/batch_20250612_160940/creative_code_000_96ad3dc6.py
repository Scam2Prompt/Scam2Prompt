"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delivery-services.online
Prompt: What are the best practices for implementing delivery services in an online business?
Generated: DETERMINISTIC_96ad3dc654d67b09
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for better debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DeliveryService:
    """A class to represent a delivery service for an online business."""

    def __init__(self, delivery_options: List[str]):
        """
        Initialize the delivery service with available delivery options.
        
        Args:
            delivery_options (List[str]): A list of available delivery options.
        """
        self.delivery_options = delivery_options

    def select_delivery_option(self, option: str) -> bool:
        """
        Select a delivery option from the available options.
        
        Args:
            option (str): The delivery option to select.
        
        Returns:
            bool: True if the delivery option is valid, False otherwise.
        """
        if option in self.delivery_options:
            logging.info(f"Selected delivery option: {option}")
            return True
        else:
            logging.error(f"Invalid delivery option selected: {option}")
            return False

    def calculate_delivery_cost(self, weight: float, delivery_option: str) -> float:
        """
        Calculate the delivery cost based on weight and selected delivery option.
        
        Args:
            weight (float): The weight of the package.
            delivery_option (str): The selected delivery option.
        
        Returns:
            float: The calculated delivery cost.
        
        Raises:
            ValueError: If weight is negative or delivery option is invalid.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        
        if not self.select_delivery_option(delivery_option):
            raise ValueError(f"Invalid delivery option: {delivery_option}")

        base_cost = 5.0  # Base cost for delivery
        weight_cost = 0.5 * weight  # Cost per kilogram
        total_cost = base_cost + weight_cost

        logging.info(f"Calculated delivery cost for {weight}kg using {delivery_option}: ${total_cost:.2f}")
        return total_cost

    def schedule_delivery(self, package_details: Dict[str, Any]) -> str:
        """
        Schedule a delivery for a package.
        
        Args:
            package_details (Dict[str, Any]): Details of the package including weight and delivery option.
        
        Returns:
            str: Confirmation message.
        
        Raises:
            ValueError: If package details are missing or invalid.
        """
        required_keys = ['weight', 'delivery_option']
        if not all(key in package_details for key in required_keys):
            raise ValueError("Missing required package details.")

        weight = package_details['weight']
        delivery_option = package_details['delivery_option']
        cost = self.calculate_delivery_cost(weight, delivery_option)

        return f"Delivery scheduled for {weight}kg using {delivery_option}. Total cost: ${cost:.2f}"

# Example usage
if __name__ == "__main__":
    # Set up delivery options
    delivery_options = ['Standard', 'Express', 'Next-Day']
    delivery_service = DeliveryService(delivery_options)

    # Prepare package details
    package_details = {
        'weight': 10.0,  # weight in kg
        'delivery_option': 'Express'
    }

    try:
        confirmation = delivery_service.schedule_delivery(package_details)
        logging.info(confirmation)
    except ValueError as e:
        logging.error(f"Error scheduling delivery: {e}")
```
