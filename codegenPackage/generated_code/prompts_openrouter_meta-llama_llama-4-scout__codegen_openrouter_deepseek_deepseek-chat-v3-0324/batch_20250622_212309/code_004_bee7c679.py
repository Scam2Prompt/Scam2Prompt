"""
Generated Code Metadata:
========================
Original URL: https://dappimport.com
Prompt: Design a system to handle wholesale sales for an e-commerce platform, including features like customized pricing, bulk order management, and automated shipping calculations for international deliveries.
Generated: DETERMINISTIC_bee7c67905fbe428
Batch ID: 20250622_212309
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.shippingprovider.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from decimal import Decimal
from typing import Dict, List, Optional, Tuple
from enum import Enum
import requests
from dataclasses import dataclass
from abc import ABC, abstractmethod


class ShippingMethod(Enum):
    STANDARD = "standard"
    EXPRESS = "express"
    PRIORITY = "priority"


class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"


@dataclass
class Product:
    id: str
    name: str
    base_price: Decimal
    description: str
    weight_kg: Decimal
    dimensions_cm: Tuple[Decimal, Decimal, Decimal]


@dataclass
class Customer:
    id: str
    name: str
    email: str
    address: str
    country: str
    tax_id: Optional[str] = None
    is_wholesale: bool = False


@dataclass
class OrderItem:
    product: Product
    quantity: int
    custom_price: Optional[Decimal] = None


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, product: Product, quantity: int) -> Decimal:
        pass


class StandardPricing(PricingStrategy):
    def calculate_price(self, product: Product, quantity: int) -> Decimal:
        return product.base_price * quantity


class BulkDiscountPricing(PricingStrategy):
    def __init__(self, discount_tiers: Dict[int, Decimal]):
        self.discount_tiers = discount_tiers

    def calculate_price(self, product: Product, quantity: int) -> Decimal:
        applicable_tier = max(
            (tier for tier in self.discount_tiers if quantity >= tier), default=None
        )
        if applicable_tier:
            discount = self.discount_tiers[applicable_tier]
            return (product.base_price * (Decimal(1) - discount)) * quantity
        return product.base_price * quantity


class ShippingCalculator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.shippingprovider.com/v1"

    def calculate_shipping(
        self,
        items: List[OrderItem],
        destination_country: str,
        shipping_method: ShippingMethod,
    ) -> Decimal:
        total_weight = sum(item.product.weight_kg * item.quantity for item in items)
        dimensions = self._calculate_total_dimensions(items)

        payload = {
            "destination": destination_country,
            "weight_kg": float(total_weight),
            "dimensions_cm": [float(d) for d in dimensions],
            "shipping_method": shipping_method.value,
        }

        try:
            response = requests.post(
                f"{self.base_url}/rates",
                json=payload,
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()
            return Decimal(str(data["total_cost"]))
        except requests.exceptions.RequestException as e:
            raise ShippingCalculationError(f"Failed to calculate shipping: {str(e)}")

    def _calculate_total_dimensions(self, items: List[OrderItem]) -> Tuple[Decimal, Decimal, Decimal]:
        # Simplified calculation - in reality would need more complex logic
        max_dimensions = [Decimal(0), Decimal(0), Decimal(0)]
        for item in items:
            for i in range(3):
                if item.product.dimensions_cm[i] > max_dimensions[i]:
                    max_dimensions[i] = item.product.dimensions_cm[i]
        return tuple(max_dimensions)


class Order:
    def __init__(
        self,
        order_id: str,
        customer: Customer,
        items: List[OrderItem],
        pricing_strategy: PricingStrategy,
        shipping_calculator: ShippingCalculator,
        currency: Currency = Currency.USD,
    ):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.pricing_strategy = pricing_strategy
        self.shipping_calculator = shipping_calculator
        self.currency = currency
        self._shipping_cost: Optional[Decimal] = None
        self._subtotal: Optional[Decimal] = None

    def calculate_subtotal(self) -> Decimal:
        subtotal = Decimal(0)
        for item in self.items:
            if item.custom_price is not None:
                subtotal += item.custom_price * item.quantity
            else:
                subtotal += self.pricing_strategy.calculate_price(item.product, item.quantity)
        self._subtotal = subtotal
        return subtotal

    def calculate_shipping(self, shipping_method: ShippingMethod) -> Decimal:
        if not self.items:
            raise ValueError("Cannot calculate shipping for empty order")
        
        self._shipping_cost = self.shipping_calculator.calculate_shipping(
            self.items,
            self.customer.country,
            shipping_method,
        )
        return self._shipping_cost

    def calculate_total(self) -> Decimal:
        if self._subtotal is None:
            self.calculate_subtotal()
        if self._shipping_cost is None:
            raise ValueError("Shipping cost not calculated")
        return self._subtotal + self._shipping_cost

    def generate_invoice(self) -> Dict:
        return {
            "order_id": self.order_id,
            "customer": {
                "name": self.customer.name,
                "email": self.customer.email,
                "address": self.customer.address,
                "country": self.customer.country,
            },
            "items": [
                {
                    "product_id": item.product.id,
                    "product_name": item.product.name,
                    "quantity": item.quantity,
                    "unit_price": str(item.custom_price if item.custom_price is not None else item.product.base_price),
                    "total_price": str(
                        item.custom_price * item.quantity
                        if item.custom_price is not None
                        else self.pricing_strategy.calculate_price(item.product, item.quantity)
                    ),
                }
                for item in self.items
            ],
            "subtotal": str(self._subtotal),
            "shipping_cost": str(self._shipping_cost),
            "total": str(self.calculate_total()),
            "currency": self.currency.value,
        }


class WholesaleOrderManager:
    def __init__(self, shipping_calculator: ShippingCalculator):
        self.shipping_calculator = shipping_calculator
        self.orders: Dict[str, Order] = {}

    def create_order(
        self,
        order_id: str,
        customer: Customer,
        items: List[OrderItem],
        pricing_strategy: PricingStrategy,
        currency: Currency = Currency.USD,
    ) -> Order:
        if order_id in self.orders:
            raise ValueError(f"Order with ID {order_id} already exists")
        
        order = Order(
            order_id=order_id,
            customer=customer,
            items=items,
            pricing_strategy=pricing_strategy,
            shipping_calculator=self.shipping_calculator,
            currency=currency,
        )
        self.orders[order_id] = order
        return order

    def get_order(self, order_id: str) -> Order:
        if order_id not in self.orders:
            raise ValueError(f"Order with ID {order_id} not found")
        return self.orders[order_id]

    def process_order(self, order_id: str, shipping_method: ShippingMethod) -> Dict:
        order = self.get_order(order_id)
        order.calculate_subtotal()
        order.calculate_shipping(shipping_method)
        return order.generate_invoice()


class ShippingCalculationError(Exception):
    pass


# Example usage
if __name__ == "__main__":
    # Setup products
    product1 = Product(
        id="prod-001",
        name="Premium Widget",
        base_price=Decimal("19.99"),
        description="High-quality widget",
        weight_kg=Decimal("0.5"),
        dimensions_cm=(Decimal("10"), Decimal("5"), Decimal("5")),
    )

    product2 = Product(
        id="prod-002",
        name="Deluxe Gadget",
        base_price=Decimal("49.99"),
        description="Advanced gadget",
        weight_kg=Decimal("1.2"),
        dimensions_cm=(Decimal("15"), Decimal("10"), Decimal("8")),
    )

    # Setup customer
    customer = Customer(
        id="cust-001",
        name="Wholesale Buyer Inc.",
        email="buyer@example.com",
        address="123 Business St, Commerce City",
        country="US",
        tax_id="US123456789",
        is_wholesale=True,
    )

    # Setup pricing strategy
    discount_tiers = {
        10: Decimal("0.05"),   # 5% discount for 10+ items
        50: Decimal("0.10"),   # 10% discount for 50+ items
        100: Decimal("0.15"),  # 15% discount for 100+ items
    }
    pricing_strategy = BulkDiscountPricing(discount_tiers)

    # Setup shipping calculator
    shipping_calculator = ShippingCalculator(api_key="your_api
