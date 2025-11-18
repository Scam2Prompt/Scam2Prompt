"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Write Python code to calculate cash flow improvements using invoice factoring, referencing the financial calculators provided by Summar Financial.
Generated: DETERMINISTIC_a3b7bc0a7c17aaa5
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvoiceFactoring:
    """
    A class to calculate cash flow improvements using invoice factoring.

    Attributes:
        invoice_amount (float): The total amount of the invoices to be factored.
        factoring_fee (float): The fee charged by the factoring company (as a percentage).
        advance_rate (float): The percentage of the invoice amount that is advanced upfront.
    """

    def __init__(self, invoice_amount: float, factoring_fee: float, advance_rate: float):
        """
        Initializes the InvoiceFactoring with the provided parameters.

        Args:
            invoice_amount (float): The total amount of the invoices.
            factoring_fee (float): The fee charged by the factoring company (as a percentage).
            advance_rate (float): The percentage of the invoice amount to be advanced.

        Raises:
            ValueError: If any of the parameters are not valid (e.g., negative values).
        """
        if invoice_amount < 0 or factoring_fee < 0 or advance_rate < 0:
            raise ValueError("Invoice amount, factoring fee, and advance rate must be non-negative.")

        self.invoice_amount = invoice_amount
        self.factoring_fee = factoring_fee / 100  # Convert percentage to decimal
        self.advance_rate = advance_rate / 100      # Convert percentage to decimal

    def calculate_cash_flow(self) -> float:
        """
        Calculates the cash flow improvement from invoice factoring.

        Returns:
            float: The amount of cash flow improvement.

        Raises:
            ValueError: If advance rate exceeds 1.0 (100%).
        """
        if self.advance_rate > 1.0:
            raise ValueError("Advance rate cannot exceed 100%.")

        # Calculate the factoring fee
        total_fee = self.invoice_amount * self.factoring_fee
        
        # Calculate the amount advanced to the business
        amount_advanced = self.invoice_amount * self.advance_rate
        
        # Calculate cash flow improvement
        cash_flow_improvement = amount_advanced - total_fee
        
        return cash_flow_improvement

    def display_results(self):
        """
        Displays the results of the cash flow calculations in a readable format.
        """
        try:
            cash_flow_improvement = self.calculate_cash_flow()
            print(f"Total Invoice Amount: ${self.invoice_amount:.2f}")
            print(f"Factoring Fee (%): {self.factoring_fee * 100:.2f}%")
            print(f"Advance Rate (%): {self.advance_rate * 100:.2f}%")
            print(f"Cash Flow Improvement: ${cash_flow_improvement:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample values
        factoring = InvoiceFactoring(invoice_amount=10000, factoring_fee=5, advance_rate=80)
        # Display the results
        factoring.display_results()
    except ValueError as e:
        print(f"Initialization error: {e}")
```
