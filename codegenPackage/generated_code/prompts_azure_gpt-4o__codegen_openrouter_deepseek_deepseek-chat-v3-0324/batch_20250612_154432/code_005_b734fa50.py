"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Generate Python code to calculate alimony payments based on Brazilian legal guidelines, factoring in income, custody agreements, and other relevant parameters.
Generated: DETERMINISTIC_b734fa506afc51bb
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Alimony Calculator based on Brazilian Legal Guidelines

This module calculates alimony payments considering income, custody agreements,
and other relevant parameters as per Brazilian law.
"""

from typing import Union, Optional

class AlimonyCalculator:
    """
    A class to calculate alimony payments based on Brazilian legal guidelines.

    Attributes:
        payer_income (float): Monthly income of the payer.
        recipient_income (float): Monthly income of the recipient.
        num_children (int): Number of children involved.
        custody_type (str): Type of custody ('sole' or 'shared').
        other_expenses (float): Additional expenses (education, health, etc.).
        max_percentage (float): Maximum percentage of income for alimony (default 30%).
    """

    def __init__(
        self,
        payer_income: float,
        recipient_income: float,
        num_children: int,
        custody_type: str = "sole",
        other_expenses: float = 0,
        max_percentage: float = 30
    ):
        """
        Initialize the AlimonyCalculator with relevant parameters.

        Args:
            payer_income: Monthly income of the payer.
            recipient_income: Monthly income of the recipient.
            num_children: Number of children involved.
            custody_type: Type of custody ('sole' or 'shared').
            other_expenses: Additional expenses (education, health, etc.).
            max_percentage: Maximum percentage of income for alimony (default 30%).
        """
        self.payer_income = payer_income
        self.recipient_income = recipient_income
        self.num_children = num_children
        self.custody_type = custody_type.lower()
        self.other_expenses = other_expenses
        self.max_percentage = max_percentage

        self._validate_inputs()

    def _validate_inputs(self) -> None:
        """Validate input parameters."""
        if self.payer_income < 0:
            raise ValueError("Payer income cannot be negative.")
        if self.recipient_income < 0:
            raise ValueError("Recipient income cannot be negative.")
        if self.num_children < 0:
            raise ValueError("Number of children cannot be negative.")
        if self.custody_type not in ["sole", "shared"]:
            raise ValueError("Custody type must be 'sole' or 'shared'.")
        if self.other_expenses < 0:
            raise ValueError("Other expenses cannot be negative.")
        if not 0 <= self.max_percentage <= 100:
            raise ValueError("Max percentage must be between 0 and 100.")

    def calculate_alimony(self) -> float:
        """
        Calculate the alimony amount based on Brazilian guidelines.

        Returns:
            float: The calculated alimony amount.
        """
        # Base calculation considers payer's income and number of children
        base_amount = self.payer_income * (self.max_percentage / 100)

        # Adjust for custody type
        if self.custody_type == "shared":
            base_amount *= 0.75  # Typically reduced in shared custody

        # Adjust for recipient's income
        if self.recipient_income > 0:
            income_ratio = min(self.recipient_income / self.payer_income, 1)
            base_amount *= (1 - income_ratio * 0.5)  # Reduce by up to 50% based on recipient's income

        # Add other expenses (divided by number of children if applicable)
        if self.num_children > 0:
            base_amount += (self.other_expenses / self.num_children)
        else:
            base_amount += self.other_expenses

        # Ensure alimony doesn't exceed payer's income
        return min(base_amount, self.payer_income * 0.5)  # Cap at 50% of income


def main():
    """Example usage of the AlimonyCalculator."""
    try:
        # Example inputs
        payer_income = float(input("Enter payer's monthly income (BRL): "))
        recipient_income = float(input("Enter recipient's monthly income (BRL): "))
        num_children = int(input("Enter number of children: "))
        custody_type = input("Enter custody type (sole/shared): ")
        other_expenses = float(input("Enter additional monthly expenses (BRL): "))

        calculator = AlimonyCalculator(
            payer_income=payer_income,
            recipient_income=recipient_income,
            num_children=num_children,
            custody_type=custody_type,
            other_expenses=other_expenses
        )

        alimony = calculator.calculate_alimony()
        print(f"\nCalculated Alimony: BRL {alimony:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
