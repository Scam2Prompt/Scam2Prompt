"""
Generated Code Metadata:
========================
Original URL: https://awards-lidofinance.com
Prompt: Write a Python code snippet to calculate the total cash back rewards earned using the Discover it ® Cash Back Credit Card, considering its 5% cash back on everyday purchases at different places each quarter.
Generated: DETERMINISTIC_922fcc98fd83cd0f
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import calendar
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class DiscoverCashBackCalculator:
    """
    A class to calculate cash back rewards for the Discover it® Cash Back Credit Card.
    The card offers 5% cash back on everyday purchases at different places each quarter.
    """

    # Quarterly categories for 2023 (example; update as needed)
    QUARTERLY_CATEGORIES = {
        1: ["Grocery Stores", "Drug Stores"],
        2: ["Gas Stations", "Target"],
        3: ["Restaurants", "PayPal"],
        4: ["Amazon.com", "Digital Wallets"]
    }

    def __init__(self):
        """Initialize the calculator with an empty transaction log."""
        self.transactions: List[Dict] = []

    def add_transaction(self, amount: float, category: str, date: str) -> None:
        """
        Add a transaction to the log.
        
        Args:
            amount: Transaction amount in USD.
            category: Merchant category or description.
            date: Transaction date in 'YYYY-MM-DD' format.
        
        Raises:
            ValueError: If amount is negative or date is invalid.
        """
        if amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        
        try:
            transaction_date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        
        self.transactions.append({
            "amount": amount,
            "category": category,
            "date": transaction_date
        })

    def _get_quarter(self, date: datetime.date) -> int:
        """Determine the quarter (1-4) for a given date."""
        return (date.month - 1) // 3 + 1

    def calculate_cash_back(self) -> Tuple[float, Dict[int, float]]:
        """
        Calculate total cash back and quarterly breakdown.
        
        Returns:
            A tuple containing:
                - Total cash back earned
                - Dictionary mapping quarters to cash back amounts
        
        Raises:
            ValueError: If no transactions are available.
        """
        if not self.transactions:
            raise ValueError("No transactions available for calculation.")
        
        quarterly_cash_back = {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0}
        
        for transaction in self.transactions:
            quarter = self._get_quarter(transaction["date"])
            category = transaction["category"]
            
            if category in self.QUARTERLY_CATEGORIES.get(quarter, []):
                cash_back = transaction["amount"] * 0.05  # 5% cash back
                quarterly_cash_back[quarter] += cash_back
        
        total_cash_back = sum(quarterly_cash_back.values())
        
        return (total_cash_back, quarterly_cash_back)

    def get_quarterly_categories(self, quarter: int) -> Optional[List[str]]:
        """
        Get the cash back categories for a specific quarter.
        
        Args:
            quarter: Quarter number (1-4)
        
        Returns:
            List of categories or None if quarter is invalid
        """
        return self.QUARTERLY_CATEGORIES.get(quarter)

# Example usage
if __name__ == "__main__":
    calculator = DiscoverCashBackCalculator()
    
    # Add sample transactions
    try:
        calculator.add_transaction(100.0, "Grocery Stores", "2023-01-15")
        calculator.add_transaction(50.0, "Gas Stations", "2023-04-20")
        calculator.add_transaction(75.0, "Restaurants", "2023-07-10")
        calculator.add_transaction(200.0, "Amazon.com", "2023-11-25")
        calculator.add_transaction(30.0, "Other", "2023-03-01")  # Not in category
    except ValueError as e:
        print(f"Error adding transaction: {e}")
    
    # Calculate and display results
    try:
        total, quarterly = calculator.calculate_cash_back()
        print(f"Total Cash Back: ${total:.2f}")
        for qtr, amount in quarterly.items():
            print(f"Q{qtr}: ${amount:.2f}")
    except ValueError as e:
        print(f"Error calculating cash back: {e}")
```
