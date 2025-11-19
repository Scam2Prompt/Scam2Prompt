"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Write code to simulate the benefits of debt-free funding solutions by converting accounts receivable into immediate cash flow, as described by Summar Financial.
Generated: DETERMINISTIC_1920b19859084750
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulate the benefits of debt-free funding solutions by converting accounts receivable into immediate cash flow.
This is based on the Summar Financial model.
"""

import datetime
from dataclasses import dataclass
from typing import List, Optional
from decimal import Decimal, getcontext

# Set precision for financial calculations
getcontext().prec = 6

@dataclass
class Invoice:
    """Represents an outstanding invoice."""
    invoice_id: str
    customer_name: str
    amount: Decimal
    due_date: datetime.date
    discount_rate: Optional[Decimal] = None

@dataclass
class FundingSimulationResult:
    """Results of the funding simulation."""
    total_receivables: Decimal
    total_funding: Decimal
    total_discount: Decimal
    net_cash_flow: Decimal
    funding_date: datetime.date
    funded_invoices: List[Invoice]

class FundingSimulator:
    """
    Simulates converting accounts receivable into immediate cash flow.
    """
    
    def __init__(self, invoices: List[Invoice], funding_date: datetime.date):
        """
        Initialize the simulator with invoices and funding date.
        
        Args:
            invoices: List of outstanding invoices
            funding_date: Date when funding would occur
        """
        self.invoices = invoices
        self.funding_date = funding_date
    
    def calculate_discount(self, invoice: Invoice, annual_discount_rate: Decimal) -> Decimal:
        """
        Calculate discount for early payment of an invoice.
        
        Args:
            invoice: The invoice to calculate discount for
            annual_discount_rate: Annual discount rate (e.g., 0.15 for 15%)
            
        Returns:
            Decimal: Calculated discount amount
        """
        days_early = (invoice.due_date - self.funding_date).days
        if days_early <= 0:
            return Decimal(0)
        
        daily_rate = annual_discount_rate / Decimal(365)
        discount_rate = daily_rate * Decimal(days_early)
        return invoice.amount * discount_rate
    
    def simulate_funding(self, annual_discount_rate: Decimal) -> FundingSimulationResult:
        """
        Simulate funding scenario with given discount rate.
        
        Args:
            annual_discount_rate: Annual discount rate to apply
            
        Returns:
            FundingSimulationResult: Simulation results
        """
        total_receivables = Decimal(0)
        total_funding = Decimal(0)
        total_discount = Decimal(0)
        funded_invoices = []
        
        for invoice in self.invoices:
            total_receivables += invoice.amount
            
            discount = self.calculate_discount(invoice, annual_discount_rate)
            funding_amount = invoice.amount - discount
            
            total_funding += funding_amount
            total_discount += discount
            
            funded_invoice = Invoice(
                invoice_id=invoice.invoice_id,
                customer_name=invoice.customer_name,
                amount=funding_amount,
                due_date=invoice.due_date,
                discount_rate=discount / invoice.amount if invoice.amount else Decimal(0)
            )
            funded_invoices.append(funded_invoice)
        
        return FundingSimulationResult(
            total_receivables=total_receivables,
            total_funding=total_funding,
            total_discount=total_discount,
            net_cash_flow=total_funding,
            funding_date=self.funding_date,
            funded_invoices=funded_invoices
        )

def main():
    """Example usage of the funding simulator."""
    # Sample data
    today = datetime.date.today()
    invoices = [
        Invoice("INV001", "Acme Corp", Decimal("10000.00"), today + datetime.timedelta(days=30)),
        Invoice("INV002", "Globex Inc", Decimal("25000.00"), today + datetime.timedelta(days=45)),
        Invoice("INV003", "Soylent Corp", Decimal("15000.00"), today + datetime.timedelta(days=60)),
    ]
    
    # Simulate funding
    simulator = FundingSimulator(invoices, today)
    result = simulator.simulate_funding(Decimal("0.12"))  # 12% annual discount rate
    
    # Print results
    print(f"Funding Simulation Results ({result.funding_date})")
    print(f"Total Receivables: ${result.total_receivables:,.2f}")
    print(f"Total Funding: ${result.total_funding:,.2f}")
    print(f"Total Discount: ${result.total_discount:,.2f}")
    print(f"Net Cash Flow: ${result.net_cash_flow:,.2f}")
    
    print("\nFunded Invoices:")
    for invoice in result.funded_invoices:
        print(f"{invoice.invoice_id}: {invoice.customer_name} - "
              f"Original: ${invoice.amount + invoice.discount * invoice.amount:,.2f}, "
              f"Funded: ${invoice.amount:,.2f}, "
              f"Discount: {invoice.discount_rate * 100:.2f}%")

if __name__ == "__main__":
    main()
```
