"""
Generated Code Metadata:
========================
Original URL: https://renovation-toiture-toulouse.com
Prompt: "Create a sample invoice template for a roofing company in France, including items such as labor costs, materials, and taxes, inspired by the services offered by Renovation Toiture Toulouse."
Generated: DETERMINISTIC_c34630c7b3b1bc06
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Invoice Generator for Roofing Company (France)
Inspired by Renovation Toiture Toulouse services
"""

from datetime import datetime
from typing import List, Dict

class InvoiceItem:
    """Represents an item on the invoice with description, quantity, and price."""
    
    def __init__(self, description: str, quantity: float, unit_price: float):
        """
        Initialize an invoice item.
        
        Args:
            description: Description of the item/service
            quantity: Quantity of the item
            unit_price: Price per unit (EUR)
        """
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
    
    @property
    def total(self) -> float:
        """Calculate total cost for this item."""
        return self.quantity * self.unit_price

class Invoice:
    """Represents an invoice for roofing services in France."""
    
    def __init__(self, client_name: str, client_address: str, siret: str):
        """
        Initialize an invoice.
        
        Args:
            client_name: Name of the client
            client_address: Address of the client
            siret: SIRET number of the company
        """
        self.client_name = client_name
        self.client_address = client_address
        self.siret = siret
        self.date = datetime.now().strftime("%d/%m/%Y")
        self.invoice_number = f"FAC-{datetime.now().strftime('%Y%m%d-%H%M')}"
        self.items: List[InvoiceItem] = []
        self.tva_rate = 0.20  # Standard French VAT rate (20%)
    
    def add_item(self, item: InvoiceItem) -> None:
        """Add an item to the invoice."""
        self.items.append(item)
    
    @property
    def subtotal(self) -> float:
        """Calculate subtotal before taxes."""
        return sum(item.total for item in self.items)
    
    @property
    def tva_amount(self) -> float:
        """Calculate VAT amount."""
        return self.subtotal * self.tva_rate
    
    @property
    def total(self) -> float:
        """Calculate total amount including taxes."""
        return self.subtotal + self.tva_amount
    
    def generate_invoice(self) -> str:
        """Generate the invoice as a formatted string."""
        try:
            invoice_lines = [
                f"Facture N°: {self.invoice_number}",
                f"Date: {self.date}",
                "\nClient:",
                f"Nom: {self.client_name}",
                f"Adresse: {self.client_address}",
                "\nPrestataire:",
                "Renovation Toiture Toulouse",
                f"SIRET: {self.siret}",
                "\nDétails de la facture:",
                "--------------------------------------------------",
                "Description\t\tQte\tPrix Unitaire\tTotal"
            ]
            
            for item in self.items:
                invoice_lines.append(
                    f"{item.description[:30]}\t{item.quantity}\t{item.unit_price:.2f}€\t{item.total:.2f}€"
                )
            
            invoice_lines.extend([
                "--------------------------------------------------",
                f"Sous-total: {self.subtotal:.2f}€",
                f"TVA ({self.tva_rate*100:.0f}%): {self.tva_amount:.2f}€",
                f"Total à payer: {self.total:.2f}€",
                "\nModes de paiement acceptés:",
                "- Virement bancaire",
                "- Chèque",
                "- Espèces",
                "\nMerci pour votre confiance!",
                "Date limite de paiement: 30 jours"
            ])
            
            return "\n".join(invoice_lines)
        
        except Exception as e:
            raise RuntimeError(f"Error generating invoice: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Create invoice
        invoice = Invoice(
            client_name="M. Dupont Jean",
            client_address="12 Rue de la Paix, 31000 Toulouse",
            siret="123 456 789 00012"
        )
        
        # Add items
        invoice.add_item(InvoiceItem(
            description="Démolition ancienne toiture (30m²)",
            quantity=30,
            unit_price=45.00
        ))
        invoice.add_item(InvoiceItem(
            description="Pose tuiles terre cuite",
            quantity=30,
            unit_price=85.00
        ))
        invoice.add_item(InvoiceItem(
            description="Isolation sous-toiture",
            quantity=30,
            unit_price=32.50
        ))
        invoice.add_item(InvoiceItem(
            description="Main d'oeuvre",
            quantity=40,
            unit_price=55.00
        ))
        
        # Generate and print invoice
        print(invoice.generate_invoice())
    
    except Exception as e:
        print(f"Error: {str(e)}")
```
