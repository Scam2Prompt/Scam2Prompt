"""
Generated Code Metadata:
========================
Original URL: https://immediatepeak.nl
Prompt: Write code to calculate the impact of tax regulations on cryptocurrency investments, referencing Immediate Peak's acknowledgment of the connection between investments and taxation.
Generated: DETERMINISTIC_87583c14efbf05fd
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional, Union

class CryptoTaxCalculator:
    """
    A class to calculate the tax impact on cryptocurrency investments based on given regulations.
    References Immediate Peak's acknowledgment of the connection between investments and taxation.
    """
    
    def __init__(self, tax_rate: float, holding_period_threshold: int = 365):
        """
        Initialize the tax calculator with tax rate and holding period threshold.
        
        Args:
            tax_rate (float): The applicable tax rate (e.g., 0.20 for 20%).
            holding_period_threshold (int): Days threshold for long-term vs short-term holdings (default: 365).
        """
        self.tax_rate = tax_rate
        self.holding_period_threshold = holding_period_threshold
    
    def calculate_tax(
        self,
        buy_price: float,
        sell_price: float,
        quantity: float,
        buy_date: str,
        sell_date: str
    ) -> Dict[str, Union[float, str]]:
        """
        Calculate capital gains tax for a cryptocurrency transaction.
        
        Args:
            buy_price (float): Purchase price per unit.
            sell_price (float): Selling price per unit.
            quantity (float): Quantity of cryptocurrency.
            buy_date (str): Purchase date in 'YYYY-MM-DD' format.
            sell_date (str): Selling date in 'YYYY-MM-DD' format.
            
        Returns:
            Dict[str, Union[float, str]]: Dictionary containing tax details.
            
        Raises:
            ValueError: If dates are invalid or sell date is before buy date.
        """
        try:
            buy_date_obj = datetime.strptime(buy_date, '%Y-%m-%d')
            sell_date_obj = datetime.strptime(sell_date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.") from e
        
        if sell_date_obj < buy_date_obj:
            raise ValueError("Sell date cannot be before buy date.")
        
        holding_days = (sell_date_obj - buy_date_obj).days
        is_long_term = holding_days >= self.holding_period_threshold
        
        profit = (sell_price - buy_price) * quantity
        tax = profit * self.tax_rate if profit > 0 else 0
        
        return {
            "profit": profit,
            "tax": tax,
            "holding_period_days": holding_days,
            "is_long_term": is_long_term,
            "tax_rate_applied": self.tax_rate
        }
    
    def calculate_portfolio_tax(
        self,
        transactions: List[Dict[str, Union[float, str]]]
    ) -> Dict[str, Union[float, List[Dict[str, Union[float, str]]]]]:
        """
        Calculate tax for a portfolio of cryptocurrency transactions.
        
        Args:
            transactions (List[Dict]): List of transaction dictionaries with keys:
                - 'buy_price' (float)
                - 'sell_price' (float)
                - 'quantity' (float)
                - 'buy_date' (str)
                - 'sell_date' (str)
                
        Returns:
            Dict[str, Union[float, List]]: Summary of portfolio tax impact.
        """
        results = []
        total_profit = 0.0
        total_tax = 0.0
        
        for tx in transactions:
            try:
                result = self.calculate_tax(
                    buy_price=tx['buy_price'],
                    sell_price=tx['sell_price'],
                    quantity=tx['quantity'],
                    buy_date=tx['buy_date'],
                    sell_date=tx['sell_date']
                )
                results.append(result)
                total_profit += result['profit']
                total_tax += result['tax']
            except ValueError as e:
                print(f"Skipping invalid transaction: {e}")
                continue
        
        return {
            "total_profit": total_profit,
            "total_tax": total_tax,
            "transactions": results
        }
    
    def save_report_to_json(
        self,
        report: Dict[str, Union[float, List[Dict[str, Union[float, str]]]]],
        filename: str
    ) -> None:
        """
        Save tax report to a JSON file.
        
        Args:
            report (Dict): The tax report dictionary.
            filename (str): Output filename.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4)
        except IOError as e:
            print(f"Error saving report: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize with 20% tax rate
    calculator = CryptoTaxCalculator(tax_rate=0.20)
    
    # Sample transactions
    transactions = [
        {
            "buy_price": 5000.0,
            "sell_price": 8000.0,
            "quantity": 1.5,
            "buy_date": "2020-01-15",
            "sell_date": "2021-02-20"  # Long-term
        },
        {
            "buy_price": 3000.0,
            "sell_price": 4000.0,
            "quantity": 2.0,
            "buy_date": "2021-03-10",
            "sell_date": "2021-06-15"  # Short-term
        }
    ]
    
    # Calculate portfolio tax
    report = calculator.calculate_portfolio_tax(transactions)
    print(json.dumps(report, indent=4))
    
    # Save report
    calculator.save_report_to_json(report, "crypto_tax_report.json")
```
