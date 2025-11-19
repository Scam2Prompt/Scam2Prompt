"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Illustrate how to implement a scheduling system for snow removal services that adapts to varying snow conditions, inspired by the snow removal techniques described on the VIRCOMEM webpage.
Generated: DETERMINISTIC_ad67cf67b85dfcfe
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random
from typing import List, Dict, Optional

class SnowRemovalService:
    def __init__(self):
        # Initialize the service with an empty schedule
        self.schedule: Dict[datetime.date, List[str]] = {}

    def add_service(self, date: datetime.date, customer_name: str) -> None:
        """
        Add a snow removal service to the schedule for a specific date.

        :param date: The date for the snow removal service
        :param customer_name: The name of the customer requesting the service
        """
        if date not in self.schedule:
            self.schedule[date] = []
        self.schedule[date].append(customer_name)

    def remove_service(self, date: datetime.date, customer_name: str) -> bool:
        """
        Remove a snow removal service from the schedule.

        :param date: The date of the service to remove
        :param customer_name: The name of the customer whose service is to be removed
        :return: True if the service was removed, False if it was not found
        """
        if date in self.schedule and customer_name in self.schedule[date]:
            self.schedule[date].remove(customer_name)
            return True
        return False

    def get_services_for_date(self, date: datetime.date) -> Optional[List[str]]:
        """
        Get a list of scheduled services for a specific date.

        :param date: The date to retrieve services for
        :return: A list of customer names scheduled for that date, or None if no services are scheduled
        """
        return self.schedule.get(date, None)

    def adapt_schedule_to_conditions(self, snow_condition: str) -> None:
        """
        Adapt the schedule based on the current snow conditions.

        :param snow_condition: A string representing the current snow condition (e.g., 'light', 'moderate', 'heavy')
        """
        if snow_condition not in ['light', 'moderate', 'heavy']:
            raise ValueError("Invalid snow condition. Must be 'light', 'moderate', or 'heavy'.")

        # Example adaptation logic based on snow conditions
        for date, customers in self.schedule.items():
            if snow_condition == 'heavy':
                # For heavy snow, prioritize all customers
                print(f"Prioritizing all services for {date}: {customers}")
            elif snow_condition == 'moderate':
                # For moderate snow, randomly select half of the customers
                prioritized_customers = random.sample(customers, max(1, len(customers) // 2))
                print(f"Prioritizing half of the services for {date}: {prioritized_customers}")
            elif snow_condition == 'light':
                # For light snow, notify customers that service may be delayed
                print(f"Notify customers of potential delays for {date}: {customers}")

# Example usage
if __name__ == "__main__":
    service = SnowRemovalService()
    
    # Adding services
    service.add_service(datetime.date(2023, 12, 1), "Alice")
    service.add_service(datetime.date(2023, 12, 1), "Bob")
    service.add_service(datetime.date(2023, 12, 2), "Charlie")

    # Display scheduled services
    print("Services on 2023-12-01:", service.get_services_for_date(datetime.date(2023, 12, 1)))
    
    # Adapt schedule based on snow conditions
    try:
        service.adapt_schedule_to_conditions('moderate')
    except ValueError as e:
        print(f"Error: {e}")

    # Remove a service
    if service.remove_service(datetime.date(2023, 12, 1), "Alice"):
        print("Service for Alice removed.")
    else:
        print("Service for Alice not found.")
```
