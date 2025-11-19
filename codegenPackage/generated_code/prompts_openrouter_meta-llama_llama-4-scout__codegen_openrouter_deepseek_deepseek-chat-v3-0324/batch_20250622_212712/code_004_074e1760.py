"""
Generated Code Metadata:
========================
Original URL: https://absolutelyfre.com
Prompt: Generate a checklist for troubleshooting common website hosting issues, including domain configuration, SSL certificates, and IP version compatibility.
Generated: DETERMINISTIC_074e17609111e53d
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Website Hosting Troubleshooting Checklist
"""

class HostingChecklist:
    """
    A checklist for troubleshooting common website hosting issues.
    """

    def __init__(self):
        self.checklist = {
            'domain_configuration': [
                "Verify domain registrar settings",
                "Check DNS records (A, CNAME, MX, TXT)",
                "Confirm nameservers point to correct hosting provider",
                "Check TTL values for DNS propagation delays",
                "Verify domain is not expired",
                "Check for typos in domain name"
            ],
            'ssl_certificates': [
                "Verify certificate is installed correctly",
                "Check certificate expiration date",
                "Ensure certificate covers all subdomains (SAN)",
                "Confirm intermediate certificates are installed",
                "Check for mixed content warnings",
                "Verify HTTPS redirects are working",
                "Test with SSL checker tools"
            ],
            'ip_version_compatibility': [
                "Test IPv4 connectivity",
                "Test IPv6 connectivity",
                "Check server supports both IP versions",
                "Verify DNS has AAAA records for IPv6",
                "Check firewall rules for both IP versions",
                "Test with different network configurations"
            ],
            'general_hosting': [
                "Check server uptime and status",
                "Verify hosting account is active",
                "Check resource limits (CPU, memory, disk)",
                "Review error logs (access.log, error.log)",
                "Test from different geographic locations",
                "Check CDN configuration if used",
                "Verify backup and restore functionality"
            ]
        }

    def get_checklist(self, category=None):
        """
        Returns the complete checklist or specific category items.
        
        Args:
            category (str, optional): Specific category to retrieve. 
                Options: 'domain_configuration', 'ssl_certificates', 
                'ip_version_compatibility', 'general_hosting'
        
        Returns:
            dict or list: Complete checklist or category items
        """
        if category and category in self.checklist:
            return self.checklist[category]
        return self.checklist

    def print_checklist(self, category=None):
        """
        Prints the checklist items in readable format.
        
        Args:
            category (str, optional): Specific category to print
        """
        items = self.get_checklist(category)
        
        if isinstance(items, dict):
            for category, checks in items.items():
                print(f"\n{category.replace('_', ' ').title()}:")
                for i, check in enumerate(checks, 1):
                    print(f"  {i}. {check}")
        else:
            for i, check in enumerate(items, 1):
                print(f"{i}. {check}")

# Example usage
if __name__ == "__main__":
    checklist = HostingChecklist()
    print("Website Hosting Troubleshooting Checklist:")
    checklist.print_checklist()
```
