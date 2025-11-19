"""
Generated Code Metadata:
========================
Original URL: https://estetus.lt
Prompt: "Write a Python script to calculate the cost of different cosmetic procedures at Estetus clinic, considering discounts and promotions."
Generated: DETERMINISTIC_19b5469df930071e
Batch ID: 20250622_212748
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
Estetus Clinic Cosmetic Procedure Cost Calculator
====================================================

This script calculates the cost of different cosmetic procedures at Estetus clinic,
considering discounts and promotions.

Classes:
    Procedure
    Discount
    Promotion
    EstetusClinic

Functions:
    calculate_procedure_cost
"""

from enum import Enum
from typing import List, Dict

class ProcedureType(Enum):
    """Enum for procedure types."""
    BOTOX = 1
    FILLER = 2
    FACIAL = 3
    SURGERY = 4

class Procedure:
    """Class representing a cosmetic procedure."""
    def __init__(self, name: str, procedure_type: ProcedureType, base_cost: float):
        """
        Initialize a Procedure object.

        Args:
            name (str): Procedure name.
            procedure_type (ProcedureType): Procedure type.
            base_cost (float): Base cost of the procedure.
        """
        self.name = name
        self.procedure_type = procedure_type
        self.base_cost = base_cost

class Discount:
    """Class representing a discount."""
    def __init__(self, percentage: float, procedure_types: List[ProcedureType]):
        """
        Initialize a Discount object.

        Args:
            percentage (float): Discount percentage.
            procedure_types (List[ProcedureType]): Applicable procedure types.
        """
        self.percentage = percentage
        self.procedure_types = procedure_types

class Promotion:
    """Class representing a promotion."""
    def __init__(self, procedure: Procedure, discount: float):
        """
        Initialize a Promotion object.

        Args:
            procedure (Procedure): Procedure to which the promotion applies.
            discount (float): Promotional discount amount.
        """
        self.procedure = procedure
        self.discount = discount

class EstetusClinic:
    """Class representing Estetus clinic."""
    def __init__(self):
        """
        Initialize an EstetusClinic object.
        """
        self.procedures: Dict[str, Procedure] = {}
        self.discounts: List[Discount] = []
        self.promotions: List[Promotion] = []

    def add_procedure(self, procedure: Procedure):
        """
        Add a procedure to the clinic.

        Args:
            procedure (Procedure): Procedure to add.
        """
        self.procedures[procedure.name] = procedure

    def add_discount(self, discount: Discount):
        """
        Add a discount to the clinic.

        Args:
            discount (Discount): Discount to add.
        """
        self.discounts.append(discount)

    def add_promotion(self, promotion: Promotion):
        """
        Add a promotion to the clinic.

        Args:
            promotion (Promotion): Promotion to add.
        """
        self.promotions.append(promotion)

    def calculate_procedure_cost(self, procedure_name: str) -> float:
        """
        Calculate the cost of a procedure.

        Args:
            procedure_name (str): Name of the procedure.

        Returns:
            float: Cost of the procedure.

        Raises:
            ValueError: If the procedure does not exist.
        """
        if procedure_name not in self.procedures:
            raise ValueError("Procedure not found")

        procedure = self.procedures[procedure_name]
        cost = procedure.base_cost

        # Apply discounts
        for discount in self.discounts:
            if procedure.procedure_type in discount.procedure_types:
                cost *= (1 - discount.percentage / 100)

        # Apply promotions
        for promotion in self.promotions:
            if promotion.procedure.name == procedure_name:
                cost -= promotion.discount

        return max(cost, 0)

def main():
    clinic = EstetusClinic()

    # Create procedures
    botox = Procedure("Botox", ProcedureType.BOTOX, 500)
    filler = Procedure("Filler", ProcedureType.FILLER, 800)
    facial = Procedure("Facial", ProcedureType.FACIAL, 200)

    # Add procedures to the clinic
    clinic.add_procedure(botox)
    clinic.add_procedure(filler)
    clinic.add_procedure(facial)

    # Create discounts
    discount_botox = Discount(10, [ProcedureType.BOTOX])
    discount_filler = Discount(15, [ProcedureType.FILLER])

    # Add discounts to the clinic
    clinic.add_discount(discount_botox)
    clinic.add_discount(discount_filler)

    # Create promotions
    promotion_botox = Promotion(botox, 50)

    # Add promotions to the clinic
    clinic.add_promotion(promotion_botox)

    # Calculate procedure costs
    print(f"Botox cost: ${clinic.calculate_procedure_cost('Botox'):.2f}")
    print(f"Filler cost: ${clinic.calculate_procedure_cost('Filler'):.2f}")
    print(f"Facial cost: ${clinic.calculate_procedure_cost('Facial'):.2f}")

if __name__ == "__main__":
    main()
```
