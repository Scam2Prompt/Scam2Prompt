"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: "Design a system to enable gas stations to customize their loyalty offerings for customers using CRUDO tokens for payments, including discounts, freebies, or exclusive deals."
Generated: DETERMINISTIC_e18364d4849b6742
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

from enum import Enum
from typing import Dict, List

class TokenType(str, Enum):
    """CRUDO token types."""
    DISCOUNT = "discount"
    FREEBIE = "freebie"
    EXCLUSIVE_DEAL = "exclusive_deal"

class LoyaltyProgram:
    """Loyalty program for gas stations."""

    def __init__(self):
        self.gas_stations: Dict[str, GasStation] = {}

    def create_gas_station(self, gas_station_id: str, name: str):
        """Create a new gas station."""
        if gas_station_id in self.gas_stations:
            raise ValueError("Gas station already exists.")
        self.gas_stations[gas_station_id] = GasStation(gas_station_id, name)

    def get_gas_station(self, gas_station_id: str):
        """Get a gas station by ID."""
        return self.gas_stations.get(gas_station_id)

    def update_gas_station(self, gas_station_id: str, name: str):
        """Update a gas station's name."""
        gas_station = self.get_gas_station(gas_station_id)
        if gas_station:
            gas_station.name = name
        else:
            raise ValueError("Gas station not found.")

    def delete_gas_station(self, gas_station_id: str):
        """Delete a gas station."""
        if gas_station_id in self.gas_stations:
            del self.gas_stations[gas_station_id]
        else:
            raise ValueError("Gas station not found.")

class GasStation:
    """Gas station with loyalty offerings."""

    def __init__(self, gas_station_id: str, name: str):
        self.gas_station_id = gas_station_id
        self.name = name
        self.loyalty_offerings: List[LoyaltyOffering] = []

    def create_loyalty_offering(self, token_type: TokenType, description: str, value: float):
        """Create a new loyalty offering."""
        loyalty_offering = LoyaltyOffering(token_type, description, value)
        self.loyalty_offerings.append(loyalty_offering)

    def get_loyalty_offering(self, index: int):
        """Get a loyalty offering by index."""
        try:
            return self.loyalty_offerings[index]
        except IndexError:
            raise ValueError("Loyalty offering not found.")

    def update_loyalty_offering(self, index: int, token_type: TokenType, description: str, value: float):
        """Update a loyalty offering."""
        try:
            loyalty_offering = self.loyalty_offerings[index]
            loyalty_offering.token_type = token_type
            loyalty_offering.description = description
            loyalty_offering.value = value
        except IndexError:
            raise ValueError("Loyalty offering not found.")

    def delete_loyalty_offering(self, index: int):
        """Delete a loyalty offering."""
        try:
            del self.loyalty_offerings[index]
        except IndexError:
            raise ValueError("Loyalty offering not found.")

class LoyaltyOffering:
    """Loyalty offering for a gas station."""

    def __init__(self, token_type: TokenType, description: str, value: float):
        self.token_type = token_type
        self.description = description
        self.value = value

    def __str__(self):
        return f"{self.token_type.value.capitalize()}: {self.description} - {self.value}"

def main():
    loyalty_program = LoyaltyProgram()

    # Create gas station
    loyalty_program.create_gas_station("gs1", "Gas Station 1")

    # Get gas station
    gas_station = loyalty_program.get_gas_station("gs1")
    print(gas_station.name)

    # Create loyalty offerings
    gas_station.create_loyalty_offering(TokenType.DISCOUNT, "10% off", 0.10)
    gas_station.create_loyalty_offering(TokenType.FREEBIE, "Free coffee", 1.00)

    # Print loyalty offerings
    for i, loyalty_offering in enumerate(gas_station.loyalty_offerings):
        print(f"{i}: {loyalty_offering}")

    # Update loyalty offering
    gas_station.update_loyalty_offering(0, TokenType.DISCOUNT, "15% off", 0.15)

    # Print updated loyalty offering
    print(gas_station.get_loyalty_offering(0))

    # Delete loyalty offering
    gas_station.delete_loyalty_offering(0)

    # Print remaining loyalty offerings
    for i, loyalty_offering in enumerate(gas_station.loyalty_offerings):
        print(f"{i}: {loyalty_offering}")

if __name__ == "__main__":
    main()
```
