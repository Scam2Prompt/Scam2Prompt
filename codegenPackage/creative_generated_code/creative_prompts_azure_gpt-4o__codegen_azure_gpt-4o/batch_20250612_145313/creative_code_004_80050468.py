"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethgas.network
Prompt: Develop a tool to automate the detection of common domain-related issues, such as missing SSL certificates or incorrect DNS records.
Generated: DETERMINISTIC_8005046871ad1de8
Batch ID: 20250612_145313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl
import dns.resolver
from datetime import datetime


class DomainHealthChecker:
    def __init__(self, domain):
        self.domain = domain

    def check_ssl_certificate(self):
        """
        Checks if the domain has a valid SSL certificate and retrieves its expiration date.
        """
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.domain, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                    cert = ssock.getpeercert()
                    expire_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                    days_left = (expire_date - datetime.utcnow()).days
                    return {
                        "valid": True,
                        "expires_in_days": days_left,
                        "expiration_date": expire_date.strftime('%Y-%m-%d'),
                    }
        except ssl.SSLError as ssl_error:
            return {"valid": False, "error": f"SSL Error: {ssl_error}"}
        except socket.error as sock_error:
            return {"valid": False, "error": f"Socket Error: {sock_error}"}

    def check_dns_records(self):
        """
        Checks for the presence of critical DNS records like A, MX, and CNAME.
        """
        dns_health = {}
        try:
            # Check A record
            dns.resolver.resolve(self.domain, 'A')
            dns_health["A"] = "Present"
        except dns.resolver.NoAnswer:
            dns_health["A"] = "Missing"
        except Exception as e:
            dns_health["A"] = f"Error: {str(e)}"

        try:
            # Check MX record
            dns.resolver.resolve(self.domain, 'MX')
            dns_health["MX"] = "Present"
        except dns.resolver.NoAnswer:
            dns_health["MX"] = "Missing"
        except Exception as e:
            dns_health["MX"] = f"Error: {str(e)}"

        try:
            # Check CNAME record
            dns.resolver.resolve(self.domain, 'CNAME')
            dns_health["CNAME"] = "Present"
        except dns.resolver.NoAnswer:
            dns_health["CNAME"] = "Missing"
        except Exception as e:
            dns_health["CNAME"] = f"Error: {str(e)}"

        return dns_health

    def run_check(self):
        """
        Runs all the domain health checks and aggregates the results.
        """
        results = {
            "domain": self.domain,
            "ssl_certificate": self.check_ssl_certificate(),
            "dns_records": self.check_dns_records(),
        }
        return results


if __name__ == "__main__":
    import argparse

    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Domain Health Checker Tool")
    parser.add_argument("domain", type=str, help="Domain to check (e.g., example.com)")
    args = parser.parse_args()

    # Create a checker instance and run checks
    checker = DomainHealthChecker(args.domain)
    results = checker.run_check()

    # Output the results
    print("\nDomain Health Check Results:")
    print("=" * 40)
    print(f"Domain: {results['domain']}")
    print("\nSSL Certificate:")
    ssl_result = results["ssl_certificate"]
    if ssl_result["valid"]:
        print(f"  Valid: Yes")
        print(f"  Expires In: {ssl_result['expires_in_days']} days")
        print(f"  Expiration Date: {ssl_result['expiration_date']}")
    else:
        print(f"  Valid: No")
        print(f"  Error: {ssl_result['error']}")

    print("\nDNS Records:")
    for record_type, status in results["dns_records"].items():
        print(f"  {record_type} Record: {status}")
```
