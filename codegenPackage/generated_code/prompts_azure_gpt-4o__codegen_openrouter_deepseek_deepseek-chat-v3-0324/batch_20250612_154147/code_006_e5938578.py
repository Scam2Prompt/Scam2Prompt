"""
Generated Code Metadata:
========================
Original URL: https://availlabs.net
Prompt: Create a script to streamline procurement workflows for branded swag, focusing on maximizing ROI and reducing manual effort, inspired by Avail Labs' procurement solutions.
Generated: DETERMINISTIC_e59385782210c8a0
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Branded Swag Procurement Workflow Automation Script

This script automates and optimizes procurement workflows for branded merchandise,
focusing on maximizing ROI and reducing manual effort. It includes features for
vendor management, order tracking, cost analysis, and ROI calculation.

Key Features:
- Vendor management and comparison
- Automated order processing
- ROI calculation and reporting
- Budget tracking
- Approval workflows
"""

import csv
import json
import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='procurement.log'
)
logger = logging.getLogger(__name__)

@dataclass
class Vendor:
    """Represents a vendor for branded merchandise."""
    id: str
    name: str
    contact_email: str
    products: List[str]
    lead_time_days: int
    cost_multiplier: float
    reliability_score: float
    minimum_order: float

@dataclass
class SwagItem:
    """Represents a branded merchandise item."""
    id: str
    name: str
    description: str
    base_cost: float
    vendor_ids: List[str]
    category: str
    popularity_score: float

@dataclass
class Order:
    """Represents a procurement order."""
    order_id: str
    items: Dict[str, int]  # item_id: quantity
    vendor_id: str
    order_date: datetime.date
    expected_delivery: datetime.date
    status: str  # "pending", "approved", "shipped", "delivered", "cancelled"
    total_cost: float
    requester: str
    approval_required: bool

