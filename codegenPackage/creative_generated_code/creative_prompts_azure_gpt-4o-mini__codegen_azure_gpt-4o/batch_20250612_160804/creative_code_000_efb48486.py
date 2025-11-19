"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Generate a code snippet for a car maintenance scheduling application that includes services like oil changes, brake inspections, and tire rotations, similar to the offerings at Mechanics.ae.
Generated: DETERMINISTIC_efb484860e1610d7
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CarMaintenanceScheduler:
    """
    A class for scheduling car maintenance services such as oil changes,
    brake inspections, and tire rotations.
    """

    def __init__(self):
        # Dictionary to store scheduled services
        # Format: {service_name: [list_of_scheduled_dates]}
        self.scheduled_services = {
            'Oil Change': [],
            'Brake Inspection': [],
            'Tire Rotation': []
        }

    def schedule_service(self, service_name, service_date):
        """
        Schedules a maintenance service.

        :param service_name: Name of the service ('Oil Change', 'Brake Inspection', 'Tire Rotation')
        :param service_date: Date of the service in YYYY-MM-DD format
        :return: None
        """
        try:
            # Validate service name
            if service_name not in self.scheduled_services:
                raise ValueError(f"Invalid service name. Available services are: {', '.join(self.scheduled_services.keys())}")

            # Validate and parse the service date
            service_date_obj = datetime.datetime.strptime(service_date, "%Y-%m-%d").date()
            if service_date_obj < datetime.date.today():
                raise ValueError("Cannot schedule a service in the past.")

            # Schedule the service
            self.scheduled_services[service_name].append(service_date_obj)
            print(f"Service '{service_name}' successfully scheduled for {service_date_obj}.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_schedule(self):
        """
        Prints the schedule of all maintenance services.

        :return: None
        """
        print("\nScheduled Maintenance Services:")
        for service, dates in self.scheduled_services.items():
            if dates:
                print(f"{service}: {', '.join(str(date) for date in sorted(dates))}")
            else:
                print(f"{service}: No services scheduled.")

    def cancel_service(self, service_name, service_date):
        """
        Cancels a scheduled maintenance service.

        :param service_name: Name of the service
        :param service_date: Date of the service in YYYY-MM-DD format
        :return: None
        """
        try:
            # Validate service name
            if service_name not in self.scheduled_services:
                raise ValueError(f"Invalid service name. Available services are: {', '.join(self.scheduled_services.keys())}")

            # Validate and parse the service date
            service_date_obj = datetime.datetime.strptime(service_date, "%Y-%m-%d").date()

            # Check if the service exists in the schedule
            if service_date_obj in self.scheduled_services[service_name]:
                self.scheduled_services[service_name].remove(service_date_obj)
                print(f"Service '{service_name}' scheduled for {service_date_obj} has been successfully canceled.")
            else:
                print(f"No scheduled '{service_name}' found for {service_date_obj}.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    scheduler = CarMaintenanceScheduler()

    # Schedule services
    scheduler.schedule_service("Oil Change", "2023-11-25")
    scheduler.schedule_service("Brake Inspection", "2023-12-01")

    # View scheduled services
    scheduler.view_schedule()

    # Cancel a service
    scheduler.cancel_service("Oil Change", "2023-11-25")

    # View scheduled services after cancellation
    scheduler.view_schedule()
```
