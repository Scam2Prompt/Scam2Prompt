"""
Generated Code Metadata:
========================
Original URL: https://claim-resolv.digital
Prompt: What are the common DNS record issues that cause a website to not load, and how can I troubleshoot them using tools like `dig` and `nslookup`?
Generated: DETERMINISTIC_f8f44093f3bf5b1b
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import sys
from typing import Optional, List, Dict

class DNSTroubleshooter:
    """
    A class to troubleshoot common DNS record issues using dig and nslookup.
    """
    
    def __init__(self, domain: str):
        self.domain = domain
        self.common_records = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SOA']
    
    def run_command(self, command: List[str]) -> Optional[str]:
        """
        Execute a shell command and return its output.
        
        Args:
            command: List of command and arguments
            
        Returns:
            Command output as string or None if error occurs
        """
        try:
            result = subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing command {' '.join(command)}: {e.stderr}")
            return None
    
    def check_dig(self, record_type: str = 'A') -> Optional[str]:
        """
        Query DNS records using dig.
        
        Args:
            record_type: Type of DNS record to query
            
        Returns:
            dig command output or None if error occurs
        """
        command = ['dig', '+short', self.domain, record_type]
        return self.run_command(command)
    
    def check_nslookup(self, record_type: str = 'A') -> Optional[str]:
        """
        Query DNS records using nslookup.
        
        Args:
            record_type: Type of DNS record to query
            
        Returns:
            nslookup command output or None if error occurs
        """
        command = ['nslookup', '-query=' + record_type, self.domain]
        return self.run_command(command)
    
    def check_all_records(self) -> Dict[str, Optional[str]]:
        """
        Check all common DNS record types for the domain.
        
        Returns:
            Dictionary mapping record types to their query results
        """
        results = {}
        for record in self.common_records:
            dig_result = self.check_dig(record)
            nslookup_result = self.check_nslookup(record)
            results[f"dig_{record}"] = dig_result
            results[f"nslookup_{record}"] = nslookup_result
        return results
    
    def verify_dns_resolution(self) -> bool:
        """
        Verify basic DNS resolution works for the domain.
        
        Returns:
            True if A or AAAA records exist, False otherwise
        """
        a_record = self.check_dig('A')
        aaaa_record = self.check_dig('AAAA')
        
        if a_record or aaaa_record:
            return True
        return False
    
    def check_nameservers(self) -> Optional[str]:
        """
        Check the NS records for the domain.
        
        Returns:
            Nameserver information or None if error occurs
        """
        return self.check_dig('NS')
    
    def check_mx_records(self) -> Optional[str]:
        """
        Check the MX records for the domain.
        
        Returns:
            MX record information or None if error occurs
        """
        return self.check_dig('MX')

def main():
    if len(sys.argv) < 2:
        print("Usage: python dns_troubleshooter.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    troubleshooter = DNSTroubleshooter(domain)
    
    print(f"\nChecking DNS records for {domain}:\n")
    
    # Basic resolution check
    if not troubleshooter.verify_dns_resolution():
        print("ERROR: Domain does not resolve to any IP address (missing A/AAAA records)")
    else:
        print("✓ Domain resolves to an IP address")
    
    # Check nameservers
    print("\nNameservers:")
    ns_records = troubleshooter.check_nameservers()
    if ns_records:
        print(ns_records)
    else:
        print("ERROR: Could not retrieve nameserver records")
    
    # Check MX records
    print("\nMail servers (MX records):")
    mx_records = troubleshooter.check_mx_records()
    if mx_records:
        print(mx_records)
    else:
        print("No MX records found or error retrieving them")
    
    # Full record check
    print("\nChecking all common record types:")
    all_records = troubleshooter.check_all_records()
    for record_type, result in all_records.items():
        print(f"\n{record_type}:")
        print(result if result else "No records found or error occurred")

if __name__ == "__main__":
    main()
```
