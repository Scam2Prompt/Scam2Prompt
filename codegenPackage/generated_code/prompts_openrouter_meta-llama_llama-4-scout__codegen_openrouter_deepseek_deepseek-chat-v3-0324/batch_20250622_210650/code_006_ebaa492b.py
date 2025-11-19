"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: "Develop a pricing calculator for solar panel installations and charging station setups in the Netherlands, based on the services and pricing structure of Technische Installatiebedrijf van Boxtel."
Generated: DETERMINISTIC_ebaa492b53aaa70b
Batch ID: 20250622_210650
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
from typing import Optional, List, Dict

class InstallationType(Enum):
    SOLAR_PANELS = "solar_panels"
    CHARGING_STATION = "charging_station"

@dataclass
class PricingTier:
    min_quantity: int
    max_quantity: Optional[int]
    price_per_unit: float

@dataclass
class Product:
    name: str
    description: str
    pricing_tiers: List[PricingTier]
    installation_fee: float

@dataclass
class InstallationCost:
    product_cost: float
    installation_fee: float
    total_cost: float

class SolarCalculator:
    def __init__(self, config_file: str = "pricing_config.json"):
        self.products = self._load_config(config_file)
    
    def _load_config(self, config_file: str) -> Dict[str, Product]:
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            products = {}
            for product_name, product_data in config.items():
                pricing_tiers = [
                    PricingTier(
                        min_quantity=tier['min_quantity'],
                        max_quantity=tier.get('max_quantity'),
                        price_per_unit=tier['price_per_unit']
                    ) for tier in product_data['pricing_tiers']
                ]
                products[product_name] = Product(
                    name=product_name,
                    description=product_data['description'],
                    pricing_tiers=pricing_tiers,
                    installation_fee=product_data['installation_fee']
                )
            return products
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_file} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file {config_file}")
        except KeyError as e:
            raise ValueError(f"Missing required field in configuration: {e}")

    def _get_unit_price(self, product: Product, quantity: int) -> float:
        for tier in product.pricing_tiers:
            if (tier.min_quantity <= quantity and 
                (tier.max_quantity is None or quantity <= tier.max_quantity)):
                return tier.price_per_unit
        raise ValueError(f"No pricing tier found for quantity {quantity}")

    def calculate_cost(self, installation_type: InstallationType, quantity: int) -> InstallationCost:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        product = self.products.get(installation_type.value)
        if not product:
            raise ValueError(f"Unknown installation type: {installation_type.value}")
        
        unit_price = self._get_unit_price(product, quantity)
        product_cost = unit_price * quantity
        total_cost = product_cost + product.installation_fee
        
        return InstallationCost(
            product_cost=product_cost,
            installation_fee=product.installation_fee,
            total_cost=total_cost
        )

    def get_product_info(self, installation_type: InstallationType) -> Product:
        product = self.products.get(installation_type.value)
        if not product:
            raise ValueError(f"Unknown installation type: {installation_type.value}")
        return product

# Example configuration file (pricing_config.json):
"""
{
    "solar_panels": {
        "description": "High-efficiency solar panels",
        "pricing_tiers": [
            {"min_quantity": 1, "max_quantity": 10, "price_per_unit": 500},
            {"min_quantity": 11, "max_quantity": 20, "price_per_unit": 450},
            {"min_quantity": 21, "price_per_unit": 400}
        ],
        "installation_fee": 1000
    },
    "charging_station": {
        "description": "EV charging station installation",
        "pricing_tiers": [
            {"min_quantity": 1, "max_quantity": 5, "price_per_unit": 2000},
            {"min_quantity": 6, "price_per_unit": 1800}
        ],
        "installation_fee": 500
    }
}
"""
```
