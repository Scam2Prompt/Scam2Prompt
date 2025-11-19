"""
Generated Code Metadata:
========================
Original URL: https://buzo-lola.pages.dev
Prompt: "Design a library for managing Tesla Reward Programme accounts, including functions for tracking energy savings, rewards points, and redeeming rewards for Tesla products."
Generated: DETERMINISTIC_73d03cb5aae18fa4
Batch ID: 20250622_211048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tesla Reward Programme Library

This library provides functionality to manage Tesla Reward Programme accounts,
including tracking energy savings, rewards points, and redeeming rewards for Tesla products.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
import datetime
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class TeslaProduct:
    """Represents a Tesla product available for reward redemption."""
    id: str
    name: str
    description: str
    points_cost: int
    stock_quantity: int

@dataclass
class RewardTransaction:
    """Represents a reward points transaction."""
    id: str
    account_id: str
    points: int
    transaction_type: str  # 'earned' or 'redeemed'
    product_id: Optional[str] = None
    timestamp: datetime.datetime = datetime.datetime.now()

@dataclass
class EnergySavingsRecord:
    """Represents an energy savings record."""
    id: str
    account_id: str
    kwh_saved: float
    timestamp: datetime.datetime = datetime.datetime.now()

class TeslaRewardAccount:
    """Represents a Tesla Reward Programme account."""
    
    def __init__(self, account_id: str, owner_name: str):
        """
        Initialize a new Tesla Reward account.
        
        Args:
            account_id: Unique identifier for the account
            owner_name: Name of the account owner
        """
        self.account_id = account_id
        self.owner_name = owner_name
        self.points_balance = 0
        self.reward_transactions: List[RewardTransaction] = []
        self.energy_savings: List[EnergySavingsRecord] = []
        
    def add_points(self, points: int) -> bool:
        """
        Add points to the account balance.
        
        Args:
            points: Number of points to add (must be positive)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if points <= 0:
            logger.error("Points must be a positive number")
            return False
            
        self.points_balance += points
        transaction = RewardTransaction(
            id=str(uuid.uuid4()),
            account_id=self.account_id,
            points=points,
            transaction_type='earned'
        )
        self.reward_transactions.append(transaction)
        logger.info(f"Added {points} points to account {self.account_id}")
        return True
        
    def record_energy_savings(self, kwh_saved: float) -> bool:
        """
        Record energy savings in kWh.
        
        Args:
            kwh_saved: Amount of energy saved in kWh (must be positive)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if kwh_saved <= 0:
            logger.error("Energy savings must be a positive number")
            return False
            
        record = EnergySavingsRecord(
            id=str(uuid.uuid4()),
            account_id=self.account_id,
            kwh_saved=kwh_saved
        )
        self.energy_savings.append(record)
        logger.info(f"Recorded {kwh_saved} kWh savings for account {self.account_id}")
        return True
        
    def get_total_energy_savings(self) -> float:
        """Return the total energy savings in kWh."""
        return sum(record.kwh_saved for record in self.energy_savings)

class TeslaRewardProgramme:
    """Main class for managing the Tesla Reward Programme."""
    
    def __init__(self):
        self.accounts: Dict[str, TeslaRewardAccount] = {}
        self.products: Dict[str, TeslaProduct] = {}
        
    def create_account(self, owner_name: str) -> Optional[TeslaRewardAccount]:
        """
        Create a new Tesla Reward account.
        
        Args:
            owner_name: Name of the account owner
            
        Returns:
            TeslaRewardAccount: The created account, or None if failed
        """
        account_id = str(uuid.uuid4())
        account = TeslaRewardAccount(account_id, owner_name)
        self.accounts[account_id] = account
        logger.info(f"Created new account {account_id} for {owner_name}")
        return account
        
    def get_account(self, account_id: str) -> Optional[TeslaRewardAccount]:
        """
        Retrieve an account by ID.
        
        Args:
            account_id: ID of the account to retrieve
            
        Returns:
            TeslaRewardAccount: The account if found, None otherwise
        """
        return self.accounts.get(account_id)
        
    def add_product(self, name: str, description: str, points_cost: int, stock_quantity: int) -> Optional[TeslaProduct]:
        """
        Add a product to the reward catalogue.
        
        Args:
            name: Product name
            description: Product description
            points_cost: Points required to redeem
            stock_quantity: Initial stock quantity
            
        Returns:
            TeslaProduct: The created product, or None if failed
        """
        if points_cost <= 0:
            logger.error("Points cost must be positive")
            return None
        if stock_quantity < 0:
            logger.error("Stock quantity cannot be negative")
            return None
            
        product_id = str(uuid.uuid4())
        product = TeslaProduct(
            id=product_id,
            name=name,
            description=description,
            points_cost=points_cost,
            stock_quantity=stock_quantity
        )
        self.products[product_id] = product
        logger.info(f"Added product {product_id} to catalogue")
        return product
        
    def redeem_reward(self, account_id: str, product_id: str) -> bool:
        """
        Redeem a reward product using account points.
        
        Args:
            account_id: ID of the account redeeming the reward
            product_id: ID of the product to redeem
            
        Returns:
            bool: True if successful, False otherwise
        """
        account = self.get_account(account_id)
        product = self.products.get(product_id)
        
        if not account:
            logger.error(f"Account {account_id} not found")
            return False
        if not product:
            logger.error(f"Product {product_id} not found")
            return False
        if product.stock_quantity <= 0:
            logger.error(f"Product {product_id} is out of stock")
            return False
        if account.points_balance < product.points_cost:
            logger.error(f"Account {account_id} has insufficient points")
            return False
            
        # Deduct points
        account.points_balance -= product.points_cost
        
        # Record transaction
        transaction = RewardTransaction(
            id=str(uuid.uuid4()),
            account_id=account_id,
            points=product.points_cost,
            transaction_type='redeemed',
            product_id=product_id
        )
        account.reward_transactions.append(transaction)
        
        # Update product stock
        product.stock_quantity -= 1
        
        logger.info(f"Account {account_id} redeemed product {product_id}")
        return True
        
    def get_available_products(self) -> List[TeslaProduct]:
        """Return all available products (with stock > 0)."""
        return [p for p in self.products.values() if p.stock_quantity > 0]
```
