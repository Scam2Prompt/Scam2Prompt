"""
Generated Code Metadata:
========================
Original URL: https://www.vidaglobaltrade.com
Prompt: Create a program to consolidate shipments for small distributors, reducing operational costs and streamlining sourcing, as described by VIDA TRADE LLC.
Generated: DETERMINISTIC_c2430bd3aba09d19
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Shipment Consolidation Program for Small Distributors

This program helps small distributors consolidate shipments to reduce operational costs
and streamline sourcing. It provides functionality to manage suppliers, shipments,
and consolidation logic.

Key Features:
- Supplier management
- Shipment tracking
- Consolidation optimization
- Cost calculation
- Reporting

Developed for VIDA TRADE LLC
"""

import csv
import json
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Supplier:
    """Represents a supplier in the system."""
    id: str
    name: str
    contact: str
    lead_time: int  # in days
    minimum_order: float
    shipping_cost: float

@dataclass
class Product:
    """Represents a product available from suppliers."""
    sku: str
    name: str
    description: str
    unit_cost: float
    supplier_id: str

@dataclass
class Shipment:
    """Represents a shipment from a supplier."""
    id: str
    supplier_id: str
    products: Dict[str, int]  # SKU: quantity
    order_date: datetime
    estimated_delivery: datetime
    status: str  # pending, in_transit, delivered
    shipping_cost: float

class ShipmentConsolidator:
    """Main class for shipment consolidation logic."""
    
    def __init__(self):
        self.suppliers: Dict[str, Supplier] = {}
        self.products: Dict[str, Product] = {}
        self.shipments: Dict[str, Shipment] = {}
        self.pending_orders: List[Dict] = []
        
    def load_suppliers(self, file_path: str) -> bool:
        """Load suppliers from a CSV file."""
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        supplier = Supplier(
                            id=row['id'],
                            name=row['name'],
                            contact=row['contact'],
                            lead_time=int(row['lead_time']),
                            minimum_order=float(row['minimum_order']),
                            shipping_cost=float(row['shipping_cost'])
                        )
                        self.suppliers[supplier.id] = supplier
                    except (ValueError, KeyError) as e:
                        logger.error(f"Error parsing supplier data: {e}")
                        continue
            logger.info(f"Loaded {len(self.suppliers)} suppliers")
            return True
        except FileNotFoundError:
            logger.error(f"Supplier file not found: {file_path}")
            return False
        except Exception as e:
            logger.error(f"Error loading suppliers: {e}")
            return False
    
    def load_products(self, file_path: str) -> bool:
        """Load products from a CSV file."""
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        product = Product(
                            sku=row['sku'],
                            name=row['name'],
                            description=row['description'],
                            unit_cost=float(row['unit_cost']),
                            supplier_id=row['supplier_id']
                        )
                        self.products[product.sku] = product
                    except (ValueError, KeyError) as e:
                        logger.error(f"Error parsing product data: {e}")
                        continue
            logger.info(f"Loaded {len(self.products)} products")
            return True
        except FileNotFoundError:
            logger.error(f"Product file not found: {file_path}")
            return False
        except Exception as e:
            logger.error(f"Error loading products: {e}")
            return False
    
    def add_order(self, order_items: List[Dict]) -> bool:
        """Add a new order to the system."""
        try:
            for item in order_items:
                if item['sku'] not in self.products:
                    logger.error(f"Product SKU not found: {item['sku']}")
                    return False
            
            self.pending_orders.extend(order_items)
            logger.info(f"Added {len(order_items)} order items")
            return True
        except Exception as e:
            logger.error(f"Error adding order: {e}")
            return False
    
    def consolidate_shipments(self) -> List[Shipment]:
        """Consolidate pending orders into optimal shipments."""
        consolidated = []
        
        # Group by supplier
        supplier_orders: Dict[str, Dict[str, int]] = {}
        for item in self.pending_orders:
            product = self.products[item['sku']]
            supplier_id = product.supplier_id
            
            if supplier_id not in supplier_orders:
                supplier_orders[supplier_id] = {}
            
            if item['sku'] not in supplier_orders[supplier_id]:
                supplier_orders[supplier_id][item['sku']] = 0
                
            supplier_orders[supplier_id][item['sku']] += item['quantity']
        
        # Create shipments for each supplier
        for supplier_id, products in supplier_orders.items():
            if supplier_id not in self.suppliers:
                logger.warning(f"Supplier not found: {supplier_id}")
                continue
                
            supplier = self.suppliers[supplier_id]
            total_value = sum(
                self.products[sku].unit_cost * qty 
                for sku, qty in products.items()
            )
            
            # Check if minimum order is met
            if total_value < supplier.minimum_order:
                logger.info(f"Order value for supplier {supplier_id} below minimum. Adding to next consolidation.")
                continue
                
            # Create shipment
            shipment_id = f"SH-{datetime.now().strftime('%Y%m%d%H%M%S')}-{supplier_id}"
            shipment = Shipment(
                id=shipment_id,
                supplier_id=supplier_id,
                products=products,
                order_date=datetime.now(),
                estimated_delivery=datetime.now() + timedelta(days=supplier.lead_time),
                status="pending",
                shipping_cost=supplier.shipping_cost
            )
            
            consolidated.append(shipment)
            self.shipments[shipment_id] = shipment
            logger.info(f"Created shipment {shipment_id} for supplier {supplier_id}")
        
        # Clear pending orders if shipments were created
        if consolidated:
            self.pending_orders = []
            
        return consolidated
    
    def calculate_savings(self) -> Dict[str, float]:
        """Calculate potential savings from consolidation."""
        savings = {
            'total_shipments': 0,
            'total_shipping_cost': 0,
            'potential_savings': 0
        }
        
        if not self.shipments:
            return savings
            
        # Calculate actual shipping costs
        actual_shipping = sum(s.shipping_cost for s in self.shipments.values())
        
        # Estimate shipping costs without consolidation (one shipment per product)
        estimated_shipping = 0
        for shipment in self.shipments.values():
            supplier = self.suppliers[shipment.supplier_id]
            estimated_shipping += supplier.shipping_cost * len(shipment.products)
        
        savings['total_shipments'] = len(self.shipments)
        savings['total_shipping_cost'] = actual_shipping
        savings['potential_savings'] = estimated_shipping - actual_shipping
        
        return savings
    
    def generate_report(self, report_type: str = "summary") -> Optional[Dict]:
        """Generate a consolidation report."""
        if report_type == "summary":
            return {
                'total_suppliers': len(self.suppliers),
                'total_products': len(self.products),
                'total_shipments': len(self.shipments),
                'pending_orders': len(self.pending_orders),
                **self.calculate_savings()
            }
        elif report_type == "detailed":
            shipments = []
            for shipment in self.shipments.values():
                supplier = self.suppliers[shipment.supplier_id]
                shipments.append({
                    'shipment_id': shipment.id,
                    'supplier': supplier.name,
                    'order_date': shipment.order_date.isoformat(),
                    'estimated_delivery': shipment.estimated_delivery.isoformat(),
                    'products': shipment.products,
                    'shipping_cost': shipment.shipping_cost,
                    'status': shipment.status
                })
            return {
                'shipments': shipments,
                'summary': self.generate_report("summary")
            }
        else:
            logger.error(f"Invalid report type: {report_type}")
            return None
    
    def save_to_json(self, file_path: str) -> bool:
        """Save current state to JSON file."""
        try:
            data = {
                'suppliers': {s.id: s.__dict__ for s in self.suppliers.values()},
                'products': {p.sku: p.__dict__ for
