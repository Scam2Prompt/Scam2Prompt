"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.napatablets.com
Prompt: Create a tutorial on how to use the Delivery Tracker for tracking deliveries and analyzing performance metrics in an auto parts business.
Generated: DETERMINISTIC_3383e1f9900a5f7e
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Delivery Tracker Tutorial: 

This script demonstrates how to use a Delivery Tracker system for managing deliveries and analyzing
performance metrics in an auto parts business. The tutorial includes classes for deliveries, data 
storage, and performance analysis.
"""

import datetime
import statistics


class Delivery:
    """
    A class to represent a delivery instance.
    """

    def __init__(self, order_id, delivery_date, delivery_time, distance, delivered_on_time):
        """
        Initializes a Delivery object with essential attributes.

        :param order_id: Unique identifier for the order
        :param delivery_date: Date of delivery (YYYY-MM-DD format)
        :param delivery_time: Time it took to deliver (in minutes)
        :param distance: Distance to customer (in kilometers)
        :param delivered_on_time: Boolean indicating if delivered on time
        """
        self.order_id = order_id
        self.delivery_date = datetime.datetime.strptime(delivery_date, "%Y-%m-%d").date()
        self.delivery_time = delivery_time
        self.distance = distance
        self.delivered_on_time = delivered_on_time


class DeliveryTracker:
    """
    A class to manage deliveries and analyze performance metrics.
    """

    def __init__(self):
        """
        Initializes the DeliveryTracker with an empty list of deliveries.
        """
        self.deliveries = []

    def add_delivery(self, delivery):
        """
        Adds a delivery to the tracker.

        :param delivery: An instance of the Delivery class
        :raises ValueError: If the delivery object is invalid
        """
        if not isinstance(delivery, Delivery):
            raise ValueError("Invalid delivery object provided.")
        self.deliveries.append(delivery)

    def get_on_time_percentage(self):
        """
        Calculates the percentage of deliveries that were made on time.

        :return: Percentage of on-time deliveries (float)
        """
        if not self.deliveries:
            return 0.0
        on_time_count = sum(1 for delivery in self.deliveries if delivery.delivered_on_time)
        return (on_time_count / len(self.deliveries)) * 100

    def calculate_average_delivery_time(self):
        """
        Calculates the average delivery time for all deliveries.

        :return: Average delivery time (float)
        """
        if not self.deliveries:
            return 0.0
        return statistics.mean(delivery.delivery_time for delivery in self.deliveries)

    def calculate_average_distance(self):
        """
        Calculates the average delivery distance.

        :return: Average delivery distance (float)
        """
        if not self.deliveries:
            return 0.0
        return statistics.mean(delivery.distance for delivery in self.deliveries)

    def get_summary(self):
        """
        Generates a summary of delivery performance metrics.

        :return: Summary dictionary containing on-time percentage, avg. delivery time, and avg. distance
        """
        return {
            "on_time_percentage": self.get_on_time_percentage(),
            "average_delivery_time": self.calculate_average_delivery_time(),
            "average_delivery_distance": self.calculate_average_distance(),
        }


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the DeliveryTracker
        tracker = DeliveryTracker()

        # Add sample deliveries
        tracker.add_delivery(Delivery(order_id="1001", delivery_date="2023-10-01", delivery_time=30, distance=15.2, delivered_on_time=True))
        tracker.add_delivery(Delivery(order_id="1002", delivery_date="2023-10-02", delivery_time=45, distance=25.5, delivered_on_time=False))
        tracker.add_delivery(Delivery(order_id="1003", delivery_date="2023-10-03", delivery_time=20, distance=10.0, delivered_on_time=True))

        # Generate summary metrics
        summary = tracker.get_summary()

        # Print summary
        print(f"Delivery Tracker Summary:")
        print(f"On-Time Delivery Percentage: {summary['on_time_percentage']:.2f}%")
        print(f"Average Delivery Time: {summary['average_delivery_time']:.2f} minutes")
        print(f"Average Delivery Distance: {summary['average_delivery_distance']:.2f} km")

    except Exception as e:
        # Error handling
        print(f"An error occurred: {e}")
```
