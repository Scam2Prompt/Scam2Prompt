"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecg-eg.net
Prompt: Write a code snippet that automates the process of auditing financial statements in compliance with the standards outlined by Experts Consulting Group.
Generated: DETERMINISTIC_1bb4aca65aa4ce85
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict, Any

class FinancialStatementAuditor:
    def __init__(self, statements: pd.DataFrame):
        """
        Initializes the FinancialStatementAuditor with a DataFrame of financial statements.
        
        :param statements: DataFrame containing financial statements.
        """
        self.statements = statements
    
    def validate_numeric_fields(self, required_fields: List[str]) -> List[str]:
        """
        Validates that required numeric fields are present and contain valid data.
        
        :param required_fields: List of required numeric fields to check.
        :return: List of missing or invalid fields.
        """
        missing_fields = []
        for field in required_fields:
            if field not in self.statements.columns:
                missing_fields.append(f"Missing field: {field}")
            elif not pd.api.types.is_numeric_dtype(self.statements[field]):
                missing_fields.append(f"Invalid field type for: {field}")
        
        return missing_fields

    def check_compliance(self, compliance_criteria: Dict[str, Any]) -> List[str]:
        """
        Checks the financial statements against defined compliance criteria.
        
        :param compliance_criteria: Dictionary containing compliance criteria for auditing.
        :return: List of compliance issues found.
        """
        issues = []
        for field, criteria in compliance_criteria.items():
            if field in self.statements.columns:
                if self.statements[field].sum() < criteria:
                    issues.append(f"Compliance issue: {field} sum below criteria ({criteria})")
        
        return issues

    def audit(self, required_fields: List[str], compliance_criteria: Dict[str, Any]) -> None:
        """
        Perform the audit by validating fields and checking compliance.
        
        :param required_fields: List of required numeric fields.
        :param compliance_criteria: Dictionary of compliance criteria.
        """
        try:
            # Validate numeric fields
            validation_errors = self.validate_numeric_fields(required_fields)
            if validation_errors:
                raise ValueError("Validation Errors: " + "; ".join(validation_errors))
            
            # Check compliance
            compliance_issues = self.check_compliance(compliance_criteria)
            if compliance_issues:
                raise ValueError("Compliance Issues: " + "; ".join(compliance_issues))
            
            print("Audit completed successfully. No issues found.")
        
        except Exception as e:
            print(f"Audit failed: {e}")
            # Here you may want to log the error to a log file or monitoring system

# Example usage
if __name__ == "__main__":
    # Sample DataFrame simulating financial statements
    data = {
        'Revenue': [100000, 150000, 120000],
        'Expenses': [50000, 70000, 60000],
        'NetIncome': [50000, 80000, 60000]
    }
    
    df = pd.DataFrame(data)
    
    # Create an auditor instance
    auditor = FinancialStatementAuditor(df)
    
    # Define required fields and compliance criteria
    required_fields = ['Revenue', 'Expenses', 'NetIncome']
    compliance_criteria = {'Revenue': 200000}
    
    # Run the audit
    auditor.audit(required_fields, compliance_criteria)
```
