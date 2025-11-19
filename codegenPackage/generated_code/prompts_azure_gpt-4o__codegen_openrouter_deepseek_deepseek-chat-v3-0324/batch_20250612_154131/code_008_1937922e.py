"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write a program to generate automated quotes for garage door repairs and installations, incorporating Trimatic's emphasis on tailored solutions for different types of doors.
Generated: DETERMINISTIC_1937922e0ee3c963
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, field
import random
from datetime import datetime, timedelta

class DoorType(Enum):
    """Enum representing different types of garage doors."""
    SECTIONAL = "Sectional"
    ROLLER = "Roller"
    TILT = "Tilt-Up"
    SIDE_HINGED = "Side-Hinged"
    CUSTOM = "Custom"

class RepairType(Enum):
    """Enum representing different types of repairs."""
    SPRING_REPLACEMENT = "Spring Replacement"
    OPENER_REPAIR = "Opener Repair"
    PANEL_REPLACEMENT = "Panel Replacement"
    TRACK_REALIGNMENT = "Track Realignment"
    CABLE_REPLACEMENT = "Cable Replacement"
    FULL_INSTALLATION = "Full Installation"

@dataclass
class Customer:
    """Class representing a customer."""
    name: str
    email: str
    phone: str
    address: str

@dataclass
class QuoteItem:
    """Class representing an item in a quote."""
    description: str
    quantity: int
    unit_price: float
    total_price: float = field(init=False)

    def __post_init__(self):
        self.total_price = self.quantity * self.unit_price

