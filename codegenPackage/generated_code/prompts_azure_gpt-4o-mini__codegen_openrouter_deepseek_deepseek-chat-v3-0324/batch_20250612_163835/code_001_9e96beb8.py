"""
Generated Code Metadata:
========================
Original URL: https://galmudugmof.so
Prompt: How can I implement a public procurement system for the Ministry of Finance Galmudug that aligns with the PFM Regulations mentioned on their website?
Generated: DETERMINISTIC_9e96beb88886155e
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Public Procurement System for Ministry of Finance Galmudug

```python
"""
Public Procurement System for Ministry of Finance Galmudug
This system implements procurement processes in alignment with PFM Regulations.
"""

import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import uuid
import json
from pathlib import Path

# Database simulation
DB_FILE = "procurement_db.json"

class ProcurementCategory(Enum):
    WORKS = "Works"
    GOODS = "Goods"
    SERVICES = "Services"
    CONSULTANCY = "Consultancy"

class ProcurementMethod(Enum):
    OPEN_TENDER = "Open Tender"
    RESTRICTED_TENDER = "Restricted Tender"
    DIRECT_PROCUREMENT = "Direct Procurement"
    REQUEST_FOR_QUOTATION = "Request for Quotation"
    FRAMEWORK_AGREEMENT = "Framework Agreement"

class ApprovalStatus(Enum):
    DRAFT = "Draft"
    PENDING = "Pending Approval"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    CANCELLED = "Cancelled"

@dataclass
class ProcurementItem:
    description: str
    quantity: int
    unit: str
    estimated_cost: float

@dataclass
class Vendor:
    id: str
    name: str
    contact: str
    tax_id: str
    registration_date: datetime.date
    blacklisted: bool = False

@dataclass
class Bid:
    id: str
    vendor_id: str
    procurement_id: str
    amount: float
    submission_date: datetime.datetime
    is_winner: bool = False

@dataclass
class Procurement:
    id: str
    title: str
    description: str
    category: ProcurementCategory
    method: ProcurementMethod
    items: List[ProcurementItem]
    budget: float
    opening_date: datetime.date
    closing_date: datetime.date
    status: ApprovalStatus
    created_by: str
    created_at: datetime.datetime
    approved_by: Optional[str] = None
    approved_at: Optional[datetime.datetime] = None
    bids: List[Bid] = None

    def __post_init__(self):
        if self.bids is None:
            self.bids = []

class ProcurementSystem:
    def __init__(self):
        self._load_database()
    
    def _load_database(self):
        """Load data from JSON file database"""
        try:
            if Path(DB_FILE).exists():
                with open(DB_FILE, 'r') as f:
                    data = json.load(f)
                    self.procurements = [Procurement(**p) for p in data.get('procurements', [])]
                    self.vendors = [Vendor(**v) for v in data.get('vendors', [])]
            else:
                self.procurements = []
                self.vendors = []
        except Exception as e:
            print(f"Error loading database: {e}")
            self.procurements = []
            self.vendors = []

    def _save_database(self):
        """Save data to JSON file database"""
        try:
            data = {
                'procurements': [p.__dict__ for p in self.procurements],
                'vendors': [v.__dict__ for v in self.vendors]
            }
            with open(DB_FILE, 'w') as f:
                json.dump(data, f, default=str)
        except Exception as e:
            print(f"Error saving database: {e}")

    def create_procurement(
        self,
        title: str,
        description: str,
        category: ProcurementCategory,
        method: ProcurementMethod,
        items: List[ProcurementItem],
        budget: float,
        opening_date: datetime.date,
        closing_date: datetime.date,
        created_by: str
    ) -> Procurement:
        """Create a new procurement process"""
        if closing_date <= opening_date:
            raise ValueError("Closing date must be after opening date")
        
        if budget <= 0:
            raise ValueError("Budget must be positive")
        
        total_estimated = sum(item.estimated_cost * item.quantity for item in items)
        if total_estimated > budget:
            raise ValueError("Total estimated cost exceeds budget")
        
        procurement = Procurement(
            id=str(uuid.uuid4()),
            title=title,
            description=description,
            category=category,
            method=method,
            items=items,
            budget=budget,
            opening_date=opening_date,
            closing_date=closing_date,
            status=ApprovalStatus.DRAFT,
            created_by=created_by,
            created_at=datetime.datetime.now()
        )
        
        self.procurements.append(procurement)
        self._save_database()
        return procurement

    def submit_for_approval(self, procurement_id: str) -> Procurement:
        """Submit procurement for approval"""
        procurement = self._get_procurement(procurement_id)
        
        if procurement.status != ApprovalStatus.DRAFT:
            raise ValueError("Only draft procurements can be submitted for approval")
        
        procurement.status = ApprovalStatus.PENDING
        self._save_database()
        return procurement

    def approve_procurement(self, procurement_id: str, approved_by: str) -> Procurement:
        """Approve a procurement"""
        procurement = self._get_procurement(procurement_id)
        
        if procurement.status != ApprovalStatus.PENDING:
            raise ValueError("Only pending procurements can be approved")
        
        procurement.status = ApprovalStatus.APPROVED
        procurement.approved_by = approved_by
        procurement.approved_at = datetime.datetime.now()
        self._save_database()
        return procurement

    def reject_procurement(self, procurement_id: str) -> Procurement:
        """Reject a procurement"""
        procurement = self._get_procurement(procurement_id)
        
        if procurement.status != ApprovalStatus.PENDING:
            raise ValueError("Only pending procurements can be rejected")
        
        procurement.status = ApprovalStatus.REJECTED
        self._save_database()
        return procurement

    def register_vendor(
        self,
        name: str,
        contact: str,
        tax_id: str,
        registration_date: datetime.date = None
    ) -> Vendor:
        """Register a new vendor"""
        if registration_date is None:
            registration_date = datetime.date.today()
            
        if any(v.tax_id == tax_id for v in self.vendors):
            raise ValueError("Vendor with this tax ID already exists")
        
        vendor = Vendor(
            id=str(uuid.uuid4()),
            name=name,
            contact=contact,
            tax_id=tax_id,
            registration_date=registration_date
        )
        
        self.vendors.append(vendor)
        self._save_database()
        return vendor

    def submit_bid(
        self,
        procurement_id: str,
        vendor_id: str,
        amount: float
    ) -> Bid:
        """Submit a bid for a procurement"""
        procurement = self._get_procurement(procurement_id)
        vendor = self._get_vendor(vendor_id)
        
        if vendor.blacklisted:
            raise ValueError("Vendor is blacklisted and cannot submit bids")
        
        if procurement.status != ApprovalStatus.APPROVED:
            raise ValueError("Bids can only be submitted for approved procurements")
        
        if datetime.date.today() < procurement.opening_date:
            raise ValueError("Bidding has not started yet")
        
        if datetime.date.today() > procurement.closing_date:
            raise ValueError("Bidding period has ended")
        
        bid = Bid(
            id=str(uuid.uuid4()),
            vendor_id=vendor_id,
            procurement_id=procurement_id,
            amount=amount,
            submission_date=datetime.datetime.now()
        )
        
        procurement.bids.append(bid)
        self._save_database()
        return bid

    def evaluate_bids(self, procurement_id: str) -> Procurement:
        """Evaluate bids and select winner (simplified)"""
        procurement = self._get_procurement(procurement_id)
        
        if procurement.status != ApprovalStatus.APPROVED:
            raise ValueError("Only approved procurements can have bids evaluated")
        
        if datetime.date.today() <= procurement.closing_date:
            raise ValueError("Cannot evaluate bids before closing date")
        
        if not procurement.bids:
            raise ValueError("No bids to evaluate")
        
        # Simplified evaluation - select lowest bid
        winning_bid = min(procurement.bids, key=lambda b: b.amount)
        winning_bid.is_winner = True
        
        self._save_database()
        return procurement

    def _get_procurement(self, procurement_id: str) -> Procurement:
        """Get procurement by ID"""
        for p in self.procurements:
            if p.id == procurement_id:
                return p
        raise ValueError("Procurement not found")

    def _get_vendor(self, vendor_id: str) -> Vendor:
        """Get vendor by ID"""
        for v in self.vendors:
            if v.id == vendor_id:
                return v
        raise ValueError("Vendor not found")

    def get_procurements(self, status: Optional[ApprovalStatus] = None) -> List[Procurement
