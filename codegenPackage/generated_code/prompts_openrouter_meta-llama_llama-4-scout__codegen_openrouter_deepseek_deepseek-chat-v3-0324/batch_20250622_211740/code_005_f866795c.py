"""
Generated Code Metadata:
========================
Original URL: https://vejanoticiabrasil.online
Prompt: What are the deadlines for paying taxes on imported goods in Brazil, and what are the consequences of not paying within the given timeframe, according to the Correios and Receita Federal rules?
Generated: DETERMINISTIC_f866795c2b82593f
Batch ID: 20250622_211740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, Optional

class BrazilImportTaxDeadlines:
    """
    A class to handle tax payment deadlines for imported goods in Brazil according to
    Correios and Receita Federal rules.
    """

    def __init__(self):
        self._deadline_rules = {
            'regular': 30,  # Regular deadline in days
            'extension': 60,  # Extended deadline in days (with fine)
            'max_extension': 90  # Maximum deadline before severe penalties
        }

        self._penalties = {
            'late_payment_fee': 0.33,  # 0.33% per day
            'max_late_fee_percentage': 20,  # Maximum 20% of tax value
            'interest_rate': 0.01,  # 1% per month
            'legal_consequences': (
                "Goods may be seized, additional fines imposed, "
                "and legal action may be taken by Receita Federal"
            )
        }

    def calculate_deadline(
        self, 
        arrival_date: datetime.date, 
        extension_requested: bool = False
    ) -> Dict[str, datetime.date]:
        """
        Calculate payment deadlines based on arrival date and extension status.

        Args:
            arrival_date: Date when goods arrived in Brazil.
            extension_requested: Whether an extension was requested.

        Returns:
            Dictionary with 'regular_deadline', 'extended_deadline', and 'max_deadline'.
        """
        if not isinstance(arrival_date, datetime.date):
            raise ValueError("arrival_date must be a datetime.date object")

        regular_deadline = arrival_date + datetime.timedelta(days=self._deadline_rules['regular'])
        extended_deadline = arrival_date + datetime.timedelta(days=self._deadline_rules['extension'])
        max_deadline = arrival_date + datetime.timedelta(days=self._deadline_rules['max_extension'])

        return {
            'regular_deadline': regular_deadline,
            'extended_deadline': extended_deadline if extension_requested else None,
            'max_deadline': max_deadline
        }

    def calculate_penalties(
        self,
        tax_amount: float,
        payment_date: datetime.date,
        deadline: datetime.date
    ) -> Dict[str, Optional[float]]:
        """
        Calculate penalties for late payment.

        Args:
            tax_amount: Original tax amount due.
            payment_date: Actual payment date.
            deadline: Original deadline date.

        Returns:
            Dictionary with 'late_fee', 'interest', and 'total_amount_due'.
        """
        if payment_date <= deadline:
            return {
                'late_fee': 0.0,
                'interest': 0.0,
                'total_amount_due': tax_amount
            }

        days_late = (payment_date - deadline).days
        if days_late <= 0:
            return {
                'late_fee': 0.0,
                'interest': 0.0,
                'total_amount_due': tax_amount
            }

        # Calculate late fee (0.33% per day, capped at 20%)
        late_fee_percentage = min(
            days_late * self._penalties['late_payment_fee'],
            self._penalties['max_late_fee_percentage']
        )
        late_fee = tax_amount * (late_fee_percentage / 100)

        # Calculate interest (1% per month)
        months_late = days_late / 30  # Approximate
        interest = tax_amount * (self._penalties['interest_rate'] * months_late)

        total_amount_due = tax_amount + late_fee + interest

        return {
            'late_fee': late_fee,
            'interest': interest,
            'total_amount_due': total_amount_due
        }

    def get_legal_consequences(self) -> str:
        """
        Get description of legal consequences for missing deadlines.

        Returns:
            String describing legal consequences.
        """
        return self._penalties['legal_consequences']

# Example usage
if __name__ == "__main__":
    tax_handler = BrazilImportTaxDeadlines()

    # Example 1: Calculate deadlines
    arrival = datetime.date(2023, 1, 1)
    deadlines = tax_handler.calculate_deadline(arrival, extension_requested=True)
    print("Deadlines:", deadlines)

    # Example 2: Calculate penalties
    tax_due = 1000.00
    payment_date = datetime.date(2023, 2, 15)  # 15 days late for regular deadline
    penalties = tax_handler.calculate_penalties(tax_due, payment_date, deadlines['regular_deadline'])
    print("Penalties:", penalties)

    # Example 3: Legal consequences
    print("Legal consequences:", tax_handler.get_legal_consequences())
```
