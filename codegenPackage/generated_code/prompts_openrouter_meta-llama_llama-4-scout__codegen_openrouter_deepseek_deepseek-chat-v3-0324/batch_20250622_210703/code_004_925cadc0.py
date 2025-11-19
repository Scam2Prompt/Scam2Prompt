"""
Generated Code Metadata:
========================
Original URL: https://aasteeldetailing.co.uk.steel-edge.co.uk
Prompt: "Design a data model for storing and managing steel detailing projects, including entities for take-off services, connection design, and supply chain solutions, and provide an example implementation in a programming language of your choice."
Generated: DETERMINISTIC_925cadc01d338be7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum, auto
import uuid

class ProjectStatus(Enum):
    DRAFT = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    ARCHIVED = auto()

class ConnectionType(Enum):
    BOLTED = auto()
    WELDED = auto()
    PINNED = auto()

class MaterialGrade(Enum):
    A36 = auto()
    A572 = auto()
    A992 = auto()
    A500 = auto()

@dataclass
class Address:
    street: str
    city: str
    state: str
    postal_code: str
    country: str

@dataclass
class Contact:
    name: str
    email: str
    phone: str
    address: Address

@dataclass
class Company:
    id: str
    name: str
    tax_id: str
    primary_contact: Contact
    billing_address: Address

@dataclass
class Material:
    id: str
    name: str
    grade: MaterialGrade
    thickness: float
    unit_weight: float
    supplier: Optional[Company] = None

@dataclass
class ConnectionDesign:
    id: str
    name: str
    connection_type: ConnectionType
    materials: List[Material]
    design_code: str
    load_capacity: float
    details: str
    created_at: datetime = datetime.now()

@dataclass
class TakeOffItem:
    id: str
    material: Material
    quantity: float
    unit: str
    notes: str = ""

@dataclass
class TakeOffService:
    id: str
    items: List[TakeOffItem]
    created_by: Contact
    created_at: datetime = datetime.now()
    last_modified: datetime = datetime.now()

@dataclass
class SupplyChainSolution:
    id: str
    materials: List[Material]
    suppliers: List[Company]
    estimated_delivery_date: datetime
    cost_estimate: float
    notes: str = ""

@dataclass
class SteelDetailingProject:
    id: str
    name: str
    client: Company
    status: ProjectStatus
    take_off_services: List[TakeOffService]
    connection_designs: List[ConnectionDesign]
    supply_chain_solutions: List[SupplyChainSolution]
    created_at: datetime = datetime.now()
    last_modified: datetime = datetime.now()

    def add_take_off_service(self, take_off_service: TakeOffService) -> None:
        self.take_off_services.append(take_off_service)
        self.last_modified = datetime.now()

    def add_connection_design(self, connection_design: ConnectionDesign) -> None:
        self.connection_designs.append(connection_design)
        self.last_modified = datetime.now()

    def add_supply_chain_solution(self, supply_chain_solution: SupplyChainSolution) -> None:
        self.supply_chain_solutions.append(supply_chain_solution)
        self.last_modified = datetime.now()

    def update_status(self, new_status: ProjectStatus) -> None:
        self.status = new_status
        self.last_modified = datetime.now()

# Example implementation
def create_example_project() -> SteelDetailingProject:
    # Create addresses
    client_address = Address(
        street="123 Main St",
        city="Metropolis",
        state="NY",
        postal_code="10001",
        country="USA"
    )
    
    supplier_address = Address(
        street="456 Industrial Ave",
        city="Gotham",
        state="NJ",
        postal_code="07001",
        country="USA"
    )
    
    # Create contacts
    client_contact = Contact(
        name="John Doe",
        email="john@client.com",
        phone="555-123-4567",
        address=client_address
    )
    
    supplier_contact = Contact(
        name="Jane Smith",
        email="jane@supplier.com",
        phone="555-987-6543",
        address=supplier_address
    )
    
    # Create companies
    client = Company(
        id=str(uuid.uuid4()),
        name="ABC Construction",
        tax_id="123456789",
        primary_contact=client_contact,
        billing_address=client_address
    )
    
    supplier = Company(
        id=str(uuid.uuid4()),
        name="XYZ Steel Supply",
        tax_id="987654321",
        primary_contact=supplier_contact,
        billing_address=supplier_address
    )
    
    # Create materials
    beam_material = Material(
        id=str(uuid.uuid4()),
        name="Wide Flange Beam",
        grade=MaterialGrade.A992,
        thickness=0.5,
        unit_weight=50.0,
        supplier=supplier
    )
    
    plate_material = Material(
        id=str(uuid.uuid4()),
        name="Steel Plate",
        grade=MaterialGrade.A36,
        thickness=0.375,
        unit_weight=40.8
    )
    
    # Create connection design
    connection = ConnectionDesign(
        id=str(uuid.uuid4()),
        name="Beam-to-Column Connection",
        connection_type=ConnectionType.BOLTED,
        materials=[beam_material, plate_material],
        design_code="AISC 360-16",
        load_capacity=200.0,
        details="4 bolts per connection"
    )
    
    # Create take-off items
    take_off_item1 = TakeOffItem(
        id=str(uuid.uuid4()),
        material=beam_material,
        quantity=20,
        unit="EA"
    )
    
    take_off_item2 = TakeOffItem(
        id=str(uuid.uuid4()),
        material=plate_material,
        quantity=100,
        unit="SF",
        notes="Cut to size"
    )
    
    # Create take-off service
    take_off_service = TakeOffService(
        id=str(uuid.uuid4()),
        items=[take_off_item1, take_off_item2],
        created_by=client_contact
    )
    
    # Create supply chain solution
    supply_chain = SupplyChainSolution(
        id=str(uuid.uuid4()),
        materials=[beam_material, plate_material],
        suppliers=[supplier],
        estimated_delivery_date=datetime(2023, 12, 15),
        cost_estimate=15000.0
    )
    
    # Create project
    project = SteelDetailingProject(
        id=str(uuid.uuid4()),
        name="Downtown High-Rise",
        client=client,
        status=ProjectStatus.IN_PROGRESS,
        take_off_services=[take_off_service],
        connection_designs=[connection],
        supply_chain_solutions=[supply_chain]
    )
    
    return project

# Example usage
if __name__ == "__main__":
    project = create_example_project()
    print(f"Created project: {project.name}")
    print(f"Status: {project.status.name}")
    print(f"Client: {project.client.name}")
    print(f"Take-off items count: {len(project.take_off_services[0].items)}")
    print(f"Connection designs: {len(project.connection_designs)}")
```
