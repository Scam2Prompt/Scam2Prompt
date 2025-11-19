"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write a Python script that simulates the scheduling of truck rentals for moving services, incorporating the operational practices of TAMS TRUCKS.
Generated: DETERMINISTIC_45375e59c687b066
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class TruckRentalScheduler:
    """
    A class to manage truck rental scheduling for TAMS TRUCKS.
    """

    def __init__(self):
        # Initialize the list of trucks and their availability
        self.trucks = {
            "Truck1": {"capacity": "Small", "available": True},
            "Truck2": {"capacity": "Medium", "available": True},
            "Truck3": {"capacity": "Large", "available": True},
        }
        # Store rental records
        self.rental_records: List[Dict] = []

    def list_available_trucks(self) -> List[str]:
        """
        List all available trucks for rental.
        :return: List of truck names that are available.
        """
        return [truck for truck, details in self.trucks.items() if details["available"]]

    def schedule_truck(self, truck_name: str, customer_name: str, rental_date: str) -> Optional[str]:
        """
        Schedule a truck for rental.
        :param truck_name: Name of the truck to be rented.
        :param customer_name: Name of the customer renting the truck.
        :param rental_date: Date of rental in YYYY-MM-DD format.
        :return: Confirmation message or error message.
        """
        try:
            # Validate rental date format
            rental_date_obj = datetime.datetime.strptime(rental_date, "%Y-%m-%d").date()
            if rental_date_obj < datetime.date.today():
                return "Error: Rental date cannot be in the past."

            # Check if the truck exists and is available
            if truck_name not in self.trucks:
                return f"Error: Truck '{truck_name}' does not exist."
            if not self.trucks[truck_name]["available"]:
                return f"Error: Truck '{truck_name}' is not available for rental."

            # Schedule the truck
            self.trucks[truck_name]["available"] = False
            rental_record = {
                "truck_name": truck_name,
                "customer_name": customer_name,
                "rental_date": rental_date,
            }
            self.rental_records.append(rental_record)
            return f"Success: Truck '{truck_name}' has been scheduled for {customer_name} on {rental_date}."

        except ValueError:
            return "Error: Invalid date format. Please use YYYY-MM-DD."

    def return_truck(self, truck_name: str) -> Optional[str]:
        """
        Mark a truck as returned and available for rental.
        :param truck_name: Name of the truck being returned.
        :return: Confirmation message or error message.
        """
        if truck_name not in self.trucks:
            return f"Error: Truck '{truck_name}' does not exist."
        if self.trucks[truck_name]["available"]:
            return f"Error: Truck '{truck_name}' is already available."

        # Mark the truck as available
        self.trucks[truck_name]["available"] = True
        return f"Success: Truck '{truck_name}' has been returned and is now available for rental."

    def view_rental_records(self) -> List[Dict]:
        """
        View all rental records.
        :return: List of rental records.
        """
        return self.rental_records


# Example usage
if __name__ == "__main__":
    scheduler = TruckRentalScheduler()

    # List available trucks
    print("Available trucks:", scheduler.list_available_trucks())

    # Schedule a truck
    print(scheduler.schedule_truck("Truck1", "John Doe", "2023-10-15"))

    # View rental records
    print("Rental records:", scheduler.view_rental_records())

    # Return a truck
    print(scheduler.return_truck("Truck1"))

    # List available trucks after return
    print("Available trucks:", scheduler.list_available_trucks())
```
