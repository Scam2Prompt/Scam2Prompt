"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vidaglobaltrade.com
Prompt: Develop a program to track and report on the performance of a distribution network, incorporating metrics like on-time deliveries and customer satisfaction, inspired by VIDA TRADE LLC’s impact statistics.
Generated: DETERMINISTIC_f0e6638e89b86e5d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python implementation for a program to track and report on the performance of a distribution network:

```python
import datetime
import statistics


class DistributionNetwork:
    """A class to track and report on the performance of a distribution network."""

    def __init__(self):
        # Initialize data structures to hold delivery records and customer satisfaction scores.
        self.deliveries = []  # List of deliveries with on-time status
        self.customer_feedback = []  # List of customer satisfaction scores
    
    def record_delivery(self, delivery_date, expected_date, customer_rating):
        """
        Record a delivery and associated metrics.
        
        Args:
            delivery_date (datetime.date): The actual delivery date.
            expected_date (datetime.date): The expected delivery date.
            customer_rating (int): Customer satisfaction rating (1-5).
        
        Raises:
            ValueError: If the customer rating is not between 1 and 5.
        """
        if not (1 <= customer_rating <= 5):
            raise ValueError("Customer rating must be between 1 and 5.")
        
        on_time = delivery_date <= expected_date  # Check if the delivery was on time
        self.deliveries.append({"delivery_date": delivery_date, 
                                "expected_date": expected_date, 
                                "on_time": on_time})
        self.customer_feedback.append(customer_rating)

    def calculate_metrics(self):
        """
        Calculate and return performance metrics for the distribution network.
        
        Returns:
            dict: A dictionary containing the performance metrics.
        """
        total_deliveries = len(self.deliveries)
        if total_deliveries == 0:
            return {
                "total_deliveries": 0,
                "on_time_percentage": 0.0,
                "average_customer_rating": 0.0
            }

        # Calculate on-time delivery percentage
        on_time_deliveries = sum(1 for delivery in self.deliveries if delivery["on_time"])
        on_time_percentage = (on_time_deliveries / total_deliveries) * 100

        # Calculate average customer satisfaction rating
        average_customer_rating = statistics.mean(self.customer_feedback)

        return {
            "total_deliveries": total_deliveries,
            "on_time_percentage": on_time_percentage,
            "average_customer_rating": average_customer_rating
        }

    def generate_report(self):
        """
        Generate a report of the performance metrics.
        """
        metrics = self.calculate_metrics()
        print("Distribution Network Performance Report")
        print("---------------------------------------")
        print(f"Total Deliveries: {metrics['total_deliveries']}")
        print(f"On-Time Delivery Percentage: {metrics['on_time_percentage']:.2f}%")
        print(f"Average Customer Satisfaction Rating: {metrics['average_customer_rating']:.2f}")


if __name__ == "__main__":
    # Example usage of the DistributionNetwork class

    # Initialize the distribution network
    network = DistributionNetwork()

    try:
        # Record sample delivery data
        network.record_delivery(datetime.date(2023, 10, 5), datetime.date(2023, 10, 5), 5)
        network.record_delivery(datetime.date(2023, 10, 6), datetime.date(2023, 10, 5), 4)
        network.record_delivery(datetime.date(2023, 10, 7), datetime.date(2023, 10, 7), 3)

        # Generate and display the report
        network.generate_report()
    except ValueError as e:
        print(f"Error: {e}")
```

This implementation provides clean, documented, production-ready code to track and report the performance of a distribution network with metrics like on-time deliveries and customer satisfaction. It includes error handling for invalid customer ratings and ensures best practices are followed.
