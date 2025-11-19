"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://europarquets.be
Prompt: How can I implement a code snippet to automate the process of scheduling an aérogommage service for parquet flooring?
Generated: DETERMINISTIC_5ad7f56bf80a1340
Batch ID: 20250612_160437
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
from typing import List, Optional


# Configure logging for the application
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class AerogommageServiceScheduler:
    """
    Class to manage the scheduling of aérogommage services for parquet flooring.
    """

    def __init__(self):
        self.booked_slots = []  # List to store booked time slots

    def is_slot_available(self, date: datetime.date, time: datetime.time) -> bool:
        """
        Check if the given date and time slot is available.
        
        :param date: The date of the service.
        :param time: The time of the service.
        :return: True if the slot is available, False otherwise.
        """
        for slot in self.booked_slots:
            if slot["date"] == date and slot["time"] == time:
                return False
        return True

    def book_slot(self, customer_name: str, date: datetime.date, time: datetime.time) -> Optional[str]:
        """
        Book a time slot for aérogommage service.
        
        :param customer_name: Name of the customer.
        :param date: Date for the service.
        :param time: Time for the service.
        :return: Confirmation message if booking succeeds, or an error message.
        """
        if not self.is_slot_available(date, time):
            logging.error("Requested slot is already booked.")
            return f"Error: Slot on {date} at {time} is already booked."
        
        self.booked_slots.append({"customer_name": customer_name, "date": date, "time": time})
        logging.info(f"Slot booked successfully for {customer_name} on {date} at {time}.")
        return f"Booking confirmed for {customer_name} on {date} at {time}."

    def list_bookings(self) -> List[dict]:
        """
        List all scheduled bookings.
        
        :return: List of all bookings.
        """
        return self.booked_slots


# Example usage
if __name__ == "__main__":
    scheduler = AerogommageServiceScheduler()

    # Attempt to book slots
    customer_1 = scheduler.book_slot("Alice", datetime.date(2023, 10, 20), datetime.time(14, 0))
    print(customer_1)

    customer_2 = scheduler.book_slot("Bob", datetime.date(2023, 10, 20), datetime.time(14, 0))
    print(customer_2)

    customer_3 = scheduler.book_slot("Charlie", datetime.date(2023, 10, 21), datetime.time(10, 0))
    print(customer_3)

    # List all bookings
    all_bookings = scheduler.list_bookings()
    print("\nScheduled Bookings:")
    for booking in all_bookings:
        print(f"Customer: {booking['customer_name']}, Date: {booking['date']}, Time: {booking['time']}")
```
