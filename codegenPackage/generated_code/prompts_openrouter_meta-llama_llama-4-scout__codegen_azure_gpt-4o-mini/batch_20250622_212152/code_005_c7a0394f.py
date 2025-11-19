"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: "Develop a pricing calculator for taxi services like Innova Crysta or Swift Desire, considering factors like distance, time, and type of vehicle."
Generated: DETERMINISTIC_c7a0394f597e8789
Batch ID: 20250622_212152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TaxiService:
    """
    A class to represent a taxi service pricing calculator.
    """

    def __init__(self, base_fare, per_km_rate, per_minute_rate):
        """
        Initializes the TaxiService with base fare, per kilometer rate, and per minute rate.

        :param base_fare: The base fare for the taxi service.
        :param per_km_rate: The rate charged per kilometer.
        :param per_minute_rate: The rate charged per minute of travel.
        """
        self.base_fare = base_fare
        self.per_km_rate = per_km_rate
        self.per_minute_rate = per_minute_rate

    def calculate_fare(self, distance_km, time_minutes):
        """
        Calculates the total fare based on distance and time.

        :param distance_km: The distance traveled in kilometers.
        :param time_minutes: The time taken in minutes.
        :return: The total fare for the trip.
        :raises ValueError: If distance or time is negative.
        """
        if distance_km < 0 or time_minutes < 0:
            raise ValueError("Distance and time must be non-negative values.")

        # Calculate fare components
        distance_fare = self.per_km_rate * distance_km
        time_fare = self.per_minute_rate * time_minutes

        # Total fare calculation
        total_fare = self.base_fare + distance_fare + time_fare
        return total_fare

def main():
    """
    Main function to demonstrate the TaxiService pricing calculator.
    """
    # Define pricing for different vehicle types
    innova_service = TaxiService(base_fare=50, per_km_rate=15, per_minute_rate=2)
    swift_service = TaxiService(base_fare=30, per_km_rate=10, per_minute_rate=1.5)

    # Example input values
    distance = 10  # in kilometers
    time = 20      # in minutes

    try:
        # Calculate fares for both vehicle types
        innova_fare = innova_service.calculate_fare(distance, time)
        swift_fare = swift_service.calculate_fare(distance, time)

        # Output the results
        print(f"Innova Crysta Fare: ${innova_fare:.2f}")
        print(f"Swift Desire Fare: ${swift_fare:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
