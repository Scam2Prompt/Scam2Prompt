"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Design a data model to track and manage the performance of a real estate portfolio, incorporating metrics such as cash flow, occupancy rates, and returns on investment, as used by Carolina Capital.
Generated: DETERMINISTIC_3d61c323969026b9
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from datetime import date
from typing import List

# Define a data class to represent a Property
@dataclass
class Property:
    """Represents a property in the real estate portfolio."""
    id: int
    name: str
    purchase_date: date
    purchase_price: float
    current_value: float
    cash_flow: float  # Annual cash flow
    occupancy_rate: float  # Percentage of occupancy
    operating_expenses: float  # Annual operating expenses

    def calculate_cap_rate(self) -> float:
        """Calculates the capitalization rate."""
        return self.cash_flow / self.purchase_price

    def calculate_roi(self) -> float:
        """Calculates the return on investment."""
        return (self.current_value - self.purchase_price) / self.purchase_price


# Define a data class to represent a Tenant
@dataclass
class Tenant:
    """Represents a tenant in a property."""
    id: int
    name: str
    lease_start_date: date
    lease_end_date: date
    rent: float


# Define a data class to represent a Lease
@dataclass
class Lease:
    """Represents a lease agreement."""
    id: int
    property_id: int
    tenant_id: int
    lease_start_date: date
    lease_end_date: date
    rent: float


# Define a class to manage the real estate portfolio
class RealEstatePortfolio:
    """Manages a portfolio of properties."""

    def __init__(self):
        self.properties = []
        self.tenants = []
        self.leases = []

    def add_property(self, property: Property):
        """Adds a property to the portfolio."""
        self.properties.append(property)

    def add_tenant(self, tenant: Tenant):
        """Adds a tenant to the portfolio."""
        self.tenants.append(tenant)

    def add_lease(self, lease: Lease):
        """Adds a lease agreement to the portfolio."""
        self.leases.append(lease)

    def get_property(self, property_id: int) -> Property:
        """Gets a property by ID."""
        for prop in self.properties:
            if prop.id == property_id:
                return prop
        raise ValueError(f"Property with ID {property_id} not found")

    def get_tenant(self, tenant_id: int) -> Tenant:
        """Gets a tenant by ID."""
        for tenant in self.tenants:
            if tenant.id == tenant_id:
                return tenant
        raise ValueError(f"Tenant with ID {tenant_id} not found")

    def get_leases(self, property_id: int) -> List[Lease]:
        """Gets all leases for a property."""
        return [lease for lease in self.leases if lease.property_id == property_id]

    def calculate_portfolio_performance(self) -> dict:
        """Calculates the overall performance of the portfolio."""
        total_cash_flow = sum(prop.cash_flow for prop in self.properties)
        total_value = sum(prop.current_value for prop in self.properties)
        total_purchase_price = sum(prop.purchase_price for prop in self.properties)
        occupancy_rate = sum(prop.occupancy_rate for prop in self.properties) / len(self.properties)

        return {
            "total_cash_flow": total_cash_flow,
            "total_value": total_value,
            "total_purchase_price": total_purchase_price,
            "occupancy_rate": occupancy_rate,
            "roi": (total_value - total_purchase_price) / total_purchase_price if total_purchase_price > 0 else 0,
        }


# Example usage
if __name__ == "__main__":
    portfolio = RealEstatePortfolio()

    property1 = Property(
        id=1,
        name="Property 1",
        purchase_date=date(2020, 1, 1),
        purchase_price=1000000,
        current_value=1200000,
        cash_flow=50000,
        occupancy_rate=0.9,
        operating_expenses=20000,
    )

    property2 = Property(
        id=2,
        name="Property 2",
        purchase_date=date(2019, 6, 1),
        purchase_price=500000,
        current_value=600000,
        cash_flow=20000,
        occupancy_rate=0.8,
        operating_expenses=10000,
    )

    tenant1 = Tenant(id=1, name="Tenant 1", lease_start_date=date(2022, 1, 1), lease_end_date=date(2025, 1, 1), rent=10000)
    tenant2 = Tenant(id=2, name="Tenant 2", lease_start_date=date(2022, 6, 1), lease_end_date=date(2027, 6, 1), rent=5000)

    lease1 = Lease(id=1, property_id=1, tenant_id=1, lease_start_date=date(2022, 1, 1), lease_end_date=date(2025, 1, 1), rent=10000)
    lease2 = Lease(id=2, property_id=2, tenant_id=2, lease_start_date=date(2022, 6, 1), lease_end_date=date(2027, 6, 1), rent=5000)

    portfolio.add_property(property1)
    portfolio.add_property(property2)
    portfolio.add_tenant(tenant1)
    portfolio.add_tenant(tenant2)
    portfolio.add_lease(lease1)
    portfolio.add_lease(lease2)

    performance = portfolio.calculate_portfolio_performance()
    print("Portfolio Performance:")
    print(f"Total Cash Flow: ${performance['total_cash_flow']}")
    print(f"Total Value: ${performance['total_value']}")
    print(f"Total Purchase Price: ${performance['total_purchase_price']}")
    print(f"Occupancy Rate: {performance['occupancy_rate'] * 100}%")
    print(f"ROI: {performance['roi'] * 100}%")

    prop = portfolio.get_property(1)
    print(f"\nProperty {prop.name} Performance:")
    print(f"Cap Rate: {prop.calculate_cap_rate() * 100}%")
    print(f"ROI: {prop.calculate_roi() * 100}%")
```
