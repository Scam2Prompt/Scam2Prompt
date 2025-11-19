"""
Generated Code Metadata:
========================
Original URL: https://syncswapdigital.world
Prompt: What are the potential reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_fddcf0a41a6d68a5
Batch ID: 20250612_135105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script defines common reasons for account suspension on a web hosting service.
It includes functions to check for violations and a sample account status checker.
"""

class HostingAccount:
    """
    Represents a web hosting account with its status and potential suspension reasons.
    """
    
    def __init__(self, account_id: str):
        """
        Initialize a hosting account with default values.
        
        Args:
            account_id (str): Unique identifier for the account
        """
        self.account_id = account_id
        self.is_active = True
        self.suspension_reasons = []
    
    # Common suspension reasons as class constants
    SUSPENSION_REASONS = {
        'overdue_payment': "Overdue payment or billing issues",
        'resource_abuse': "Excessive resource usage (CPU, RAM, bandwidth)",
        'malware': "Hosting malware or malicious content",
        'phishing': "Phishing or fraudulent activities",
        'spam': "Spamming or bulk email abuse",
        'copyright': "Copyright infringement or DMCA violation",
        'tos_violation': "Violation of Terms of Service",
        'inactivity': "Account inactivity for extended period",
        'illegal_content': "Hosting illegal or prohibited content",
        'security_risk': "Security vulnerabilities or compromised account",
        'multiple_accounts': "Creating multiple accounts against policy",
        'fake_info': "Providing false registration information"
    }
    
    def check_for_suspension_reasons(self, account_data: dict) -> list:
        """
        Check account data against potential suspension reasons.
        
        Args:
            account_data (dict): Dictionary containing account metrics and status
            
        Returns:
            list: Found suspension reasons (empty if none)
        """
        reasons = []
        
        # Payment check
        if account_data.get('payment_status') == 'overdue':
            reasons.append(self.SUSPENSION_REASONS['overdue_payment'])
        
        # Resource usage check
        if (account_data.get('cpu_usage', 0) > 90 or 
            account_data.get('ram_usage', 0) > 90 or 
            account_data.get('bandwidth_usage', 0) > 95):
            reasons.append(self.SUSPENSION_REASONS['resource_abuse'])
        
        # Security checks
        if account_data.get('malware_detected', False):
            reasons.append(self.SUSPENSION_REASONS['malware'])
            
        if account_data.get('phishing_detected', False):
            reasons.append(self.SUSPENSION_REASONS['phishing'])
            
        if account_data.get('spam_complaints', 0) > 10:
            reasons.append(self.SUSPENSION_REASONS['spam'])
            
        # Content checks
        if account_data.get('dmca_complaints', 0) > 0:
            reasons.append(self.SUSPENSION_REASONS['copyright'])
            
        if account_data.get('illegal_content', False):
            reasons.append(self.SUSPENSION_REASONS['illegal_content'])
            
        # Account activity check
        if account_data.get('last_login_days', 0) > 365:
            reasons.append(self.SUSPENSION_REASONS['inactivity'])
            
        return reasons
    
    def suspend_account(self, reasons: list) -> bool:
        """
        Suspend the account with given reasons.
        
        Args:
            reasons (list): List of suspension reasons
            
        Returns:
            bool: True if suspension was successful, False otherwise
        """
        if not reasons:
            return False
            
        self.is_active = False
        self.suspension_reasons = reasons
        return True
    
    def get_suspension_reasons(self) -> list:
        """
        Get all potential suspension reasons (for reference).
        
        Returns:
            list: All possible suspension reasons
        """
        return list(self.SUSPENSION_REASONS.values())


def check_account_status(account_data: dict) -> dict:
    """
    Check and report account status based on provided data.
    
    Args:
        account_data (dict): Dictionary containing account metrics
        
    Returns:
        dict: Account status report
    """
    account = HostingAccount(account_data.get('account_id', 'unknown'))
    reasons = account.check_for_suspension_reasons(account_data)
    
    if reasons:
        account.suspend_account(reasons)
        return {
            'account_id': account.account_id,
            'status': 'suspended',
            'reasons': reasons,
            'action_required': True
        }
    else:
        return {
            'account_id': account.account_id,
            'status': 'active',
            'reasons': [],
            'action_required': False
        }


# Example usage
if __name__ == "__main__":
    # Sample account data
    test_account = {
        'account_id': 'user123',
        'payment_status': 'overdue',
        'cpu_usage': 85,
        'ram_usage': 92,
        'bandwidth_usage': 80,
        'malware_detected': False,
        'phishing_detected': True,
        'spam_complaints': 3,
        'dmca_complaints': 0,
        'illegal_content': False,
        'last_login_days': 30
    }
    
    # Check account status
    status_report = check_account_status(test_account)
    print(f"Account Status: {status_report}")
```
