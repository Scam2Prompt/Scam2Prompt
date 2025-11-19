"""
Generated Code Metadata:
========================
Original URL: https://hosico-cat.fun
Prompt: Create a diagnostic tool to automate the detection of common server configuration issues mentioned in FASTPANEL, including domain pointing and SSL certificate problems.
Generated: DETERMINISTIC_2f706c52cb3c4029
Batch ID: 20250612_155106
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
FASTPANEL Server Configuration Diagnostic Tool

This script automates the detection of common server configuration issues
including domain pointing and SSL certificate problems.
"""

import os
import sys
import socket
import ssl
import dns.resolver
import datetime
import argparse
from urllib.parse import urlparse
from typing import List, Dict, Tuple, Optional

class ServerDiagnosticTool:
    def __init__(self, domain: str, verbose: bool = False):
        """
        Initialize the diagnostic tool with the target domain.
        
        Args:
            domain: The domain to diagnose
            verbose: Whether to show detailed output
        """
        self.domain = domain
        self.verbose = verbose
        self.results = {
            'domain': domain,
            'dns': {},
            'ssl': {},
            'connectivity': {},
            'issues': []
        }

    def log(self, message: str) -> None:
        """Log messages if verbose mode is enabled."""
        if self.verbose:
            print(f"[DEBUG] {message}")

    def check_dns_records(self) -> None:
        """Check DNS records for the domain."""
        try:
            self.log(f"Checking DNS records for {self.domain}")
            
            # Check A records
            try:
                a_records = dns.resolver.resolve(self.domain, 'A')
                self.results['dns']['a_records'] = [str(record) for record in a_records]
                self.log(f"A records found: {self.results['dns']['a_records']}")
            except dns.resolver.NoAnswer:
                self.results['dns']['a_records'] = []
                self.results['issues'].append(f"No A records found for {self.domain}")
            
            # Check CNAME records
            try:
                cname_records = dns.resolver.resolve(self.domain, 'CNAME')
                self.results['dns']['cname_records'] = [str(record) for record in cname_records]
                self.log(f"CNAME records found: {self.results['dns']['cname_records']}")
            except dns.resolver.NoAnswer:
                self.results['dns']['cname_records'] = []
            
            # Check MX records
            try:
                mx_records = dns.resolver.resolve(self.domain, 'MX')
                self.results['dns']['mx_records'] = [str(record) for record in mx_records]
                self.log(f"MX records found: {self.results['dns']['mx_records']}")
            except dns.resolver.NoAnswer:
                self.results['dns']['mx_records'] = []
            
        except dns.resolver.NXDOMAIN:
            self.results['issues'].append(f"Domain {self.domain} does not exist (NXDOMAIN)")
        except Exception as e:
            self.results['issues'].append(f"DNS lookup failed: {str(e)}")

    def check_ssl_certificate(self) -> None:
        """Check SSL certificate validity and configuration."""
        try:
            self.log(f"Checking SSL certificate for {self.domain}")
            
            context = ssl.create_default_context()
            with socket.create_connection((self.domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                    cert = ssock.getpeercert()
            
            # Parse certificate information
            self.results['ssl']['issued_to'] = dict(x[0] for x in cert['subject'])
            self.results['ssl']['issued_by'] = dict(x[0] for x in cert['issuer'])
            
            # Check expiration
            not_after = cert['notAfter']
            expiry_date = datetime.datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
            remaining_days = (expiry_date - datetime.datetime.now()).days
            
            self.results['ssl']['expiry_date'] = expiry_date.isoformat()
            self.results['ssl']['remaining_days'] = remaining_days
            
            if remaining_days < 7:
                self.results['issues'].append(
                    f"SSL certificate expires in {remaining_days} days ({expiry_date.date()})"
                )
            
            # Check subject alternative names
            san = []
            for ext in cert.get('subjectAltName', []):
                san.append(ext[1])
            self.results['ssl']['subject_alt_names'] = san
            
            if self.domain not in san and f"*.{self.domain}" not in san:
                self.results['issues'].append(
                    f"Domain {self.domain} not found in certificate's Subject Alternative Names"
                )
            
        except ssl.SSLError as e:
            self.results['issues'].append(f"SSL certificate error: {str(e)}")
        except Exception as e:
            self.results['issues'].append(f"SSL check failed: {str(e)}")

    def check_connectivity(self) -> None:
        """Check basic connectivity to common ports."""
        ports_to_check = [80, 443, 21, 22, 25]
        
        for port in ports_to_check:
            try:
                self.log(f"Checking connectivity to {self.domain}:{port}")
                with socket.create_connection((self.domain, port), timeout=5):
                    self.results['connectivity'][str(port)] = "Open"
            except socket.timeout:
                self.results['connectivity'][str(port)] = "Timeout"
                if port in [80, 443]:
                    self.results['issues'].append(f"Timeout connecting to port {port}")
            except ConnectionRefusedError:
                self.results['connectivity'][str(port)] = "Refused"
            except Exception as e:
                self.results['connectivity'][str(port)] = f"Error: {str(e)}"
                if port in [80, 443]:
                    self.results['issues'].append(f"Connection error on port {port}: {str(e)}")

    def run_checks(self) -> Dict:
        """Run all diagnostic checks."""
        self.check_dns_records()
        self.check_ssl_certificate()
        self.check_connectivity()
        return self.results

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="FASTPANEL Server Configuration Diagnostic Tool"
    )
    parser.add_argument(
        "domain",
        help="Domain name to diagnose"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file to save results (JSON format)"
    )
    return parser.parse_args()

def main() -> None:
    """Main entry point for the diagnostic tool."""
    args = parse_args()
    
    try:
        tool = ServerDiagnosticTool(args.domain, args.verbose)
        results = tool.run_checks()
        
        # Print results
        print("\nDiagnostic Results:")
        print(f"Domain: {results['domain']}")
        
        print("\nIssues Found:")
        if results['issues']:
            for issue in results['issues']:
                print(f"- {issue}")
        else:
            print("- No critical issues found")
        
        if args.output:
            import json
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\nResults saved to {args.output}")
    
    except Exception as e:
        print(f"Error running diagnostics: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
