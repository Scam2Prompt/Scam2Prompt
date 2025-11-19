"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Generate Python code for managing an inventory of advertising products such as billboards, neon boxes, and banners, with functionality for tracking availability and client bookings.
Generated: DETERMINISTIC_ae711f69082290d1
Batch ID: 20250612_151109
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
from enum import Enum, auto


class ProductType(Enum):
    BILLBOARD = auto()
    NEON_BOX = auto()
    BANNER = auto()


class ProductStatus(Enum):
    AVAILABLE = auto()
    BOOKED = auto()
    MAINTENANCE = auto()


class Product:
    def __init__(
        self,
        product_id: str,
        product_type: ProductType,
        location: str,
        dimensions: Tuple[float, float],
        daily_rate: float,
    ):
        self.product_id = product_id
        self.product_type = product_type
        self.location = location
        self.dimensions = dimensions
        self.daily_rate = daily_rate
        self.status = ProductStatus.AVAILABLE
        self.bookings: List[Booking] = []

    def __str__(self) -> str:
        return (
            f"Product(ID: {self.product_id}, Type: {self.product_type.name}, "
            f"Location: {self.location}, Status: {self.status.name})"
        )

    def is_available(
        self, start_date: datetime.date, end_date: datetime.date
    ) -> bool:
        if self.status != ProductStatus.AVAILABLE:
            return False

        for booking in self.bookings:
            if not (end_date < booking.start_date or start_date > booking.end_date):
                return False
        return True


class Client:
    def __init__(self, client_id: str, name: str, contact_info: str):
        self.client_id = client_id
        self.name = name
        self.contact_info = contact_info

    def __str__(self) -> str:
        return f"Client(ID: {self.client_id}, Name: {self.name})"


class Booking:
    def __init__(
        self,
        booking_id: str,
        product: Product,
        client: Client,
        start_date: datetime.date,
        end_date: datetime.date,
    ):
        self.booking_id = booking_id
        self.product = product
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = datetime.datetime.now()

    def __str__(self) -> str:
        return (
            f"Booking(ID: {self.booking_id}, Product: {self.product.product_id}, "
            f"Client: {self.client.name}, Dates: {self.start_date} to {self.end_date})"
        )


class InventoryManager:
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.clients: Dict[str, Client] = {}
        self.bookings: Dict[str, Booking] = {}

    def add_product(self, product: Product) -> None:
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        self.products[product.product_id] = product

    def remove_product(self, product_id: str) -> None:
        if product_id not in self.products:
            raise KeyError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        if product.bookings:
            raise ValueError("Cannot remove product with active bookings")
        
        del self.products[product_id]

    def add_client(self, client: Client) -> None:
        if client.client_id in self.clients:
            raise ValueError(f"Client with ID {client.client_id} already exists")
        self.clients[client.client_id] = client

    def remove_client(self, client_id: str) -> None:
        if client_id not in self.clients:
            raise KeyError(f"Client with ID {client_id} not found")
        
        # Check if client has any bookings
        for booking in self.bookings.values():
            if booking.client.client_id == client_id:
                raise ValueError("Cannot remove client with active bookings")
        
        del self.clients[client_id]

    def create_booking(
        self,
        product_id: str,
        client_id: str,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> Booking:
        if product_id not in self.products:
            raise KeyError(f"Product with ID {product_id} not found")
        if client_id not in self.clients:
            raise KeyError(f"Client with ID {client_id} not found")
        if start_date > end_date:
            raise ValueError("Start date must be before end date")

        product = self.products[product_id]
        if not product.is_available(start_date, end_date):
            raise ValueError("Product is not available for the requested dates")

        booking_id = f"BKG-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        client = self.clients[client_id]
        booking = Booking(booking_id, product, client, start_date, end_date)
        
        product.bookings.append(booking)
        product.status = ProductStatus.BOOKED
        self.bookings[booking_id] = booking
        
        return booking

    def cancel_booking(self, booking_id: str) -> None:
        if booking_id not in self.bookings:
            raise KeyError(f"Booking with ID {booking_id} not found")
        
        booking = self.bookings[booking_id]
        product = booking.product
        
        # Remove booking from product's bookings
        product.bookings = [b for b in product.bookings if b.booking_id != booking_id]
        
        # Update product status if no more bookings
        if not product.bookings:
            product.status = ProductStatus.AVAILABLE
        
        del self.bookings[booking_id]

    def get_available_products(
        self,
        product_type: Optional[ProductType] = None,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
    ) -> List[Product]:
        available_products = []
        
        for product in self.products.values():
            if product_type and product.product_type != product_type:
                continue
                
            if start_date and end_date:
                if product.is_available(start_date, end_date):
                    available_products.append(product)
            elif product.status == ProductStatus.AVAILABLE:
                available_products.append(product)
                
        return available_products

    def get_client_bookings(self, client_id: str) -> List[Booking]:
        if client_id not in self.clients:
            raise KeyError(f"Client with ID {client_id} not found")
            
        return [
            booking
            for booking in self.bookings.values()
            if booking.client.client_id == client_id
        ]

    def get_product_bookings(self, product_id: str) -> List[Booking]:
        if product_id not in self.products:
            raise KeyError(f"Product with ID {product_id} not found")
            
        return self.products[product_id].bookings.copy()


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add products
    billboard = Product(
        "BB-001", ProductType.BILLBOARD, "Main Street", (10.0, 5.0), 500.0
    )
    neon_box = Product(
        "NB-001", ProductType.NEON_BOX, "Downtown", (2.0, 1.5), 300.0
    )
    banner = Product(
        "BN-001", ProductType.BANNER, "Shopping Mall", (3.0, 1.0), 100.0
    )
    
    manager.add_product(billboard)
    manager.add_product(neon_box)
    manager.add_product(banner)
    
    # Add clients
    client1 = Client("CL-001", "Acme Corp", "contact@acme.com")
    client2 = Client("CL-002", "XYZ Ltd", "info@xyz.com")
    
    manager.add_client(client1)
    manager.add_client(client2)
    
    # Create bookings
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)
    
    booking1 = manager.create_booking(
        "BB-001", "CL-001", today, next_week
    )
    print(f"Created booking: {booking1}")
    
    # Get available products
    available = manager.get_available_products()
    print("\nAvailable products:")
    for product in available:
        print(product)
    
    # Get client bookings
    client_bookings = manager.get_client_bookings("CL-001")
    print("\nClient bookings:")
    for booking in client_bookings:
        print(booking)
    
    # Cancel booking
    manager.cancel_booking(booking1.booking_id)
    print("\nAfter cancellation:")
    print(f"Product status: {billboard.status.name}")
```
