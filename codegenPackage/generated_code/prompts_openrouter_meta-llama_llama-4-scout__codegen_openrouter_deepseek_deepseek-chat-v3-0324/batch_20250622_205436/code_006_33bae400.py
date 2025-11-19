"""
Generated Code Metadata:
========================
Original URL: https://zealvsmetamask.com
Prompt: Create a security audit report template for a self-custodial wallet like Zeal, including checks for transaction security and biometrics protection.
Generated: DETERMINISTIC_33bae4003f320ab2
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional

class SecurityAuditReport:
    """
    Generates a security audit report for a self-custodial wallet.
    Includes checks for transaction security and biometrics protection.
    """

    def __init__(self, wallet_name: str, version: str):
        """
        Initialize the security audit report.
        
        Args:
            wallet_name: Name of the wallet being audited
            version: Version of the wallet being audited
        """
        self.wallet_name = wallet_name
        self.version = version
        self.report_data = {
            "metadata": {
                "wallet_name": wallet_name,
                "version": version,
                "audit_date": datetime.utcnow().isoformat(),
                "audit_id": self._generate_audit_id()
            },
            "findings": [],
            "summary": {
                "total_checks": 0,
                "passed_checks": 0,
                "failed_checks": 0,
                "critical_issues": 0,
                "high_issues": 0,
                "medium_issues": 0,
                "low_issues": 0
            }
        }

    def _generate_audit_id(self) -> str:
        """Generate a unique audit ID based on wallet name and timestamp."""
        timestamp = datetime.utcnow().isoformat()
        unique_str = f"{self.wallet_name}_{self.version}_{timestamp}"
        return hashlib.sha256(unique_str.encode()).hexdigest()

    def add_transaction_security_check(
        self,
        check_name: str,
        description: str,
        passed: bool,
        severity: str,
        details: Optional[Dict] = None
    ) -> None:
        """
        Add a transaction security check to the report.
        
        Args:
            check_name: Name of the check
            description: Description of what was checked
            passed: Whether the check passed
            severity: Severity level (critical, high, medium, low)
            details: Additional details about the check
        """
        self._add_check(
            category="transaction_security",
            check_name=check_name,
            description=description,
            passed=passed,
            severity=severity,
            details=details
        )

    def add_biometrics_check(
        self,
        check_name: str,
        description: str,
        passed: bool,
        severity: str,
        details: Optional[Dict] = None
    ) -> None:
        """
        Add a biometrics protection check to the report.
        
        Args:
            check_name: Name of the check
            description: Description of what was checked
            passed: Whether the check passed
            severity: Severity level (critical, high, medium, low)
            details: Additional details about the check
        """
        self._add_check(
            category="biometrics_protection",
            check_name=check_name,
            description=description,
            passed=passed,
            severity=severity,
            details=details
        )

    def _add_check(
        self,
        category: str,
        check_name: str,
        description: str,
        passed: bool,
        severity: str,
        details: Optional[Dict] = None
    ) -> None:
        """
        Internal method to add a check to the report and update summary statistics.
        """
        if severity.lower() not in ["critical", "high", "medium", "low"]:
            raise ValueError("Severity must be one of: critical, high, medium, low")

        finding = {
            "category": category,
            "check_name": check_name,
            "description": description,
            "passed": passed,
            "severity": severity.lower(),
            "timestamp": datetime.utcnow().isoformat(),
            "details": details or {}
        }

        self.report_data["findings"].append(finding)
        self._update_summary(passed, severity.lower())

    def _update_summary(self, passed: bool, severity: str) -> None:
        """Update the summary statistics based on check results."""
        self.report_data["summary"]["total_checks"] += 1

        if passed:
            self.report_data["summary"]["passed_checks"] += 1
        else:
            self.report_data["summary"]["failed_checks"] += 1
            if severity == "critical":
                self.report_data["summary"]["critical_issues"] += 1
            elif severity == "high":
                self.report_data["summary"]["high_issues"] += 1
            elif severity == "medium":
                self.report_data["summary"]["medium_issues"] += 1
            elif severity == "low":
                self.report_data["summary"]["low_issues"] += 1

    def generate_report(self, output_format: str = "json") -> str:
        """
        Generate the final audit report in the specified format.
        
        Args:
            output_format: Format of the report (currently only 'json' supported)
            
        Returns:
            The generated report as a string
            
        Raises:
            ValueError: If unsupported output format is requested
        """
        if output_format.lower() != "json":
            raise ValueError("Only JSON output format is currently supported")

        return json.dumps(self.report_data, indent=2)

    def save_report(self, file_path: str) -> None:
        """
        Save the audit report to a file.
        
        Args:
            file_path: Path to save the report to
            
        Raises:
            IOError: If there's an issue writing the file
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.report_data, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save report: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize the audit report
    audit = SecurityAuditReport(wallet_name="Zeal", version="1.2.0")
    
    # Add transaction security checks
    audit.add_transaction_security_check(
        check_name="Transaction Signing Security",
        description="Verify transactions are properly signed before submission",
        passed=True,
        severity="critical"
    )
    
    audit.add_transaction_security_check(
        check_name="Double Spend Protection",
        description="Check for mechanisms preventing double spending",
        passed=False,
        severity="high",
        details={"issue": "No proper sequence number validation"}
    )
    
    # Add biometrics protection checks
    audit.add_biometrics_check(
        check_name="Biometric Authentication",
        description="Verify biometric authentication is required for sensitive operations",
        passed=True,
        severity="high"
    )
    
    audit.add_biometrics_check(
        check_name="Biometric Data Storage",
        description="Check biometric data is stored securely and never leaves device",
        passed=False,
        severity="critical",
        details={"issue": "Biometric templates stored in plaintext"}
    )
    
    # Generate and print the report
    print(audit.generate_report())
```
