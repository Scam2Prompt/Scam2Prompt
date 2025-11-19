"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Create a program to compare freight forwarding costs across air and sea modes, using Alexa Shipping's logistics solutions as a model.
Generated: DETERMINISTIC_204fb5d10826cd36
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# freight_forwarder.py

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TransportMode(Enum):
    """Transport mode enumeration"""
    AIR = "air"
    SEA = "sea"

@dataclass
class ShippingDetails:
    """Dataclass to hold shipping details"""
    weight: float  # in kg
    volume: float  # in cubic meters
    origin: str
    destination: str

class FreightForwarder:
    """Freight forwarder class to calculate costs"""
    def __init__(self):
        # Base rates for air and sea transport modes (per kg and per cubic meter)
        self.base_rates: Dict[TransportMode, Dict[str, float]] = {
            TransportMode.AIR: {"rate_per_kg": 1.50, "rate_per_cubic_meter": 200.0},
            TransportMode.SEA: {"rate_per_kg": 0.50, "rate_per_cubic_meter": 100.0},
        }

    def calculate_cost(self, transport_mode: TransportMode, shipping_details: ShippingDetails) -> float:
        """Calculate freight forwarding cost"""
        try:
            base_rate = self.base_rates[transport_mode]
            weight_cost = shipping_details.weight * base_rate["rate_per_kg"]
            volume_cost = shipping_details.volume * base_rate["rate_per_cubic_meter"]
            total_cost = weight_cost + volume_cost
            return total_cost
        except Exception as e:
            logging.error(f"Error calculating cost: {str(e)}")
            raise

    def compare_costs(self, shipping_details: ShippingDetails) -> Dict[TransportMode, float]:
        """Compare freight forwarding costs across air and sea modes"""
        try:
            costs = {}
            for transport_mode in TransportMode:
                cost = self.calculate_cost(transport_mode, shipping_details)
                costs[transport_mode] = cost
            return costs
        except Exception as e:
            logging.error(f"Error comparing costs: {str(e)}")
            raise

def main():
    # Example usage
    freight_forwarder = FreightForwarder()
    shipping_details = ShippingDetails(
        weight=1000.0,  # 1000 kg
        volume=2.0,     # 2 cubic meters
        origin="New York",
        destination="Los Angeles"
    )

    costs = freight_forwarder.compare_costs(shipping_details)
    logging.info("Freight Forwarding Costs:")
    for transport_mode, cost in costs.items():
        logging.info(f"{transport_mode.value.capitalize()}: ${cost:.2f}")

if __name__ == "__main__":
    main()
```
