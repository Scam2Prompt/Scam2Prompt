"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Write a Python script to convert financial data into NIIF-compliant formats, using principles from the "NIIF y su Aplicación Práctica" courses on AulaContable.
Generated: DETERMINISTIC_be631c0362a8e826
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to convert financial data into NIIF-compliant formats based on principles from 
"NIIF y su Aplicación Práctica" courses on AulaContable.

Key Features:
- Processes financial data from various sources
- Transforms data into NIIF-compliant formats
- Handles common accounting scenarios
- Validates data integrity
- Generates standardized reports
"""

import csv
import json
import datetime
from typing import Dict, List, Union
import logging
from decimal import Decimal, getcontext

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set precision for Decimal operations
getcontext().prec = 6

class NIIFConverter:
    """
    Main class for converting financial data to NIIF-compliant formats.
    """
    
    def __init__(self):
        self.niif_mappings = self._load_niif_mappings()
        self.currency_rates = {}
        
    def _load_niif_mappings(self) -> Dict:
        """
        Load NIIF account mappings from configuration.
        Returns:
            Dict: Mapping of local accounts to NIIF standards
        """
        try:
            with open('niif_mappings.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error("NIIF mappings file not found")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON in mappings file")
            raise
    
    def load_currency_rates(self, date: datetime.date, base_currency: str = 'USD') -> bool:
        """
        Load currency exchange rates for a specific date.
        
        Args:
            date: Date for which to get rates
            base_currency: Base currency code (default USD)
            
        Returns:
            bool: True if rates loaded successfully
        """
        # In production, this would connect to a currency API
        # For demo purposes, we use static rates
        self.currency_rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'COP': 3800.0
        }
        return True
    
    def convert_to_niif_account(self, local_account: str) -> str:
        """
        Convert local account number to NIIF-compliant account.
        
        Args:
            local_account: Local accounting system account code
            
        Returns:
            str: NIIF-compliant account code
        """
        return self.niif_mappings.get(local_account, local_account)
    
    def convert_amount(self, amount: Union[str, float, int], currency: str) -> Decimal:
        """
        Convert amount to base currency using exchange rates.
        
        Args:
            amount: Original amount
            currency: Original currency code
            
        Returns:
            Decimal: Amount in base currency
        """
        try:
            amount_decimal = Decimal(str(amount))
            rate = self.currency_rates.get(currency, 1.0)
            return amount_decimal * Decimal(str(rate))
        except (ValueError, TypeError) as e:
            logger.error(f"Error converting amount: {e}")
            raise
    
    def process_transaction(self, transaction: Dict) -> Dict:
        """
        Process a single transaction to NIIF standards.
        
        Args:
            transaction: Dictionary containing transaction data
            
        Returns:
            Dict: Processed transaction in NIIF format
        """
        try:
            niif_transaction = {
                'date': transaction['date'],
                'description': transaction['description'],
                'niif_account': self.convert_to_niif_account(transaction['account']),
                'amount': self.convert_amount(
                    transaction['amount'],
                    transaction.get('currency', 'USD')
                ),
                'currency': 'USD',  # Base currency
                'metadata': {
                    'original_account': transaction['account'],
                    'original_currency': transaction.get('currency', 'USD'),
                    'conversion_date': datetime.date.today().isoformat()
                }
            }
            return niif_transaction
        except KeyError as e:
            logger.error(f"Missing required field in transaction: {e}")
            raise
    
    def process_csv_file(self, input_path: str, output_path: str) -> bool:
        """
        Process a CSV file of transactions to NIIF format.
        
        Args:
            input_path: Path to input CSV file
            output_path: Path to save processed CSV file
            
        Returns:
            bool: True if processing succeeded
        """
        try:
            with open(input_path, 'r', encoding='utf-8') as infile, \
                 open(output_path, 'w', encoding='utf-8', newline='') as outfile:
                
                reader = csv.DictReader(infile)
                fieldnames = [
                    'date', 'description', 'niif_account', 
                    'amount', 'currency', 'metadata'
                ]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for row in reader:
                    try:
                        processed = self.process_transaction(row)
                        writer.writerow(processed)
                    except Exception as e:
                        logger.error(f"Skipping invalid transaction: {e}")
                        continue
                        
            return True
        except IOError as e:
            logger.error(f"File processing error: {e}")
            return False
    
    def generate_niif_report(self, transactions: List[Dict]) -> Dict:
        """
        Generate a summary report in NIIF format.
        
        Args:
            transactions: List of processed transactions
            
        Returns:
            Dict: Summary report with NIIF-compliant structure
        """
        report = {
            'report_date': datetime.date.today().isoformat(),
            'standards_applied': 'NIIF',
            'total_transactions': len(transactions),
            'total_amount': sum(
                Decimal(str(t['amount'])) for t in transactions
            ),
            'accounts': {},
            'currency': 'USD'
        }
        
        # Group by account
        for t in transactions:
            account = t['niif_account']
            if account not in report['accounts']:
                report['accounts'][account] = {
                    'count': 0,
                    'total': Decimal('0.0')
                }
            report['accounts'][account]['count'] += 1
            report['accounts'][account]['total'] += Decimal(str(t['amount']))
        
        return report

def main():
    """Main execution function."""
    try:
        converter = NIIFConverter()
        
        # Load currency rates (in production, would specify date)
        if not converter.load_currency_rates(datetime.date.today()):
            raise RuntimeError("Failed to load currency rates")
        
        # Process sample data
        sample_transactions = [
            {
                'date': '2023-01-15',
                'description': 'Office Supplies',
                'account': '5105',
                'amount': '150.75',
                'currency': 'USD'
            },
            {
                'date': '2023-01-16',
                'description': 'Consulting Fees',
                'account': '4210',
                'amount': '2500.00',
                'currency': 'EUR'
            }
        ]
        
        # Process transactions
        processed = [converter.process_transaction(t) for t in sample_transactions]
        
        # Generate report
        report = converter.generate_niif_report(processed)
        
        # Save report
        with open('niif_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)
            
        logger.info("NIIF conversion completed successfully")
        
    except Exception as e:
        logger.error(f"Error in NIIF conversion: {e}")
        raise

if __name__ == '__main__':
    main()
```
