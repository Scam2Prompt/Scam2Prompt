"""
Generated Code Metadata:
========================
Original URL: https://0x1111.icu
Prompt: Create a diagnostic tool to identify issues with AAAA records and IPv4 compatibility for domains hosted on FASTPANEL.
Generated: DETERMINISTIC_4b30fefaa81f52ef
Batch ID: 20250612_154207
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
import concurrent.futures
import logging
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fastpanel_diagnostic.log'),
        logging.StreamHandler()
    ]
)

class FastPanelDiagnosticTool:
    def __init__(self, domains: List[str], max_workers: int = 10):
        """
        Initialize the diagnostic tool with a list of domains to check.
        
        Args:
            domains: List of domain names to diagnose
            max_workers: Maximum number of concurrent workers for DNS lookups
        """
        self.domains = domains
        self.max_workers = max_workers
        self.results: Dict[str, Dict] = {}
        self.dns_resolver = dns.resolver.Resolver()
        self.dns_resolver.timeout = 5
        self.dns_resolver.lifetime = 5

    def check_aaaa_record(self, domain: str) -> Optional[List[str]]:
        """
        Check if a domain has AAAA records (IPv6).
        
        Args:
            domain: Domain name to check
            
        Returns:
            List of AAAA records if found, None otherwise
        """
        try:
            answers = self.dns_resolver.resolve(domain, 'AAAA')
            return [str(r) for r in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            return None
        except dns.exception.DNSException as e:
            logging.warning(f"DNS lookup error for {domain} (AAAA): {str(e)}")
            return None

    def check_a_record(self, domain: str) -> Optional[List[str]]:
        """
        Check if a domain has A records (IPv4).
        
        Args:
            domain: Domain name to check
            
        Returns:
            List of A records if found, None otherwise
        """
        try:
            answers = self.dns_resolver.resolve(domain, 'A')
            return [str(r) for r in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            return None
        except dns.exception.DNSException as e:
            logging.warning(f"DNS lookup error for {domain} (A): {str(e)}")
            return None

    def check_connectivity(self, domain: str, ip_version: int = 4) -> bool:
        """
        Check basic connectivity to a domain on specified IP version.
        
        Args:
            domain: Domain name to check
            ip_version: 4 for IPv4, 6 for IPv6
            
        Returns:
            True if connection was successful, False otherwise
        """
        try:
            family = socket.AF_INET if ip_version == 4 else socket.AF_INET6
            with socket.socket(family, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((domain, 80))
                return True
        except (socket.timeout, socket.gaierror, ConnectionRefusedError, OSError) as e:
            logging.debug(f"Connectivity check failed for {domain} (IPv{ip_version}): {str(e)}")
            return False

    def diagnose_domain(self, domain: str) -> Dict:
        """
        Run full diagnostics for a single domain.
        
        Args:
            domain: Domain name to diagnose
            
        Returns:
            Dictionary with diagnostic results
        """
        result = {
            'domain': domain,
            'has_aaaa': False,
            'aaaa_records': None,
            'has_a': False,
            'a_records': None,
            'ipv6_connectivity': False,
            'ipv4_connectivity': False,
            'issues': []
        }

        # Check DNS records
        aaaa_records = self.check_aaaa_record(domain)
        a_records = self.check_a_record(domain)

        if aaaa_records:
            result['has_aaaa'] = True
            result['aaaa_records'] = aaaa_records
        else:
            result['issues'].append('No AAAA records found')

        if a_records:
            result['has_a'] = True
            result['a_records'] = a_records
        else:
            result['issues'].append('No A records found')

        # Check connectivity if records exist
        if result['has_aaaa']:
            result['ipv6_connectivity'] = self.check_connectivity(domain, 6)
            if not result['ipv6_connectivity']:
                result['issues'].append('IPv6 connectivity failed')

        if result['has_a']:
            result['ipv4_connectivity'] = self.check_connectivity(domain, 4)
            if not result['ipv4_connectivity']:
                result['issues'].append('IPv4 connectivity failed')

        # Special case: No records at all
        if not result['has_aaaa'] and not result['has_a']:
            result['issues'].append('No DNS records found (neither A nor AAAA)')

        return result

    def run_diagnostics(self) -> Dict[str, Dict]:
        """
        Run diagnostics for all domains using thread pool.
        
        Returns:
            Dictionary with results for all domains
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_domain = {
                executor.submit(self.diagnose_domain, domain): domain
                for domain in self.domains
            }
            
            for future in concurrent.futures.as_completed(future_to_domain):
                domain = future_to_domain[future]
                try:
                    self.results[domain] = future.result()
                except Exception as e:
                    logging.error(f"Error processing domain {domain}: {str(e)}")
                    self.results[domain] = {
                        'domain': domain,
                        'error': str(e),
                        'issues': ['Diagnostic failed']
                    }

        return self.results

    def generate_report(self) -> str:
        """
        Generate a human-readable report from the diagnostic results.
        
        Returns:
            Formatted report string
        """
        if not self.results:
            return "No diagnostic results available. Run diagnostics first."

        report_lines = []
        for domain, result in self.results.items():
            report_lines.append(f"\n=== Domain: {domain} ===")
            
            if 'error' in result:
                report_lines.append(f"  Error: {result['error']}")
                continue

            report_lines.append("  DNS Records:")
            if result['has_aaaa']:
                report_lines.append(f"    AAAA: {', '.join(result['aaaa_records'])}")
            else:
                report_lines.append("    AAAA: None")
                
            if result['has_a']:
                report_lines.append(f"    A: {', '.join(result['a_records'])}")
            else:
                report_lines.append("    A: None")
                
            report_lines.append("  Connectivity:")
            report_lines.append(f"    IPv6: {'OK' if result['ipv6_connectivity'] else 'FAILED'}")
            report_lines.append(f"    IPv4: {'OK' if result['ipv4_connectivity'] else 'FAILED'}")
            
            if result['issues']:
                report_lines.append("  Issues:")
                for issue in result['issues']:
                    report_lines.append(f"    - {issue}")
            else:
                report_lines.append("  No issues detected")

        return "\n".join(report_lines)

def main():
    """Main function to demonstrate the diagnostic tool."""
    # Example usage
    domains = [
        'example.com',
        'ipv6.google.com',
        'nonexistent.fastpanel.test'
    ]
    
    diagnostic_tool = FastPanelDiagnosticTool(domains)
    results = diagnostic_tool.run_diagnostics()
    report = diagnostic_tool.generate_report()
    
    print(report)
    logging.info("Diagnostic completed. Results saved to fastpanel_diagnostic.log")

if __name__ == "__main__":
    main()
```
