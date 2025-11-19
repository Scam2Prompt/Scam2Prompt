"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Write a code snippet for a basic e-commerce platform that sells digital products related to emotional wellness and personal development, such as Sabrina Alves' online courses and mentorship programs.
Generated: DETERMINISTIC_08ed90ea85413493
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_platform.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass
from datetime import datetime

# Define product categories
class ProductCategory(str, Enum):
    ONLINE_COURSE = "online_course"
    MENTORSHIP_PROGRAM = "mentorship_program"
    EBOOK = "ebook"
    WORKBOOK = "workbook"

# Define product status
class ProductStatus(str, Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"

# Define product data class
@dataclass
class Product:
    id: int
    name: str
    description: str
    category: ProductCategory
    status: ProductStatus
    price: float
    created_at: datetime

# Define user data class
@dataclass
class User:
    id: int
    email: str
    password: str
    name: str

# Define order data class
@dataclass
class Order:
    id: int
    user_id: int
    product_id: int
    purchase_date: datetime

# In-memory product repository
class ProductRepository:
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        self.products[product.id] = product

    def get_product(self, product_id: int) -> Product:
        return self.products.get(product_id)

    def update_product(self, product_id: int, product: Product):
        if product_id in self.products:
            self.products[product_id] = product

    def delete_product(self, product_id: int):
        if product_id in self.products:
            del self.products[product_id]

# In-memory user repository
class UserRepository:
    def __init__(self):
        self.users: Dict[int, User] = {}

    def add_user(self, user: User):
        self.users[user.id] = user

    def get_user(self, user_id: int) -> User:
        return self.users.get(user_id)

    def update_user(self, user_id: int, user: User):
        if user_id in self.users:
            self.users[user_id] = user

    def delete_user(self, user_id: int):
        if user_id in self.users:
            del self.users[user_id]

# In-memory order repository
class OrderRepository:
    def __init__(self):
        self.orders: Dict[int, Order] = {}
        self.order_id_counter = 1

    def add_order(self, order: Order):
        self.orders[self.order_id_counter] = order
        self.order_id_counter += 1

    def get_order(self, order_id: int) -> Order:
        return self.orders.get(order_id)

# E-commerce platform service
class ECommercePlatform:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.user_repository = UserRepository()
        self.order_repository = OrderRepository()

    def create_product(self, product: Product):
        self.product_repository.add_product(product)

    def get_product(self, product_id: int) -> Product:
        return self.product_repository.get_product(product_id)

    def create_user(self, user: User):
        self.user_repository.add_user(user)

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user(user_id)

    def place_order(self, user_id: int, product_id: int):
        user = self.get_user(user_id)
        product = self.get_product(product_id)

        if not user:
            raise ValueError("User not found")
        if not product:
            raise ValueError("Product not found")
        if product.status != ProductStatus.AVAILABLE:
            raise ValueError("Product is not available")

        order = Order(
            id=self.order_repository.order_id_counter,
            user_id=user_id,
            product_id=product_id,
            purchase_date=datetime.now(),
        )
        self.order_repository.add_order(order)

    def get_order(self, order_id: int) -> Order:
        return self.order_repository.get_order(order_id)

def main():
    ecommerce_platform = ECommercePlatform()

    # Create products
    product1 = Product(
        id=1,
        name="Mindfulness Online Course",
        description="Learn mindfulness techniques",
        category=ProductCategory.ONLINE_COURSE,
        status=ProductStatus.AVAILABLE,
        price=99.99,
        created_at=datetime.now(),
    )
    ecommerce_platform.create_product(product1)

    product2 = Product(
        id=2,
        name="Personal Development Mentorship Program",
        description="Get mentored by experts",
        category=ProductCategory.MENTORSHIP_PROGRAM,
        status=ProductStatus.AVAILABLE,
        price=499.99,
        created_at=datetime.now(),
    )
    ecommerce_platform.create_product(product2)

    # Create users
    user1 = User(
        id=1,
        email="user1@example.com",
        password="password123",
        name="John Doe",
    )
    ecommerce_platform.create_user(user1)

    # Place order
    ecommerce_platform.place_order(1, 1)

    # Get order
    order = ecommerce_platform.get_order(1)
    print(order)

if __name__ == "__main__":
    main()
```
