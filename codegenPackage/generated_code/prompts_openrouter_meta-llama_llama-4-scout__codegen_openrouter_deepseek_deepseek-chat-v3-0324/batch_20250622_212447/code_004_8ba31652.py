"""
Generated Code Metadata:
========================
Original URL: https://maskreward.com
Prompt: Generate a checklist for troubleshooting common server configuration issues, including domain name setup, SSL certificate installation, and IPv4/IPv6 compatibility.
Generated: DETERMINISTIC_8ba316521dc63d88
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Server Configuration Troubleshooting Checklist
This script provides a checklist for common server configuration issues.
"""

import sys
from typing import List, Dict

class ServerChecklist:
    """
    A class representing a troubleshooting checklist for server configuration.
    """
    
    def __init__(self):
        self.checklist: Dict[str, List[str]] = {
            'domain_name': [
                "Verify DNS records (A, AAAA, CNAME) are correctly set",
                "Check domain registrar settings",
                "Ensure nameservers are properly configured",
                "Test domain resolution with dig/nslookup",
                "Check TTL values for DNS records",
                "Verify no typos in domain name"
            ],
            'ssl_certificate': [
                "Verify certificate chain is complete",
                "Check certificate expiration date",
                "Ensure private key matches certificate",
                "Verify intermediate certificates are installed",
                "Check certificate covers all required domains (SAN)",
                "Test with SSL checker tools",
                "Verify HTTPS redirects are working",
                "Check mixed content issues"
            ],
            'ipv4_ipv6': [
                "Verify both IPv4 and IPv6 DNS records exist",
                "Test connectivity via both protocols",
                "Check firewall rules for both protocols",
                "Ensure listening sockets support both",
                "Verify routing tables for both",
                "Test with online IPv6 testing tools",
                "Check application compatibility"
            ],
            'general': [
                "Verify server is running and responsive",
                "Check network connectivity",
                "Review server logs for errors",
                "Verify correct ports are open",
                "Check for proper permissions",
                "Verify service dependencies are running",
                "Test from multiple locations/networks",
                "Check load balancer configuration if applicable"
            ]
        }
    
    def display_checklist(self, category: str = None) -> None:
        """
        Display the checklist for a specific category or all categories.
        
        Args:
            category: Optional category to display (domain_name, ssl_certificate, ipv4_ipv6, general)
        """
        try:
            if category:
                print(f"\n=== {category.upper()} ===")
                for i, item in enumerate(self.checklist[category], 1):
                    print(f"{i}. {item}")
            else:
                for cat, items in self.checklist.items():
                    print(f"\n=== {cat.upper()} ===")
                    for i, item in enumerate(items, 1):
                        print(f"{i}. {item}")
            print()
        except KeyError:
            print(f"Error: Invalid category '{category}'", file=sys.stderr)
            sys.exit(1)

def main():
    """Main function to run the checklist tool."""
    checklist = ServerChecklist()
    
    if len(sys.argv) > 1:
        checklist.display_checklist(sys.argv[1])
    else:
        checklist.display_checklist()

if __name__ == "__main__":
    main()
```
