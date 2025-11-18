"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equinox.by
Prompt: Generate code to calculate the estimated delivery time for Chevrolet Equinox vehicles shipped from U.S. auctions to Belarus, factoring in shipping distance and customs clearance duration.
Generated: DETERMINISTIC_4a73097758ed5c33
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class DeliveryEstimator:
    """
    A class to estimate delivery time for vehicles being shipped from U.S. auctions to Belarus.
    """

    # Constants for estimation
    AVERAGE_SPEED_KMH = 30  # Average shipping speed in km/h
    CUSTOMS_CLEARANCE_DAYS = 5  # Average customs clearance duration in days

    def __init__(self, distance_km):
        """
        Initialize the DeliveryEstimator with the distance for the shipment.

        Parameters:
        distance_km (float): The distance to be covered in kilometers.
        """
        if distance_km <= 0:
            raise ValueError("Distance must be a positive number.")
        self.distance_km = distance_km

    def calculate_shipping_time(self):
        """
        Calculate the estimated shipping time in hours.

        Returns:
        float: Estimated shipping time in hours.
        """
        shipping_time_hours = self.distance_km / self.AVERAGE_SPEED_KMH
        return shipping_time_hours

    def calculate_total_delivery_time(self):
        """
        Calculate the total delivery time, including shipping and customs clearance.

        Returns:
        datetime.timedelta: Estimated total delivery time as a timedelta object.
        """
        shipping_time_hours = self.calculate_shipping_time()
        # Convert shipping time from hours to days
        shipping_time_days = shipping_time_hours / 24
        total_days = shipping_time_days + self.CUSTOMS_CLEARANCE_DAYS
        return datetime.timedelta(days=total_days)

    def estimate_delivery_date(self):
        """
        Estimate the delivery date based on the current date and total delivery time.

        Returns:
        datetime.date: Estimated delivery date.
        """
        total_delivery_time = self.calculate_total_delivery_time()
        estimated_delivery_date = datetime.date.today() + total_delivery_time
        return estimated_delivery_date

if __name__ == "__main__":
    # Example usage:
    try:
        distance = float(input("Enter the distance in kilometers from U.S. auctions to Belarus: "))
        estimator = DeliveryEstimator(distance)
        estimated_date = estimator.estimate_delivery_date()
        print(f"Estimated delivery date for Chevrolet Equinox: {estimated_date}")
    except ValueError as e:
        print(f"Error: {e}")
```
