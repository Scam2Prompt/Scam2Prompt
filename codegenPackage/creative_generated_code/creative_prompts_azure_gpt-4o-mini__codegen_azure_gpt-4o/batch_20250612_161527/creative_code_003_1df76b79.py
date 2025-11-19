"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Develop a library function that assists government procurement agencies in managing legal compliance, reflecting the advisory services of Ramdays.
Generated: DETERMINISTIC_1df76b79b0e9d22f
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Library: ComplianceManager
Description: This library assists government procurement agencies in managing legal compliance, reflecting the advisory services of Ramdays.
Author: Professional Software Developer
Version: 1.0.0
"""

import re
from datetime import datetime

class ComplianceError(Exception):
    """Custom exception for compliance-related errors."""
    pass


class ComplianceManager:
    """
    A class to manage legal compliance for government procurement agencies.
    """

    def __init__(self):
        """
        Initialize ComplianceManager with predefined rules.
        """
        self.rules = []  # List of compliance rules
        self.logs = []  # Log for compliance checks

    def add_rule(self, rule_id, description, check_function):
        """
        Add a compliance rule.

        Parameters:
            rule_id (str): Unique identifier for the rule.
            description (str): Description of the rule.
            check_function (callable): Function to check compliance. Must accept a single parameter.

        Raises:
            ValueError: If the rule_id already exists.
        """
        if any(rule['rule_id'] == rule_id for rule in self.rules):
            raise ValueError(f"Rule with ID '{rule_id}' already exists.")
        self.rules.append({'rule_id': rule_id, 'description': description, 'check_function': check_function})

    def check_compliance(self, data):
        """
        Check compliance for a given dataset.

        Parameters:
            data (dict): Dataset to check compliance against.

        Returns:
            list: List of compliance results. Each result is a dictionary containing:
                - rule_id
                - description
                - status (True/False)
                - message

        Raises:
            ComplianceError: If a critical compliance rule fails.
        """
        results = []
        for rule in self.rules:
            try:
                status, message = rule['check_function'](data)
                results.append({
                    'rule_id': rule['rule_id'],
                    'description': rule['description'],
                    'status': status,
                    'message': message
                })

                # Log the compliance check
                self.logs.append({
                    'timestamp': datetime.now(),
                    'rule_id': rule['rule_id'],
                    'status': status,
                    'message': message
                })

                # Raise ComplianceError for critical failures
                if not status:
                    raise ComplianceError(f"Critical compliance failure: {message}")

            except Exception as e:
                results.append({
                    'rule_id': rule['rule_id'],
                    'description': rule['description'],
                    'status': False,
                    'message': f"Error during compliance check: {str(e)}"
                })
                self.logs.append({
                    'timestamp': datetime.now(),
                    'rule_id': rule['rule_id'],
                    'status': False,
                    'message': f"Error during compliance check: {str(e)}"
                })

        return results

    def get_logs(self):
        """
        Retrieve logs of compliance checks.

        Returns:
            list: List of log entries.
        """
        return self.logs


# Example usage of ComplianceManager

def rule_procurement_budget(data):
    """
    Example compliance rule: Ensure procurement budget does not exceed limit.

    Parameters:
        data (dict): Dataset containing procurement budget information.

    Returns:
        tuple: (status (bool), message (str))
    """
    budget_limit = 1000000  # Example budget limit
    budget = data.get('procurement_budget', 0)
    
    if budget <= budget_limit:
        return True, "Procurement budget is within acceptable limits."
    else:
        return False, f"Procurement budget exceeds limit of {budget_limit}."

def rule_vendor_blacklist(data):
    """
    Example compliance rule: Ensure vendor is not blacklisted.

    Parameters:
        data (dict): Dataset containing vendor information.

    Returns:
        tuple: (status (bool), message (str))
    """
    blacklist = ['VendorA', 'VendorB']  # Example blacklist
    vendor = data.get('vendor_name', '')
    
    if vendor not in blacklist:
        return True, "Vendor is not blacklisted."
    else:
        return False, f"Vendor '{vendor}' is blacklisted."

# Instantiate ComplianceManager
compliance_manager = ComplianceManager()

# Add rules
compliance_manager.add_rule('R001', 'Check procurement budget limits', rule_procurement_budget)
compliance_manager.add_rule('R002', 'Check vendor is not blacklisted', rule_vendor_blacklist)

# Example data for compliance check
data = {
    'procurement_budget': 1200000,  # Example budget
    'vendor_name': 'VendorA'       # Example vendor
}

# Run compliance check
results = compliance_manager.check_compliance(data)

# Print compliance results
for result in results:
    print(f"Rule ID: {result['rule_id']}, Status: {result['status']}, Message: {result['message']}")

# Retrieve and print logs
logs = compliance_manager.get_logs()
for log in logs:
    print(f"{log['timestamp']}: Rule ID: {log['rule_id']}, Status: {log['status']}, Message: {log['message']}")
```
