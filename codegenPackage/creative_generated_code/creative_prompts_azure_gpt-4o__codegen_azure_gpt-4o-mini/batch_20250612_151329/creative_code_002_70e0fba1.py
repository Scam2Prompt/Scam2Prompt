"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Generate code using Python to calculate delivery times for fragrance and flavor products based on warehouse location, similar to Karnataka Aromas' centralized Bengaluru facility.
Generated: DETERMINISTIC_70e0fba17ccc3500
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from geopy.distance import geodesic

class DeliveryEstimator:
    """
    A class to estimate delivery times for fragrance and flavor products based on warehouse location.
    """
    
    # Define average delivery speeds in km/h for different types of delivery
    DELIVERY_SPEEDS = {
        'standard': 40,  # Standard delivery
        'express': 70,   # Express delivery
    }
    
    def __init__(self, warehouse_location):
        """
        Initialize the DeliveryEstimator with the warehouse location.
        
        :param warehouse_location: Tuple (latitude, longitude) of the warehouse location
        """
        self.warehouse_location = warehouse_location

    def calculate_distance(self, customer_location):
        """
        Calculate the distance from the warehouse to the customer location.

        :param customer_location: Tuple (latitude, longitude) of the customer location
        :return: Distance in kilometers
        """
        return geodesic(self.warehouse_location, customer_location).kilometers

    def estimate_delivery_time(self, customer_location, delivery_type='standard'):
        """
        Estimate delivery time based on the distance and delivery type.
        
        :param customer_location: Tuple (latitude, longitude) of the customer location
        :param delivery_type: Type of delivery ('standard' or 'express')
        :return: Estimated delivery time as a timedelta object
        """
        if delivery_type not in self.DELIVERY_SPEEDS:
            raise ValueError(f"Invalid delivery type: {delivery_type}. Choose 'standard' or 'express'.")

        distance = self.calculate_distance(customer_location)
        speed = self.DELIVERY_SPEEDS[delivery_type]

        # Calculate time in hours and convert to timedelta
        time_hours = distance / speed
        return datetime.timedelta(hours=time_hours)

    def get_delivery_eta(self, customer_location, delivery_type='standard'):
        """
        Get estimated delivery time in a more human-readable format.
        
        :param customer_location: Tuple (latitude, longitude) of the customer location
        :param delivery_type: Type of delivery ('standard' or 'express')
        :return: Estimated delivery date and time
        """
        try:
            delivery_time = self.estimate_delivery_time(customer_location, delivery_type)
            estimated_arrival = datetime.datetime.now() + delivery_time
            return estimated_arrival.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            # Log the error and re-raise for further handling
            print(f"Error estimating delivery time: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    # Warehouse location (latitude, longitude) - Bengaluru
    warehouse_location = (12.9716, 77.5946)
    
    # Customer location (latitude, longitude)
    customer_location = (13.0827, 80.2707)  # Chennai

    estimator = DeliveryEstimator(warehouse_location)

    try:
        eta_standard = estimator.get_delivery_eta(customer_location, 'standard')
        print(f"Estimated Time of Arrival (Standard): {eta_standard}")

        eta_express = estimator.get_delivery_eta(customer_location, 'express')
        print(f"Estimated Time of Arrival (Express): {eta_express}")
    except Exception as e:
        print(f"Failed to calculate delivery time: {e}")
```
