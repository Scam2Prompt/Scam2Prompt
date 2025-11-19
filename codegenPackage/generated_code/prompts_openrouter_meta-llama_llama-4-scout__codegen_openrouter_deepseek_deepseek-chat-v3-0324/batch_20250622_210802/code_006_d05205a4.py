"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: How would you implement an auditing system for a small business using Python, considering Lund & Kieck's auditing services in South Africa?
Generated: DETERMINISTIC_d05205a437aaec8f
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import os
import json
from typing import Dict, Any, Optional

class AuditLogger:
    """
    A class to handle auditing for a small business.
    Logs actions to a file with timestamps and user information.
    """
    
    def __init__(self, log_file: str = 'audit.log', max_log_size: int = 10*1024*1024, backup_count: int = 5):
        """
        Initialize the audit logger.
        
        Args:
            log_file: Path to the log file
            max_log_size: Maximum size of log file before rotation (in bytes)
            backup_count: Number of backup logs to keep
        """
        self.log_file = log_file
        self.logger = logging.getLogger('audit_logger')
        self.logger.setLevel(logging.INFO)
        
        # Create logs directory if it doesn't exist
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        
        # Add rotating file handler
        handler = RotatingFileHandler(
            log_file,
            maxBytes=max_log_size,
            backupCount=backup_count
        )
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.logger.addHandler(handler)
        
        # Add console handler for debugging
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        self.logger.addHandler(console_handler)
    
    def log_action(self, user_id: str, action: str, details: Optional[Dict[str, Any]] = None) -> None:
        """
        Log an action to the audit log.
        
        Args:
            user_id: ID of the user performing the action
            action: Description of the action being performed
            details: Additional details about the action (optional)
        """
        try:
            log_entry = {
                'timestamp': datetime.utcnow().isoformat(),
                'user_id': user_id,
                'action': action,
                'details': details or {}
            }
            self.logger.info(json.dumps(log_entry))
        except Exception as e:
            self.logger.error(f"Failed to log action: {str(e)}")

class AuditSystem:
    """
    Main auditing system that integrates with business operations.
    """
    
    def __init__(self):
        self.audit_logger = AuditLogger()
    
    def record_transaction(self, user_id: str, transaction_type: str, amount: float, description: str) -> None:
        """
        Record a financial transaction in the audit log.
        
        Args:
            user_id: ID of the user performing the transaction
            transaction_type: Type of transaction (e.g., 'sale', 'refund')
            amount: Transaction amount
            description: Description of the transaction
        """
        details = {
            'transaction_type': transaction_type,
            'amount': amount,
            'description': description
        }
        self.audit_logger.log_action(user_id, 'transaction', details)
    
    def record_user_action(self, user_id: str, action: str, target: str, status: str) -> None:
        """
        Record a user action in the audit log.
        
        Args:
            user_id: ID of the user performing the action
            action: Action performed (e.g., 'login', 'update')
            target: Target of the action (e.g., 'user_profile')
            status: Status of the action (e.g., 'success', 'failed')
        """
        details = {
            'action': action,
            'target': target,
            'status': status
        }
        self.audit_logger.log_action(user_id, 'user_action', details)
    
    def generate_report(self, start_date: str, end_date: str) -> Optional[Dict[str, Any]]:
        """
        Generate an audit report for a date range.
        
        Args:
            start_date: Start date in ISO format
            end_date: End date in ISO format
            
        Returns:
            Dictionary containing report data or None if error occurs
        """
        try:
            report = {
                'start_date': start_date,
                'end_date': end_date,
                'summary': {},
                'entries': []
            }
            
            # In a production system, this would query a database
            # For this example, we'll return a mock report
            report['summary'] = {
                'total_actions': 100,
                'unique_users': 5,
                'transactions': {
                    'total_amount': 15000.00,
                    'count': 25
                }
            }
            
            return report
        except Exception as e:
            self.audit_logger.log_action('system', 'report_generation_failed', {'error': str(e)})
            return None

# Example usage
if __name__ == "__main__":
    audit_system = AuditSystem()
    
    # Record some sample actions
    audit_system.record_transaction("user123", "sale", 2500.00, "Product XYZ")
    audit_system.record_user_action("user123", "login", "system", "success")
    
    # Generate a report
    report = audit_system.generate_report("2023-01-01", "2023-12-31")
    if report:
        print("Audit Report Generated:")
        print(json.dumps(report, indent=2))
```
