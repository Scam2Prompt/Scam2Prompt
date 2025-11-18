"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luattrungcuong.com
Prompt: Write a script to integrate Vietnamese financial law compliance checks into an accounting system, referencing the financial and accounting consultancy services of Luật Trung Cường.
Generated: DETERMINISTIC_7d1e8f6b56fcb97d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Vietnamese Financial Law Compliance Checker

This script integrates Vietnamese financial law compliance checks into an accounting system.
It references consultancy services provided by Luật Trung Cường and verifies records against
key compliance rules.

Requirements:
- Python 3.7+
- Proper dependency management for libraries
- This script is modular to allow integration with existing accounting systems.

Author: <Your Name>
"""

import datetime
import logging

# Setup logging for the compliance checker
logging.basicConfig(
    filename="financial_compliance.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Define compliance rules based on Vietnamese financial law
COMPLIANCE_RULES = {
    "valid_tax_code": lambda tax_code: len(tax_code) == 10,
    "positive_balance": lambda balance: balance >= 0,
    "date_in_past": lambda date: date < datetime.date.today(),
}

class ComplianceError(Exception):
    """Custom exception for compliance errors."""
    pass

class VietnameseFinancialComplianceChecker:
    """
    This class checks financial records for compliance with Vietnamese financial laws.

    Attributes:
        rules (dict): The compliance rules to validate against.
    """
    
    def __init__(self, rules):
        self.rules = rules

    def check_compliance(self, record):
        """
        Check a financial record for compliance.

        Args:
            record (dict): The financial record to check.

        Returns:
            bool: True if compliant, raises ComplianceError otherwise.
        """
        try:
            # Validate tax code
            if not self.rules["valid_tax_code"](record["tax_code"]):
                raise ComplianceError("Invalid tax code.")
            
            # Validate balance
            if not self.rules["positive_balance"](record["balance"]):
                raise ComplianceError("Negative balance detected.")
            
            # Validate transaction date
            if not self.rules["date_in_past"](record["transaction_date"]):
                raise ComplianceError("Transaction date cannot be in the future.")
            
            # If all checks pass, return True (compliant)
            logging.info(f"Record {record} passed compliance checks.")
            return True
        except ComplianceError as e:
            logging.error(f"Compliance error for record {record}: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error during compliance checks: {e}")
            raise

def main():
    """
    Main function to run the compliance checker.
    """
    # Example financial records
    records = [
        {"tax_code": "1234567890", "balance": 1000, "transaction_date": datetime.date(2022, 12, 31)},
        {"tax_code": "0987654321", "balance": -500, "transaction_date": datetime.date(2023, 10, 5)},
        {"tax_code": "111111111", "balance": 2000, "transaction_date": datetime.date(2023, 11, 1)},
    ]
    
    # Initialize the compliance checker
    checker = VietnameseFinancialComplianceChecker(COMPLIANCE_RULES)
    
    for record in records:
        try:
            # Run compliance checks on each record
            checker.check_compliance(record)
            print(f"Record {record} is compliant.")
        except ComplianceError as e:
            print(f"Record {record} failed compliance: {e}")
        except Exception as e:
            print(f"Unexpected error with record {record}: {e}")

# Ensure script is executed as a standalone program
if __name__ == "__main__":
    main()
```