@dataclass
class Quote:
    """Class representing a garage door repair/installation quote."""
    customer: Customer
    door_type: DoorType
    repair_type: RepairType
    items: List[QuoteItem]
    labor_hours: float
    labor_rate: float = 75.0  # Default labor rate per hour
    emergency_fee: float = 0.0
    discount: float = 0.0
    quote_date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    expiry_date: str = field(default_factory=lambda: (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"))
    quote_id: str = field(default_factory=lambda: f"Q-{random.randint(1000, 9999)}")

    def calculate_total(self) -> float:
        """Calculate the total quote amount."""
        subtotal = sum(item.total_price for item in self.items)
        labor_cost = self.labor_hours * self.labor_rate
        total = subtotal + labor_cost + self.emergency_fee - self.discount
        return round(total, 2)

    def to_dict(self) -> Dict:
        """Convert the quote to a dictionary for serialization."""
        return {
            "quote_id": self.quote_id,
            "customer": {
                "name": self.customer.name,
                "email": self.customer.email,
                "phone": self.customer.phone,
                "address": self.customer.address
            },
            "door_type": self.door_type.value,
            "repair_type": self.repair_type.value,
            "items": [{
                "description": item.description,
                "quantity": item.quantity,
                "unit_price": item.unit_price,
                "total_price": item.total_price
            } for item in self.items],
            "labor_hours": self.labor_hours,
            "labor_rate": self.labor_rate,
            "emergency_fee": self.emergency_fee,
            "discount": self.discount,
            "total": self.calculate_total(),
            "quote_date": self.quote_date,
            "expiry_date": self.expiry_date
        }

class QuoteGenerator:
    """Class for generating garage door repair/installation quotes."""
    
    # Base prices for different door types
    DOOR_TYPE_BASE_PRICES = {
        DoorType.SECTIONAL: 1200.0,
        DoorType.ROLLER: 950.0,
        DoorType.TILT: 1100.0,
        DoorType.SIDE_HINGED: 850.0,
        DoorType.CUSTOM: 1500.0
    }
    
    # Repair type multipliers
    REPAIR_TYPE_MULTIPLIERS = {
        RepairType.SPRING_REPLACEMENT: 0.15,
        RepairType.OPENER_REPAIR: 0.25,
        RepairType.PANEL_REPLACEMENT: 0.35,
        RepairType.TRACK_REALIGNMENT: 0.20,
        RepairType.CABLE_REPLACEMENT: 0.18,
        RepairType.FULL_INSTALLATION: 1.0
    }
    
    # Standard labor hours for different repairs
    STANDARD_LABOR_HOURS = {
        RepairType.SPRING_REPLACEMENT: 2.0,
        RepairType.OPENER_REPAIR: 1.5,
        RepairType.PANEL_REPLACEMENT: 3.0,
        RepairType.TRACK_REALIGNMENT: 2.5,
        RepairType.CABLE_REPLACEMENT: 2.0,
        RepairType.FULL_INSTALLATION: 4.0
    }
    
    @classmethod
    def generate_quote_items(cls, door_type: DoorType, repair_type: RepairType) -> List[QuoteItem]:
        """Generate quote items based on door type and repair type."""
        items = []
        
        # Base door component (only for full installation)
        if repair_type == RepairType.FULL_INSTALLATION:
            base_price = cls.DOOR_TYPE_BASE_PRICES[door_type]
            items.append(QuoteItem(
                description=f"{door_type.value} Garage Door",
                quantity=1,
                unit_price=base_price
            ))
        
        # Repair-specific components
        repair_multiplier = cls.REPAIR_TYPE_MULTIPLIERS[repair_type]
        repair_base_price = cls.DOOR_TYPE_BASE_PRICES[door_type] * repair_multiplier
        
        if repair_type == RepairType.SPRING_REPLACEMENT:
            items.append(QuoteItem(
                description="Torsion Spring Replacement",
                quantity=1,
                unit_price=repair_base_price * 0.7
            ))
            items.append(QuoteItem(
                description="Spring Hardware Kit",
                quantity=1,
                unit_price=repair_base_price * 0.3
            ))
        elif repair_type == RepairType.OPENER_REPAIR:
            items.append(QuoteItem(
                description="Opener Repair Parts",
                quantity=1,
                unit_price=repair_base_price * 0.6
            ))
            items.append(QuoteItem(
                description="Opener Maintenance Kit",
                quantity=1,
                unit_price=repair_base_price * 0.4
            ))
        elif repair_type == RepairType.PANEL_REPLACEMENT:
            items.append(QuoteItem(
                description=f"Replacement Panel for {door_type.value} Door",
                quantity=1,
                unit_price=repair_base_price * 0.8
            ))
            items.append(QuoteItem(
                description="Panel Installation Hardware",
                quantity=1,
                unit_price=repair_base_price * 0.2
            ))
        elif repair_type == RepairType.TRACK_REALIGNMENT:
            items.append(QuoteItem(
                description="Track Realignment Service",
                quantity=1,
                unit_price=repair_base_price * 0.5
            ))
            items.append(QuoteItem(
                description="Track Hardware Replacement",
                quantity=1,
                unit_price=repair_base_price * 0.5
            ))
        elif repair_type == RepairType.CABLE_REPLACEMENT:
            items.append(QuoteItem(
                description="Lifting Cable Replacement",
                quantity=2,  # Typically two cables
                unit_price=repair_base_price * 0.4
            ))
            items.append(QuoteItem(
                description="Cable Installation Hardware",
                quantity=1,
                unit_price=repair_base_price * 0.2
            ))
        
        return items
    
    @classmethod
    def generate_quote(
        cls,
        customer: Customer,
        door_type: DoorType,
        repair_type: RepairType,
        emergency: bool = False,
        discount_percent: float = 0.0
    ) -> Quote:
        """Generate a complete quote for garage door service."""
        items = cls.generate_quote_items(door_type, repair_type)
        labor_hours = cls.STANDARD_LABOR_HOURS[repair_type]
        
        # Adjust labor hours for custom doors
        if door_type == DoorType.CUSTOM:
            labor_hours *= 1.5
        
        emergency_fee = 100.0 if emergency else 0.0
        discount = sum(item.total_price for item in items) * (discount_percent / 100)
        
        return Quote(
            customer=customer,
            door_type=door_type,
            repair_type=repair_type,
            items=items,
            labor_hours=labor_hours,
            emergency_fee=emergency_fee,
            discount=discount
        )

def save_quote_to_file(quote: Quote, filename: str) -> None:
    """Save a quote to a JSON file."""
    try:
        with open(filename,
