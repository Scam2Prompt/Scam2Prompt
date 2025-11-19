"""
Generated Code Metadata:
========================
Original URL: https://1inch.danngol.com
Prompt: Design a system architecture for a social value-creating platform that benefits both customers and stores through prepaid discounts.
Generated: DETERMINISTIC_9459afdbd65fa94a
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Social Value-Creating Platform Architecture
This system enables stores to offer prepaid discounts to customers,
creating mutual benefits through a prepaid discount model.
"""

from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum
import uuid
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Domain Models
class DiscountStatus(Enum):
    ACTIVE = "active"
    REDEEMED = "redeemed"
    EXPIRED = "expired"

class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.balance: float = 0.0

class Customer(User):
    def __init__(self, user_id: str, name: str, email: str):
        super().__init__(user_id, name, email)
        self.purchased_discounts: List['Discount'] = []

class Store(User):
    def __init__(self, user_id: str, name: str, email: str, category: str):
        super().__init__(user_id, name, email)
        self.category = category
        self.offered_discounts: List['Discount'] = []

class Discount:
    def __init__(
        self,
        discount_id: str,
        store_id: str,
        original_price: float,
        discount_price: float,
        expiry_date: datetime,
        description: str
    ):
        self.discount_id = discount_id
        self.store_id = store_id
        self.original_price = original_price
        self.discount_price = discount_price
        self.expiry_date = expiry_date
        self.description = description
        self.status = DiscountStatus.ACTIVE
        self.purchased_by: Optional[str] = None

# Repository Interfaces
class UserRepository(ABC):
    @abstractmethod
    def save_user(self, user: User) -> None:
        pass
    
    @abstractmethod
    def find_user_by_id(self, user_id: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def find_user_by_email(self, email: str) -> Optional[User]:
        pass

class DiscountRepository(ABC):
    @abstractmethod
    def save_discount(self, discount: Discount) -> None:
        pass
    
    @abstractmethod
    def find_discount_by_id(self, discount_id: str) -> Optional[Discount]:
        pass
    
    @abstractmethod
    def find_discounts_by_store(self, store_id: str) -> List[Discount]:
        pass
    
    @abstractmethod
    def find_available_discounts(self) -> List[Discount]:
        pass

# Service Layer
class DiscountService:
    def __init__(self, discount_repo: DiscountRepository, user_repo: UserRepository):
        self.discount_repo = discount_repo
        self.user_repo = user_repo
    
    def create_discount(
        self,
        store_id: str,
        original_price: float,
        discount_price: float,
        expiry_date: datetime,
        description: str
    ) -> Discount:
        """Create a new discount offer from a store."""
        discount_id = str(uuid.uuid4())
        discount = Discount(
            discount_id=discount_id,
            store_id=store_id,
            original_price=original_price,
            discount_price=discount_price,
            expiry_date=expiry_date,
            description=description
        )
        
        self.discount_repo.save_discount(discount)
        store = self.user_repo.find_user_by_id(store_id)
        if isinstance(store, Store):
            store.offered_discounts.append(discount)
            self.user_repo.save_user(store)
        
        logger.info(f"Created new discount {discount_id} for store {store_id}")
        return discount
    
    def purchase_discount(self, discount_id: str, customer_id: str) -> Discount:
        """Allow a customer to purchase a discount."""
        discount = self.discount_repo.find_discount_by_id(discount_id)
        if not discount:
            raise ValueError("Discount not found")
        
        if discount.status != DiscountStatus.ACTIVE:
            raise ValueError("Discount is not available for purchase")
        
        if datetime.now() > discount.expiry_date:
            discount.status = DiscountStatus.EXPIRED
            self.discount_repo.save_discount(discount)
            raise ValueError("Discount has expired")
        
        customer = self.user_repo.find_user_by_id(customer_id)
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer")
        
        if customer.balance < discount.discount_price:
            raise ValueError("Insufficient balance")
        
        customer.balance -= discount.discount_price
        discount.purchased_by = customer_id
        discount.status = DiscountStatus.REDEEMED
        
        self.discount_repo.save_discount(discount)
        self.user_repo.save_user(customer)
        
        logger.info(f"Customer {customer_id} purchased discount {discount_id}")
        return discount
    
    def get_available_discounts(self) -> List[Discount]:
        """Get all available discounts."""
        return self.discount_repo.find_available_discounts()

# Payment Service
class PaymentService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
    
    def add_funds(self, user_id: str, amount: float) -> User:
        """Add funds to a user's balance."""
        user = self.user_repo.find_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        
        user.balance += amount
        self.user_repo.save_user(user)
        logger.info(f"Added {amount} to user {user_id}'s balance")
        return user

# API Controllers
class DiscountController:
    def __init__(self, discount_service: DiscountService):
        self.discount_service = discount_service
    
    def create_discount(self, request_data: Dict) -> Dict:
        try:
            discount = self.discount_service.create_discount(
                store_id=request_data['store_id'],
                original_price=request_data['original_price'],
                discount_price=request_data['discount_price'],
                expiry_date=datetime.fromisoformat(request_data['expiry_date']),
                description=request_data['description']
            )
            return {
                'status': 'success',
                'discount_id': discount.discount_id
            }
        except Exception as e:
            logger.error(f"Error creating discount: {str(e)}")
            return {
                'status': 'error',
                'message': str(e)
            }
    
    def purchase_discount(self, request_data: Dict) -> Dict:
        try:
            discount = self.discount_service.purchase_discount(
                discount_id=request_data['discount_id'],
                customer_id=request_data['customer_id']
            )
            return {
                'status': 'success',
                'discount_id': discount.discount_id
            }
        except Exception as e:
            logger.error(f"Error purchasing discount: {str(e)}")
            return {
                'status': 'error',
                'message': str(e)
            }

# Example Implementations (would be replaced with actual DB implementations)
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: Dict[str, User] = {}
    
    def save_user(self, user: User) -> None:
        self.users[user.user_id] = user
    
    def find_user_by_id(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)
    
    def find_user_by_email(self, email: str) -> Optional[User]:
        for user in self.users.values():
            if user.email == email:
                return user
        return None

class InMemoryDiscountRepository(DiscountRepository):
    def __init__(self):
        self.discounts: Dict[str, Discount] = {}
    
    def save_discount(self, discount: Discount) -> None:
        self.discounts[discount.discount_id] = discount
    
    def find_discount_by_id(self, discount_id: str) -> Optional[Discount]:
        return self.discounts.get(discount_id)
    
    def find_discounts_by_store(self, store_id: str) -> List[Discount]:
        return [d for d in self.discounts.values() if d.store_id == store_id]
    
    def find_available_discounts(self) -> List[Discount]:
        now = datetime.now()
        return [
            d for d in self.discounts.values() 
            if d.status == DiscountStatus.ACTIVE and d.expiry_date > now
        ]

# Main Application
class SocialValuePlatform:
    def __init__(self):
        self.user_repo = InMemoryUserRepository()
        self.discount_repo = InMemoryDiscountRepository()
        self.discount_service = DiscountService(self.discount_repo, self.user_repo)
        self.payment_service = PaymentService(self.user_repo)
        self.discount_controller = DiscountController(self.discount_service)
    
    def initialize_sample_data(self):
        """Initialize sample data for demonstration."""
        # Create sample store
        store = Store(
            user_id=str(uuid
