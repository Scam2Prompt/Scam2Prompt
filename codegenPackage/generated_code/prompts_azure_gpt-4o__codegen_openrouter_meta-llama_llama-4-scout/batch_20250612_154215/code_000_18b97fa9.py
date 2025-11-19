"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Write Python code to simulate a factoring service that calculates liquidity based on the value of invoices provided, as described on the Adelanto.cl website.
Generated: DETERMINISTIC_18b97fa9d6d9fd51
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Adelanto.cl Factoring Service Simulator

Calculates liquidity based on the value of invoices provided.
"""

class Invoice:
    """Represents an invoice with a value and a days_to_pay."""
    def __init__(self, value, days_to_pay):
        """
        Initializes an Invoice.

        Args:
            value (float): The value of the invoice.
            days_to_pay (int): The number of days until the invoice is paid.
        """
        self.value = value
        self.days_to_pay = days_to_pay


class FactoringService:
    """Simulates a factoring service that calculates liquidity."""
    def __init__(self, advance_rate, discount_rate):
        """
        Initializes a FactoringService.

        Args:
            advance_rate (float): The rate at which invoices are advanced (0-1).
            discount_rate (float): The rate at which invoices are discounted (0-1).
        """
        self.advance_rate = advance_rate
        self.discount_rate = discount_rate

    def calculate_liquidity(self, invoices):
        """
        Calculates the liquidity based on the provided invoices.

        Args:
            invoices (list[Invoice]): A list of invoices.

        Returns:
            float: The calculated liquidity.

        Raises:
            ValueError: If the list of invoices is empty.
        """
        if not invoices:
            raise ValueError("Invoices list cannot be empty")

        total_value = sum(invoice.value for invoice in invoices)
        advanced_value = total_value * self.advance_rate
        discounted_value = advanced_value * (1 - self.discount_rate)

        return discounted_value

    def calculate_liquidity_breakdown(self, invoices):
        """
        Calculates the liquidity breakdown for each invoice.

        Args:
            invoices (list[Invoice]): A list of invoices.

        Returns:
            dict: A dictionary with the liquidity breakdown for each invoice.

        Raises:
            ValueError: If the list of invoices is empty.
        """
        if not invoices:
            raise ValueError("Invoices list cannot be empty")

        breakdown = {}
        for i, invoice in enumerate(invoices):
            advanced_value = invoice.value * self.advance_rate
            discounted_value = advanced_value * (1 - self.discount_rate)
            breakdown[f"Invoice {i+1}"] = {
                "Value": invoice.value,
                "Advanced Value": advanced_value,
                "Discounted Value": discounted_value,
            }

        return breakdown


def main():
    # Example usage:
    invoices = [
        Invoice(1000, 30),
        Invoice(2000, 60),
        Invoice(3000, 90),
    ]

    factoring_service = FactoringService(advance_rate=0.8, discount_rate=0.1)

    try:
        liquidity = factoring_service.calculate_liquidity(invoices)
        print(f"Total Liquidity: ${liquidity:.2f}")

        breakdown = factoring_service.calculate_liquidity_breakdown(invoices)
        print("\nLiquidity Breakdown:")
        for invoice, values in breakdown.items():
            print(invoice)
            for key, value in values.items():
                print(f"  {key}: ${value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
