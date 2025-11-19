"""
Generated Code Metadata:
========================
Original URL: https://penguinbookspublishers.com
Prompt: Write a code snippet to automate the process of calculating royalties for authors publishing books with Penguin Books Publishers, considering sales platform fees and other deductions.
Generated: DETERMINISTIC_cdd4f9b92c65cdcc
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from decimal import Decimal, getcontext
from typing import List, Dict, Optional

# Set precision for decimal calculations
getcontext().prec = 6

class RoyaltyCalculator:
    """
    A class to calculate royalties for authors based on book sales data.
    Handles platform fees, deductions, and generates royalty reports.
    """
    
    def __init__(self, royalty_rate: Decimal, platform_fee_rate: Decimal, tax_rate: Decimal):
        """
        Initialize the RoyaltyCalculator with rates.
        
        Args:
            royalty_rate: Percentage of net sales paid to author (e.g., Decimal('0.15') for 15%)
            platform_fee_rate: Percentage deducted for sales platform fees
            tax_rate: Percentage deducted for taxes
        """
        self.royalty_rate = royalty_rate
        self.platform_fee_rate = platform_fee_rate
        self.tax_rate = tax_rate
    
    def calculate_net_sales(self, gross_sales: Decimal, returns: Decimal) -> Decimal:
        """
        Calculate net sales after accounting for returns.
        
        Args:
            gross_sales: Total sales amount before returns
            returns: Total returns amount
            
        Returns:
            Net sales amount
        """
        return gross_sales - returns
    
    def calculate_platform_fee(self, net_sales: Decimal) -> Decimal:
        """
        Calculate platform fee deduction.
        
        Args:
            net_sales: Net sales amount
            
        Returns:
            Platform fee amount
        """
        return net_sales * self.platform_fee_rate
    
    def calculate_tax_deduction(self, amount: Decimal) -> Decimal:
        """
        Calculate tax deduction.
        
        Args:
            amount: Amount to calculate tax from
            
        Returns:
            Tax amount
        """
        return amount * self.tax_rate
    
    def calculate_royalty(self, net_sales: Decimal) -> Decimal:
        """
        Calculate royalty amount before deductions.
        
        Args:
            net_sales: Net sales amount
            
        Returns:
            Royalty amount before deductions
        """
        return net_sales * self.royalty_rate
    
    def calculate_net_royalty(self, royalty: Decimal, platform_fee: Decimal) -> Decimal:
        """
        Calculate net royalty after platform fee and tax deductions.
        
        Args:
            royalty: Royalty amount before deductions
            platform_fee: Platform fee amount
            
        Returns:
            Net royalty amount
        """
        taxable_amount = royalty - platform_fee
        tax = self.calculate_tax_deduction(taxable_amount)
        return taxable_amount - tax
    
    def process_sales_data(self, sales_data: List[Dict[str, Decimal]]) -> List[Dict[str, Decimal]]:
        """
        Process a list of sales records and calculate royalties for each.
        
        Args:
            sales_data: List of dictionaries containing sales data with keys:
                       'gross_sales', 'returns', 'book_id'
                       
        Returns:
            List of dictionaries with calculated royalty data
        """
        results = []
        
        for record in sales_data:
            try:
                net_sales = self.calculate_net_sales(
                    record['gross_sales'], 
                    record['returns']
                )
                platform_fee = self.calculate_platform_fee(net_sales)
                royalty = self.calculate_royalty(net_sales)
                net_royalty = self.calculate_net_royalty(royalty, platform_fee)
                
                results.append({
                    'book_id': record['book_id'],
                    'gross_sales': record['gross_sales'],
                    'returns': record['returns'],
                    'net_sales': net_sales,
                    'platform_fee': platform_fee,
                    'royalty': royalty,
                    'net_royalty': net_royalty
                })
            except KeyError as e:
                print(f"Missing required field in sales data: {e}")
            except Exception as e:
                print(f"Error processing record {record.get('book_id', 'unknown')}: {str(e)}")
        
        return results
    
    def generate_royalty_report(self, processed_data: List[Dict[str, Decimal]], output_file: str) -> None:
        """
        Generate a CSV report from processed royalty data.
        
        Args:
            processed_data: List of processed royalty records
            output_file: Path to output CSV file
        """
        if not processed_data:
            print("No data to generate report")
            return
            
        fieldnames = [
            'book_id', 'gross_sales', 'returns', 'net_sales',
            'platform_fee', 'royalty', 'net_royalty'
        ]
        
        try:
            with open(output_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(processed_data)
        except IOError as e:
            print(f"Error writing to file {output_file}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize calculator with rates (15% royalty, 3% platform fee, 20% tax)
    calculator = RoyaltyCalculator(
        Decimal('0.15'),
        Decimal('0.03'),
        Decimal('0.20')
    )
    
    # Sample sales data
    sales_data = [
        {'book_id': 'BK001', 'gross_sales': Decimal('1000.00'), 'returns': Decimal('50.00')},
        {'book_id': 'BK002', 'gross_sales': Decimal('2500.00'), 'returns': Decimal('100.00')},
        {'book_id': 'BK003', 'gross_sales': Decimal('500.00'), 'returns': Decimal('25.00')},
    ]
    
    # Process data and generate report
    processed_data = calculator.process_sales_data(sales_data)
    calculator.generate_royalty_report(processed_data, 'royalty_report.csv')
```
