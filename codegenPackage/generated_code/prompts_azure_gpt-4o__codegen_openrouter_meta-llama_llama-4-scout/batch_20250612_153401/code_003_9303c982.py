"""
Generated Code Metadata:
========================
Original URL: https://sif.com.bo
Prompt: Create a Python program to manage preventive, administrative, extrajudicial, and judicial debt collection processes, inspired by the cobranzas services described on SIF's site.
Generated: DETERMINISTIC_9303c9821654e6a5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# debt_collection.py

from enum import Enum
from typing import Dict, List

class DebtCollectionStatus(Enum):
    """Debt collection status"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    FAILED = 4

class DebtCollectionType(Enum):
    """Debt collection type"""
    PREVENTIVE = 1
    ADMINISTRATIVE = 2
    EXTRAJUDICIAL = 3
    JUDICIAL = 4

class Debt:
    """Debt entity"""
    def __init__(self, id: int, amount: float, collection_type: DebtCollectionType):
        self.id = id
        self.amount = amount
        self.collection_type = collection_type
        self.status = DebtCollectionStatus.PENDING

class DebtCollectionProcess:
    """Debt collection process"""
    def __init__(self):
        self.debts: Dict[int, Debt] = {}

    def add_debt(self, debt: Debt):
        """Add debt to the collection process"""
        self.debts[debt.id] = debt

    def update_debt_status(self, debt_id: int, status: DebtCollectionStatus):
        """Update debt status"""
        if debt_id in self.debts:
            self.debts[debt_id].status = status
        else:
            raise ValueError("Debt not found")

    def get_debt(self, debt_id: int) -> Debt:
        """Get debt by ID"""
        return self.debts.get(debt_id)

    def get_debts_by_collection_type(self, collection_type: DebtCollectionType) -> List[Debt]:
        """Get debts by collection type"""
        return [debt for debt in self.debts.values() if debt.collection_type == collection_type]

def main():
    try:
        # Create debt collection process
        process = DebtCollectionProcess()

        # Create debts
        debt1 = Debt(1, 1000.0, DebtCollectionType.PREVENTIVE)
        debt2 = Debt(2, 2000.0, DebtCollectionType.ADMINISTRATIVE)
        debt3 = Debt(3, 3000.0, DebtCollectionType.EXTRAJUDICIAL)

        # Add debts to the collection process
        process.add_debt(debt1)
        process.add_debt(debt2)
        process.add_debt(debt3)

        # Update debt status
        process.update_debt_status(1, DebtCollectionStatus.IN_PROGRESS)

        # Get debt by ID
        debt = process.get_debt(2)
        print(f"Debt {debt.id}: {debt.amount}, Status: {debt.status.name}")

        # Get debts by collection type
        debts = process.get_debts_by_collection_type(DebtCollectionType.PREVENTIVE)
        print("Preventive debts:")
        for debt in debts:
            print(f"Debt {debt.id}: {debt.amount}, Status: {debt.status.name}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
