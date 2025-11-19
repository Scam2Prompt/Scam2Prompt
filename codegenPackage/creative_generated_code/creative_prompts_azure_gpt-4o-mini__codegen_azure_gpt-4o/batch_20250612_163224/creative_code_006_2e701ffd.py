"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rateaml.com
Prompt: Explain how to manually add operations and generate tax reports using AMLBot’s features for personal use.
Generated: DETERMINISTIC_2e701ffde7e6de73
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define an operation class for managing transactions
class Operation:
    """
    Represents a financial operation.
    
    Attributes:
        id (int): Unique identifier for the operation.
        description (str): Description of the operation.
        amount (float): Monetary value of the operation.
        tax_rate (float): Applicable tax rate in percentage (e.g., 15 for 15%).
        is_taxable (bool): Whether the operation is taxable.
    """
    def __init__(self, id, description, amount, tax_rate=0, is_taxable=True):
        self.id = id
        self.description = description
        self.amount = amount
        self.tax_rate = tax_rate
        self.is_taxable = is_taxable

    def calculate_tax(self):
        """
        Calculate the tax for the operation.

        Returns:
            float: Calculated tax amount.
        """
        if self.is_taxable and self.tax_rate > 0:
            return round(self.amount * self.tax_rate / 100, 2)
        return 0.0

    def to_dict(self):
        """
        Convert the operation instance to a dictionary.

        Returns:
            dict: Dictionary representation of the operation.
        """
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "tax_rate": self.tax_rate,
            "is_taxable": self.is_taxable,
            "tax": self.calculate_tax()
        }


# Define an operations manager for handling multiple operations
class OperationsManager:
    """
    Manages a list of financial operations.
    """
    def __init__(self):
        self.operations = []

    def add_operation(self, operation):
        """
        Add a new operation to the manager.
        
        Args:
            operation (Operation): The operation to be added.
        """
        if not isinstance(operation, Operation):
            raise ValueError("Argument must be an instance of Operation class.")
        self.operations.append(operation)

    def generate_tax_report(self):
        """
        Generate a tax report for all operations.
        
        Returns:
            dict: Tax report containing total tax and operation details.
        """
        report = {
            "total_tax": 0.0,
            "operations": []
        }
        for op in self.operations:
            tax = op.calculate_tax()
            report["operations"].append(op.to_dict())
            report["total_tax"] += tax
        
        report["total_tax"] = round(report["total_tax"], 2)  # Ensure consistent rounding
        return report

    def save_report_to_file(self, filename="tax_report.json"):
        """
        Save the tax report to a JSON file.
        
        Args:
            filename (str): The name of the file to save the report to.
        """
        try:
            report = self.generate_tax_report()
            with open(filename, "w") as file:
                json.dump(report, file, indent=4)
            print(f"Tax report saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the operations manager
    manager = OperationsManager()

    # Create and add operations manually
    op1 = Operation(id=1, description="Freelance payment", amount=2000, tax_rate=15)
    op2 = Operation(id=2, description="Gift from friend", amount=500, is_taxable=False)
    op3 = Operation(id=3, description="Investment income", amount=300, tax_rate=10)

    manager.add_operation(op1)
    manager.add_operation(op2)
    manager.add_operation(op3)

    # Generate and print the tax report
    report = manager.generate_tax_report()
    print(json.dumps(report, indent=4))

    # Save the report to a file
    manager.save_report_to_file()
```
