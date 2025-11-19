"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: Write a Python script to calculate the cost of a taxi ride based on the rates provided on the "Best Holidays All India" website, including options for different vehicle types like Innova Crysta, Fortuner, and Swift Desire.
Generated: DETERMINISTIC_57b9db9aef1e56ba
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


class VehicleType(Enum):
    """Enum representing different vehicle types."""
    INNOVA_CRYSTA = "Innova Crysta"
    FORTUNER = "Fortuner"
    SWIFT_DESIRE = "Swift Desire"


@dataclass
class RateCard:
    """Data class to hold rate card information for a vehicle."""
    base_fare: float
    per_km_rate: float
    min_km: float
    driver_allowance: float = 0.0


class TaxiCalculator:
    """Main class to calculate taxi fare based on vehicle type and distance."""
    
    def __init__(self):
        self.rate_cards: Dict[VehicleType, RateCard] = {
            VehicleType.INNOVA_CRYSTA: RateCard(
                base_fare=1500.0,
                per_km_rate=18.0,
                min_km=80.0,
                driver_allowance=300.0
            ),
            VehicleType.FORTUNER: RateCard(
                base_fare=1800.0,
                per_km_rate=20.0,
                min_km=80.0,
                driver_allowance=350.0
            ),
            VehicleType.SWIFT_DESIRE: RateCard(
                base_fare=1000.0,
                per_km_rate=14.0,
                min_km=80.0,
                driver_allowance=200.0
            )
        }
    
    def calculate_fare(
        self,
        vehicle_type: VehicleType,
        distance_km: float,
        tolls: Optional[float] = 0.0,
        parking: Optional[float] = 0.0
    ) -> float:
        """
        Calculate total fare for a taxi ride.
        
        Args:
            vehicle_type: Type of vehicle (from VehicleType enum)
            distance_km: Distance to travel in kilometers
            tolls: Additional toll charges (default 0)
            parking: Additional parking charges (default 0)
            
        Returns:
            Total fare for the ride
            
        Raises:
            ValueError: If distance is negative or vehicle type is invalid
        """
        if distance_km < 0:
            raise ValueError("Distance cannot be negative")
        
        try:
            rate_card = self.rate_cards[vehicle_type]
        except KeyError:
            raise ValueError(f"Invalid vehicle type: {vehicle_type}")
        
        if distance_km <= rate_card.min_km:
            total_fare = rate_card.base_fare
        else:
            extra_km = distance_km - rate_card.min_km
            total_fare = rate_card.base_fare + (extra_km * rate_card.per_km_rate)
        
        total_fare += rate_card.driver_allowance + tolls + parking
        return total_fare
    
    def get_rate_card_json(self) -> str:
        """Return rate cards in JSON format for display purposes."""
        rate_cards_dict = {
            vehicle_type.value: {
                "base_fare": rate_card.base_fare,
                "per_km_rate": rate_card.per_km_rate,
                "min_km": rate_card.min_km,
                "driver_allowance": rate_card.driver_allowance
            }
            for vehicle_type, rate_card in self.rate_cards.items()
        }
        return json.dumps(rate_cards_dict, indent=2)


def main():
    """Example usage of the TaxiCalculator."""
    calculator = TaxiCalculator()
    
    print("Available vehicles and their rates:")
    print(calculator.get_rate_card_json())
    
    try:
        vehicle = VehicleType.INNOVA_CRYSTA
        distance = 100.0
        tolls = 150.0
        parking = 50.0
        
        fare = calculator.calculate_fare(vehicle, distance, tolls, parking)
        print(f"\nFare for {distance} km in {vehicle.value}: ₹{fare:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
