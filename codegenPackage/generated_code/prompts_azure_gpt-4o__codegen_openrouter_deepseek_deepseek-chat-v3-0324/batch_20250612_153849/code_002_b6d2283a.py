"""
Generated Code Metadata:
========================
Original URL: https://msu.best
Prompt: Create a Python script to detect and resolve issues with AAAA records for domains that only support IPv4 on FASTPANEL servers.
Generated: DETERMINISTIC_b6d2283a25d2a3e0
Batch ID: 20250612_153849
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
Script to detect and resolve issues with AAAA records for domains that only support IPv4 on FASTPANEL servers.
"""

import dns.resolver
import logging
import sys
from typing import List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('aaaa_record_checker.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AAAARecordChecker:
    def __init__(self, domain_list: List[str], nameservers: Optional[List[str]] = None):
        """
        Initialize the checker with a list of domains and optional nameservers.
        
        Args:
            domain_list: List of domains to check
            nameservers: Optional list of nameservers to use for DNS queries
        """
        self.domains = domain_list
        self.resolver = dns.resolver.Resolver()
        
        if nameservers:
            self.resolver.nameservers = nameservers

    def check_aaaa_records(self, domain: str) -> Tuple[bool, Optional[List[str]]]:
        """
        Check if a domain has AAAA records.
        
        Args:
            domain: Domain to check
            
        Returns:
            Tuple of (has_aaaa, records) where has_aaaa is a boolean indicating
            if AAAA records exist, and records is the list of AAAA records or None
        """
        try:
            answers = self.resolver.resolve(domain, 'AAAA')
            return (True, [str(r) for r in answers])
        except dns.resolver.NoAnswer:
            return (False, None)
        except dns.resolver.NXDOMAIN:
            logger.warning(f"Domain {domain} does not exist (NXDOMAIN)")
            return (False, None)
        except dns.resolver.NoNameservers:
            logger.warning(f"No nameservers found for domain {domain}")
            return (False, None)
        except Exception as e:
            logger.error(f"Error checking AAAA records for {domain}: {str(e)}")
            return (False, None)

    def check_a_records(self, domain: str) -> bool:
        """
        Check if a domain has A records (IPv4 support).
        
        Args:
            domain: Domain to check
            
        Returns:
            Boolean indicating if A records exist
        """
        try:
            self.resolver.resolve(domain, 'A')
            return True
        except dns.resolver.NoAnswer:
            return False
        except Exception as e:
            logger.error(f"Error checking A records for {domain}: {str(e)}")
            return False

    def process_domains(self) -> List[str]:
        """
        Process all domains to find those with AAAA records but no A records.
        
        Returns:
            List of domains that have AAAA records but no A records
        """
        problematic_domains = []
        
        for domain in self.domains:
            logger.info(f"Checking domain: {domain}")
            
            has_aaaa, aaaa_records = self.check_aaaa_records(domain)
            has_a = self.check_a_records(domain)
            
            if has_aaaa and not has_a:
                logger.warning(f"Domain {domain} has AAAA records but no A records: {aaaa_records}")
                problematic_domains.append(domain)
            elif has_aaaa and has_a:
                logger.info(f"Domain {domain} has both A and AAAA records (IPv4 and IPv6 supported)")
            elif not has_aaaa and has_a:
                logger.info(f"Domain {domain} has only A records (IPv4 only)")
            else:
                logger.warning(f"Domain {domain} has neither A nor AAAA records")
                
        return problematic_domains

    def generate_fastpanel_commands(self, domains: List[str]) -> str:
        """
        Generate FASTPANEL commands to remove AAAA records for given domains.
        
        Args:
            domains: List of domains to generate commands for
            
        Returns:
            String containing the FASTPANEL commands
        """
        commands = []
        for domain in domains:
            commands.append(f"fastpanel dns remove {domain} AAAA")
        return "\n".join(commands)

def main():
    # Example usage - in production, you might want to read domains from a file
    domains_to_check = [
        "example.com",
        "test.example.org",
        "ipv6-only.test",
    ]
    
    # Optional: Specify FASTPANEL nameservers if needed
    nameservers = None  # or ["ns1.fastpanel.example", "ns2.fastpanel.example"]
    
    checker = AAAARecordChecker(domains_to_check, nameservers)
    problematic_domains = checker.process_domains()
    
    if problematic_domains:
        logger.warning("The following domains have AAAA records but no A records:")
        for domain in problematic_domains:
            logger.warning(f"- {domain}")
        
        commands = checker.generate_fastpanel_commands(problematic_domains)
        logger.info("\nFASTPANEL commands to remove AAAA records:\n")
        logger.info(commands)
    else:
        logger.info("No domains with AAAA records but no A records found.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Script interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        sys.exit(1)
```
