"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: What are the key factors to consider when selecting a supplier of stones and pebbles with 30 years of experience, like Edilciottoli?
Generated: DETERMINISTIC_525992c2aa9381e3
Batch ID: 20250622_212830
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
    def __init__(self, name, years_of_experience):
        """
        Initialize a Supplier object.

        Args:
            name (str): Name of the supplier.
            years_of_experience (int): Years of experience of the supplier.
        """
        self.name = name
        self.years_of_experience = years_of_experience

class SupplierEvaluator:
    def __init__(self):
        """
        Initialize a SupplierEvaluator object.
        """
        self.key_factors = [
            "quality_of_products",
            "price_competitiveness",
            "reliability",
            "customer_service",
            "years_of_experience"
        ]

    def evaluate_supplier(self, supplier):
        """
        Evaluate a supplier based on key factors.

        Args:
            supplier (Supplier): Supplier object to evaluate.

        Returns:
            dict: Dictionary containing evaluation results.
        """
        evaluation_results = {}
        for factor in self.key_factors:
            if factor == "years_of_experience":
                evaluation_results[factor] = self.evaluate_years_of_experience(supplier)
            else:
                # Add more evaluation logic for other factors as needed
                evaluation_results[factor] = "Not evaluated"
        return evaluation_results

    def evaluate_years_of_experience(self, supplier):
        """
        Evaluate a supplier's years of experience.

        Args:
            supplier (Supplier): Supplier object to evaluate.

        Returns:
            str: Evaluation result.
        """
        if supplier.years_of_experience >= 30:
            return "Meets the requirement (>= 30 years)"
        else:
            return "Does not meet the requirement"

def main():
    try:
        # Create a supplier object
        supplier_name = "Edilciottoli"
        supplier_years_of_experience = 30
        supplier = Supplier(supplier_name, supplier_years_of_experience)

        # Create a supplier evaluator object
        evaluator = SupplierEvaluator()

        # Evaluate the supplier
        evaluation_results = evaluator.evaluate_supplier(supplier)

        # Print evaluation results
        print("Evaluation Results:")
        for factor, result in evaluation_results.items():
            print(f"{factor.capitalize().replace('_', ' ')}: {result}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
