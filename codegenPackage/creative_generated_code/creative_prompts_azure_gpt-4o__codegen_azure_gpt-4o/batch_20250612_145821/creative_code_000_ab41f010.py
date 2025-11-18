"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: Write Python code to integrate a custom booking calendar system that filters out unqualified leads, as described in Client Fuel's "self-booking process."
Generated: DETERMINISTIC_ab41f01028bc6d79
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BookingCalendar:
    def __init__(self):
        # Initialize the calendar with time slots and qualified leads list
        self.time_slots = self._generate_time_slots()
        self.qualified_leads = []

    def _generate_time_slots(self):
        """
        Generate available time slots for the next 7 days in hourly intervals.
        Returns a dictionary with dates as keys and lists of time slots as values.
        """
        time_slots = {}
        today = datetime.date.today()
        for day in range(7):
            date = today + datetime.timedelta(days=day)
            time_slots[date] = [f"{hour}:00" for hour in range(9, 17)]  # 9 AM to 5 PM slots
        return time_slots

    def add_lead(self, lead_data):
        """
        Add a lead to the qualified leads list if they pass the qualifications.
        :param lead_data: Dictionary containing lead information.
        """
        try:
            if self._is_lead_qualified(lead_data):
                self.qualified_leads.append(lead_data)
                print(f"Lead {lead_data['name']} was successfully added.")
            else:
                print(f"Lead {lead_data['name']} did not meet qualifications.")
        except KeyError as e:
            print(f"Missing required lead information: {e}")

    def _is_lead_qualified(self, lead_data):
        """
        Check if a lead meets the qualifications.
        Example criteria: lead must provide a budget > $5000 and a valid email.
        :param lead_data: Dictionary containing lead information.
        :return: Boolean indicating whether the lead is qualified.
        """
        required_budget = 5000
        try:
            return lead_data.get('budget', 0) > required_budget and '@' in lead_data.get('email', '')
        except Exception as e:
            print(f"Error while checking qualifications: {e}")
            return False

    def book_time_slot(self, lead_name, date, time_slot):
        """
        Book a time slot for a qualified lead.
        :param lead_name: Name of the lead.
        :param date: Date (in YYYY-MM-DD format) to book.
        :param time_slot: Time slot (e.g., "10:00") to book.
        """
        try:
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            if date_obj not in self.time_slots:
                raise ValueError("Invalid date. Please select a date within the next 7 days.")
            if time_slot not in self.time_slots[date_obj]:
                raise ValueError("Invalid or unavailable time slot.")
            
            # Check if the lead is qualified
            lead = next((lead for lead in self.qualified_leads if lead['name'] == lead_name), None)
            if not lead:
                raise ValueError("Lead is not qualified to book a time slot.")

            # Book the time slot
            self.time_slots[date_obj].remove(time_slot)
            print(f"Time slot {time_slot} on {date} successfully booked for {lead_name}.")
        except ValueError as e:
            print(f"Booking error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def available_time_slots(self):
        """
        Display available time slots.
        :return: Dictionary of available slots.
        """
        return self.time_slots


# Example usage
if __name__ == "__main__":
    # Initialize BookingCalendar
    calendar = BookingCalendar()

    # Add leads
    calendar.add_lead({"name": "John Doe", "email": "john.doe@example.com", "budget": 6000})
    calendar.add_lead({"name": "Jane Smith", "email": "jane.smith@example.com", "budget": 4000})  # Not qualified

    # Display available time slots
    print("\nAvailable Time Slots:")
    for date, times in calendar.available_time_slots().items():
        print(f"{date}: {times}")

    # Book a time slot
    calendar.book_time_slot("John Doe", "2023-10-15", "10:00")

    # Display updated time slots
    print("\nUpdated Time Slots:")
    for date, times in calendar.available_time_slots().items():
        print(f"{date}: {times}")
```
