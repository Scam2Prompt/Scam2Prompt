"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Write code to calculate lead times and minimize delays in the supply chain for products such as turbines, instrumentation equipment, and plumbing materials, inspired by Cedar International Inc.'s logistics approach.
Generated: DETERMINISTIC_98420a83f4979637
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Optional, Tuple
from enum import Enum
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProductCategory(Enum):
    TURBINE = "Turbine"
    INSTRUMENTATION = "Instrumentation Equipment"
    PLUMBING = "Plumbing Materials"

class Supplier:
    def __init__(self, name: str, reliability_score: float, avg_lead_time: int):
        self.name = name
        self.reliability_score = reliability_score  # 0.0 to 1.0
        self.avg_lead_time = avg_lead_time  # in days

class Product:
    def __init__(
        self,
        id: str,
        name: str,
        category: ProductCategory,
        suppliers: List[Supplier],
        current_stock: int,
        reorder_point: int
    ):
        self.id = id
        self.name = name
        self.category = category
        self.suppliers = suppliers
        self.current_stock = current_stock
        self.reorder_point = reorder_point

class Order:
    def __init__(
        self,
        order_id: str,
        product: Product,
        supplier: Supplier,
        quantity: int,
        order_date: datetime.date,
        estimated_delivery_date: datetime.date
    ):
        self.order_id = order_id
        self.product = product
        self.supplier = supplier
        self.quantity = quantity
        self.order_date = order_date
        self.estimated_delivery_date = estimated_delivery_date
        self.actual_delivery_date: Optional[datetime.date] = None

class SupplyChainManager:
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.orders: Dict[str, Order] = {}
        self.historical_data: List[Dict] = []

    def add_product(self, product: Product) -> None:
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product
        logger.info(f"Added product: {product.name} ({product.id})")

    def place_order(
        self,
        product_id: str,
        supplier_name: str,
        quantity: int,
        order_date: Optional[datetime.date] = None
    ) -> Order:
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        supplier = next((s for s in product.suppliers if s.name == supplier_name), None)
        
        if not supplier:
            raise ValueError(f"Supplier {supplier_name} not found for product {product_id}")
        
        if not order_date:
            order_date = datetime.date.today()
        
        lead_time = self.calculate_adjusted_lead_time(supplier)
        estimated_delivery = order_date + datetime.timedelta(days=lead_time)
        
        order_id = f"ORD-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        order = Order(
            order_id=order_id,
            product=product,
            supplier=supplier,
            quantity=quantity,
            order_date=order_date,
            estimated_delivery_date=estimated_delivery
        )
        
        self.orders[order_id] = order
        logger.info(f"Placed order {order_id} for {quantity} units of {product.name}")
        
        return order

    def record_delivery(self, order_id: str, delivery_date: datetime.date) -> None:
        if order_id not in self.orders:
            raise ValueError(f"Order {order_id} not found")
        
        order = self.orders[order_id]
        order.actual_delivery_date = delivery_date
        
        # Update product stock
        order.product.current_stock += order.quantity
        logger.info(f"Recorded delivery for order {order_id}. New stock: {order.product.current_stock}")
        
        # Record historical data for analysis
        delay_days = (delivery_date - order.estimated_delivery_date).days
        self.historical_data.append({
            "order_id": order_id,
            "product_id": order.product.id,
            "supplier": order.supplier.name,
            "estimated_lead_time": (order.estimated_delivery_date - order.order_date).days,
            "actual_lead_time": (delivery_date - order.order_date).days,
            "delay_days": max(0, delay_days),
            "quantity": order.quantity
        })

    def calculate_adjusted_lead_time(self, supplier: Supplier) -> int:
        """Calculate lead time adjusted for supplier reliability"""
        base_lead_time = supplier.avg_lead_time
        reliability_factor = 1 + (1 - supplier.reliability_score)  # Less reliable = longer lead time
        return int(base_lead_time * reliability_factor)

    def get_optimal_supplier(self, product_id: str) -> Tuple[Supplier, int]:
        """Determine the optimal supplier based on reliability and lead time"""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        if not product.suppliers:
            raise ValueError(f"No suppliers available for product {product_id}")
        
        # Score each supplier (lower score is better)
        scored_suppliers = []
        for supplier in product.suppliers:
            adjusted_lead_time = self.calculate_adjusted_lead_time(supplier)
            score = adjusted_lead_time * (1 - supplier.reliability_score)
            scored_suppliers.append((supplier, score, adjusted_lead_time))
        
        # Sort by score and return the best option
        scored_suppliers.sort(key=lambda x: x[1])
        best_supplier, _, adjusted_lead_time = scored_suppliers[0]
        
        return best_supplier, adjusted_lead_time

    def check_inventory_and_reorder(self) -> List[Order]:
        """Check all products and automatically reorder if below reorder point"""
        new_orders = []
        
        for product in self.products.values():
            if product.current_stock <= product.reorder_point:
                try:
                    supplier, lead_time = self.get_optimal_supplier(product.id)
                    order_quantity = product.reorder_point * 2  # Example: order double the reorder point
                    order = self.place_order(
                        product_id=product.id,
                        supplier_name=supplier.name,
                        quantity=order_quantity
                    )
                    new_orders.append(order)
                    logger.info(f"Auto-reordered {order_quantity} units of {product.name} from {supplier.name}")
                except Exception as e:
                    logger.error(f"Failed to auto-reorder {product.name}: {str(e)}")
        
        return new_orders

    def calculate_average_lead_time(self, product_id: Optional[str] = None, supplier_name: Optional[str] = None) -> float:
        """Calculate average lead time from historical data with optional filters"""
        filtered_data = self.historical_data
        
        if product_id:
            filtered_data = [d for d in filtered_data if d["product_id"] == product_id]
        
        if supplier_name:
            filtered_data = [d for d in filtered_data if d["supplier"] == supplier_name]
        
        if not filtered_data:
            logger.warning("No historical data available for the given filters")
            return 0.0
        
        total_lead_time = sum(d["actual_lead_time"] for d in filtered_data)
        return total_lead_time / len(filtered_data)

    def calculate_delay_percentage(self) -> float:
        """Calculate percentage of orders that were delayed"""
        if not self.historical_data:
            return 0.0
        
        delayed_orders = sum(1 for d in self.historical_data if d["delay_days"] > 0)
        return (delayed_orders / len(self.historical_data)) * 100

# Example usage
if __name__ == "__main__":
    # Initialize supply chain manager
    scm = SupplyChainManager()
    
    # Create suppliers
    turbine_suppliers = [
        Supplier("TurbineCo", 0.9, 30),
        Supplier("PowerParts", 0.7, 25)
    ]
    
    inst_suppliers = [
        Supplier("PrecisionInstruments", 0.95, 15),
        Supplier("MeasureTech", 0.8, 10)
    ]
    
    plumbing_suppliers = [
        Supplier("PipeMasters", 0.85, 7),
        Supplier("AquaSupply", 0.75, 5)
    ]
    
    # Add products
    scm.add_product(Product(
        id="TURB-001",
        name="High-Efficiency Turbine",
        category=ProductCategory.TURBINE,
        suppliers=turbine
