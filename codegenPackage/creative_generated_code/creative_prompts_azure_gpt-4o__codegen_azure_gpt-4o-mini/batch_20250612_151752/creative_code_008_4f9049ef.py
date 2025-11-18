"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Create a script to generate a daily delivery schedule for an automotive parts distributor, including multiple delivery times to professional clients like garages and transport fleets.
Generated: DETERMINISTIC_4f9049ef22350f1b
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random
from typing import List, Dict, Tuple

# Define a class to represent a Delivery Schedule
class DeliverySchedule:
    def __init__(self, client_name: str, delivery_times: List[datetime.time]):
        self.client_name = client_name
        self.delivery_times = delivery_times

    def __str__(self):
        """Return a string representation of the delivery schedule."""
        times = ", ".join([time.strftime("%H:%M") for time in self.delivery_times])
        return f"Client: {self.client_name}, Delivery Times: {times}"


def generate_delivery_times(num_times: int) -> List[datetime.time]:
    """
    Generate a list of random delivery times throughout the day.
    
    Args:
        num_times (int): The number of delivery times to generate.
    
    Returns:
        List[datetime.time]: A list of unique delivery times.
    """
    delivery_times = set()
    while len(delivery_times) < num_times:
        hour = random.randint(8, 17)  # Delivery hours from 8 AM to 5 PM
        minute = random.choice([0, 15, 30, 45])  # Delivery every 15 minutes
        delivery_times.add(datetime.time(hour, minute))

    return sorted(delivery_times)


def create_daily_schedule(clients: List[str], num_deliveries_per_client: int) -> List[DeliverySchedule]:
    """
    Create a daily delivery schedule for the given clients.
    
    Args:
        clients (List[str]): A list of client names.
        num_deliveries_per_client (int): Number of delivery times per client.
    
    Returns:
        List[DeliverySchedule]: A list of DeliverySchedule objects.
    """
    schedules = []
    for client in clients:
        delivery_times = generate_delivery_times(num_deliveries_per_client)
        schedules.append(DeliverySchedule(client, delivery_times))
    
    return schedules


def print_delivery_schedules(schedules: List[DeliverySchedule]) -> None:
    """
    Print the delivery schedules for all clients.
    
    Args:
        schedules (List[DeliverySchedule]): A list of DeliverySchedule objects.
    """
    for schedule in schedules:
        print(schedule)


def main():
    """
    Main function to execute the delivery schedule generation.
    """
    clients = ["Garage A", "Fleet B", "Garage C", "Transport D"]
    num_deliveries_per_client = 3  # Number of delivery times for each client

    try:
        # Create the daily delivery schedule
        schedules = create_daily_schedule(clients, num_deliveries_per_client)
        # Print the generated schedules
        print_delivery_schedules(schedules)
    except Exception as e:
        print(f"Error occurred while generating delivery schedules: {str(e)}")


if __name__ == "__main__":
    main()
```
