"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Provide a Python implementation for contracting and tour operating processes in the Tourism & Hospitality industry, as described in Hampton's Hotel Institute's International Tourism & Hospitality Management course.
Generated: DETERMINISTIC_42efbc8fae6dcaa1
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TourOperator:
    """
    A class representing a Tour Operator that manages contracts and tours.
    """

    def __init__(self, name):
        """
        Initialize the TourOperator with a name.

        :param name: The name of the tour operator
        """
        self.name = name
        self.contracts = []
        self.tours = []

    def add_contract(self, contract):
        """
        Add a contract to the tour operator's records.

        :param contract: A dictionary containing contract details
        """
        if not isinstance(contract, dict):
            raise ValueError("Contract must be a dictionary.")
        
        self.contracts.append(contract)

    def create_tour(self, tour_name, destination, price, capacity):
        """
        Create a new tour.

        :param tour_name: The name of the tour
        :param destination: The destination of the tour
        :param price: The price of the tour
        :param capacity: The maximum capacity for the tour
        :raises ValueError: If any parameter is invalid
        :returns: A dictionary representing the tour
        """
        if not all(isinstance(param, (str, int, float)) for param in [tour_name, destination, price, capacity]):
            raise ValueError("Invalid parameter type. Ensure tour_name and destination are strings, price and capacity are numbers.")

        if price <= 0 or capacity <= 0:
            raise ValueError("Price and capacity must be greater than zero.")

        tour = {
            "name": tour_name,
            "destination": destination,
            "price": price,
            "capacity": capacity,
            "bookings": 0
        }
        self.tours.append(tour)
        return tour

    def book_tour(self, tour_name, number_of_people):
        """
        Book a tour for a specified number of people.

        :param tour_name: The name of the tour to book
        :param number_of_people: The number of people to book for
        :raises ValueError: If the booking exceeds capacity
        """
        tour = next((t for t in self.tours if t['name'] == tour_name), None)
        if not tour:
            raise ValueError("Tour not found.")

        if tour["bookings"] + number_of_people > tour["capacity"]:
            raise ValueError("Booking exceeds tour capacity.")
        
        tour["bookings"] += number_of_people
        print(f"Successfully booked {number_of_people} for {tour_name}.")

    def get_tour_info(self, tour_name):
        """
        Retrieve information about a specific tour.

        :param tour_name: The name of the tour
        :returns: A dictionary containing tour information
        :raises ValueError: If the tour is not found
        """
        tour = next((t for t in self.tours if t['name'] == tour_name), None)
        if not tour:
            raise ValueError("Tour not found.")
        
        return tour

    def list_tours(self):
        """
        List all tours managed by the Tour Operator.

        :returns: A list of tours
        """
        return self.tours


# Example Usage
if __name__ == "__main__":
    try:
        operator = TourOperator("Amazing Travels")
        contract = {
            "partner": "Local Hotels",
            "terms": "50% payment upfront, balance on completion.",
            "valid_until": "2025-12-31"
        }
        operator.add_contract(contract)
        
        tour1 = operator.create_tour("Beach Getaway", "Hawaii", 1200.00, 30)
        operator.book_tour("Beach Getaway", 5)
        
        print("Current Tours:")
        for tour in operator.list_tours():
            print(tour)
        
        tour_info = operator.get_tour_info("Beach Getaway")
        print("Tour Info:", tour_info)

    except ValueError as e:
        print(f"Error: {e}")
```
