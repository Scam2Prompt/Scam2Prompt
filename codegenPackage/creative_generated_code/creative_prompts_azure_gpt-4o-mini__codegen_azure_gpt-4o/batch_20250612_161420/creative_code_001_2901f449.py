"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herbe.bio
Prompt: Write a code snippet for a restaurant reservation system that allows users to book tables at Herbe Food & Drink, including options for special events.
Generated: DETERMINISTIC_2901f449ed3bca9a
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# restaurant_reservation.py

import datetime

class RestaurantReservationSystem:
    def __init__(self):
        # Initialize available tables and reservations
        self.available_tables = {i: True for i in range(1, 21)}  # 20 tables numbered 1-20
        self.reservations = []

    def book_table(self, name, phone_number, date, time, number_of_people, special_event=None):
        """
        Book a table at Herbe Food & Drink.
        :param name: Name of the customer
        :param phone_number: Contact number of the customer
        :param date: Date of reservation in YYYY-MM-DD format
        :param time: Time of reservation in HH:MM format (24-hour clock)
        :param number_of_people: Number of people for the reservation
        :param special_event: Optional special event description
        :return: Confirmation message or error message
        """
        try:
            # Validate date and time format
            reservation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            reservation_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Check if any table is available
            available_table = next((table for table, status in self.available_tables.items() if status), None)
            if available_table is None:
                return "Sorry, no tables are available for the selected date and time."

            # Reserve the table
            self.available_tables[available_table] = False
            reservation = {
                "table_number": available_table,
                "name": name,
                "phone_number": phone_number,
                "date": reservation_date,
                "time": reservation_time,
                "number_of_people": number_of_people,
                "special_event": special_event
            }
            self.reservations.append(reservation)

            return (f"Reservation confirmed for {name} on {date} at {time} for {number_of_people} people."
                    f" Table number: {available_table}."
                    f" Special Event: {special_event if special_event else 'None'}")

        except ValueError as e:
            # Handle invalid date/time format
            return f"Error: Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."

    def cancel_reservation(self, name, phone_number):
        """
        Cancel an existing reservation.
        :param name: Name of the customer
        :param phone_number: Contact number of the customer
        :return: Cancellation confirmation or error message
        """
        for reservation in self.reservations:
            if reservation["name"] == name and reservation["phone_number"] == phone_number:
                table_number = reservation["table_number"]
                self.available_tables[table_number] = True
                self.reservations.remove(reservation)
                return f"Reservation for {name} has been successfully canceled."

        return "Error: No matching reservation found."

    def view_reservations(self):
        """
        View all reservations.
        :return: List of all reservations
        """
        return self.reservations


# Example usage
if __name__ == "__main__":
    system = RestaurantReservationSystem()

    # Book a table
    print(system.book_table(
        name="John Doe",
        phone_number="123-456-7890",
        date="2023-12-15",
        time="19:00",
        number_of_people=4,
        special_event="Birthday Party"
    ))

    # View reservations
    print(system.view_reservations())

    # Cancel a reservation
    print(system.cancel_reservation(name="John Doe", phone_number="123-456-7890"))

    # View reservations after cancellation
    print(system.view_reservations())
```
