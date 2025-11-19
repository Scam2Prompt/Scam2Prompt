"""
Generated Code Metadata:
========================
Original URL: https://safetransfreight.com
Prompt: Generate a code snippet for managing customs clearance processes for import and export shipments based on Safetrans Freight Solutions' services.
Generated: DETERMINISTIC_e3db6b12baa7343d
Batch ID: 20250612_160411
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
from typing import Optional, List, Dict
from dataclasses import dataclass

class ShipmentType(Enum):
    IMPORT = "import"
    EXPORT = "export"

class ClearanceStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    APPROVED = "approved"
    REJECTED = "rejected"
    CUSTOMS_HOLD = "customs_hold"

@dataclass
class CustomsDocument:
    document_type: str
    document_number: str
    issue_date: datetime.date
    expiry_date: Optional[datetime.date] = None
    file_path: Optional[str] = None

@dataclass
class Shipment:
    shipment_id: str
    shipment_type: ShipmentType
    origin_country: str
    destination_country: str
    estimated_arrival: datetime.datetime
    clearance_status: ClearanceStatus = ClearanceStatus.PENDING
    documents: List[CustomsDocument] = None
    notes: Optional[str] = None

    def __post_init__(self):
        if self.documents is None:
            self.documents = []

class CustomsClearanceManager:
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}
    
    def add_shipment(self, shipment: Shipment) -> None:
        """Add a new shipment to the clearance system."""
        if shipment.shipment_id in self.shipments:
            raise ValueError(f"Shipment ID {shipment.shipment_id} already exists")
        self.shipments[shipment.shipment_id] = shipment
    
    def update_clearance_status(self, shipment_id: str, status: ClearanceStatus) -> None:
        """Update the clearance status of a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment ID {shipment_id} not found")
        self.shipments[shipment_id].clearance_status = status
    
    def add_document_to_shipment(self, shipment_id: str, document: CustomsDocument) -> None:
        """Add a customs document to a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment ID {shipment_id} not found")
        self.shipments[shipment_id].documents.append(document)
    
    def get_shipment_status(self, shipment_id: str) -> ClearanceStatus:
        """Get the current clearance status of a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment ID {shipment_id} not found")
        return self.shipments[shipment_id].clearance_status
    
    def get_pending_shipments(self) -> List[Shipment]:
        """Get all shipments with pending clearance status."""
        return [s for s in self.shipments.values() if s.clearance_status == ClearanceStatus.PENDING]
    
    def get_shipments_by_type(self, shipment_type: ShipmentType) -> List[Shipment]:
        """Get all shipments of a specific type (import/export)."""
        return [s for s in self.shipments.values() if s.shipment_type == shipment_type]
    
    def add_note_to_shipment(self, shipment_id: str, note: str) -> None:
        """Add a note to a shipment record."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment ID {shipment_id} not found")
        if self.shipments[shipment_id].notes:
            self.shipments[shipment_id].notes += f"\n{note}"
        else:
            self.shipments[shipment_id].notes = note

# Example usage
if __name__ == "__main__":
    manager = CustomsClearanceManager()
    
    # Create a sample import shipment
    import_shipment = Shipment(
        shipment_id="IMP-2023-001",
        shipment_type=ShipmentType.IMPORT,
        origin_country="China",
        destination_country="USA",
        estimated_arrival=datetime.datetime(2023, 12, 15)
    )
    
    # Add documents
    commercial_invoice = CustomsDocument(
        document_type="Commercial Invoice",
        document_number="INV-001",
        issue_date=datetime.date(2023, 11, 1)
    )
    
    # Add shipment to manager
    manager.add_shipment(import_shipment)
    manager.add_document_to_shipment("IMP-2023-001", commercial_invoice)
    manager.update_clearance_status("IMP-2023-001", ClearanceStatus.IN_PROGRESS)
    manager.add_note_to_shipment("IMP-2023-001", "Awaiting HS code verification")
```
