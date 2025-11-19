"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Write a Python code snippet to calculate the benefits of using freight factoring for a small trucking company, considering same-day funding and non-recourse programs.
Generated: DETERMINISTIC_a83d46ee9ce6c9e2
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# freight_factoring_calculator.py

class FreightFactoringCalculator:
    """
    Calculates the benefits of using freight factoring for a small trucking company.

    Attributes:
        invoice_amount (float): The total invoice amount.
        factoring_fee (float): The factoring fee as a percentage.
        advance_rate (float): The advance rate as a percentage.
        same_day_funding_fee (float): The same-day funding fee.
        non_recourse_fee (float): The non-recourse fee.
    """

    def __init__(self, invoice_amount, factoring_fee, advance_rate, same_day_funding_fee, non_recourse_fee):
        """
        Initializes the FreightFactoringCalculator.

        Args:
            invoice_amount (float): The total invoice amount.
            factoring_fee (float): The factoring fee as a percentage.
            advance_rate (float): The advance rate as a percentage.
            same_day_funding_fee (float): The same-day funding fee.
            non_recourse_fee (float): The non-recourse fee.
        """
        self.invoice_amount = invoice_amount
        self.factoring_fee = factoring_fee / 100  # convert to decimal
        self.advance_rate = advance_rate / 100  # convert to decimal
        self.same_day_funding_fee = same_day_funding_fee / 100  # convert to decimal
        self.non_recourse_fee = non_recourse_fee / 100  # convert to decimal

    def calculate_factoring_fee(self):
        """
        Calculates the factoring fee.

        Returns:
            float: The factoring fee.
        """
        return self.invoice_amount * self.factoring_fee

    def calculate_advance(self):
        """
        Calculates the advance amount.

        Returns:
            float: The advance amount.
        """
        return self.invoice_amount * self.advance_rate

    def calculate_same_day_funding_fee(self):
        """
        Calculates the same-day funding fee.

        Returns:
            float: The same-day funding fee.
        """
        return self.invoice_amount * self.same_day_funding_fee

    def calculate_non_recourse_fee(self):
        """
        Calculates the non-recourse fee.

        Returns:
            float: The non-recourse fee.
        """
        return self.invoice_amount * self.non_recourse_fee

    def calculate_total_cost(self):
        """
        Calculates the total cost.

        Returns:
            float: The total cost.
        """
        return (self.calculate_factoring_fee() +
                self.calculate_same_day_funding_fee() +
                self.calculate_non_recourse_fee())

    def calculate_net_advance(self):
        """
        Calculates the net advance amount.

        Returns:
            float: The net advance amount.
        """
        return self.calculate_advance() - self.calculate_total_cost()

    def calculate_benefit(self, current_funding_time, current_funding_cost):
        """
        Calculates the benefit of using freight factoring.

        Args:
            current_funding_time (int): The current funding time in days.
            current_funding_cost (float): The current funding cost.

        Returns:
            dict: A dictionary containing the benefit details.
        """
        benefit_details = {
            'current_funding_time': current_funding_time,
            'current_funding_cost': current_funding_cost,
            'factoring_fee': self.calculate_factoring_fee(),
            'advance': self.calculate_advance(),
            'same_day_funding_fee': self.calculate_same_day_funding_fee(),
            'non_recourse_fee': self.calculate_non_recourse_fee(),
            'total_cost': self.calculate_total_cost(),
            'net_advance': self.calculate_net_advance(),
            'benefit': self.calculate_net_advance() - (current_funding_cost * (current_funding_time / 365))
        }
        return benefit_details


def main():
    try:
        invoice_amount = 10000.0
        factoring_fee = 2.5
        advance_rate = 80.0
        same_day_funding_fee = 0.5
        non_recourse_fee = 1.0
        current_funding_time = 30
        current_funding_cost = 500.0

        calculator = FreightFactoringCalculator(invoice_amount, factoring_fee, advance_rate, same_day_funding_fee, non_recourse_fee)
        benefit_details = calculator.calculate_benefit(current_funding_time, current_funding_cost)

        print("Benefit Details:")
        for key, value in benefit_details.items():
            print(f"{key.capitalize().replace('_', ' ')}: ${value:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
