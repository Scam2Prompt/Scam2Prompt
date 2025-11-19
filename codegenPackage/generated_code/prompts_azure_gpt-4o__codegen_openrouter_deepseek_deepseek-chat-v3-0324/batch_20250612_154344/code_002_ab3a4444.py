"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Generate a script to automate customer quotes for bulk salt and UltraGLOW™ Snow and Ice Melt orders, factoring in delivery zones and product availability.
Generated: DETERMINISTIC_ab3a444480ca25ed
Batch ID: 20250612_154344
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
from enum import Enum, auto
from typing import Dict, List, Optional


class DeliveryZone(Enum):
    """Enum representing different delivery zones with their respective surcharges."""
    ZONE_1 = auto()  # Local: no surcharge
    ZONE_2 = auto()  # Regional: 10% surcharge
    ZONE_3 = auto()  # National: 20% surcharge


class ProductType(Enum):
    """Enum representing available products."""
    BULK_SALT = auto()
    ULTRAGLOW = auto()


@dataclass
class Product:
    """Class representing a product with its properties."""
    product_type: ProductType
    price_per_ton: float
    available_quantity: float  # in tons


@dataclass
class OrderItem:
    """Class representing an item in an order."""
    product_type: ProductType
    quantity: float  # in tons


@dataclass
class Quote:
    """Class representing a customer quote."""
    order_items: List[OrderItem]
    delivery_zone: DeliveryZone
    subtotal: float
    delivery_surcharge: float
    total: float


class QuoteGenerator:
    """Generates quotes for bulk salt and UltraGLOW orders."""
    
    def __init__(self, product_catalog: Dict[ProductType, Product]):
        """Initialize with a product catalog."""
        self.product_catalog = product_catalog
    
    def calculate_delivery_surcharge(self, subtotal: float, zone: DeliveryZone) -> float:
        """Calculate delivery surcharge based on zone."""
        if zone == DeliveryZone.ZONE_1:
            return 0
        elif zone == DeliveryZone.ZONE_2:
            return subtotal * 0.1
        elif zone == DeliveryZone.ZONE_3:
            return subtotal * 0.2
        else:
            raise ValueError("Invalid delivery zone")
    
    def check_availability(self, order_items: List[OrderItem]) -> bool:
        """Check if all products in the order are available in sufficient quantity."""
        for item in order_items:
            product = self.product_catalog.get(item.product_type)
            if not product or product.available_quantity < item.quantity:
                return False
        return True
    
    def generate_quote(self, order_items: List[OrderItem], delivery_zone: DeliveryZone) -> Optional[Quote]:
        """
        Generate a quote for the given order items and delivery zone.
        Returns None if products are not available.
        """
        if not self.check_availability(order_items):
            return None
        
        subtotal = sum(
            self.product_catalog[item.product_type].price_per_ton * item.quantity
            for item in order_items
        )
        
        delivery_surcharge = self.calculate_delivery_surcharge(subtotal, delivery_zone)
        total = subtotal + delivery_surcharge
        
        return Quote(
            order_items=order_items,
            delivery_zone=delivery_zone,
            subtotal=subtotal,
            delivery_surcharge=delivery_surcharge,
            total=total
        )


def load_product_catalog(file_path: str) -> Dict[ProductType, Product]:
    """Load product catalog from a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    catalog = {}
    for product_data in data['products']:
        product_type = ProductType[product_data['product_type']]
        catalog[product_type] = Product(
            product_type=product_type,
            price_per_ton=product_data['price_per_ton'],
            available_quantity=product_data['available_quantity']
        )
    return catalog


def main():
    """Main function to demonstrate quote generation."""
    try:
        # Load product catalog
        catalog = load_product_catalog('product_catalog.json')
        quote_generator = QuoteGenerator(catalog)
        
        # Example order
        order_items = [
            OrderItem(product_type=ProductType.BULK_SALT, quantity=5),
            OrderItem(product_type=ProductType.ULTRAGLOW, quantity=2)
        ]
        delivery_zone = DeliveryZone.ZONE_2
        
        # Generate quote
        quote = quote_generator.generate_quote(order_items, delivery_zone)
        
        if quote:
            print(f"Subtotal: ${quote.subtotal:.2f}")
            print(f"Delivery Surcharge: ${quote.delivery_surcharge:.2f}")
            print(f"Total: ${quote.total:.2f}")
        else:
            print("Unable to generate quote: products not available in requested quantities.")
    
    except FileNotFoundError:
        print("Error: Product catalog file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid product catalog file format.")
    except KeyError as e:
        print(f"Error: Invalid product type or missing data in catalog - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

**Example product_catalog.json:**
```json
{
    "products": [
        {
            "product_type": "BULK_SALT",
            "price_per_ton": 50.00,
            "available_quantity": 100
        },
        {
            "product_type": "ULTRAGLOW",
            "price_per_ton": 75.00,
            "available_quantity": 50
        }
    ]
}
```