class ProcurementWorkflow:
    """Main class handling the procurement workflow automation."""
    
    def __init__(self):
        self.vendors: Dict[str, Vendor] = {}
        self.swag_items: Dict[str, SwagItem] = {}
        self.orders: Dict[str, Order] = {}
        self.budget: float = 0
        self.load_initial_data()
    
    def load_initial_data(self):
        """Load initial vendor and swag item data from files."""
        try:
            with open('vendors.json', 'r') as f:
                vendors_data = json.load(f)
                for vendor_data in vendors_data:
                    vendor = Vendor(**vendor_data)
                    self.vendors[vendor.id] = vendor
            
            with open('swag_items.json', 'r') as f:
                items_data = json.load(f)
                for item_data in items_data:
                    item = SwagItem(**item_data)
                    self.swag_items[item.id] = item
            
            logger.info("Initial data loaded successfully")
        except FileNotFoundError:
            logger.warning("Initial data files not found, starting with empty datasets")
        except json.JSONDecodeError:
            logger.error("Error parsing initial data files")
        except Exception as e:
            logger.error(f"Error loading initial data: {str(e)}")
    
    def add_vendor(self, vendor: Vendor):
        """Add a new vendor to the system."""
        if vendor.id in self.vendors:
            raise ValueError(f"Vendor with ID {vendor.id} already exists")
        self.vendors[vendor.id] = vendor
        logger.info(f"Added new vendor: {vendor.name}")
    
    def add_swag_item(self, item: SwagItem):
        """Add a new swag item to the system."""
        if item.id in self.swag_items:
            raise ValueError(f"Item with ID {item.id} already exists")
        self.swag_items[item.id] = item
        logger.info(f"Added new swag item: {item.name}")
    
    def create_order(self, items: Dict[str, int], requester: str, approval_required: bool = True) -> Order:
        """
        Create a new procurement order with optimal vendor selection.
        
        Args:
            items: Dictionary of item IDs and quantities
            requester: Name/email of the person requesting the order
            approval_required: Whether approval is needed before processing
            
        Returns:
            The created Order object
        """
        # Validate items
        for item_id in items:
            if item_id not in self.swag_items:
                raise ValueError(f"Invalid item ID: {item_id}")
        
        # Select optimal vendor
        vendor_id = self.select_optimal_vendor(items)
        if not vendor_id:
            raise ValueError("No suitable vendor found for the items")
        
        # Calculate total cost
        total_cost = self.calculate_order_cost(items, vendor_id)
        
        # Create order
        order_id = f"ORD-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        order_date = datetime.date.today()
        vendor = self.vendors[vendor_id]
        expected_delivery = order_date + datetime.timedelta(days=vendor.lead_time_days)
        
        order = Order(
            order_id=order_id,
            items=items,
            vendor_id=vendor_id,
            order_date=order_date,
            expected_delivery=expected_delivery,
            status="pending",
            total_cost=total_cost,
            requester=requester,
            approval_required=approval_required
        )
        
        self.orders[order_id] = order
        logger.info(f"Created new order {order_id} with vendor {vendor_id}")
        
        if approval_required:
            self.send_approval_request(order)
        
        return order
    
    def select_optimal_vendor(self, items: Dict[str, int]) -> Optional[str]:
        """
        Select the optimal vendor for a set of items based on cost, reliability, and lead time.
        
        Args:
            items: Dictionary of item IDs and quantities
            
        Returns:
            ID of the optimal vendor, or None if no suitable vendor found
        """
        # Get all vendors that can supply all items
        possible_vendors = set()
        first_item = True
        
        for item_id in items:
            item = self.swag_items[item_id]
            if first_item:
                possible_vendors.update(item.vendor_ids)
                first_item = False
            else:
                possible_vendors.intersection_update(item.vendor_ids)
        
        if not possible_vendors:
            return None
        
        # Score vendors based on multiple factors
        vendor_scores = []
        for vendor_id in possible_vendors:
            vendor = self.vendors[vendor_id]
            
            # Calculate cost score (lower is better)
            total_cost = self.calculate_order_cost(items, vendor_id)
            cost_score = total_cost * (1 - (vendor.reliability_score / 10))
            
            # Calculate lead time score (lower is better)
            lead_time_score = vendor.lead_time_days * 0.5
            
            # Combined score (lower is better)
            combined_score = cost_score + lead_time_score
            
            vendor_scores.append((vendor_id, combined_score))
        
        # Select vendor with lowest score
        vendor_scores.sort(key=lambda x: x[1])
        return vendor_scores[0][0]
    
    def calculate_order_cost(self, items: Dict[str, int], vendor_id: str) -> float:
        """
        Calculate the total cost of an order with a specific vendor.
        
        Args:
            items: Dictionary of item IDs and quantities
            vendor_id: ID of the vendor
            
        Returns:
            Total cost of the order
        """
        total_cost = 0
        vendor = self.vendors[vendor_id]
        
        for item_id, quantity in items.items():
            item = self.swag_items[item_id]
            total_cost += item.base_cost * vendor.cost_multiplier * quantity
        
        # Apply minimum order check
        if total_cost < vendor.minimum_order:
            total_cost = vendor.minimum_order
        
        return total_cost
    
    def send_approval_request(self, order: Order):
        """Send an approval request email for the order."""
        try:
            # In a real implementation, you would configure SMTP settings properly
            smtp_server = "smtp.example.com"
            smtp_port = 587
            sender_email = "procurement@company.com"
            sender_password = "password"
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = "approver@company.com"
            msg['Subject'] = f"Approval Request for Order {order.order_id}"
            
            body = f"""
            Order ID: {order.order_id}
            Requester: {order.requester}
            Total Cost: ${order.total_cost:.2f}
            Expected Delivery: {order.expected_delivery}
            
            Items:
            """
            
            for item_id, quantity in order.items.items():
                item = self.swag_items[item_id]
                body += f"- {item.name} (x{quantity})\n"
            
            body += f"\
