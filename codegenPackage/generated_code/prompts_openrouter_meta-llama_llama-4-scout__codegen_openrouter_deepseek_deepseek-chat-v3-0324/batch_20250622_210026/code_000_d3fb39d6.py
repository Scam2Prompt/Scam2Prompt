"""
Generated Code Metadata:
========================
Original URL: https://accounting-team.com
Prompt: Write a Python script to manage bookkeeping for a small business, including tracking expenses and income, and generating financial reports.
Generated: DETERMINISTIC_d3fb39d6f3c6ba75
Batch ID: 20250622_210026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional

class BookkeepingSystem:
    """
    A simple bookkeeping system for small businesses to track expenses and income.
    """
    
    def __init__(self, data_file: str = "bookkeeping_data.csv"):
        """
        Initialize the bookkeeping system with a data file.
        
        Args:
            data_file: Path to the CSV file storing transactions.
        """
        self.data_file = data_file
        self._initialize_data_file()
    
    def _initialize_data_file(self) -> None:
        """
        Create the data file with headers if it doesn't exist.
        """
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self._get_fieldnames())
                writer.writeheader()
    
    def _get_fieldnames(self) -> List[str]:
        """
        Get the fieldnames for the CSV file.
        
        Returns:
            List of fieldnames.
        """
        return ["date", "type", "category", "amount", "description"]
    
    def add_transaction(self, transaction_type: str, category: str, amount: float, description: str = "") -> None:
        """
        Add a new transaction (expense or income).
        
        Args:
            transaction_type: "expense" or "income".
            category: Category of the transaction.
            amount: Amount of money.
            description: Optional description.
            
        Raises:
            ValueError: If transaction_type is invalid or amount is negative.
        """
        if transaction_type.lower() not in ["expense", "income"]:
            raise ValueError("Transaction type must be 'expense' or 'income'")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type.lower(),
            "category": category,
            "amount": amount,
            "description": description
        }
        
        with open(self.data_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self._get_fieldnames())
            writer.writerow(transaction)
    
    def get_transactions(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Dict]:
        """
        Retrieve transactions within a date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format.
            end_date: End date in YYYY-MM-DD format.
            
        Returns:
            List of transactions as dictionaries.
            
        Raises:
            ValueError: If date format is invalid.
        """
        transactions = []
        
        try:
            with open(self.data_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    transaction_date = datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S").date()
                    
                    if start_date:
                        start = datetime.strptime(start_date, "%Y-%m-%d").date()
                        if transaction_date < start:
                            continue
                    
                    if end_date:
                        end = datetime.strptime(end_date, "%Y-%m-%d").date()
                        if transaction_date > end:
                            continue
                    
                    row["amount"] = float(row["amount"])
                    transactions.append(row)
        
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")
        
        return transactions
    
    def generate_financial_report(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict:
        """
        Generate a financial report with summary statistics.
        
        Args:
            start_date: Start date in YYYY-MM-DD format.
            end_date: End date in YYYY-MM-DD format.
            
        Returns:
            Dictionary containing financial summary.
        """
        transactions = self.get_transactions(start_date, end_date)
        
        total_income = 0.0
        total_expenses = 0.0
        income_by_category = {}
        expenses_by_category = {}
        
        for transaction in transactions:
            amount = transaction["amount"]
            category = transaction["category"]
            
            if transaction["type"] == "income":
                total_income += amount
                income_by_category[category] = income_by_category.get(category, 0) + amount
            else:
                total_expenses += amount
                expenses_by_category[category] = expenses_by_category.get(category, 0) + amount
        
        net_profit = total_income - total_expenses
        
        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_profit": net_profit,
            "income_by_category": income_by_category,
            "expenses_by_category": expenses_by_category,
            "start_date": start_date,
            "end_date": end_date
        }
    
    def export_report_to_csv(self, report: Dict, output_file: str = "financial_report.csv") -> None:
        """
        Export financial report to a CSV file.
        
        Args:
            report: Financial report dictionary.
            output_file: Path to the output CSV file.
        """
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow(["Financial Report"])
            if report.get("start_date") or report.get("end_date"):
                writer.writerow([f"Period: {report.get('start_date', 'N/A')} to {report.get('end_date', 'N/A')}"])
            
            # Write summary
            writer.writerow([])
            writer.writerow(["Summary"])
            writer.writerow(["Total Income", report["total_income"]])
            writer.writerow(["Total Expenses", report["total_expenses"]])
            writer.writerow(["Net Profit", report["net_profit"]])
            
            # Write income by category
            writer.writerow([])
            writer.writerow(["Income by Category"])
            for category, amount in report["income_by_category"].items():
                writer.writerow([category, amount])
            
            # Write expenses by category
            writer.writerow([])
            writer.writerow(["Expenses by Category"])
            for category, amount in report["expenses_by_category"].items():
                writer.writerow([category, amount])

# Example usage
if __name__ == "__main__":
    bookkeeper = BookkeepingSystem()
    
    # Add some sample transactions
    try:
        bookkeeper.add_transaction("income", "Sales", 1000.50, "Product sales")
        bookkeeper.add_transaction("expense", "Rent", 500.00, "Office rent")
        bookkeeper.add_transaction("expense", "Supplies", 75.25, "Office supplies")
        bookkeeper.add_transaction("income", "Services", 350.00, "Consulting services")
    except ValueError as e:
        print(f"Error adding transaction: {e}")
    
    # Generate and export report
    try:
        report = bookkeeper.generate_financial_report()
        print("Financial Report:")
        print(f"Total Income: ${report['total_income']:.2f}")
        print(f"Total Expenses: ${report['total_expenses']:.2f}")
        print(f"Net Profit: ${report['net_profit']:.2f}")
        
        bookkeeper.export_report_to_csv(report)
        print(f"\nReport exported to {os.path.abspath('financial_report.csv')}")
    except Exception as e:
        print(f"Error generating report: {e}")
```
