"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Write a program to generate a detailed invoice for a customer purchasing plexiglass and polycarbonate sheets, including CNC cutting services, as described on Bursa Pleksi Merkezi's website.
Generated: DETERMINISTIC_df244939e535b9ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Invoice Generator for Bursa Pleksi Merkezi
Generates detailed invoices for plexiglass and polycarbonate sheet purchases,
including CNC cutting services.
"""

import datetime
from decimal import Decimal, ROUND_HALF_UP

class Product:
    """Represents a product with its properties and pricing."""
    
    def __init__(self, name, material_type, thickness, width, length, price_per_sqm, cnc_cutting=False, cnc_price_per_meter=0):
        """
        Initialize a product.
        
        Args:
            name (str): Product name
            material_type (str): 'plexiglass' or 'polycarbonate'
            thickness (Decimal): Thickness in mm
            width (Decimal): Width in mm
            length (Decimal): Length in mm
            price_per_sqm (Decimal): Price per square meter
            cnc_cutting (bool): Whether CNC cutting is required
            cnc_price_per_meter (Decimal): Price per meter for CNC cutting
        """
        self.name = name
        self.material_type = material_type
        self.thickness = Decimal(thickness)
        self.width = Decimal(width)
        self.length = Decimal(length)
        self.price_per_sqm = Decimal(price_per_sqm)
        self.cnc_cutting = cnc_cutting
        self.cnc_price_per_meter = Decimal(cnc_price_per_meter)
    
    def calculate_area(self):
        """Calculate area in square meters."""
        return (self.width * self.length) / Decimal('1000000')  # mm² to m²
    
    def calculate_cutting_length(self):
        """Calculate total cutting length in meters."""
        if not self.cnc_cutting:
            return Decimal('0')
        return (self.width * 2 + self.length * 2) / Decimal('1000')  # mm to m
    
    def calculate_material_cost(self):
        """Calculate material cost."""
        area = self.calculate_area()
        return area * self.price_per_sqm
    
    def calculate_cutting_cost(self):
        """Calculate CNC cutting cost."""
        if not self.cnc_cutting:
            return Decimal('0')
        cutting_length = self.calculate_cutting_length()
        return cutting_length * self.cnc_price_per_meter
    
    def calculate_total_cost(self):
        """Calculate total cost for this product."""
        return self.calculate_material_cost() + self.calculate_cutting_cost()

class Customer:
    """Represents a customer with their information."""
    
    def __init__(self, name, address, phone, tax_id=None):
        """
        Initialize a customer.
        
        Args:
            name (str): Customer name
            address (str): Customer address
            phone (str): Customer phone number
            tax_id (str, optional): Tax identification number
        """
        self.name = name
        self.address = address
        self.phone = phone
        self.tax_id = tax_id

class Invoice:
    """Represents an invoice with customer, products, and calculations."""
    
    def __init__(self, customer, invoice_number, date=None):
        """
        Initialize an invoice.
        
        Args:
            customer (Customer): Customer object
            invoice_number (str): Invoice number
            date (datetime.date, optional): Invoice date (defaults to today)
        """
        self.customer = customer
        self.invoice_number = invoice_number
        self.date = date if date else datetime.date.today()
        self.items = []
        self.tax_rate = Decimal('0.18')  # 18% VAT
    
    def add_item(self, product, quantity=1):
        """
        Add a product to the invoice.
        
        Args:
            product (Product): Product to add
            quantity (int): Quantity of the product
        """
        self.items.append({
            'product': product,
            'quantity': quantity
        })
    
    def calculate_subtotal(self):
        """Calculate subtotal before taxes."""
        subtotal = Decimal('0')
        for item in self.items:
            subtotal += item['product'].calculate_total_cost() * item['quantity']
        return subtotal
    
    def calculate_tax(self):
        """Calculate tax amount."""
        return self.calculate_subtotal() * self.tax_rate
    
    def calculate_total(self):
        """Calculate total amount including taxes."""
        return self.calculate_subtotal() + self.calculate_tax()
    
    def generate_invoice(self):
        """Generate a formatted invoice string."""
        invoice_lines = []
        
        # Header
        invoice_lines.append("BURSA PLEKSI MERKEZI")
        invoice_lines.append("1234 Sokak No:56, Bursa, Turkey")
        invoice_lines.append("Tel: +90 224 123 4567 | www.bursapleksi.com")
        invoice_lines.append("")
        invoice_lines.append(f"INVOICE #{self.invoice_number}")
        invoice_lines.append(f"Date: {self.date.strftime('%d/%m/%Y')}")
        invoice_lines.append("")
        
        # Customer info
        invoice_lines.append("BILL TO:")
        invoice_lines.append(f"Name: {self.customer.name}")
        invoice_lines.append(f"Address: {self.customer.address}")
        invoice_lines.append(f"Phone: {self.customer.phone}")
        if self.customer.tax_id:
            invoice_lines.append(f"Tax ID: {self.customer.tax_id}")
        invoice_lines.append("")
        
        # Items header
        invoice_lines.append("-" * 100)
        invoice_lines.append(
            "NO  DESCRIPTION           MATERIAL   THICKNESS  WIDTH  LENGTH  AREA    CNC    QTY  UNIT PRICE  AMOUNT"
        )
        invoice_lines.append("-" * 100)
        
        # Items
        for i, item in enumerate(self.items, 1):
            product = item['product']
            area = product.calculate_area()
            cutting_length = product.calculate_cutting_length()
            unit_price = product.calculate_total_cost()
            amount = unit_price * item['quantity']
            
            invoice_lines.append(
                f"{i:<3} {product.name[:20]:<20} {product.material_type[:8]:<10} "
                f"{product.thickness:<9} {product.width:<6} {product.length:<6} "
                f"{area:.3f}  {'Yes' if product.cnc_cutting else 'No':<5} "
                f"{item['quantity']:<4} {unit_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP):<10} "
                f"{amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}"
            )
        
        # Summary
        invoice_lines.append("-" * 100)
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()
        
        invoice_lines.append(f"SUBTOTAL: {subtotal.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
        invoice_lines.append(f"TAX ({self.tax_rate*100}%): {tax.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
        invoice_lines.append(f"TOTAL: {total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
        invoice_lines.append("")
        invoice_lines.append("Thank you for your business!")
        invoice_lines.append("Payment due within 15 days")
        
        return "\n".join(invoice_lines)

# Example usage
if __name__ == "__main__":
    # Create a customer
    customer = Customer(
        name="Ahmet Yılmaz",
        address="Atatürk Caddesi No:123, Osmangazi, Bursa",
        phone="+90 555 123 4567",
        tax_id="1234567890"
    )
    
    # Create an invoice
    invoice = Invoice(
        customer=customer,
        invoice_number="INV-2023-001"
    )
    
    # Add products
    product1 = Product(
        name="Clear Plexiglass",
        material_type="plexiglass",
        thickness=5,
        width=1000,
        length=2000,
        price_per_sqm=150,
        cnc_cutting=True,
        cnc_price_per_meter=5
    )
    
    product2 = Product(
        name="Polycarbonate Sheet",
        material_type="polycarbonate",
        thickness=8,
        width=1200,
        length=2400,
        price_per_sqm=220,
        cnc_cutting=False
    )
    
    invoice.add_item(product1, quantity=2)
    invoice.add_item(product2, quantity=1)
    
    # Generate and print the invoice
    print(invoice.generate_invoice())
```
