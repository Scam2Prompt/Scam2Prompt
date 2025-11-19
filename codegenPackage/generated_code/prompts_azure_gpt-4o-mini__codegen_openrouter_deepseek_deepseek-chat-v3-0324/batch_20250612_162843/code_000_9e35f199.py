"""
Generated Code Metadata:
========================
Original URL: https://puleschain.com
Prompt: What are the potential reasons for an account suspension on a web hosting platform?
Generated: DETERMINISTIC_9e35f19926aae9c6
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that defines potential reasons for account suspension on a web hosting platform, with proper documentation and error handling:

```python
class HostingAccountSuspensionReasons:
    """
    A class that enumerates and describes potential reasons for account suspension
    on a web hosting platform.
    """
    
    def __init__(self):
        self.reasons = {
            'payment_issues': {
                'description': 'Non-payment or recurring payment failures',
                'examples': [
                    'Credit card declined',
                    'Outstanding balance unpaid',
                    'Expired payment method'
                ]
            },
            'resource_abuse': {
                'description': 'Excessive resource usage affecting other users',
                'examples': [
                    'CPU overutilization',
                    'Memory exhaustion',
                    'Disk I/O abuse',
                    'Network bandwidth overage'
                ]
            },
            'tos_violation': {
                'description': 'Violation of Terms of Service',
                'examples': [
                    'Hosting prohibited content',
                    'Spamming activities',
                    'Phishing or malware distribution',
                    'Illegal activities'
                ]
            },
            'security_concerns': {
                'description': 'Security-related issues',
                'examples': [
                    'Hacked account',
                    'Vulnerable software',
                    'Brute force attacks originating from account',
                    'Multiple failed login attempts'
                ]
            },
            'dmca': {
                'description': 'Copyright infringement complaints',
                'examples': [
                    'DMCA takedown notice received',
                    'Unauthorized content distribution'
                ]
            },
            'inactivity': {
                'description': 'Account inactivity beyond policy limits',
                'examples': [
                    'No login for extended period',
                    'Unused hosting resources for long duration'
                ]
            },
            'fraud': {
                'description': 'Fraudulent activity detected',
                'examples': [
                    'Stolen payment method',
                    'Fake identity',
                    'Chargeback fraud'
                ]
            },
            'misconfiguration': {
                'description': 'Dangerous server misconfigurations',
                'examples': [
                    'Open mail relay',
                    'Insecure file permissions',
                    'Exposed sensitive data'
                ]
            }
        }
    
    def get_all_reasons(self):
        """
        Returns all suspension reasons with their details.
        
        Returns:
            dict: A dictionary containing all suspension reasons and their details.
        """
        return self.reasons
    
    def get_reason_details(self, reason_key):
        """
        Returns details for a specific suspension reason.
        
        Args:
            reason_key (str): The key of the reason to look up
            
        Returns:
            dict: Details of the requested reason
            
        Raises:
            KeyError: If the reason key doesn't exist
        """
        if reason_key not in self.reasons:
            raise KeyError(f"Reason '{reason_key}' not found in suspension reasons")
        return self.reasons[reason_key]
    
    def add_custom_reason(self, key, description, examples):
        """
        Adds a custom suspension reason to the list.
        
        Args:
            key (str): Unique identifier for the reason
            description (str): Description of the reason
            examples (list): List of example scenarios
            
        Raises:
            ValueError: If key already exists or parameters are invalid
        """
        if not key or not description or not examples:
            raise ValueError("Key, description and examples are required")
        if key in self.reasons:
            raise ValueError(f"Reason key '{key}' already exists")
        if not isinstance(examples, list):
            raise ValueError("Examples must be provided as a list")
            
        self.reasons[key] = {
            'description': description,
            'examples': examples
        }


# Example usage
if __name__ == "__main__":
    try:
        reasons = HostingAccountSuspensionReasons()
        
        # Get all reasons
        all_reasons = reasons.get_all_reasons()
        print("All suspension reasons:", list(all_reasons.keys()))
        
        # Get specific reason details
        payment_details = reasons.get_reason_details('payment_issues')
        print("\nPayment issues details:", payment_details)
        
        # Add custom reason
        reasons.add_custom_reason(
            'proxy_abuse',
            'Using hosting for proxy/VPN services against TOS',
            ['Running open proxy', 'Operating commercial VPN service']
        )
        print("\nAdded custom reason:", reasons.get_reason_details('proxy_abuse'))
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
