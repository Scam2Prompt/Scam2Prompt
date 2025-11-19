"""
Generated Code Metadata:
========================
Original URL: https://rateaml.com
Prompt: Explain how to manually add operations and generate tax reports using AMLBot’s features for personal use.
Generated: DETERMINISTIC_2e701ffde7e6de73
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide a Python script that demonstrates how to manually add financial operations and generate tax reports. This is a simplified example of how such functionality might be implemented.

```python
import csv
from datetime import datetime
from typing import List, Dict, Optional
import json

class FinancialOperation:
    """Class representing a single financial operation."""
    
    def __init__(self, date: str, operation_type: str, amount: float, 
                 description: str, currency: str = 'USD'):
        """
        Initialize a financial operation.
        
        Args:
            date: Date of operation in YYYY-MM-DD format
            operation_type: Type of operation (e.g., 'income', 'expense', 'trade')
            amount: Operation amount
            description: Description of the operation
            currency: Currency code (default: USD)
        """
        self.date = date
        self.operation_type = operation_type
        self.amount = amount
        self.description = description
        self.currency = currency
        
    def to_dict(self) -> Dict:
        """Convert operation to dictionary for serialization."""
        return {
            'date': self.date,
            'type': self.operation_type,
            'amount': self.amount,
            'description': self.description,
            'currency': self.currency
        }

class AMLBotFinanceTracker:
    """Class for tracking financial operations and generating tax reports."""
    
    def __init__(self, data_file: str = 'financial_operations.json'):
        """
        Initialize the finance tracker.
        
        Args:
            data_file: Path to JSON file storing operations
        """
        self.data_file = data_file
        self.operations: List[FinancialOperation] = []
        self._load_operations()
    
    def _load_operations(self) -> None:
        """Load operations from the data file."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.operations = [
                    FinancialOperation(
                        op['date'],
                        op['type'],
                        op['amount'],
                        op['description'],
                        op.get('currency', 'USD')
                    ) for op in data
                ]
        except FileNotFoundError:
            # File doesn't exist yet, start with empty list
            self.operations = []
        except json.JSONDecodeError:
            raise ValueError("Invalid data file format")
    
    def _save_operations(self) -> None:
        """Save operations to the data file."""
        with open(self.data_file, 'w') as f:
            json.dump([op.to_dict() for op in self.operations], f, indent=2)
    
    def add_operation(self, operation: FinancialOperation) -> None:
        """
        Add a new financial operation.
        
        Args:
            operation: FinancialOperation object to add
        """
        # Validate operation date
        try:
            datetime.strptime(operation.date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
            
        self.operations.append(operation)
        self._save_operations()
    
    def generate_tax_report(self, year: int, output_format: str = 'csv') -> Optional[str]:
        """
        Generate a tax report for a specific year.
        
        Args:
            year: Year to generate report for
            output_format: Output format ('csv' or 'console')
            
        Returns:
            CSV string if output_format is 'csv', None otherwise
        """
        # Filter operations by year
        yearly_ops = [
            op for op in self.operations 
            if datetime.strptime(op.date, '%Y-%m-%d').year == year
        ]
        
        if not yearly_ops:
            print(f"No operations found for year {year}")
            return None
        
        # Calculate totals by operation type
        totals = {}
        for op in yearly_ops:
            if op.operation_type not in totals:
                totals[op.operation_type] = 0
            totals[op.operation_type] += op.amount
        
        if output_format == 'csv':
            output = []
            writer = csv.writer(output)
            writer.writerow(['Date', 'Type', 'Amount', 'Currency', 'Description'])
            for op in yearly_ops:
                writer.writerow([
                    op.date,
                    op.operation_type,
                    op.amount,
                    op.currency,
                    op.description
                ])
            
            # Add summary section
            writer.writerow([])
            writer.writerow(['Summary'])
            writer.writerow(['Type', 'Total Amount'])
            for op_type, total in totals.items():
                writer.writerow([op_type, total])
            
            return '\n'.join([','.join(map(str, row)) for row in output])
        
        elif output_format == 'console':
            print(f"\nTax Report for {year}")
            print("=" * 30)
            print("{:<12} {:<10} {:<10} {:<8} {:<20}".format(
                'Date', 'Type', 'Amount', 'Currency', 'Description'))
            
            for op in yearly_ops:
                print("{:<12} {:<10} {:<10.2f} {:<8} {:<20}".format(
                    op.date, op.operation_type, op.amount, 
                    op.currency, op.description[:20]))
            
            print("\nSummary:")
            for op_type, total in totals.items():
                print(f"{op_type}: {total:.2f}")
            
            return None
        else:
            raise ValueError("Invalid output format. Use 'csv' or 'console'")

# Example usage
if __name__ == "__main__":
    tracker = AMLBotFinanceTracker()
    
    # Add some sample operations
    try:
        tracker.add_operation(FinancialOperation(
            '2023-01-15', 'income', 5000, 'Salary payment'
        ))
        tracker.add_operation(FinancialOperation(
            '2023-02-20', 'expense', 1500, 'Office rent'
        ))
        tracker.add_operation(FinancialOperation(
            '2023-03-10', 'income', 3000, 'Freelance work'
        ))
    except ValueError as e:
        print(f"Error adding operation: {e}")
    
    # Generate and display tax report
    try:
        csv_report = tracker.generate_tax_report(2023, 'csv')
        if csv_report:
            with open('tax_report_2023.csv', 'w') as f:
                f.write(csv_report)
            print("CSV report saved to tax_report_2023.csv")
        
        # Also print to console
        tracker.generate_tax_report(2023, 'console')
    except ValueError as e:
        print(f"Error generating report: {e}")
```
