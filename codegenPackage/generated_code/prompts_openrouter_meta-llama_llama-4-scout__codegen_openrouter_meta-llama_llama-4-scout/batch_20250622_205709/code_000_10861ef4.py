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
# dj_event_bookings.py

class DjPackage:
    """Represents a DJ package deal."""

    def __init__(self, name, base_price, overtime_rate):
        """
        Initializes a DjPackage.

        Args:
            name (str): Package name.
            base_price (float): Base price of the package.
            overtime_rate (float): Overtime rate per hour.
        """
        self.name = name
        self.base_price = base_price
        self.overtime_rate = overtime_rate

class DjEventBooking:
    """Represents a DJ event booking."""

    def __init__(self, package, event_date, start_time, end_time):
        """
        Initializes a DjEventBooking.

        Args:
            package (DjPackage): DJ package deal.
            event_date (str): Event date (YYYY-MM-DD).
            start_time (str): Event start time (HH:MM).
            end_time (str): Event end time (HH:MM).
        """
        self.package = package
        self.event_date = event_date
        self.start_time = start_time
        self.end_time = end_time

    def calculate_duration(self):
        """
        Calculates the event duration in hours.

        Returns:
            float: Event duration in hours.
        """
        from datetime import datetime

        start_datetime = datetime.strptime(f"{self.event_date} {self.start_time}", "%Y-%m-%d %H:%M")
        end_datetime = datetime.strptime(f"{self.event_date} {self.end_time}", "%Y-%m-%d %H:%M")

        duration = (end_datetime - start_datetime).total_seconds() / 3600
        return duration

    def calculate_overtime(self):
        """
        Calculates the overtime cost.

        Returns:
            float: Overtime cost.
        """
        duration = self.calculate_duration()
        overtime_threshold = 8  # 8 hours

        if duration <= overtime_threshold:
            return 0
        else:
            overtime_hours = duration - overtime_threshold
            return overtime_hours * self.package.overtime_rate

    def calculate_total_cost(self):
        """
        Calculates the total cost, including overtime.

        Returns:
            float: Total cost.
        """
        duration = self.calculate_duration()
        base_cost = self.package.base_price
        overtime_cost = self.calculate_overtime()

        # Check if event duration exceeds 4 hours for overtime consideration
        if duration > 4:
            return base_cost + overtime_cost
        else:
            return base_cost

def generate_invoice(event_booking):
    """
    Generates an invoice for the event booking.

    Args:
        event_booking (DjEventBooking): Event booking.

    Returns:
        str: Invoice.
    """
    invoice = f"Invoice for {event_booking.event_date}\n"
    invoice += f"Package: {event_booking.package.name}\n"
    invoice += f"Duration: {event_booking.calculate_duration():.2f} hours\n"
    invoice += f"Base Price: ${event_booking.package.base_price:.2f}\n"

    overtime_cost = event_booking.calculate_overtime()
    if overtime_cost > 0:
        invoice += f"Overtime Cost: ${overtime_cost:.2f}\n"

    total_cost = event_booking.calculate_total_cost()
    invoice += f"Total: ${total_cost:.2f}\n"

    return invoice

def main():
    # Define DJ packages
    pop_up_package = DjPackage("Pop-Up", 500, 100)
    everything_package = DjPackage("Everything", 1250, 150)

    # Create event booking
    event_date = "2024-09-20"
    start_time = "18:00"
    end_time = "22:00"
    event_booking = DjEventBooking(everything_package, event_date, start_time, end_time)

    try:
        # Generate invoice
        invoice = generate_invoice(event_booking)
        print(invoice)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
