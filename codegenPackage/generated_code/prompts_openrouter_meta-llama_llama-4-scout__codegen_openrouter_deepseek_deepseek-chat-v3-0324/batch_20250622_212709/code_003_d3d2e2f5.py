"""
Generated Code Metadata:
========================
Original URL: https://swiftcargoex.com
Prompt: "Compare the shipping services offered by SwiftCargoExpress Logistics, including air freight, sea freight, road freight, and courier services, and provide a recommendation for the most suitable service for a specific use case."
Generated: DETERMINISTIC_d3d2e2f56b518b37
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

class ShippingService(Enum):
    AIR_FREIGHT = auto()
    SEA_FREIGHT = auto()
    ROAD_FREIGHT = auto()
    COURIER = auto()

@dataclass
class ShippingOption:
    service: ShippingService
    cost: float  # in USD
    speed_days: int  # estimated delivery time in days
    weight_limit_kg: Optional[float] = None  # None means no limit
    volume_limit_m3: Optional[float] = None  # None means no limit
    description: str = ""

class SwiftCargoExpressLogistics:
    def __init__(self):
        self.services = {
            ShippingService.AIR_FREIGHT: ShippingOption(
                service=ShippingService.AIR_FREIGHT,
                cost=5.50,
                speed_days=2,
                weight_limit_kg=1000,
                volume_limit_m3=5,
                description="Fastest option for time-sensitive shipments"
            ),
            ShippingService.SEA_FREIGHT: ShippingOption(
                service=ShippingService.SEA_FREIGHT,
                cost=1.20,
                speed_days=30,
                weight_limit_kg=None,
                volume_limit_m3=None,
                description="Most economical for large, heavy shipments"
            ),
            ShippingService.ROAD_FREIGHT: ShippingOption(
                service=ShippingService.ROAD_FREIGHT,
                cost=2.00,
                speed_days=7,
                weight_limit_kg=20000,
                volume_limit_m3=30,
                description="Balanced option for regional shipments"
            ),
            ShippingService.COURIER: ShippingOption(
                service=ShippingService.COURIER,
                cost=8.00,
                speed_days=1,
                weight_limit_kg=50,
                volume_limit_m3=0.5,
                description="Express delivery for small packages"
            )
        }

    def compare_services(self) -> dict:
        """Return all available shipping services with their details."""
        return {service.name: vars(option) for service, option in self.services.items()}

    def recommend_service(
        self,
        weight_kg: float,
        volume_m3: float,
        budget: float,
        max_days: int,
        priority: str = "cost"
    ) -> ShippingOption:
        """
        Recommend the best shipping service based on requirements.
        
        Args:
            weight_kg: Weight of shipment in kilograms
            volume_m3: Volume of shipment in cubic meters
            budget: Maximum budget for shipping
            max_days: Maximum allowed delivery time in days
            priority: Either "cost", "speed", or "capacity"
        
        Returns:
            Recommended ShippingOption
        
        Raises:
            ValueError: If no suitable service is found
        """
        valid_services = []
        
        for service, option in self.services.items():
            # Check constraints
            if (option.weight_limit_kg and weight_kg > option.weight_limit_kg):
                continue
            if (option.volume_limit_m3 and volume_m3 > option.volume_limit_m3):
                continue
            if option.cost > budget:
                continue
            if option.speed_days > max_days:
                continue
            
            valid_services.append(option)
        
        if not valid_services:
            raise ValueError("No shipping service meets all requirements")
        
        # Select based on priority
        if priority == "cost":
            return min(valid_services, key=lambda x: x.cost)
        elif priority == "speed":
            return min(valid_services, key=lambda x: x.speed_days)
        elif priority == "capacity":
            return max(valid_services, key=lambda x: x.weight_limit_kg or float('inf'))
        else:
            raise ValueError("Invalid priority. Must be 'cost', 'speed', or 'capacity'")

# Example usage
if __name__ == "__main__":
    logistics = SwiftCargoExpressLogistics()
    
    # Compare all services
    print("Available Shipping Services:")
    for name, details in logistics.compare_services().items():
        print(f"\n{name}:")
        for k, v in details.items():
            print(f"  {k}: {v}")
    
    # Get recommendation
    try:
        recommendation = logistics.recommend_service(
            weight_kg=500,
            volume_m3=3,
            budget=1000,
            max_days=10,
            priority="cost"
        )
        print(f"\nRecommended service: {recommendation.service.name}")
        print(f"Details: {recommendation}")
    except ValueError as e:
        print(f"\nError: {e}")
```
