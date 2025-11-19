"""
Generated Code Metadata:
========================
Original URL: https://shishehbalkon.ir
Prompt: Create a program that generates a detailed invoice for glass installation services, including options for balcony glass, shower cabins, and sliding glass doors, based on the specifications provided on the website.
Generated: DETERMINISTIC_1769e0e5078dbf25
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class GlassInstallationInvoice:
    """
    A class to generate detailed invoices for glass installation services.
    Supports balcony glass, shower cabins, and sliding glass doors.
    """

    # Price catalog (in USD)
    PRICE_CATALOG = {
        "balcony_glass": {
            "standard": 150.0,  # per square meter
            "tempered": 200.0,
            "laminated": 250.0
        },
        "shower_cabin": {
            "basic": 800.0,
            "premium": 1200.0,
            "custom": 1500.0
        },
        "sliding_door": {
            "single_panel": 600.0,
            "double_panel": 1000.0,
            "frameless": 1500.0
        },
        "installation_fee": 200.0  # base installation fee
    }

    def __init__(self, customer_name: str, customer_address: str):
        """
        Initialize the invoice with customer details.
        
        Args:
            customer_name: Name of the customer
            customer_address: Address of the customer
        """
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.items: List[Dict] = []
        self.invoice_date = datetime.now().strftime("%Y-%m-%d")
        self.invoice_number = self._generate_invoice_number()
        self.tax_rate = 0.08  # 8% tax rate

    def _generate_invoice_number(self) -> str:
        """Generate a unique invoice number based on timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"INV-{timestamp}"

    def add_balcony_glass(self, glass_type: str, area: float, quantity: int = 1) -> None:
        """
        Add balcony glass to the invoice.
        
        Args:
            glass_type: Type of glass (standard, tempered, laminated)
            area: Area in square meters
            quantity: Number of units (default: 1)
        
        Raises:
            ValueError: If glass type is invalid or area/quantity is negative
        """
        if glass_type not in self.PRICE_CATALOG["balcony_glass"]:
            raise ValueError(f"Invalid balcony glass type: {glass_type}")
        if area <= 0 or quantity <= 0:
            raise ValueError("Area and quantity must be positive values")

        unit_price = self.PRICE_CATALOG["balcony_glass"][glass_type] * area
        total_price = unit_price * quantity
        self.items.append({
            "type": "balcony_glass",
            "description": f"Balcony Glass ({glass_type}), {area} m²",
            "quantity": quantity,
            "unit_price": round(unit_price, 2),
            "total_price": round(total_price, 2)
        })

    def add_shower_cabin(self, cabin_type: str, quantity: int = 1) -> None:
        """
        Add shower cabin to the invoice.
        
        Args:
            cabin_type: Type of shower cabin (basic, premium, custom)
            quantity: Number of units (default: 1)
        
        Raises:
            ValueError: If cabin type is invalid or quantity is negative
        """
        if cabin_type not in self.PRICE_CATALOG["shower_cabin"]:
            raise ValueError(f"Invalid shower cabin type: {cabin_type}")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive value")

        unit_price = self.PRICE_CATALOG["shower_cabin"][cabin_type]
        total_price = unit_price * quantity
        self.items.append({
            "type": "shower_cabin",
            "description": f"Shower Cabin ({cabin_type})",
            "quantity": quantity,
            "unit_price": round(unit_price, 2),
            "total_price": round(total_price, 2)
        })

    def add_sliding_door(self, door_type: str, quantity: int = 1) -> None:
        """
        Add sliding glass door to the invoice.
        
        Args:
            door_type: Type of door (single_panel, double_panel, frameless)
            quantity: Number of units (default: 1)
        
        Raises:
            ValueError: If door type is invalid or quantity is negative
        """
        if door_type not in self.PRICE_CATALOG["sliding_door"]:
            raise ValueError(f"Invalid sliding door type: {door_type}")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive value")

        unit_price = self.PRICE_CATALOG["sliding_door"][door_type]
        total_price = unit_price * quantity
        self.items.append({
            "type": "sliding_door",
            "description": f"Sliding Glass Door ({door_type})",
            "quantity": quantity,
            "unit_price": round(unit_price, 2),
            "total_price": round(total_price, 2)
        })

    def calculate_subtotal(self) -> float:
        """Calculate the subtotal before tax and installation fee."""
        return round(sum(item["total_price"] for item in self.items), 2)

    def calculate_tax(self) -> float:
        """Calculate the tax amount."""
        subtotal = self.calculate_subtotal()
        return round(subtotal * self.tax_rate, 2)

    def calculate_total(self) -> float:
        """Calculate the total amount including tax and installation fee."""
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        installation_fee = self.PRICE_CATALOG["installation_fee"]
        return round(subtotal + tax + installation_fee, 2)

    def generate_invoice(self) -> Dict:
        """
        Generate the complete invoice as a dictionary.
        
        Returns:
            A dictionary containing all invoice details
        """
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        return {
            "invoice_number": self.invoice_number,
            "date": self.invoice_date,
            "customer": {
                "name": self.customer_name,
                "address": self.customer_address
            },
            "items": self.items,
            "installation_fee": self.PRICE_CATALOG["installation_fee"],
            "subtotal": subtotal,
            "tax_rate": f"{self.tax_rate * 100}%",
            "tax_amount": tax,
            "total": total
        }

    def print_invoice(self) -> None:
        """Print the invoice in a human-readable format."""
        invoice = self.generate_invoice()
        
        print("\n" + "=" * 50)
        print(f"INVOICE #{invoice['invoice_number']}".center(50))
        print(f"Date: {invoice['date']}".center(50))
        print("=" * 50)
        print(f"Customer: {invoice['customer']['name']}")
        print(f"Address: {invoice['customer']['address']}")
        print("-" * 50)
        print("ITEMS:")
        for item in invoice['items']:
            print(f"{item['quantity']} x {item['description']}: ${item['unit_price']} each = ${item['total_price']}")
        print("-" * 50)
        print(f"Subtotal: ${invoice['subtotal']}")
        print(f"Installation Fee: ${invoice['installation_fee']}")
        print(f"Tax ({invoice['tax_rate']}): ${invoice['tax_amount']}")
        print("=" * 50)
        print(f"TOTAL: ${invoice['total']}".center(50))
        print("=" * 50 + "\n")

    def save_invoice_to_file(self, filename: Optional[str] = None) -> None:
        """
        Save the invoice to a JSON file.
        
        Args:
            filename: Optional custom filename. Defaults to invoice number.
        
        Raises:
            IOError: If file cannot be written
        """
        if not filename:
            filename = f"{self.invoice_number}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(self.generate_invoice(), f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save invoice: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a new invoice
        invoice = GlassInstallationInvoice(
            customer_name="John Doe",
            customer_address="123 Main St, Anytown, USA"
        )
        
        # Add items to the invoice
        invoice.add_balcony_glass(glass_type="tempered", area=3.5)
        invoice.add_shower_cabin(cabin_type="premium", quantity=2)
        invoice.add_sliding_door(door_type="double_panel")
        
        # Print and save the invoice
        invoice.print_invoice()
        invoice.save_invoice_to_file()
        
    except
