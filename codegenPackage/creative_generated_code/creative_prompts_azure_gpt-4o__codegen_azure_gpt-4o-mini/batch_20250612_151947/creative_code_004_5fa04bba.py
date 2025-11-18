"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.espglobal.co
Prompt: Write a script to implement ESP Global's "Pay as you Earn" model for subscription-free access to PropTech solutions in a real estate management system.
Generated: DETERMINISTIC_5fa04bba82248064
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PayAsYouEarn:
    """
    A class to implement the Pay as You Earn model for subscription-free access
    to PropTech solutions in a real estate management system.
    """

    def __init__(self, user_id, hourly_rate):
        """
        Initializes the PayAsYouEarn instance.

        :param user_id: Unique identifier for the user
        :param hourly_rate: Rate charged per hour of service
        """
        self.user_id = user_id
        self.hourly_rate = hourly_rate
        self.total_hours = 0
        self.service_log = []

    def log_service(self, start_time, end_time):
        """
        Logs the service usage between start_time and end_time.

        :param start_time: datetime object representing when the service started
        :param end_time: datetime object representing when the service ended
        :raises ValueError: If end_time is earlier than start_time
        """
        if end_time < start_time:
            raise ValueError("End time must be later than start time.")
        
        duration = end_time - start_time
        hours = duration.total_seconds() / 3600  # Convert seconds to hours

        self.total_hours += hours
        self.service_log.append((start_time, end_time, hours))
        print(f"Service logged: {hours:.2f} hours from {start_time} to {end_time}.")

    def calculate_total_cost(self):
        """
        Calculates the total cost incurred by the user.

        :return: Total cost based on usage
        """
        total_cost = self.total_hours * self.hourly_rate
        return total_cost

    def generate_invoice(self):
        """
        Generates an invoice for the user based on total service usage.

        :return: A dictionary with the invoice details
        """
        total_cost = self.calculate_total_cost()
        invoice = {
            "user_id": self.user_id,
            "total_hours": self.total_hours,
            "hourly_rate": self.hourly_rate,
            "total_cost": total_cost,
            "service_log": self.service_log
        }
        return invoice

# Example usage of the PayAsYouEarn class
if __name__ == "__main__":
    try:
        user = PayAsYouEarn(user_id="user123", hourly_rate=50.0)

        # Log some services
        user.log_service(datetime.datetime(2023, 10, 1, 9, 0), datetime.datetime(2023, 10, 1, 12, 0))
        user.log_service(datetime.datetime(2023, 10, 2, 14, 0), datetime.datetime(2023, 10, 2, 16, 30))

        # Generate invoice
        invoice = user.generate_invoice()
        print("Invoice generated:", invoice)

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
