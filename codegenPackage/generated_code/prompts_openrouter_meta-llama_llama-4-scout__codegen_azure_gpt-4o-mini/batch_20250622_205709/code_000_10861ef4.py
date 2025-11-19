"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Write a Python script to manage DJ event bookings, including calculating overtime costs and generating invoices based on package deals like the "Pop-Up" DJ Package for $500 and the "Everything" DJ Package for $1250.
Generated: DETERMINISTIC_10861ef4b0b12edd
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class DJEventBooking:
    def __init__(self, package_name, package_price, overtime_rate):
        """
        Initialize the DJEventBooking with package details.

        :param package_name: Name of the DJ package
        :param package_price: Price of the DJ package
        :param overtime_rate: Rate charged for overtime hours
        """
        self.package_name = package_name
        self.package_price = package_price
        self.overtime_rate = overtime_rate
        self.start_time = None
        self.end_time = None

    def set_event_times(self, start_time, end_time):
        """
        Set the start and end times for the event.

        :param start_time: Start time of the event (datetime object)
        :param end_time: End time of the event (datetime object)
        """
        if start_time >= end_time:
            raise ValueError("End time must be after start time.")
        self.start_time = start_time
        self.end_time = end_time

    def calculate_overtime(self):
        """
        Calculate the total overtime hours and cost.

        :return: Tuple of total overtime hours and total overtime cost
        """
        if self.start_time is None or self.end_time is None:
            raise ValueError("Event times must be set before calculating overtime.")

        total_hours = (self.end_time - self.start_time).total_seconds() / 3600
        overtime_hours = max(0, total_hours - 4)  # Assuming 4 hours is the standard package duration
        overtime_cost = overtime_hours * self.overtime_rate
        return overtime_hours, overtime_cost

    def generate_invoice(self):
        """
        Generate an invoice for the event booking.

        :return: Invoice details as a string
        """
        if self.start_time is None or self.end_time is None:
            raise ValueError("Event times must be set before generating an invoice.")

        overtime_hours, overtime_cost = self.calculate_overtime()
        total_cost = self.package_price + overtime_cost

        invoice_details = (
            f"--- Invoice ---\n"
            f"Package: {self.package_name}\n"
            f"Package Price: ${self.package_price:.2f}\n"
            f"Overtime Hours: {overtime_hours:.2f} hours\n"
            f"Overtime Cost: ${overtime_cost:.2f}\n"
            f"Total Cost: ${total_cost:.2f}\n"
            f"Event Date: {self.start_time.date()}\n"
            f"Event Time: {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}\n"
            f"----------------"
        )
        return invoice_details


def main():
    # Define package details
    packages = {
        "Pop-Up": (500, 50),  # Package price and overtime rate
        "Everything": (1250, 100)
    }

    # Example usage
    try:
        package_name = "Pop-Up"
        package_price, overtime_rate = packages[package_name]

        # Create a booking instance
        booking = DJEventBooking(package_name, package_price, overtime_rate)

        # Set event times
        start_time = datetime.datetime(2023, 10, 15, 18, 0)  # 6 PM
        end_time = datetime.datetime(2023, 10, 15, 22, 30)    # 10:30 PM
        booking.set_event_times(start_time, end_time)

        # Generate and print the invoice
        invoice = booking.generate_invoice()
        print(invoice)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
