"""
Generated Code Metadata:
========================
Original URL: https://bmi-supply.com
Prompt: What are the key factors to consider when selecting a supplier for industrial equipment, and how can I evaluate the reliability of a supplier like BMI Supply?
Generated: DETERMINISTIC_08e7f4ae1cc4d00d
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Supplier Evaluation Program

class Supplier:
    """Represents an industrial equipment supplier."""

    def __init__(self, name, reputation, quality_rating, lead_time, price):
        """
        Initializes a Supplier object.

        Args:
            name (str): Supplier name.
            reputation (str): Supplier reputation (e.g., "good", "bad").
            quality_rating (float): Supplier quality rating (0-1).
            lead_time (int): Supplier lead time in days.
            price (float): Supplier price per unit.
        """
        self.name = name
        self.reputation = reputation
        self.quality_rating = quality_rating
        self.lead_time = lead_time
        self.price = price

    def __str__(self):
        return f"{self.name} - Reputation: {self.reputation}, Quality Rating: {self.quality_rating:.2f}, Lead Time: {self.lead_time} days, Price: ${self.price:.2f}"


class SupplierEvaluator:
    """Evaluates the reliability of a supplier."""

    def __init__(self):
        self.suppliers = {}

    def add_supplier(self, supplier):
        """
        Adds a supplier to the evaluator.

        Args:
            supplier (Supplier): Supplier object.
        """
        self.suppliers[supplier.name] = supplier

    def evaluate_reliability(self, supplier_name):
        """
        Evaluates the reliability of a supplier.

        Args:
            supplier_name (str): Name of the supplier to evaluate.

        Returns:
            dict: Reliability evaluation result.

        Raises:
            ValueError: If the supplier is not found.
        """
        if supplier_name not in self.suppliers:
            raise ValueError(f"Supplier '{supplier_name}' not found.")

        supplier = self.suppliers[supplier_name]
        reliability_score = self.calculate_reliability_score(supplier)

        return {
            "supplier": supplier_name,
            "reputation": supplier.reputation,
            "quality_rating": supplier.quality_rating,
            "lead_time": supplier.lead_time,
            "price": supplier.price,
            "reliability_score": reliability_score,
        }

    @staticmethod
    def calculate_reliability_score(supplier):
        """
        Calculates a reliability score based on supplier attributes.

        Args:
            supplier (Supplier): Supplier object.

        Returns:
            float: Reliability score (0-1).
        """
        # Weighting factors for each attribute
        reputation_weight = 0.3
        quality_rating_weight = 0.3
        lead_time_weight = 0.2
        price_weight = 0.2

        # Normalize reputation (good = 1, bad = 0)
        reputation_score = 1 if supplier.reputation == "good" else 0

        # Calculate reliability score
        reliability_score = (
            reputation_weight * reputation_score
            + quality_rating_weight * supplier.quality_rating
            + lead_time_weight * (1 - supplier.lead_time / 100)
            + price_weight * (1 - supplier.price / 1000)
        )

        return reliability_score


def main():
    evaluator = SupplierEvaluator()

    # Create suppliers
    bmi_supply = Supplier("BMI Supply", "good", 0.9, 30, 500)
    competitor_supply = Supplier("Competitor Supply", "bad", 0.7, 60, 400)

    # Add suppliers to evaluator
    evaluator.add_supplier(bmi_supply)
    evaluator.add_supplier(competitor_supply)

    # Evaluate reliability of BMI Supply
    try:
        result = evaluator.evaluate_reliability("BMI Supply")
        print("Reliability Evaluation Result:")
        for key, value in result.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
