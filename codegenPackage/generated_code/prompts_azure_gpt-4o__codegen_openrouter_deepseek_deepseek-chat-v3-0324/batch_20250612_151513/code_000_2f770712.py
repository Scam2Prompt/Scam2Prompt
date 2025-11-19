"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Write Python code to generate a monthly profit and loss report for a small business, including fields for income, expenses, and net profit, as described in the services offered by Hispanic Services.
Generated: DETERMINISTIC_2f770712e9c2b93f
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import List, Dict, Optional

class ProfitLossReport:
    """Generate a monthly profit and loss report for a small business."""
    
    def __init__(self, business_name: str, month: int, year: int):
        """
        Initialize the report with business details and reporting period.
        
        Args:
            business_name: Name of the business
            month: Month number (1-12)
            year: Year (e.g., 2023)
        """
        self.business_name = business_name
        self.month = month
        self.year = year
        self.income_items: List[Dict[str, float]] = []
        self.expense_items: List[Dict[str, float]] = []
        
    def add_income(self, description: str, amount: float) -> None:
        """Add an income item to the report."""
        if amount <= 0:
            raise ValueError("Income amount must be positive")
        self.income_items.append({"description": description, "amount": amount})
        
    def add_expense(self, description: str, amount: float) -> None:
        """Add an expense item to the report."""
        if amount <= 0:
            raise ValueError("Expense amount must be positive")
        self.expense_items.append({"description": description, "amount": amount})
        
    def calculate_total_income(self) -> float:
        """Calculate the total income from all income items."""
        return sum(item["amount"] for item in self.income_items)
    
    def calculate_total_expenses(self) -> float:
        """Calculate the total expenses from all expense items."""
        return sum(item["amount"] for item in self.expense_items)
    
    def calculate_net_profit(self) -> float:
        """Calculate the net profit (income - expenses)."""
        return self.calculate_total_income() - self.calculate_total_expenses()
    
    def generate_report(self, output_format: str = "text") -> Optional[str]:
        """
        Generate the report in the specified format.
        
        Args:
            output_format: Format of the report ("text", "csv")
            
        Returns:
            The report as a string (for text format) or None (for CSV)
        """
        if output_format not in ["text", "csv"]:
            raise ValueError("Invalid output format. Choose 'text' or 'csv'.")
            
        month_name = datetime.strptime(str(self.month), "%m").strftime("%B")
        report_title = f"{self.business_name} - Profit & Loss Report for {month_name} {self.year}"
        
        if output_format == "text":
            report_lines = [
                "=" * len(report_title),
                report_title,
                "=" * len(report_title),
                "\nINCOME:",
            ]
            
            for item in self.income_items:
                report_lines.append(f"- {item['description']}: ${item['amount']:.2f}")
                
            report_lines.append(f"\nTotal Income: ${self.calculate_total_income():.2f}")
            report_lines.append("\nEXPENSES:")
            
            for item in self.expense_items:
                report_lines.append(f"- {item['description']}: ${item['amount']:.2f}")
                
            report_lines.append(f"\nTotal Expenses: ${self.calculate_total_expenses():.2f}")
            report_lines.append("\nNET PROFIT:")
            net_profit = self.calculate_net_profit()
            profit_status = "Profit" if net_profit >= 0 else "Loss"
            report_lines.append(f"{profit_status}: ${abs(net_profit):.2f}")
            
            return "\n".join(report_lines)
            
        elif output_format == "csv":
            filename = f"profit_loss_{self.business_name.lower().replace(' ', '_')}_{month_name.lower()}_{self.year}.csv"
            
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([report_title])
                writer.writerow([])
                writer.writerow(["Type", "Description", "Amount"])
                
                for item in self.income_items:
                    writer.writerow(["Income", item["description"], item["amount"]])
                    
                writer.writerow(["Total Income", "", self.calculate_total_income()])
                writer.writerow([])
                
                for item in self.expense_items:
                    writer.writerow(["Expense", item["description"], item["amount"]])
                    
                writer.writerow(["Total Expenses", "", self.calculate_total_expenses()])
                writer.writerow([])
                writer.writerow(["Net Profit", "", self.calculate_net_profit()])
                
            return None

# Example usage
if __name__ == "__main__":
    report = ProfitLossReport("Hispanic Services", 10, 2023)
    
    # Add income items
    report.add_income("Consulting Services", 5000.00)
    report.add_income("Product Sales", 3200.50)
    report.add_income("Other Income", 200.00)
    
    # Add expense items
    report.add_expense("Rent", 1200.00)
    report.add_expense("Salaries", 2500.00)
    report.add_expense("Utilities", 300.75)
    report.add_expense("Supplies", 150.25)
    
    # Generate and print text report
    text_report = report.generate_report("text")
    print(text_report)
    
    # Generate CSV report
    report.generate_report("csv")
```
