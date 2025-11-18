"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superstep.org
Prompt: Write code to simulate yacht charter reservations, based on the "Top Reasons to Reserve Yacht Charter Today" article on Superstep.org.
Generated: DETERMINISTIC_dd39e82c092c8334
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Yacht:
    """
    Represents a yacht available for charter.
    """
    def __init__(self, name: str, capacity: int, price_per_day: float):
        """
        Initializes a new yacht instance.
        
        :param name: The name of the yacht.
        :param capacity: Maximum number of guests the yacht can accommodate.
        :param price_per_day: Daily rental price of the yacht.
        """
        self.name = name
        self.capacity = capacity
        self.price_per_day = price_per_day

    def __str__(self):
        return f"{self.name} (Capacity: {self.capacity}, Price: ${self.price_per_day}/day)"


class Reservation:
    """
    Represents a yacht charter reservation.
    """
    def __init__(self, yacht: Yacht, days: int):
        """
        Initializes a reservation with a yacht and number of days.
        
        :param yacht: The yacht being reserved.
        :param days: Number of days for the reservation.
        """
        if days <= 0:
            raise ValueError("Number of days must be a positive integer.")
        
        self.yacht = yacht
        self.days = days
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the reservation.
        
        :return: Total cost for the reserved days.
        """
        return self.yacht.price_per_day * self.days

    def __str__(self):
        return f"Reservation for {self.yacht.name} for {self.days} day(s). Total cost: ${self.total_cost}"


class CharterService:
    """
    Handles yacht charter reservations.
    """
    def __init__(self):
        """
        Initializes the charter service with available yachts.
        """
        self.yachts = [
            Yacht("Serenity", 10, 1500.0),
            Yacht("Ocean Explorer", 12, 2000.0),
            Yacht("Luxury Voyage", 8, 2500.0),
        ]

    def list_yachts(self):
        """
        Lists all available yachts for charter.
        """
        print("Available Yachts:")
        for yacht in self.yachts:
            print(yacht)

    def reserve_yacht(self, yacht_name: str, days: int) -> Reservation:
        """
        Reserves a yacht given its name and the number of days.
        
        :param yacht_name: Name of the yacht to reserve.
        :param days: Number of days for the reservation.
        :return: A Reservation object.
        """
        yacht = next((y for y in self.yachts if y.name == yacht_name), None)
        if yacht is None:
            raise ValueError("Yacht not found.")
        
        reservation = Reservation(yacht, days)
        return reservation


def main():
    """
    Main function to run the yacht charter reservation system.
    """
    charter_service = CharterService()
    
    try:
        # List available yachts
        charter_service.list_yachts()
        
        # Sample reservation
        yacht_name = "Serenity"
        days = 3
        reservation = charter_service.reserve_yacht(yacht_name, days)
        
        print(reservation)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
