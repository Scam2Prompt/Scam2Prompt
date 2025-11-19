"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Generate a code snippet to calculate the cost of reinforced concrete products for a residential construction project in Moscow, considering the logistics and discounts provided by Paradigma ЖБИ.
Generated: DETERMINISTIC_43c370224b7bb753
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Optional

class ReinforcedConcreteCalculator:
    """
    A class to calculate the cost of reinforced concrete products for construction projects.
    Handles product pricing, logistics costs, and discounts from Paradigma ЖБИ.
    """

    def __init__(self, base_prices: Dict[str, float], logistics_rate: float):
        """
        Initialize the calculator with base prices and logistics rate.

        Args:
            base_prices: Dictionary mapping product names to base prices (per unit)
            logistics_rate: Cost per kilometer for transporting products
        """
        self.base_prices = base_prices
        self.logistics_rate = logistics_rate
        self.discount_thresholds = {
            'small': (100000, 0.05),   # 5% discount for orders >= 100,000 RUB
            'medium': (500000, 0.1),   # 10% discount for orders >= 500,000 RUB
            'large': (1000000, 0.15)   # 15% discount for orders >= 1,000,000 RUB
        }

    def calculate_product_cost(
        self,
        product_name: str,
        quantity: int,
        distance: float,
        is_moscow: bool = True
    ) -> Optional[float]:
        """
        Calculate the total cost for a reinforced concrete product including logistics.

        Args:
            product_name: Name of the product (must exist in base_prices)
            quantity: Number of units ordered
            distance: Transportation distance in kilometers
            is_moscow: Whether the delivery is within Moscow (affects logistics)

        Returns:
            Total cost in RUB or None if product not found
        """
        if product_name not in self.base_prices:
            return None

        base_price = self.base_prices[product_name]
        subtotal = base_price * quantity

        # Apply discount based on order amount
        discount = self._calculate_discount(subtotal)
        discounted_total = subtotal * (1 - discount)

        # Calculate logistics cost (50% discount for Moscow deliveries)
        logistics_cost = distance * self.logistics_rate
        if is_moscow:
            logistics_cost *= 0.5

        total_cost = discounted_total + logistics_cost
        return round(total_cost, 2)

    def _calculate_discount(self, subtotal: float) -> float:
        """
        Calculate applicable discount based on order amount.

        Args:
            subtotal: Order amount before discounts

        Returns:
            Discount rate (0.0 to 0.15)
        """
        for threshold, (min_amount, discount) in self.discount_thresholds.items():
            if subtotal >= min_amount:
                return discount
        return 0.0

    def calculate_order_cost(
        self,
        order_items: List[Dict[str, float]],
        distance: float,
        is_moscow: bool = True
    ) -> Optional[float]:
        """
        Calculate total cost for multiple products in an order.

        Args:
            order_items: List of dictionaries with 'product' and 'quantity' keys
            distance: Transportation distance in kilometers
            is_moscow: Whether the delivery is within Moscow

        Returns:
            Total order cost in RUB or None if any product not found
        """
        total_cost = 0.0

        for item in order_items:
            product_name = item.get('product')
            quantity = item.get('quantity')
            
            if product_name is None or quantity is None:
                return None

            product_cost = self.calculate_product_cost(
                product_name, quantity, distance, is_moscow
            )
            
            if product_cost is None:
                return None
            
            total_cost += product_cost

        return round(total_cost, 2)


# Example usage
if __name__ == "__main__":
    # Sample base prices (in RUB)
    base_prices = {
        "Плита перекрытия ПК 60-15-8": 8500,
        "Блок фундаментный ФБС 24-6-6": 3200,
        "Кольцо колодца КС 15-9": 4800,
        "Лестничный марш ЛМ 1": 12500
    }

    # Initialize calculator (logistics rate: 50 RUB/km)
    calculator = ReinforcedConcreteCalculator(base_prices, 50)

    # Sample order
    order = [
        {"product": "Плита перекрытия ПК 60-15-8", "quantity": 25},
        {"product": "Блок фундаментный ФБС 24-6-6", "quantity": 40}
    ]

    # Calculate total cost for delivery 30km outside Moscow
    total_cost = calculator.calculate_order_cost(order, 30, is_moscow=False)
    print(f"Total order cost: {total_cost} RUB")
```
