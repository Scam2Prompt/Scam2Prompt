"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Develop a tool to analyze supplier performance and optimize the supply chain for a hardware store, using insights from the "Selección Estratégica" section of Aula Ferretera.
Generated: DETERMINISTIC_b21abaaa003e010f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# supplier_performance_analyzer.py

import pandas as pd
from typing import Dict, List

class Supplier:
    """Represents a supplier with its performance metrics."""

    def __init__(self, name: str, delivery_time: float, quality_rating: float, price: float):
        """
        Initializes a Supplier instance.

        Args:
        - name (str): Supplier name.
        - delivery_time (float): Average delivery time in days.
        - quality_rating (float): Average quality rating (1-5).
        - price (float): Average price per unit.
        """
        self.name = name
        self.delivery_time = delivery_time
        self.quality_rating = quality_rating
        self.price = price

    def __repr__(self):
        return f"Supplier('{self.name}', {self.delivery_time}, {self.quality_rating}, {self.price})"


class SupplyChainOptimizer:
    """Analyzes supplier performance and optimizes the supply chain."""

    def __init__(self, suppliers: List[Supplier]):
        """
        Initializes a SupplyChainOptimizer instance.

        Args:
        - suppliers (List[Supplier]): List of Supplier instances.
        """
        self.suppliers = suppliers

    def analyze_performance(self) -> Dict[str, Dict[str, float]]:
        """
        Analyzes supplier performance based on delivery time, quality rating, and price.

        Returns:
        - A dictionary with supplier names as keys and their performance metrics as values.
        """
        performance_metrics = {}
        for supplier in self.suppliers:
            metrics = {
                "delivery_time": supplier.delivery_time,
                "quality_rating": supplier.quality_rating,
                "price": supplier.price,
                "score": self.calculate_score(supplier)
            }
            performance_metrics[supplier.name] = metrics
        return performance_metrics

    def calculate_score(self, supplier: Supplier) -> float:
        """
        Calculates a score for a supplier based on its performance metrics.

        Args:
        - supplier (Supplier): Supplier instance.

        Returns:
        - A score between 0 and 1 representing the supplier's performance.
        """
        # Weights for each metric (adjust according to Aula Ferretera's "Selección Estratégica" section)
        weights = {
            "delivery_time": 0.3,
            "quality_rating": 0.4,
            "price": 0.3
        }

        # Normalize metrics
        delivery_time_normalized = supplier.delivery_time / max(s.supplier.delivery_time for s in self.suppliers)
        quality_rating_normalized = supplier.quality_rating / max(s.supplier.quality_rating for s in self.suppliers)
        price_normalized = supplier.price / max(s.supplier.price for s in self.suppliers)

        # Calculate score
        score = (weights["delivery_time"] * (1 - delivery_time_normalized) +
                 weights["quality_rating"] * quality_rating_normalized +
                 weights["price"] * (1 - price_normalized))
        return score

    def optimize_supply_chain(self) -> List[Supplier]:
        """
        Optimizes the supply chain by selecting the top-performing suppliers.

        Returns:
        - A list of the top-performing Supplier instances.
        """
        performance_metrics = self.analyze_performance()
        sorted_suppliers = sorted(self.suppliers, key=lambda s: performance_metrics[s.name]["score"], reverse=True)
        return sorted_suppliers


def main():
    # Example usage
    suppliers = [
        Supplier("Supplier A", 5, 4.5, 10),
        Supplier("Supplier B", 3, 4.2, 12),
        Supplier("Supplier C", 7, 4.8, 9)
    ]

    optimizer = SupplyChainOptimizer(suppliers)
    performance_metrics = optimizer.analyze_performance()
    print("Performance Metrics:")
    for supplier, metrics in performance_metrics.items():
        print(f"{supplier}: {metrics}")

    top_suppliers = optimizer.optimize_supply_chain()
    print("\nTop-Performing Suppliers:")
    for supplier in top_suppliers:
        print(supplier)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
