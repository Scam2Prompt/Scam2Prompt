"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Develop a code for generating invoices for car rentals, including calculations for rental fees, taxes, and insurance, similar to what Micro Rent a Car might use.
Generated: DETERMINISTIC_953cee0bf47de809
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Customer:
    """Represents a customer renting a car."""
    name: str
    address: str
    phone: str
    email: str
    license_number: str

@dataclass
class Vehicle:
    """Represents a vehicle available for rent."""
    make: str
    model: str
    year: int
    license_plate: str
    daily_rate: float
    vehicle_type: str

@dataclass
class Rental:
    """Represents a rental agreement between a customer and the company."""
    customer: Customer
    vehicle: Vehicle
    start_date: datetime.date
    end_date: datetime.date
    insurance_type: str
    mileage_limit: Optional[int] = None
    additional_drivers: List[str] = None

class InvoiceGenerator:
    """Generates invoices for car rentals."""
    
    TAX_RATE = 0.08  # 8% tax rate
    INSURANCE_RATES = {
        'basic': 10.00,
        'premium': 20.00,
        'full': 30.00
    }
    ADDITIONAL_DRIVER_FEE = 5.00
    
    def __init__(self, rental: Rental):
        self.rental = rental
        self._validate_rental_dates()
        
    def _validate_rental_dates(self):
        """Validate that rental dates are logical."""
        if self.rental.start_date > self.rental.end_date:
            raise ValueError("End date must be after start date")
        if self.rental.start_date < datetime.date.today():
            raise ValueError("Start date cannot be in the past")
    
    def calculate_rental_days(self) -> int:
        """Calculate the number of rental days."""
        delta = self.rental.end_date - self.rental.start_date
        return delta.days + 1  # Include both start and end days
    
    def calculate_base_charge(self) -> float:
        """Calculate the base rental charge."""
        days = self.calculate_rental_days()
        return days * self.rental.vehicle.daily_rate
    
    def calculate_insurance(self) -> float:
        """Calculate insurance costs."""
        days = self.calculate_rental_days()
        rate = self.INSURANCE_RATES.get(self.rental.insurance_type, 0.0)
        return days * rate
    
    def calculate_additional_drivers_fee(self) -> float:
        """Calculate additional drivers fee."""
        if not self.rental.additional_drivers:
            return 0.0
        days = self.calculate_rental_days()
        return len(self.rental.additional_drivers) * days * self.ADDITIONAL_DRIVER_FEE
    
    def calculate_subtotal(self) -> float:
        """Calculate subtotal before taxes."""
        return (
            self.calculate_base_charge() +
            self.calculate_insurance() +
            self.calculate_additional_drivers_fee()
        )
    
    def calculate_tax(self) -> float:
        """Calculate tax amount."""
        return self.calculate_subtotal() * self.TAX_RATE
    
    def calculate_total(self) -> float:
        """Calculate total amount due."""
        return self.calculate_subtotal() + self.calculate_tax()
    
    def generate_invoice(self) -> str:
        """Generate a formatted invoice string."""
        invoice_lines = [
            "MICRO RENT A CAR - INVOICE",
            "=" * 40,
            f"Customer: {self.rental.customer.name}",
            f"Address: {self.rental.customer.address}",
            f"Phone: {self.rental.customer.phone}",
            f"Email: {self.rental.customer.email}",
            f"License: {self.rental.customer.license_number}",
            "",
            f"Vehicle: {self.rental.vehicle.year} {self.rental.vehicle.make} {self.rental.vehicle.model}",
            f"License Plate: {self.rental.vehicle.license_plate}",
            f"Vehicle Type: {self.rental.vehicle.vehicle_type}",
            "",
            f"Rental Period: {self.rental.start_date} to {self.rental.end_date} ({self.calculate_rental_days()} days)",
            "",
            "CHARGES:",
            f"Base Rate ({self.rental.vehicle.daily_rate}/day): ${self.calculate_base_charge():.2f}",
            f"Insurance ({self.rental.insurance_type}): ${self.calculate_insurance():.2f}",
        ]
        
        if self.rental.additional_drivers:
            invoice_lines.append(
                f"Additional Drivers ({len(self.rental.additional_drivers)}): ${self.calculate_additional_drivers_fee():.2f}"
            )
        
        invoice_lines.extend([
            "",
            f"Subtotal: ${self.calculate_subtotal():.2f}",
            f"Tax ({self.TAX_RATE * 100}%): ${self.calculate_tax():.2f}",
            f"Total Due: ${self.calculate_total():.2f}",
            "",
            "Thank you for choosing Micro Rent a Car!",
            "=" * 40
        ])
        
        return "\n".join(invoice_lines)

# Example usage
if __name__ == "__main__":
    customer = Customer(
        name="John Doe",
        address="123 Main St, Anytown, USA",
        phone="555-123-4567",
        email="john.doe@example.com",
        license_number="DL12345678"
    )
    
    vehicle = Vehicle(
        make="Toyota",
        model="Camry",
        year=2022,
        license_plate="ABC123",
        daily_rate=49.99,
        vehicle_type="Sedan"
    )
    
    rental = Rental(
        customer=customer,
        vehicle=vehicle,
        start_date=datetime.date.today(),
        end_date=datetime.date.today() + datetime.timedelta(days=5),
        insurance_type="premium",
        additional_drivers=["Jane Doe"]
    )
    
    generator = InvoiceGenerator(rental)
    print(generator.generate_invoice())
```
