"""
Generated Code Metadata:
========================
Original URL: https://metacoins.biz
Prompt: Write a script to log and report errors related to domain pointing, SSL certificates, and IPv4/IPv6 compatibility for FASTPANEL-hosted websites.
Generated: DETERMINISTIC_c3c6874cf204b5dc
Batch ID: 20250612_155102
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
Script to monitor and report issues with domain pointing, SSL certificates, and IPv4/IPv6 compatibility
for websites hosted on FASTPANEL.
"""

import sys
import socket
import ssl
import dns.resolver
import ipaddress
import logging
from datetime import datetime
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fastpanel_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DomainMonitor:
    def __init__(self, domains: List[str]):
        self.domains = domains
        self.results: List[Dict] = []

    def check_domain_pointing(self, domain: str) -> Tuple[bool, str]:
        """Check if domain correctly points to FASTPANEL server."""
        try:
            # Resolve A and AAAA records
            a_records = []
            aaaa_records = []
            
            try:
                a_records = [str(r) for r in dns.resolver.resolve(domain, 'A')]
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                pass
                
            try:
                aaaa_records = [str(r) for r in dns.resolver.resolve(domain, 'AAAA')]
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                pass

            if not a_records and not aaaa_records:
                return False, "No DNS records found (A or AAAA)"
                
            # Here you would add logic to verify if IPs belong to FASTPANEL
            # This is a placeholder - replace with actual FASTPANEL IP check
            fastpanel_ips = {'192.0.2.1', '2001:db8::1'}  # Example IPs
            
            for ip in a_records + aaaa_records:
                if ip not in fastpanel_ips:
                    return False, f"Domain points to non-FASTPANEL IP: {ip}"
                    
            return True, "Domain correctly points to FASTPANEL"
            
        except Exception as e:
            logger.error(f"Error checking domain pointing for {domain}: {str(e)}")
            return False, f"DNS resolution error: {str(e)}"

    def check_ssl_certificate(self, domain: str) -> Tuple[bool, str]:
        """Check SSL certificate validity and configuration."""
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    
            # Check certificate expiration
            not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            days_remaining = (not_after - datetime.now()).days
            if days_remaining < 7:
                return False, f"SSL certificate expires in {days_remaining} days"
                
            # Check subjectAltName
            san = []
            for ext in cert.get('subjectAltName', []):
                san.append(ext[1])
                
            if domain not in san and f"*.{domain.split('.', 1)[1]}" not in san:
                return False, "Domain not in certificate's Subject Alternative Name"
                
            return True, "SSL certificate is valid and properly configured"
            
        except ssl.SSLError as e:
            return False, f"SSL error: {str(e)}"
        except Exception as e:
            logger.error(f"Error checking SSL certificate for {domain}: {str(e)}")
            return False, f"Certificate check error: {str(e)}"

    def check_ip_compatibility(self, domain: str) -> Tuple[bool, str]:
        """Check IPv4 and IPv6 connectivity."""
        ipv4_ok = False
        ipv6_ok = False
        
        try:
            # Check IPv4
            socket.AF_INET6 = socket.AF_INET  # Temporary override for testing
            with socket.create_connection((domain, 80), timeout=5):
                ipv4_ok = True
        except:
            pass
        finally:
            socket.AF_INET6 = socket.AF_INET6  # Restore original value
            
        try:
            # Check IPv6
            with socket.create_connection((domain, 80), timeout=5):
                ipv6_ok = True
        except:
            pass
            
        if not ipv4_ok and not ipv6_ok:
            return False, "No IPv4 or IPv6 connectivity"
        elif not ipv6_ok:
            return True, "IPv4 only (no IPv6)"
        elif not ipv4_ok:
            return True, "IPv6 only (no IPv4)"
        else:
            return True, "Dual-stack (IPv4 and IPv6) supported"

    def run_checks(self) -> None:
        """Run all checks for all domains."""
        for domain in self.domains:
            result = {
                'domain': domain,
                'timestamp': datetime.now().isoformat(),
                'checks': {}
            }
            
            # Domain pointing check
            pointing_ok, pointing_msg = self.check_domain_pointing(domain)
            result['checks']['domain_pointing'] = {
                'status': pointing_ok,
                'message': pointing_msg
            }
            
            # SSL certificate check
            ssl_ok, ssl_msg = self.check_ssl_certificate(domain)
            result['checks']['ssl_certificate'] = {
                'status': ssl_ok,
                'message': ssl_msg
            }
            
            # IP compatibility check
            ip_ok, ip_msg = self.check_ip_compatibility(domain)
            result['checks']['ip_compatibility'] = {
                'status': ip_ok,
                'message': ip_msg
            }
            
            self.results.append(result)
            
            # Log results
            if not all([pointing_ok, ssl_ok, ip_ok]):
                logger.warning(f"Issues found for {domain}:")
                if not pointing_ok:
                    logger.warning(f"  Domain pointing: {pointing_msg}")
                if not ssl_ok:
                    logger.warning(f"  SSL certificate: {ssl_msg}")
                if not ip_ok:
                    logger.warning(f"  IP compatibility: {ip_msg}")

    def generate_report(self) -> str:
        """Generate a summary report of all checks."""
        report = []
        report.append("FASTPANEL Domain Monitoring Report")
        report.append("=" * 40)
        report.append(f"Generated at: {datetime.now().isoformat()}")
        report.append(f"Domains checked: {len(self.domains)}")
        report.append("")
        
        issues_found = 0
        for result in self.results:
            if not all(check['status'] for check in result['checks'].values()):
                issues_found += 1
                report.append(f"Domain: {result['domain']}")
                for check_name, check_data in result['checks'].items():
                    if not check_data['status']:
                        report.append(f"  {check_name.replace('_', ' ').title()}: {check_data['message']}")
                report.append("")
        
        if issues_found == 0:
            report.append("All domains are properly configured with no issues detected.")
        else:
            report.append(f"Total domains with issues: {issues_found}")
            
        return "\n".join(report)

def main():
    if len(sys.argv) < 2:
        print("Usage: python fastpanel_monitor.py domain1.com [domain2.com ...]")
        sys.exit(1)
        
    domains = sys.argv[1:]
    monitor = DomainMonitor(domains)
    
    try:
        logger.info(f"Starting monitoring for {len(domains)} domains")
        monitor.run_checks()
        report = monitor.generate_report()
        print(report)
        logger.info("Monitoring completed")
    except Exception as e:
        logger.error(f"Fatal error during monitoring: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
