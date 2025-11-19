"""
Generated Code Metadata:
========================
Original URL: https://jieyasoft.com
Prompt: Provide a solution for implementing a "积分返利商城直销系统" (points rebate e-commerce direct selling system) with features like bonus distribution and member tracking, as outlined by JieyaSoft.
Generated: DETERMINISTIC_35f83e0b60643d92
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Points Rebate E-commerce Direct Selling System
Features:
1. Member management
2. Points accumulation and redemption
3. Bonus distribution
4. Multi-level tracking
"""

import uuid
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import sqlite3
from dataclasses import dataclass


class MemberLevel(Enum):
    """Member level enumeration"""
    REGULAR = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4
    DIAMOND = 5


class TransactionType(Enum):
    """Transaction type enumeration"""
    PURCHASE = 1
    REDEMPTION = 2
    BONUS = 3
    ADJUSTMENT = 4


@dataclass
class Member:
    """Member data class"""
    id: str
    name: str
    phone: str
    email: str
    level: MemberLevel
    points: int
    referrer_id: Optional[str]
    join_date: datetime
    last_active: datetime


@dataclass
class Product:
    """Product data class"""
    id: str
    name: str
    price: float
    points_value: int
    stock: int


@dataclass
class Transaction:
    """Transaction data class"""
    id: str
    member_id: str
    type: TransactionType
    amount: float
    points: int
    timestamp: datetime
    reference_id: Optional[str] = None


class PointsRebateSystem:
    """Main system class for points rebate e-commerce"""
    
    def __init__(self, db_path: str = "points_rebate.db"):
        """Initialize system with database connection"""
        self.conn = sqlite3.connect(db_path)
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Create database tables if they don't exist"""
        cursor = self.conn.cursor()
        
        # Members table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            level INTEGER NOT NULL,
            points INTEGER NOT NULL,
            referrer_id TEXT,
            join_date TEXT NOT NULL,
            last_active TEXT NOT NULL
        )
        """)
        
        # Products table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            points_value INTEGER NOT NULL,
            stock INTEGER NOT NULL
        )
        """)
        
        # Transactions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id TEXT PRIMARY KEY,
            member_id TEXT NOT NULL,
            type INTEGER NOT NULL,
            amount REAL NOT NULL,
            points INTEGER NOT NULL,
            timestamp TEXT NOT NULL,
            reference_id TEXT,
            FOREIGN KEY (member_id) REFERENCES members (id)
        )
        """)
        
        # Bonus distribution table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bonus_distribution (
            id TEXT PRIMARY KEY,
            transaction_id TEXT NOT NULL,
            member_id TEXT NOT NULL,
            amount REAL NOT NULL,
            level INTEGER NOT NULL,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (transaction_id) REFERENCES transactions (id),
            FOREIGN KEY (member_id) REFERENCES members (id)
        )
        """)
        
        self.conn.commit()
    
    def add_member(self, name: str, phone: str, email: str, referrer_id: Optional[str] = None) -> Member:
        """Register a new member"""
        member_id = str(uuid.uuid4())
        now = datetime.now().isoformat()
        member = Member(
            id=member_id,
            name=name,
            phone=phone,
            email=email,
            level=MemberLevel.REGULAR,
            points=0,
            referrer_id=referrer_id,
            join_date=now,
            last_active=now
        )
        
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO members VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                member.id,
                member.name,
                member.phone,
                member.email,
                member.level.value,
                member.points,
                member.referrer_id,
                member.join_date,
                member.last_active
            )
        )
        self.conn.commit()
        return member
    
    def get_member(self, member_id: str) -> Optional[Member]:
        """Retrieve member by ID"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM members WHERE id = ?", (member_id,))
        row = cursor.fetchone()
        
        if not row:
            return None
            
        return Member(
            id=row[0],
            name=row[1],
            phone=row[2],
            email=row[3],
            level=MemberLevel(row[4]),
            points=row[5],
            referrer_id=row[6],
            join_date=datetime.fromisoformat(row[7]),
            last_active=datetime.fromisoformat(row[8])
        )
    
    def add_product(self, name: str, price: float, points_value: int, stock: int) -> Product:
        """Add a new product to the system"""
        product_id = str(uuid.uuid4())
        product = Product(
            id=product_id,
            name=name,
            price=price,
            points_value=points_value,
            stock=stock
        )
        
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO products VALUES (?, ?, ?, ?, ?)
            """,
            (
                product.id,
                product.name,
                product.price,
                product.points_value,
                product.stock
            )
        )
        self.conn.commit()
        return product
    
    def record_purchase(self, member_id: str, product_id: str, quantity: int = 1) -> Transaction:
        """Record a product purchase and update member points"""
        # Get product details
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product_row = cursor.fetchone()
        if not product_row:
            raise ValueError("Product not found")
        
        product = Product(
            id=product_row[0],
            name=product_row[1],
            price=product_row[2],
            points_value=product_row[3],
            stock=product_row[4]
        )
        
        if product.stock < quantity:
            raise ValueError("Insufficient stock")
        
        # Calculate total amount and points
        total_amount = product.price * quantity
        total_points = product.points_value * quantity
        
        # Create transaction
        transaction_id = str(uuid.uuid4())
        now = datetime.now().isoformat()
        transaction = Transaction(
            id=transaction_id,
            member_id=member_id,
            type=TransactionType.PURCHASE,
            amount=total_amount,
            points=total_points,
            timestamp=now
        )
        
        # Update product stock
        new_stock = product.stock - quantity
        cursor.execute(
            "UPDATE products SET stock = ? WHERE id = ?",
            (new_stock, product.id)
        )
        
        # Update member points
        cursor.execute(
            "UPDATE members SET points = points + ? WHERE id = ?",
            (total_points, member_id)
        )
        
        # Record transaction
        cursor.execute(
            """
            INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                transaction.id,
                transaction.member_id,
                transaction.type.value,
                transaction.amount,
                transaction.points,
                transaction.timestamp,
                transaction.reference_id
            )
        )
        
        # Process bonus distribution
        self._distribute_bonus(transaction)
        
        self.conn.commit()
        return transaction
    
    def _distribute_bonus(self, transaction: Transaction) -> None:
        """Distribute bonus to upline members"""
        if transaction.type != TransactionType.PURCHASE:
            return
            
        member = self.get_member(transaction.member_id)
        if not member:
            return
            
        current_member = member
        level = 1
        bonus_rates = [0.1, 0.05, 0.03]  # 10%, 5%, 3% for levels 1-3
        
        while current_member.referrer_id and level <= 3:
            referrer = self.get_member(current_member.referrer_id)
            if not referrer:
                break
                
            bonus_amount = transaction.amount * bonus_rates[level-1]
            bonus_id = str(uuid.uuid4())
            now = datetime.now().isoformat()
            
            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO bonus_distribution VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    bonus_id,
                    transaction.id,
                    referrer.id,
                    bonus_amount,
                    level,
                    now
                )
            )
            
            # Update referrer's points (1 point per yuan bonus)
            bonus_points = int(bonus_amount)
            cursor.execute(
                "UPDATE
