"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: "Write a Python script to manage and track the financial obligations of a company undergoing insolvency, considering the Czech insolvency law."
Generated: DETERMINISTIC_5da507f03c93fbbb
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Insolvency Financial Obligations Manager

This script manages and tracks the financial obligations of a company undergoing insolvency,
considering the Czech insolvency law.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
from enum import Enum
from typing import List, Dict

class InsolvencyStatus(Enum):
    """Insolvency status of a creditor"""
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
    PAID = 4

class Creditor:
    """Represents a creditor in the insolvency process"""
    def __init__(self, name: str, amount: float):
        """
        Initializes a Creditor object.

        Args:
            name (str): Name of the creditor
            amount (float): Amount owed to the creditor
        """
        self.name = name
        self.amount = amount
        self.status = InsolvencyStatus.PENDING

class InsolvencyManager:
    """Manages and tracks financial obligations during insolvency"""
    def __init__(self):
        self.creditors: Dict[str, Creditor] = {}
        self.insolvency_start_date = datetime.date.today()

    def add_creditor(self, creditor: Creditor):
        """
        Adds a creditor to the insolvency process.

        Args:
            creditor (Creditor): Creditor object to add
        """
        self.creditors[creditor.name] = creditor

    def update_creditor_status(self, name: str, status: InsolvencyStatus):
        """
        Updates the status of a creditor.

        Args:
            name (str): Name of the creditor
            status (InsolvencyStatus): New status of the creditor

        Raises:
            ValueError: If the creditor does not exist
        """
        if name not in self.creditors:
            raise ValueError("Creditor not found")
        self.creditors[name].status = status

    def get_total_creditors_amount(self) -> float:
        """
        Calculates the total amount owed to all creditors.

        Returns:
            float: Total amount owed
        """
        return sum(creditor.amount for creditor in self.creditors.values())

    def get_paid_creditors_amount(self) -> float:
        """
        Calculates the total amount owed to paid creditors.

        Returns:
            float: Total amount owed to paid creditors
        """
        return sum(creditor.amount for creditor in self.creditors.values() if creditor.status == InsolvencyStatus.PAID)

    def generate_insolvency_report(self):
        """
        Generates an insolvency report.

        Returns:
            str: Insolvency report
        """
        report = "Insolvency Report\n"
        report += f"Start Date: {self.insolvency_start_date}\n"
        report += "Creditors:\n"
        for creditor in self.creditors.values():
            report += f"- {creditor.name}: {creditor.amount} ({creditor.status.name})\n"
        report += f"Total Amount: {self.get_total_creditors_amount()}\n"
        report += f"Paid Amount: {self.get_paid_creditors_amount()}\n"
        return report

def main():
    try:
        # Create an insolvency manager
        manager = InsolvencyManager()

        # Create creditors
        creditor1 = Creditor("Creditor 1", 10000.0)
        creditor2 = Creditor("Creditor 2", 20000.0)

        # Add creditors to the manager
        manager.add_creditor(creditor1)
        manager.add_creditor(creditor2)

        # Update creditor status
        manager.update_creditor_status("Creditor 1", InsolvencyStatus.APPROVED)
        manager.update_creditor_status("Creditor 2", InsolvencyStatus.PAID)

        # Generate insolvency report
        report = manager.generate_insolvency_report()
        print(report)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
