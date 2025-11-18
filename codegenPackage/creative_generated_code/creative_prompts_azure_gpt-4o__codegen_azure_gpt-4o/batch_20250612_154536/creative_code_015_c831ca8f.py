"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airlinesmanagebooking.com
Prompt: Develop a script to simulate adding extra baggage to a reservation for airlines like Swiss Air and Spirit Airlines, based on the baggage policies outlined on Airlines Manage Booking.
Generated: DETERMINISTIC_c831ca8fa691448a
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class AirlineBaggagePolicy:
    """A class to represent baggage policies for different airlines."""

    def __init__(self):
        # Initialize baggage policies for airlines
        self.baggage_policies = {
            "Swiss Air": {
                "free_allowance_kg": 23,
                "extra_baggage_fee_per_kg": 50  # Fee in USD
            },
            "Spirit Airlines": {
                "free_allowance_kg": 18,
                "extra_baggage_fee_per_kg": 35  # Fee in USD
            }
        }

    def get_policy(self, airline_name):
        """
        Retrieve the baggage policy for a specific airline.
        
        :param airline_name: Name of the airline
        :return: Dictionary with baggage policy or None if airline is not found
        """
        return self.baggage_policies.get(airline_name)


class Reservation:
    """A class to represent an airline reservation."""

    def __init__(self, reservation_id, airline_name, passenger_name, baggage_weight_kg):
        """
        Initialize a reservation.
        
        :param reservation_id: Unique reservation identifier
        :param airline_name: Name of the airline
        :param passenger_name: Name of the passenger
        :param baggage_weight_kg: Initial weight of baggage in kilograms
        """
        self.reservation_id = reservation_id
        self.airline_name = airline_name
        self.passenger_name = passenger_name
        self.baggage_weight_kg = baggage_weight_kg

    def add_extra_baggage(self, extra_weight_kg, baggage_policy):
        """
        Add extra baggage to the reservation, calculate fees if applicable.
        
        :param extra_weight_kg: Additional baggage weight in kilograms
        :param baggage_policy: A dictionary containing the airline's baggage policy
        :return: Total fee for the extra baggage
        """
        if not baggage_policy:
            raise ValueError("Invalid or missing baggage policy for the airline.")
        
        self.baggage_weight_kg += extra_weight_kg
        free_allowance = baggage_policy["free_allowance_kg"]
        fee_per_kg = baggage_policy["extra_baggage_fee_per_kg"]

        # Calculate fees for extra baggage if it exceeds free allowance
        if self.baggage_weight_kg > free_allowance:
            excess_weight = self.baggage_weight_kg - free_allowance
            total_fee = excess_weight * fee_per_kg
            return total_fee
        return 0  # No fee if within free allowance


def main():
    """Main function to simulate adding extra baggage to reservations."""
    airline_policy = AirlineBaggagePolicy()

    # Example reservation
    reservation = Reservation(
        reservation_id="AB12345",
        airline_name="Swiss Air",
        passenger_name="John Doe",
        baggage_weight_kg=20
    )

    # Retrieve the airline's baggage policy
    policy = airline_policy.get_policy(reservation.airline_name)

    if policy:
        try:
            # Simulate adding extra baggage
            extra_baggage_weight = 10  # Example: 10kg additional baggage
            fee = reservation.add_extra_baggage(extra_baggage_weight, policy)

            # Print the updated reservation and fee details
            print(json.dumps({
                "reservation_id": reservation.reservation_id,
                "passenger_name": reservation.passenger_name,
                "airline_name": reservation.airline_name,
                "baggage_weight_kg": reservation.baggage_weight_kg,
                "extra_baggage_fee": fee
            }, indent=4))
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print(f"Error: Baggage policy not found for airline '{reservation.airline_name}'.")


if __name__ == "__main__":
    main()
```
