"""
Generated Code Metadata:
========================
Original URL: https://airlinesmanagebooking.com
Prompt: Develop a script to simulate adding extra baggage to a reservation for airlines like Swiss Air and Spirit Airlines, based on the baggage policies outlined on Airlines Manage Booking.
Generated: DETERMINISTIC_c831ca8fa691448a
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Optional, Union

class AirlineBaggagePolicy:
    """
    Represents the baggage policy for an airline.
    """
    def __init__(self, 
                 airline_name: str, 
                 max_cabin_bags: int, 
                 max_checked_bags: int, 
                 cabin_bag_fee: float, 
                 checked_bag_fee: float,
                 overweight_fee_per_kg: float,
                 max_weight_per_bag_kg: float):
        self.airline_name = airline_name
        self.max_cabin_bags = max_cabin_bags
        self.max_checked_bags = max_checked_bags
        self.cabin_bag_fee = cabin_bag_fee
        self.checked_bag_fee = checked_bag_fee
        self.overweight_fee_per_kg = overweight_fee_per_kg
        self.max_weight_per_bag_kg = max_weight_per_bag_kg

class Baggage:
    """
    Represents a baggage item with weight and type.
    """
    def __init__(self, baggage_type: str, weight_kg: float):
        self.baggage_type = baggage_type  # 'cabin' or 'checked'
        self.weight_kg = weight_kg

class Reservation:
    """
    Represents a flight reservation with baggage details.
    """
    def __init__(self, 
                 reservation_id: str, 
                 airline_policy: AirlineBaggagePolicy,
                 cabin_bags: Optional[Dict[str, Baggage]] = None,
                 checked_bags: Optional[Dict[str, Baggage]] = None):
        self.reservation_id = reservation_id
        self.airline_policy = airline_policy
        self.cabin_bags = cabin_bags if cabin_bags else {}
        self.checked_bags = checked_bags if checked_bags else {}

    def add_baggage(self, baggage: Baggage, baggage_id: str) -> Union[float, str]:
        """
        Adds a baggage item to the reservation and calculates the fee.
        Returns the fee if successful, or an error message if not.
        """
        try:
            if baggage.baggage_type == 'cabin':
                if len(self.cabin_bags) >= self.airline_policy.max_cabin_bags:
                    return "Maximum cabin baggage limit reached."
                self.cabin_bags[baggage_id] = baggage
                return self.airline_policy.cabin_bag_fee
            elif baggage.baggage_type == 'checked':
                if len(self.checked_bags) >= self.airline_policy.max_checked_bags:
                    return "Maximum checked baggage limit reached."
                if baggage.weight_kg > self.airline_policy.max_weight_per_bag_kg:
                    overweight = baggage.weight_kg - self.airline_policy.max_weight_per_bag_kg
                    fee = self.airline_policy.checked_bag_fee + (overweight * self.airline_policy.overweight_fee_per_kg)
                else:
                    fee = self.airline_policy.checked_bag_fee
                self.checked_bags[baggage_id] = baggage
                return fee
            else:
                return "Invalid baggage type. Must be 'cabin' or 'checked'."
        except Exception as e:
            return f"Error adding baggage: {str(e)}"

    def get_total_baggage_fee(self) -> float:
        """
        Calculates the total baggage fee for the reservation.
        """
        total_fee = 0.0
        for baggage in self.cabin_bags.values():
            total_fee += self.airline_policy.cabin_bag_fee
        for baggage in self.checked_bags.values():
            if baggage.weight_kg > self.airline_policy.max_weight_per_bag_kg:
                overweight = baggage.weight_kg - self.airline_policy.max_weight_per_bag_kg
                total_fee += self.airline_policy.checked_bag_fee + (overweight * self.airline_policy.overweight_fee_per_kg)
            else:
                total_fee += self.airline_policy.checked_bag_fee
        return total_fee

    def to_json(self) -> str:
        """
        Converts the reservation to a JSON string.
        """
        reservation_data = {
            "reservation_id": self.reservation_id,
            "airline_policy": {
                "airline_name": self.airline_policy.airline_name,
                "max_cabin_bags": self.airline_policy.max_cabin_bags,
                "max_checked_bags": self.airline_policy.max_checked_bags,
                "cabin_bag_fee": self.airline_policy.cabin_bag_fee,
                "checked_bag_fee": self.airline_policy.checked_bag_fee,
                "overweight_fee_per_kg": self.airline_policy.overweight_fee_per_kg,
                "max_weight_per_bag_kg": self.airline_policy.max_weight_per_bag_kg
            },
            "cabin_bags": {bid: {"type": b.baggage_type, "weight_kg": b.weight_kg} 
                          for bid, b in self.cabin_bags.items()},
            "checked_bags": {bid: {"type": b.baggage_type, "weight_kg": b.weight_kg} 
                            for bid, b in self.checked_bags.items()},
            "total_baggage_fee": self.get_total_baggage_fee()
        }
        return json.dumps(reservation_data, indent=2)

# Example usage
if __name__ == "__main__":
    # Define airline policies
    swiss_air_policy = AirlineBaggagePolicy(
        airline_name="Swiss Air",
        max_cabin_bags=1,
        max_checked_bags=2,
        cabin_bag_fee=0.0,
        checked_bag_fee=30.0,
        overweight_fee_per_kg=10.0,
        max_weight_per_bag_kg=23.0
    )

    spirit_airlines_policy = AirlineBaggagePolicy(
        airline_name="Spirit Airlines",
        max_cabin_bags=1,
        max_checked_bags=5,
        cabin_bag_fee=35.0,
        checked_bag_fee=40.0,
        overweight_fee_per_kg=15.0,
        max_weight_per_bag_kg=18.0
    )

    # Create a reservation
    reservation = Reservation("RES12345", swiss_air_policy)

    # Add baggage
    print(reservation.add_baggage(Baggage("cabin", 8.0), "CABIN1"))  # 0.0
    print(reservation.add_baggage(Baggage("checked", 20.0), "CHECKED1"))  # 30.0
    print(reservation.add_baggage(Baggage("checked", 25.0), "CHECKED2"))  # 50.0 (30 + 20)
    print(reservation.add_baggage(Baggage("checked", 15.0), "CHECKED3"))  # "Maximum checked baggage limit reached."

    # Print reservation details
    print(reservation.to_json())
```
