"""
Generated Code Metadata:
========================
Original URL: https://etherveum.org
Prompt: Generate a script to identify whether a domain is correctly pointed to a server and suggest fixes based on FASTPANEL's common issues.
Generated: DETERMINISTIC_3673ddab5b80f639
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dns.resolver
import socket
import sys
from typing import Optional, Tuple, List

class DomainChecker:
    """
    A class to check if a domain is correctly pointed to a server and suggest fixes.
    """
    
    def __init__(self, domain: str, expected_ip: str):
        """
        Initialize the DomainChecker with the domain and expected IP.
        
        Args:
            domain (str): The domain to check.
            expected_ip (str): The expected IP address the domain should resolve to.
        """
        self.domain = domain
        self.expected_ip = expected_ip
        self.common_issues = {
            "DNS_PROBLEM": "DNS records are not properly configured.",
            "NO_A_RECORD": "No A record found for the domain.",
            "WRONG_IP": "Domain resolves to a different IP than expected.",
            "NO_CNAME": "No CNAME record found for www subdomain.",
            "WWW_NOT_POINTED": "www subdomain is not pointed to the main domain.",
            "NO_NS_RECORDS": "No NS records found for the domain.",
            "NS_NOT_FASTPANEL": "NS records are not pointing to FASTPANEL nameservers."
        }
    
    def resolve_a_record(self) -> Tuple[Optional[List[str]], Optional[str]]:
        """
        Resolve A records for the domain.
        
        Returns:
            Tuple[Optional[List[str]], Optional[str]]: A list of resolved IPs and an error message if any.
        """
        try:
            answers = dns.resolver.resolve(self.domain, 'A')
            ips = [str(answer) for answer in answers]
            return ips, None
        except dns.resolver.NoAnswer:
            return None, self.common_issues["NO_A_RECORD"]
        except dns.resolver.NXDOMAIN:
            return None, f"Domain {self.domain} does not exist."
        except dns.resolver.NoNameservers:
            return None, "No nameservers found for the domain."
        except Exception as e:
            return None, f"DNS resolution error: {str(e)}"
    
    def resolve_cname(self, subdomain: str = 'www') -> Tuple[Optional[List[str]], Optional[str]]:
        """
        Resolve CNAME records for a subdomain.
        
        Args:
            subdomain (str): The subdomain to check (default is 'www').
            
        Returns:
            Tuple[Optional[List[str]], Optional[str]]: A list of resolved CNAMEs and an error message if any.
        """
        try:
            answers = dns.resolver.resolve(f"{subdomain}.{self.domain}", 'CNAME')
            cnames = [str(answer) for answer in answers]
            return cnames, None
        except dns.resolver.NoAnswer:
            return None, f"No CNAME record found for {subdomain}.{self.domain}."
        except dns.resolver.NXDOMAIN:
            return None, f"Subdomain {subdomain}.{self.domain} does not exist."
        except Exception as e:
            return None, f"DNS resolution error: {str(e)}"
    
    def resolve_ns_records(self) -> Tuple[Optional[List[str]], Optional[str]]:
        """
        Resolve NS records for the domain.
        
        Returns:
            Tuple[Optional[List[str]], Optional[str]]: A list of nameservers and an error message if any.
        """
        try:
            answers = dns.resolver.resolve(self.domain, 'NS')
            nameservers = [str(answer) for answer in answers]
            return nameservers, None
        except dns.resolver.NoAnswer:
            return None, self.common_issues["NO_NS_RECORDS"]
        except Exception as e:
            return None, f"DNS resolution error: {str(e)}"
    
    def check_nameservers(self, fastpanel_ns: List[str]) -> Optional[str]:
        """
        Check if the domain's nameservers are FASTPANEL nameservers.
        
        Args:
            fastpanel_ns (List[str]): List of FASTPANEL nameservers.
            
        Returns:
            Optional[str]: Error message if nameservers are not FASTPANEL.
        """
        nameservers, error = self.resolve_ns_records()
        if error:
            return error
        
        for ns in nameservers:
            if ns.rstrip('.') not in fastpanel_ns:
                return self.common_issues["NS_NOT_FASTPANEL"]
        return None
    
    def check_domain(self, fastpanel_ns: List[str]) -> List[str]:
        """
        Perform all checks on the domain and return a list of issues.
        
        Args:
            fastpanel_ns (List[str]): List of FASTPANEL nameservers.
            
        Returns:
            List[str]: List of issues found.
        """
        issues = []
        
        # Check A record
        ips, error = self.resolve_a_record()
        if error:
            issues.append(error)
        elif self.expected_ip not in ips:
            issues.append(self.common_issues["WRONG_IP"])
        
        # Check www CNAME
        cnames, error = self.resolve_cname()
        if error:
            issues.append(error)
        elif cnames and f"{self.domain}." not in cnames:
            issues.append(self.common_issues["WWW_NOT_POINTED"])
        
        # Check nameservers
        ns_error = self.check_nameservers(fastpanel_ns)
        if ns_error:
            issues.append(ns_error)
        
        return issues
    
    def suggest_fixes(self, issues: List[str]) -> List[str]:
        """
        Suggest fixes based on the issues found.
        
        Args:
            issues (List[str]): List of issues.
            
        Returns:
            List[str]: List of suggested fixes.
        """
        fixes = []
        for issue in issues:
            if issue == self.common_issues["NO_A_RECORD"]:
                fixes.append(f"Add an A record for {self.domain} pointing to {self.expected_ip}.")
            elif issue == self.common_issues["WRONG_IP"]:
                fixes.append(f"Update the A record for {self.domain} to point to {self.expected_ip}.")
            elif issue == self.common_issues["NO_CNAME"]:
                fixes.append(f"Add a CNAME record for www.{self.domain} pointing to {self.domain}.")
            elif issue == self.common_issues["WWW_NOT_POINTED"]:
                fixes.append(f"Update the CNAME record for www.{self.domain} to point to {self.domain}.")
            elif issue == self.common_issues["NO_NS_RECORDS"]:
                fixes.append("Add NS records for the domain.")
            elif issue == self.common_issues["NS_NOT_FASTPANEL"]:
                fixes.append("Update the NS records to point to FASTPANEL nameservers.")
            else:
                fixes.append(f"Fix the issue: {issue}.")
        return fixes

def main():
    if len(sys.argv) != 3:
        print("Usage: python domain_checker.py <domain> <expected_ip>")
        sys.exit(1)
    
    domain = sys.argv[1]
    expected_ip = sys.argv[2]
    
    # Example FASTPANEL nameservers (replace with actual FASTPANEL nameservers)
    fastpanel_ns = ["ns1.fastpanel.direct", "ns2.fastpanel.direct"]
    
    checker = DomainChecker(domain, expected_ip)
    issues = checker.check_domain(fastpanel_ns)
    
    if issues:
        print("Issues found:")
        for issue in issues:
            print(f"- {issue}")
        
        print("\nSuggested fixes:")
        fixes = checker.suggest_fixes(issues)
        for fix in fixes:
            print(f"- {fix}")
    else:
        print(f"Domain {domain} is correctly pointed to {expected_ip}.")

if __name__ == "__main__":
    main()
```
