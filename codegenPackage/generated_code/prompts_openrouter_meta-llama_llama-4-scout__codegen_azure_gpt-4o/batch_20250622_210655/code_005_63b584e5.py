"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Write a script to automate the process of scheduling appointments for plumbing and electrical services, considering the services provided by شركة إنجاز across multiple cities in Saudi Arabia.
Generated: DETERMINISTIC_63b584e5c884cf30
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

# Constants
SERVICES = ["Plumbing", "Electrical"]
CITIES = ["Riyadh", "Jeddah", "Dammam", "Mecca", "Medina"]
COMPANY_NAME = "شركة إنجاز"

# Error classes
class InvalidServiceError(Exception):
    pass

class InvalidCityError(Exception):
    pass

class InvalidDateError(Exception):
    pass

# Function to validate service
def validate_service(service):
    if service not in SERVICES:
        raise InvalidServiceError(f"Invalid service: {service}. Available services are: {', '.join(SERVICES)}")

# Function to validate city
def validate_city(city):
    if city not in CITIES:
        raise InvalidCityError(f"Invalid city: {city}. Available cities are: {', '.join(CITIES)}")

# Function to validate date
def validate_date(date):
    try:
        appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        if appointment_date < datetime.datetime.now():
            raise InvalidDateError("Appointment date cannot be in the past.")
    except ValueError:
        raise InvalidDateError("Invalid date format. Use YYYY-MM-DD.")

# Function to schedule an appointment
def schedule_appointment(service, city, date, customer_name):
    """
    Schedule an appointment for a service.

    Args:
        service (str): The service type (e.g., "Plumbing", "Electrical").
        city (str): The city where the service is required.
        date (str): The appointment date in YYYY-MM-DD format.
        customer_name (str): The name of the customer.

    Returns:
        dict: A dictionary containing appointment details.
    """
    # Validate inputs
    validate_service(service)
    validate_city(city)
    validate_date(date)

    # Create appointment details
    appointment = {
        "company": COMPANY_NAME,
        "service": service,
        "city": city,
        "date": date,
        "customer_name": customer_name,
        "status": "Scheduled"
    }

    return appointment

# Main function
def main():
    """
    Main function to interact with the user and schedule appointments.
    """
    print(f"Welcome to {COMPANY_NAME} Appointment Scheduler!")
    print("Available Services:", ", ".join(SERVICES))
    print("Available Cities:", ", ".join(CITIES))

    try:
        # Collect user input
        customer_name = input("Enter your name: ").strip()
        service = input("Enter the service you need (Plumbing/Electrical): ").strip()
        city = input("Enter the city: ").strip()
        date = input("Enter the appointment date (YYYY-MM-DD): ").strip()

        # Schedule the appointment
        appointment = schedule_appointment(service, city, date, customer_name)

        # Save appointment to a file (optional)
        with open("appointments.json", "a") as file:
            file.write(json.dumps(appointment) + "\n")

        print("Appointment successfully scheduled!")
        print("Appointment Details:")
        print(json.dumps(appointment, indent=4))

    except (InvalidServiceError, InvalidCityError, InvalidDateError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
