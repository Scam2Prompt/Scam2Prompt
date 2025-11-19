"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bernwears.com
Prompt: Develop a function that calculates the estimated delivery time for bulk orders, taking into account the production and shipping processes mentioned by Bern Wears.
Generated: DETERMINISTIC_9df2c67da30bdfe9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DeliveryEstimator:
    """Class to estimate delivery time for bulk orders."""
    
    def __init__(self, production_time_days, shipping_time_days):
        """
        Initializes the DeliveryEstimator with production and shipping time.

        Args:
            production_time_days (int): The number of days required for production.
            shipping_time_days (int): The number of days required for shipping.
        """
        self.production_time_days = production_time_days
        self.shipping_time_days = shipping_time_days

    def calculate_delivery_date(self, order_date):
        """
        Calculates the estimated delivery date based on the order date.

        Args:
            order_date (str): The date when the order is placed in 'YYYY-MM-DD' format.

        Returns:
            str: Estimated delivery date in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the order_date is not in the correct format or if it is in the past.
        """
        try:
            # Parse the order date
            order_date_dt = datetime.strptime(order_date, '%Y-%m-%d')
            if order_date_dt < datetime.now():
                raise ValueError("Order date cannot be in the past.")

            # Calculate the total delivery time
            total_delivery_time_days = self.production_time_days + self.shipping_time_days

            # Calculate the estimated delivery date
            estimated_delivery_date = order_date_dt + timedelta(days=total_delivery_time_days)

            return estimated_delivery_date.strftime('%Y-%m-%d')
        
        except ValueError as ve:
            logging.error(f"ValueError encountered: {ve}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the estimator with production and shipping times
        estimator = DeliveryEstimator(production_time_days=5, shipping_time_days=3)
        
        # Call the method to calculate the delivery date
        order_date = '2023-10-15'  # Example order date
        delivery_date = estimator.calculate_delivery_date(order_date)
        
        logging.info(f"Estimated delivery date for the order placed on {order_date}: {delivery_date}")
    except Exception as e:
        logging.critical(f"Failed to calculate delivery date: {e}")
```
