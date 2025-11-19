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
import json
from typing import Dict, List, Optional, Union

class CosmeticProcedureCalculator:
    """
    A class to calculate the cost of cosmetic procedures at Estetus clinic,
    considering discounts and promotions.
    """

    def __init__(self, procedures_file: str = "procedures.json"):
        """
        Initialize the calculator with procedure data.

        Args:
            procedures_file: Path to JSON file containing procedure data.
        """
        self.procedures = self._load_procedures(procedures_file)
        self.active_promotions = {}

    def _load_procedures(self, file_path: str) -> Dict[str, Dict]:
        """
        Load procedure data from JSON file.

        Args:
            file_path: Path to JSON file.

        Returns:
            Dictionary of procedures with their details.

        Raises:
            FileNotFoundError: If the file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Procedures file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON in procedures file", file_path, 0)

    def add_promotion(self, procedure_name: str, discount_percent: float, 
                     valid_until: Optional[str] = None) -> None:
        """
        Add a promotion for a specific procedure.

        Args:
            procedure_name: Name of the procedure.
            discount_percent: Discount percentage (0-100).
            valid_until: Optional expiration date (YYYY-MM-DD format).
        """
        if procedure_name not in self.procedures:
            raise ValueError(f"Procedure '{procedure_name}' not found")

        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")

        self.active_promotions[procedure_name] = {
            'discount_percent': discount_percent,
            'valid_until': valid_until
        }

    def remove_promotion(self, procedure_name: str) -> None:
        """
        Remove an active promotion.

        Args:
            procedure_name: Name of the procedure to remove promotion for.
        """
        if procedure_name in self.active_promotions:
            del self.active_promotions[procedure_name]

    def calculate_cost(self, procedure_name: str, 
                      quantity: int = 1) -> Union[float, None]:
        """
        Calculate the total cost for a procedure, considering promotions.

        Args:
            procedure_name: Name of the procedure.
            quantity: Number of procedures (default: 1).

        Returns:
            Total cost after discounts, or None if procedure not found.
        """
        if procedure_name not in self.procedures:
            return None

        base_price = self.procedures[procedure_name]['price']
        total_cost = base_price * quantity

        # Apply promotion if available
        if procedure_name in self.active_promotions:
            promotion = self.active_promotions[procedure_name]
            discount = promotion['discount_percent'] / 100
            total_cost *= (1 - discount)

        return round(total_cost, 2)

    def calculate_multiple(self, procedures: List[Dict[str, Union[str, int]]]) -> Dict:
        """
        Calculate costs for multiple procedures in a single transaction.

        Args:
            procedures: List of dictionaries with 'name' and 'quantity' keys.

        Returns:
            Dictionary with 'total_cost', 'breakdown', and 'savings'.
        """
        total_cost = 0.0
        breakdown = []
        total_savings = 0.0

        for item in procedures:
            procedure_name = item['name']
            quantity = item.get('quantity', 1)

            if procedure_name not in self.procedures:
                continue

            base_price = self.procedures[procedure_name]['price']
            original_cost = base_price * quantity
            discounted_cost = self.calculate_cost(procedure_name, quantity)
            
            if discounted_cost is None:
                continue

            savings = original_cost - discounted_cost
            total_cost += discounted_cost
            total_savings += savings

            breakdown.append({
                'procedure': procedure_name,
                'quantity': quantity,
                'original_price': round(base_price, 2),
                'discounted_price': round(discounted_cost, 2),
                'savings': round(savings, 2)
            })

        return {
            'total_cost': round(total_cost, 2),
            'breakdown': breakdown,
            'total_savings': round(total_savings, 2)
        }

# Example usage
if __name__ == "__main__":
    try:
        calculator = CosmeticProcedureCalculator()

        # Add some promotions
        calculator.add_promotion("Botox", 15)  # 15% off Botox
        calculator.add_promotion("Lip Fillers", 20, "2023-12-31")  # 20% off until end of year

        # Calculate single procedure cost
        botox_cost = calculator.calculate_cost("Botox")
        print(f"Cost for Botox: ${botox_cost}")

        # Calculate multiple procedures
        procedures = [
            {"name": "Botox", "quantity": 2},
            {"name": "Lip Fillers", "quantity": 1},
            {"name": "Chemical Peel", "quantity": 1}
        ]
        result = calculator.calculate_multiple(procedures)
        print("\nMultiple Procedures Calculation:")
        print(f"Total Cost: ${result['total_cost']}")
        print(f"Total Savings: ${result['total_savings']}")
        print("\nBreakdown:")
        for item in result['breakdown']:
            print(f"{item['procedure']} (x{item['quantity']}): "
                  f"${item['discounted_price']} (saved ${item['savings']})")

    except Exception as e:
        print(f"Error: {e}")
```
