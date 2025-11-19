"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Write code to simulate a pharmacy inventory management system tailored for independent pharmacies, incorporating features like purchasing power optimization and flexible operational systems as described by PharmaChoice Canada.
Generated: DETERMINISTIC_ccb4c82fc84f8eeb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
import uuid
import csv
import os


@dataclass
class Medication:
    """Class representing a medication in the inventory."""
    id: str
    name: str
    generic_name: str
    quantity: int
    cost_per_unit: float
    selling_price: float
    supplier: str
    expiry_date: str
    reorder_threshold: int
    last_ordered_date: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert Medication object to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "generic_name": self.generic_name,
            "quantity": self.quantity,
            "cost_per_unit": self.cost_per_unit,
            "selling_price": self.selling_price,
            "supplier": self.supplier,
            "expiry_date": self.expiry_date,
            "reorder_threshold": self.reorder_threshold,
            "last_ordered_date": self.last_ordered_date
        }


@dataclass
class Supplier:
    """Class representing a medication supplier."""
    id: str
    name: str
    contact: str
    lead_time_days: int
    discount_threshold: int
    discount_percentage: float
    medications_supplied: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert Supplier object to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "contact": self.contact,
            "lead_time_days": self.lead_time_days,
            "discount_threshold": self.discount_threshold,
            "discount_percentage": self.discount_percentage,
            "medications_supplied": self.medications_supplied
        }


@dataclass
class Order:
    """Class representing an order to a supplier."""
    id: str
    supplier_id: str
    items: Dict[str, int]  # medication_id: quantity
    order_date: str
    expected_delivery_date: str
    total_cost: float
    status: str  # "pending", "delivered", "cancelled"

    def to_dict(self) -> Dict:
        """Convert Order object to dictionary."""
        return {
            "id": self.id,
            "supplier_id": self.supplier_id,
            "items": self.items,
            "order_date": self.order_date,
            "expected_delivery_date": self.expected_delivery_date,
            "total_cost": self.total_cost,
            "status": self.status
        }


class PharmacyInventory:
    """Main class for pharmacy inventory management system."""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize the inventory system with data directory."""
        self.data_dir = data_dir
        self.medications: Dict[str, Medication] = {}
        self.suppliers: Dict[str, Supplier] = {}
        self.orders: Dict[str, Order] = {}
        
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load existing data
        self._load_data()

    def _load_data(self) -> None:
        """Load data from JSON files if they exist."""
        try:
            # Load medications
            meds_path = os.path.join(self.data_dir, "medications.json")
            if os.path.exists(meds_path):
                with open(meds_path, "r") as f:
                    meds_data = json.load(f)
                    for med_id, med_data in meds_data.items():
                        self.medications[med_id] = Medication(**med_data)
            
            # Load suppliers
            suppliers_path = os.path.join(self.data_dir, "suppliers.json")
            if os.path.exists(suppliers_path):
                with open(suppliers_path, "r") as f:
                    suppliers_data = json.load(f)
                    for supplier_id, supplier_data in suppliers_data.items():
                        self.suppliers[supplier_id] = Supplier(**supplier_data)
            
            # Load orders
            orders_path = os.path.join(self.data_dir, "orders.json")
            if os.path.exists(orders_path):
                with open(orders_path, "r") as f:
                    orders_data = json.load(f)
                    for order_id, order_data in orders_data.items():
                        self.orders[order_id] = Order(**order_data)
                        
        except Exception as e:
            print(f"Error loading data: {e}")

    def _save_data(self) -> None:
        """Save data to JSON files."""
        try:
            # Save medications
            meds_path = os.path.join(self.data_dir, "medications.json")
            with open(meds_path, "w") as f:
                json.dump({k: v.to_dict() for k, v in self.medications.items()}, f, indent=2)
            
            # Save suppliers
            suppliers_path = os.path.join(self.data_dir, "suppliers.json")
            with open(suppliers_path, "w") as f:
                json.dump({k: v.to_dict() for k, v in self.suppliers.items()}, f, indent=2)
            
            # Save orders
            orders_path = os.path.join(self.data_dir, "orders.json")
            with open(orders_path, "w") as f:
                json.dump({k: v.to_dict() for k, v in self.orders.items()}, f, indent=2)
                
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_medication(self, name: str, generic_name: str, quantity: int, 
                      cost_per_unit: float, selling_price: float, supplier: str,
                      expiry_date: str, reorder_threshold: int) -> str:
        """Add a new medication to the inventory."""
        med_id = str(uuid.uuid4())
        medication = Medication(
            id=med_id,
            name=name,
            generic_name=generic_name,
            quantity=quantity,
            cost_per_unit=cost_per_unit,
            selling_price=selling_price,
            supplier=supplier,
            expiry_date=expiry_date,
            reorder_threshold=reorder_threshold
        )
        self.medications[med_id] = medication
        self._save_data()
        return med_id

    def update_medication_quantity(self, medication_id: str, quantity_change: int) -> bool:
        """Update medication quantity (positive for addition, negative for subtraction)."""
        if medication_id not in self.medications:
            return False
        
        new_quantity = self.medications[medication_id].quantity + quantity_change
        if new_quantity < 0:
            return False
        
        self.medications[medication_id].quantity = new_quantity
        self._save_data()
        return True

    def add_supplier(self, name: str, contact: str, lead_time_days: int,
                    discount_threshold: int, discount_percentage: float) -> str:
        """Add a new supplier to the system."""
        supplier_id = str(uuid.uuid4())
        supplier = Supplier(
            id=supplier_id,
            name=name,
            contact=contact,
            lead_time_days=lead_time_days,
            discount_threshold=discount_threshold,
            discount_percentage=discount_percentage
        )
        self.suppliers[supplier_id] = supplier
        self._save_data()
        return supplier_id

    def add_medication_to_supplier(self, supplier_id: str, medication_id: str) -> bool:
        """Associate a medication with a supplier."""
        if supplier_id not in self.suppliers or medication_id not in self.medications:
            return False
        
        if medication_id not in self.suppliers[supplier_id].medications_supplied:
            self.suppliers[supplier_id].medications_supplied.append(medication_id)
            self._save_data()
            return True
        return False

    def check_inventory_levels(self) -> List[Tuple[str, str, int]]:
        """Check for medications that need to be reordered."""
        today = datetime.date.today().isoformat()
        reorder_list = []
        
        for med_id, medication in self.medications.items():
            if (medication.quantity <= medication.reorder_threshold and 
                (medication.last_ordered_date is None or 
                 medication.last_ordered_date < today)):
                reorder_list.append((med_id, medication.name, medication.quantity))
        
        return reorder_list

    def optimize_purchase(self, medication_id: str) -> Optional[Tuple[str, int, float]]:
        """
        Optimize purchase by finding the best supplier for a medication.
        Returns (supplier_id, optimal_quantity, total_cost) or None if no supplier.
        """
        if medication_id not in self.medications:
            return None
        
        medication = self.medications[medication_id]
        possible_suppliers = [
            supplier_id for supplier_id, supplier in self.suppliers.items()
            if medication_id
