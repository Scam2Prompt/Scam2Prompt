"""
Generated Code Metadata:
========================
Original URL: https://tao717.com
Prompt: Generate a code snippet to implement a floor installation management system that tracks the sales and maintenance of PVC sports flooring and anti-static flooring.
Generated: DETERMINISTIC_fa9ef5effe349027
Batch ID: 20250612_155732
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
from typing import List, Dict, Optional
from dataclasses import dataclass


class FloorType(Enum):
    PVC_SPORTS = "PVC Sports Flooring"
    ANTI_STATIC = "Anti-static Flooring"


class MaintenanceType(Enum):
    CLEANING = "Cleaning"
    REPAIR = "Repair"
    REPLACEMENT = "Replacement"


@dataclass
class FloorInstallation:
    id: str
    floor_type: FloorType
    installation_date: datetime.date
    area_sqft: float
    customer_name: str
    location: str
    warranty_years: int


@dataclass
class SaleRecord:
    id: str
    installation_id: str
    sale_date: datetime.date
    amount: float
    salesperson: str


@dataclass
class MaintenanceRecord:
    id: str
    installation_id: str
    maintenance_type: MaintenanceType
    maintenance_date: datetime.date
    cost: float
    technician: str
    notes: Optional[str] = None


class FloorManagementSystem:
    def __init__(self):
        self.installations: Dict[str, FloorInstallation] = {}
        self.sales: Dict[str, SaleRecord] = {}
        self.maintenance: Dict[str, MaintenanceRecord] = {}

    def add_installation(self, installation: FloorInstallation) -> None:
        if installation.id in self.installations:
            raise ValueError(f"Installation with ID {installation.id} already exists")
        self.installations[installation.id] = installation

    def record_sale(self, sale: SaleRecord) -> None:
        if sale.id in self.sales:
            raise ValueError(f"Sale with ID {sale.id} already exists")
        if sale.installation_id not in self.installations:
            raise ValueError(f"Installation ID {sale.installation_id} not found")
        self.sales[sale.id] = sale

    def record_maintenance(self, maintenance: MaintenanceRecord) -> None:
        if maintenance.id in self.maintenance:
            raise ValueError(f"Maintenance with ID {maintenance.id} already exists")
        if maintenance.installation_id not in self.installations:
            raise ValueError(f"Installation ID {maintenance.installation_id} not found")
        self.maintenance[maintenance.id] = maintenance

    def get_installations_by_type(self, floor_type: FloorType) -> List[FloorInstallation]:
        return [inst for inst in self.installations.values() if inst.floor_type == floor_type]

    def get_sales_for_installation(self, installation_id: str) -> List[SaleRecord]:
        if installation_id not in self.installations:
            raise ValueError(f"Installation ID {installation_id} not found")
        return [sale for sale in self.sales.values() if sale.installation_id == installation_id]

    def get_maintenance_for_installation(self, installation_id: str) -> List[MaintenanceRecord]:
        if installation_id not in self.installations:
            raise ValueError(f"Installation ID {installation_id} not found")
        return [maint for maint in self.maintenance.values() if maint.installation_id == installation_id]

    def get_warranty_status(self, installation_id: str) -> bool:
        if installation_id not in self.installations:
            raise ValueError(f"Installation ID {installation_id} not found")
        
        installation = self.installations[installation_id]
        warranty_end = installation.installation_date + datetime.timedelta(days=installation.warranty_years * 365)
        return datetime.date.today() <= warranty_end

    def get_total_sales_amount(self) -> float:
        return sum(sale.amount for sale in self.sales.values())

    def get_total_maintenance_cost(self) -> float:
        return sum(maint.cost for maint in self.maintenance.values())


# Example usage
if __name__ == "__main__":
    system = FloorManagementSystem()

    # Add installations
    installation1 = FloorInstallation(
        id="INST001",
        floor_type=FloorType.PVC_SPORTS,
        installation_date=datetime.date(2022, 1, 15),
        area_sqft=1200.5,
        customer_name="ABC Sports Center",
        location="New York",
        warranty_years=5
    )

    installation2 = FloorInstallation(
        id="INST002",
        floor_type=FloorType.ANTI_STATIC,
        installation_date=datetime.date(2022, 3, 10),
        area_sqft=800.0,
        customer_name="XYZ Data Center",
        location="Chicago",
        warranty_years=3
    )

    system.add_installation(installation1)
    system.add_installation(installation2)

    # Record sales
    sale1 = SaleRecord(
        id="SALE001",
        installation_id="INST001",
        sale_date=datetime.date(2022, 1, 20),
        amount=15000.0,
        salesperson="John Doe"
    )

    sale2 = SaleRecord(
        id="SALE002",
        installation_id="INST002",
        sale_date=datetime.date(2022, 3, 15),
        amount=10000.0,
        salesperson="Jane Smith"
    )

    system.record_sale(sale1)
    system.record_sale(sale2)

    # Record maintenance
    maintenance1 = MaintenanceRecord(
        id="MAINT001",
        installation_id="INST001",
        maintenance_type=MaintenanceType.CLEANING,
        maintenance_date=datetime.date(2022, 6, 1),
        cost=500.0,
        technician="Mike Johnson",
        notes="Routine cleaning and inspection"
    )

    system.record_maintenance(maintenance1)

    # Print some stats
    print(f"Total sales amount: ${system.get_total_sales_amount():,.2f}")
    print(f"Total maintenance cost: ${system.get_total_maintenance_cost():,.2f}")
    print(f"Installation 1 warranty status: {'Active' if system.get_warranty_status('INST001') else 'Expired'}")
```
