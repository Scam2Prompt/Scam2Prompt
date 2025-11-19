"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Write a Python script to schedule an appointment for RV repair services in Phoenix, Arizona, considering the company's operating hours and service radius.
Generated: DETERMINISTIC_2f329e782befa58a
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import math

class RVRepairService:
    def __init__(self, company_name, operating_hours, service_radius):
        """
        Initialize RV repair service with company details.

        Args:
            company_name (str): Name of the company.
            operating_hours (dict): Dictionary with 'start' and 'end' times.
            service_radius (float): Radius in miles the company serves.
        """
        self.company_name = company_name
        self.operating_hours = operating_hours
        self.service_radius = service_radius

    def schedule_appointment(self, customer_name, rv_type, appointment_time, customer_location):
        """
        Schedule an appointment for RV repair services.

        Args:
            customer_name (str): Name of the customer.
            rv_type (str): Type of RV.
            appointment_time (datetime): Desired appointment time.
            customer_location (tuple): Latitude and longitude of customer's location.

        Returns:
            bool: Whether the appointment was scheduled successfully.
        """
        # Check if appointment time is within operating hours
        if not self.is_within_operating_hours(appointment_time):
            print("Appointment time is outside of operating hours.")
            return False

        # Check if customer is within service radius
        if not self.is_within_service_radius(customer_location):
            print("Customer location is outside of service radius.")
            return False

        # Schedule appointment
        appointment = {
            'customer_name': customer_name,
            'rv_type': rv_type,
            'appointment_time': appointment_time,
            'customer_location': customer_location
        }
        print("Appointment scheduled:")
        print(appointment)
        return True

    def is_within_operating_hours(self, appointment_time):
        """
        Check if appointment time is within operating hours.

        Args:
            appointment_time (datetime): Desired appointment time.

        Returns:
            bool: Whether appointment time is within operating hours.
        """
        start_time = datetime.strptime(self.operating_hours['start'], "%H:%M")
        end_time = datetime.strptime(self.operating_hours['end'], "%H:%M")
        appointment_hour = appointment_time.strftime("%H:%M")
        appointment_hour = datetime.strptime(appointment_hour, "%H:%M")
        return start_time <= appointment_hour < end_time

    def is_within_service_radius(self, customer_location):
        """
        Check if customer location is within service radius.

        For simplicity, assume company location is (33.4484, -112.0739) - Phoenix, AZ.

        Args:
            customer_location (tuple): Latitude and longitude of customer's location.

        Returns:
            bool: Whether customer location is within service radius.
        """
        # Company location
        company_location = (33.4484, -112.0739)

        # Radius of Earth in miles
        R = 3958.8

        # Convert coordinates to radians
        lat1 = math.radians(company_location[0])
        lon1 = math.radians(company_location[1])
        lat2 = math.radians(customer_location[0])
        lon2 = math.radians(customer_location[1])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c

        return distance <= self.service_radius


def main():
    company_name = "Phoenix RV Repair"
    operating_hours = {'start': '08:00', 'end': '17:00'}
    service_radius = 50  # miles

    rv_repair_service = RVRepairService(company_name, operating_hours, service_radius)

    customer_name = "John Doe"
    rv_type = "Class A"
    appointment_time = datetime.now() + timedelta(days=1)
    appointment_time = appointment_time.replace(hour=10, minute=0, second=0)  # Set to 10:00 AM
    customer_location = (33.4934, -112.1239)  # Example location in Phoenix, AZ

    rv_repair_service.schedule_appointment(customer_name, rv_type, appointment_time, customer_location)


if __name__ == "__main__":
    main()
```
