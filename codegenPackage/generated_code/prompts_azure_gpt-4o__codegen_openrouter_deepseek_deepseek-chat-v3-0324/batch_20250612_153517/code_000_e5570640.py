"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write code to simulate a logistics management system for tracking the storage and transportation of cosmetic products, referencing the full-service solutions described by Fabricare Cosméticos.
Generated: DETERMINISTIC_e5570640b9c84520
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
import uuid
from dataclasses import dataclass, field


class ProductCategory(Enum):
    SKINCARE = "Skincare"
    MAKEUP = "Makeup"
    HAIRCARE = "Haircare"
    FRAGRANCE = "Fragrance"
    PERSONAL_CARE = "Personal Care"


class StorageCondition(Enum):
    AMBIENT = "Ambient (15-25°C)"
    REFRIGERATED = "Refrigerated (2-8°C)"
    FROZEN = "Frozen (-20°C)"
    CONTROLLED_HUMIDITY = "Controlled Humidity (40-60%)"


class TransportationMode(Enum):
    TRUCK = "Truck"
    AIR = "Air"
    SEA = "Sea"
    RAIL = "Rail"


class ProductStatus(Enum):
    IN_STORAGE = "In Storage"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    DAMAGED = "Damaged"
    EXPIRED = "Expired"


@dataclass
class Product:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    category: ProductCategory
    batch_number: str
    manufacture_date: datetime.date
    expiry_date: datetime.date
    quantity: int
    storage_condition: StorageCondition
    status: ProductStatus = ProductStatus.IN_STORAGE
    location: Optional[str] = None
    last_updated: datetime.datetime = field(default_factory=datetime.datetime.now)

    def update_status(self, new_status: ProductStatus, location: Optional[str] = None):
        self.status = new_status
        if location:
            self.location = location
        self.last_updated = datetime.datetime.now()


@dataclass
class StorageFacility:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    location: str
    capacity: int
    storage_conditions: List[StorageCondition]
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product) -> bool:
        if product.storage_condition not in self.storage_conditions:
            raise ValueError(f"Facility doesn't support {product.storage_condition.value} storage")
        
        if len(self.products) >= self.capacity:
            raise ValueError("Facility at full capacity")
        
        self.products.append(product)
        product.update_status(ProductStatus.IN_STORAGE, self.location)
        return True

    def remove_product(self, product_id: str) -> Optional[Product]:
        for i, product in enumerate(self.products):
            if product.id == product_id:
                removed_product = self.products.pop(i)
                removed_product.update_status(ProductStatus.IN_TRANSIT, None)
                return removed_product
        return None


@dataclass
class Transportation:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    mode: TransportationMode
    origin: str
    destination: str
    departure_time: datetime.datetime
    estimated_arrival: datetime.datetime
    products: List[Product] = field(default_factory=list)
    status: str = "Scheduled"

    def add_product(self, product: Product) -> bool:
        if product.status != ProductStatus.IN_TRANSIT:
            raise ValueError("Product must be in transit to be added to transportation")
        
        self.products.append(product)
        product.update_status(ProductStatus.IN_TRANSIT, f"In transit via {self.mode.value}")
        return True

    def complete_transportation(self):
        self.status = "Completed"
        for product in self.products:
            product.update_status(ProductStatus.DELIVERED, self.destination)


class LogisticsSystem:
    def __init__(self):
        self.storage_facilities: Dict[str, StorageFacility] = {}
        self.transportations: Dict[str, Transportation] = {}
        self.products: Dict[str, Product] = {}

    def add_storage_facility(self, facility: StorageFacility) -> str:
        self.storage_facilities[facility.id] = facility
        return facility.id

    def add_transportation(self, transportation: Transportation) -> str:
        self.transportations[transportation.id] = transportation
        return transportation.id

    def register_product(self, product: Product) -> str:
        self.products[product.id] = product
        return product.id

    def move_product_to_storage(self, product_id: str, facility_id: str) -> bool:
        product = self.products.get(product_id)
        facility = self.storage_facilities.get(facility_id)
        
        if not product or not facility:
            return False
        
        try:
            return facility.add_product(product)
        except ValueError as e:
            print(f"Error moving product to storage: {e}")
            return False

    def prepare_product_for_transport(self, product_id: str, facility_id: str) -> bool:
        facility = self.storage_facilities.get(facility_id)
        if not facility:
            return False
        
        product = facility.remove_product(product_id)
        if not product:
            return False
        
        return True

    def add_product_to_transport(self, product_id: str, transport_id: str) -> bool:
        product = self.products.get(product_id)
        transport = self.transportations.get(transport_id)
        
        if not product or not transport:
            return False
        
        try:
            return transport.add_product(product)
        except ValueError as e:
            print(f"Error adding product to transport: {e}")
            return False

    def complete_transportation(self, transport_id: str) -> bool:
        transport = self.transportations.get(transport_id)
        if not transport:
            return False
        
        transport.complete_transportation()
        return True

    def check_product_status(self, product_id: str) -> Optional[Dict]:
        product = self.products.get(product_id)
        if not product:
            return None
        
        return {
            "id": product.id,
            "name": product.name,
            "status": product.status.value,
            "location": product.location,
            "last_updated": product.last_updated.isoformat()
        }

    def get_expired_products(self) -> List[Dict]:
        today = datetime.date.today()
        expired = []
        
        for product in self.products.values():
            if product.expiry_date < today and product.status != ProductStatus.EXPIRED:
                product.update_status(ProductStatus.EXPIRED)
                expired.append({
                    "id": product.id,
                    "name": product.name,
                    "batch_number": product.batch_number,
                    "expiry_date": product.expiry_date.isoformat()
                })
        
        return expired


# Example usage
if __name__ == "__main__":
    system = LogisticsSystem()
    
    # Create storage facilities
    warehouse = StorageFacility(
        name="Main Warehouse",
        location="São Paulo, BR",
        capacity=1000,
        storage_conditions=[StorageCondition.AMBIENT, StorageCondition.CONTROLLED_HUMIDITY]
    )
    warehouse_id = system.add_storage_facility(warehouse)
    
    # Create products
    moisturizer = Product(
        name="Hydrating Moisturizer",
        category=ProductCategory.SKINCARE,
        batch_number="BATCH-2023-001",
        manufacture_date=datetime.date(2023, 1, 15),
        expiry_date=datetime.date(2025, 1, 15),
        quantity=100,
        storage_condition=StorageCondition.AMBIENT
    )
    moisturizer_id = system.register_product(moisturizer)
    
    # Move product to storage
    system.move_product_to_storage(moisturizer_id, warehouse_id)
    
    # Check product status
    print(system.check_product_status(moisturizer_id))
    
    # Prepare for transport
    system.prepare_product_for_transport(moisturizer_id, warehouse_id)
    
    # Create transportation
    delivery = Transportation(
        mode=TransportationMode.TRUCK,
        origin="São Paulo, BR",
        destination="Rio de Janeiro, BR",
        departure_time=datetime.datetime.now(),
        estimated_arrival=datetime.datetime.now() + datetime.timedelta(days=1)
    )
    delivery_id = system.add_transportation(delivery)
    
    # Add product to transport
    system.add_product_to_transport(moisturizer_id, delivery_id)
    
    # Complete transportation
    system.complete_transportation(delivery_id)
    
    # Check product status after delivery
    print(system.check_product_status(moisturizer_id))
```
