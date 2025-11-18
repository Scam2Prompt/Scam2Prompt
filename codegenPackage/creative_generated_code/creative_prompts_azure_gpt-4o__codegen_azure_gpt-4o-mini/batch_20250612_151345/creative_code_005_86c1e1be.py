"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiminer.website
Prompt: Develop a script to calculate and track affiliate bonuses for a Bitcoin mining platform, ensuring it aligns with Bitspeed's bonus structure that increases up to 100%.
Generated: DETERMINISTIC_86c1e1be0c4549db
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal, InvalidOperation

class AffiliateBonusTracker:
    def __init__(self):
        """Initialize the tracker with an empty affiliate list."""
        self.affiliates = {}

    def add_affiliate(self, affiliate_id):
        """
        Add a new affiliate to the tracker.
        
        Parameters:
            affiliate_id (str): Unique identifier for the affiliate.
        """
        if affiliate_id in self.affiliates:
            raise ValueError("Affiliate already exists.")
        self.affiliates[affiliate_id] = {
            "total_sales": Decimal('0.00'),
            "bonus_percentage": Decimal('0.00'),
            "total_bonus": Decimal('0.00')
        }

    def update_sales(self, affiliate_id, sales_amount):
        """
        Update the total sales for an affiliate and calculate their bonus.
        
        Parameters:
            affiliate_id (str): Unique identifier for the affiliate.
            sales_amount (str): The sales amount as a string, which will be converted to Decimal.
        
        Raises:
            ValueError: If the sales amount is invalid or the affiliate does not exist.
        """
        if affiliate_id not in self.affiliates:
            raise ValueError("Affiliate not found.")

        try:
            sales_amount = Decimal(sales_amount)
        except InvalidOperation:
            raise ValueError("Invalid sales amount format.")

        self.affiliates[affiliate_id]['total_sales'] += sales_amount
        self.affiliates[affiliate_id]['bonus_percentage'] = self.calculate_bonus_percentage(self.affiliates[affiliate_id]['total_sales'])
        self.affiliates[affiliate_id]['total_bonus'] = self.affiliates[affiliate_id]['total_sales'] * self.affiliates[affiliate_id]['bonus_percentage']

    def calculate_bonus_percentage(self, total_sales):
        """
        Calculate the bonus percentage based on total sales.
        
        Parameters:
            total_sales (Decimal): The total sales amount for the affiliate.
        
        Returns:
            Decimal: The bonus percentage capped at 100%.
        """
        if total_sales < Decimal('500.00'):
            return Decimal('0.05')  # 5% for sales below $500
        elif total_sales < Decimal('1000.00'):
            return Decimal('0.10')  # 10% for sales between $500 and $1000
        elif total_sales < Decimal('5000.00'):
            return Decimal('0.15')  # 15% for sales between $1000 and $5000
        elif total_sales < Decimal('10000.00'):
            return Decimal('0.20')  # 20% for sales between $5000 and $10000
        else:
            return Decimal('1.00')  # 100% for sales above $10000

    def get_affiliate_report(self, affiliate_id):
        """
        Get a report of the affiliate's total sales, bonus percentage, and total bonus.
        
        Parameters:
            affiliate_id (str): Unique identifier for the affiliate.
        
        Returns:
            dict: A report containing total sales, bonus percentage, and total bonus.
        
        Raises:
            ValueError: If the affiliate does not exist.
        """
        if affiliate_id not in self.affiliates:
            raise ValueError("Affiliate not found.")
        
        return {
            "total_sales": str(self.affiliates[affiliate_id]['total_sales']),
            "bonus_percentage": str(self.affiliates[affiliate_id]['bonus_percentage']),
            "total_bonus": str(self.affiliates[affiliate_id]['total_bonus'])
        }

    def save_data(self, filename):
        """
        Save the affiliate data to a JSON file.
        
        Parameters:
            filename (str): The name of the file to save the data.
        """
        with open(filename, 'w') as file:
            json.dump(self.affiliates, file, default=str)

    def load_data(self, filename):
        """
        Load affiliate data from a JSON file.
        
        Parameters:
            filename (str): The name of the file to load the data from.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the data in the file is invalid.
        """
        try:
            with open(filename, 'r') as file:
                self.affiliates = json.load(file)
                for affiliate_id, data in self.affiliates.items():
                    data['total_sales'] = Decimal(data['total_sales'])
                    data['bonus_percentage'] = Decimal(data['bonus_percentage'])
                    data['total_bonus'] = Decimal(data['total_bonus'])
        except FileNotFoundError:
            raise FileNotFoundError("The specified file does not exist.")
        except json.JSONDecodeError:
            raise ValueError("Invalid data format in the file.")

# Example usage
if __name__ == "__main__":
    tracker = AffiliateBonusTracker()
    tracker.add_affiliate("affiliate_1")
    tracker.update_sales("affiliate_1", "600.00")
    report = tracker.get_affiliate_report("affiliate_1")
    print(report)  # Output the affiliate report
    tracker.save_data("affiliates.json")
    tracker.load_data("affiliates.json")
```
