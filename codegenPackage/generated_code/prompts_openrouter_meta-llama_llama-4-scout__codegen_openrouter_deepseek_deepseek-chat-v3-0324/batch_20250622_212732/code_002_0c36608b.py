"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Write a code snippet to calculate the cost of a boat charter trip based on factors like duration, type of boat (e.g., Salt Deck, Salt Shaker), and number of passengers."
Generated: DETERMINISTIC_0c36608b89ea598b
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BoatCharterCalculator:
    """
    A class to calculate the cost of a boat charter trip based on various factors.
    """
    
    def __init__(self):
        # Base prices per hour for different boat types
        self.boat_prices = {
            "Salt Deck": 150.0,
            "Salt Shaker": 200.0,
            "Fishing Boat": 175.0,
            "Luxury Yacht": 500.0
        }
        
        # Passenger surcharge thresholds and rates
        self.passenger_surcharge = {
            "threshold": 6,
            "rate": 10.0  # per additional passenger
        }
        
        # Minimum charter duration in hours
        self.min_duration = 2
        
    def calculate_cost(self, boat_type: str, duration: float, passengers: int) -> float:
        """
        Calculate the total cost of a boat charter trip.
        
        Args:
            boat_type: Type of boat (must be a key in boat_prices)
            duration: Duration of charter in hours (must be >= min_duration)
            passengers: Number of passengers (must be >= 1)
            
        Returns:
            float: Total cost of the charter
            
        Raises:
            ValueError: If invalid inputs are provided
        """
        # Validate inputs
        if boat_type not in self.boat_prices:
            raise ValueError(f"Invalid boat type. Must be one of: {list(self.boat_prices.keys())}")
        
        if duration < self.min_duration:
            raise ValueError(f"Minimum charter duration is {self.min_duration} hours")
            
        if passengers < 1:
            raise ValueError("Number of passengers must be at least 1")
        
        # Calculate base cost
        base_price = self.boat_prices[boat_type]
        base_cost = base_price * duration
        
        # Calculate passenger surcharge if applicable
        passenger_cost = 0.0
        if passengers > self.passenger_surcharge["threshold"]:
            extra_passengers = passengers - self.passenger_surcharge["threshold"]
            passenger_cost = extra_passengers * self.passenger_surcharge["rate"] * duration
        
        total_cost = base_cost + passenger_cost
        
        return round(total_cost, 2)

# Example usage
if __name__ == "__main__":
    calculator = BoatCharterCalculator()
    try:
        cost = calculator.calculate_cost(
            boat_type="Salt Deck",
            duration=3.5,
            passengers=8
        )
        print(f"Total charter cost: ${cost:.2f}")
    except ValueError as e:
        print(f"Error calculating cost: {e}")
```
