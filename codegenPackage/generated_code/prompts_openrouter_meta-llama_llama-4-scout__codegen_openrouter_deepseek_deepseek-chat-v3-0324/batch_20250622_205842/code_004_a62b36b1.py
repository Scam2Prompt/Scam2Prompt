"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: Generate a checklist for troubleshooting common web hosting issues, including domain configuration, SSL certificates, and IP version compatibility.
Generated: DETERMINISTIC_a62b36b1386e5864
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Web Hosting Troubleshooting Checklist
"""

class WebHostingChecklist:
    """
    A checklist for troubleshooting common web hosting issues.
    """
    
    def __init__(self):
        self.checklist = {
            'domain_configuration': [
                "Verify DNS records (A, CNAME, MX) are correctly set",
                "Check domain registrar settings",
                "Ensure domain is not expired",
                "Confirm nameservers are properly configured",
                "Check for DNS propagation delays",
                "Verify domain is pointing to correct IP/server",
                "Check for typos in domain name"
            ],
            'ssl_certificates': [
                "Verify certificate is installed correctly",
                "Check certificate expiration date",
                "Ensure certificate matches domain name",
                "Verify chain of trust is complete",
                "Check for mixed content issues",
                "Confirm HTTPS redirects are working",
                "Validate certificate with online SSL checker"
            ],
            'ip_version_compatibility': [
                "Check if IPv6 is properly configured (if used)",
                "Verify IPv4 connectivity",
                "Test both IPv4 and IPv6 DNS records",
                "Ensure firewall allows both IP versions",
                "Check for IP version-specific routing issues",
                "Test website with IPv4/IPv6 specific tools",
                "Verify CDN/load balancer IP version support"
            ],
            'general_checks': [
                "Check server status/uptime",
                "Verify hosting account is active",
                "Confirm sufficient disk space/bandwidth",
                "Check for server-side errors in logs",
                "Test from different networks/devices",
                "Verify .htaccess/web.config settings",
                "Check for recent configuration changes"
            ]
        }
    
    def get_checklist(self, category=None):
        """
        Retrieve troubleshooting checklist items.
        
        Args:
            category (str, optional): Specific category to retrieve. 
                                    If None, returns all categories.
        
        Returns:
            dict: Checklist items organized by category
        """
        if category and category in self.checklist:
            return {category: self.checklist[category]}
        return self.checklist
    
    def print_checklist(self, category=None):
        """
        Print formatted checklist to console.
        
        Args:
            category (str, optional): Specific category to print. 
                                    If None, prints all categories.
        """
        items = self.get_checklist(category)
        
        for category, checks in items.items():
            print(f"\n{category.replace('_', ' ').title()}:")
            for i, check in enumerate(checks, 1):
                print(f"  {i}. {check}")


# Example usage
if __name__ == "__main__":
    checklist = WebHostingChecklist()
    checklist.print_checklist()
```
