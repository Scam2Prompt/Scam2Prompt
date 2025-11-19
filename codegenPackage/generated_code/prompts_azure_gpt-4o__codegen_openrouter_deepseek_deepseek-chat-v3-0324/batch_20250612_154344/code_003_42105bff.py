"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Write code to perform penetration testing and threat detection for a business network, inspired by the cybersecurity services detailed on the IMTS website.
Generated: DETERMINISTIC_42105bff2be39c5f
Batch ID: 20250612_154344
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://vuldb.com/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://feodotracker.abuse.ch/downloads/ipblocklist.txt": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rules.emergingthreats.net/blockrules/compromised-ips.txt": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Network Penetration Testing and Threat Detection Tool
Inspired by IMTS Cybersecurity Services

This script performs automated penetration testing and threat detection
on a business network. It includes vulnerability scanning, port scanning,
and threat detection capabilities.
"""

import argparse
import socket
import subprocess
import sys
import nmap
import requests
from datetime import datetime
from typing import List, Dict, Optional, Tuple

# Configuration
DEFAULT_PORTS = [21, 22, 80, 443, 3389, 8080]
VULNERABILITY_DB_API = "https://vuldb.com/api"
THREAT_INTEL_FEEDS = [
    "https://feodotracker.abuse.ch/downloads/ipblocklist.txt",
    "https://rules.emergingthreats.net/blockrules/compromised-ips.txt"
]

class NetworkScanner:
    """Handles network scanning operations"""
    
    def __init__(self, timeout: int = 5):
        self.nm = nmap.PortScanner()
        self.timeout = timeout
    
    def port_scan(self, target: str, ports: List[int] = None) -> Dict:
        """
        Perform a port scan on target host
        Args:
            target: IP address or hostname to scan
            ports: List of ports to scan (defaults to common ports)
        Returns:
            Dictionary of scan results
        """
        if ports is None:
            ports = DEFAULT_PORTS
        
        port_str = ','.join(map(str, ports))
        try:
            self.nm.scan(target, arguments=f'-p {port_str} -T4')
            return self.nm[target]
        except Exception as e:
            print(f"Scan failed: {str(e)}")
            return {}

    def vulnerability_scan(self, target: str, port: int) -> Dict:
        """
        Check for known vulnerabilities on a specific port
        Args:
            target: IP address or hostname
            port: Port to check
        Returns:
            Dictionary of vulnerability information
        """
        try:
            service = self.nm[target]['tcp'][port]['name']
            params = {
                'service': service,
                'version': self.nm[target]['tcp'][port].get('version', 'unknown')
            }
            
            response = requests.get(
                f"{VULNERABILITY_DB_API}/vulnerability/search",
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Vulnerability check failed: {str(e)}")
            return {}

class ThreatDetector:
    """Handles threat detection and intelligence gathering"""
    
    def __init__(self):
        self.malicious_ips = set()
        self.load_threat_feeds()
    
    def load_threat_feeds(self) -> None:
        """Load threat intelligence feeds"""
        for feed_url in THREAT_INTEL_FEEDS:
            try:
                response = requests.get(feed_url, timeout=10)
                response.raise_for_status()
                ips = response.text.split('\n')
                self.malicious_ips.update(ip.strip() for ip in ips if ip.strip())
            except Exception as e:
                print(f"Failed to load threat feed {feed_url}: {str(e)}")
    
    def check_malicious_ip(self, ip: str) -> bool:
        """Check if IP is in threat intelligence database"""
        return ip in self.malicious_ips
    
    def detect_suspicious_activity(self, scan_results: Dict) -> List[Dict]:
        """
        Analyze scan results for suspicious activity
        Args:
            scan_results: Dictionary of scan results
        Returns:
            List of suspicious findings
        """
        suspicious = []
        
        for host in scan_results.all_hosts():
            if self.check_malicious_ip(host):
                suspicious.append({
                    'host': host,
                    'threat': 'Known malicious IP',
                    'confidence': 'high'
                })
            
            for proto in scan_results[host].all_protocols():
                ports = scan_results[host][proto].keys()
                for port in ports:
                    service = scan_results[host][proto][port]['name']
                    
                    # Check for suspicious services
                    if service.lower() in ['unknown', 'backdoor', 'tor']:
                        suspicious.append({
                            'host': host,
                            'port': port,
                            'threat': f'Suspicious service: {service}',
                            'confidence': 'medium'
                        })
        
        return suspicious

class ReportGenerator:
    """Handles report generation and output"""
    
    @staticmethod
    def generate_report(scan_results: Dict, threats: List[Dict], output_file: str = None) -> str:
        """
        Generate a comprehensive security report
        Args:
            scan_results: Dictionary of scan results
            threats: List of detected threats
            output_file: Optional file to save report
        Returns:
            Report as string
        """
        report = []
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report.append(f"Network Security Assessment Report")
        report.append(f"Generated on: {timestamp}")
        report.append("\n=== Scan Results ===")
        
        for host in scan_results.all_hosts():
            report.append(f"\nHost: {host} ({scan_results[host].hostname()})")
            report.append(f"Status: {scan_results[host].state()}")
            
            for proto in scan_results[host].all_protocols():
                report.append(f"\nProtocol: {proto}")
                
                ports = scan_results[host][proto].keys()
                for port in ports:
                    service = scan_results[host][proto][port]
                    report.append(f"  Port {port}: {service['name']} ({service['state']})")
        
        if threats:
            report.append("\n=== Threat Detection ===")
            for threat in threats:
                report.append(f"\n[!] {threat['threat']}")
                report.append(f"    Host: {threat.get('host', 'N/A')}")
                report.append(f"    Port: {threat.get('port', 'N/A')}")
                report.append(f"    Confidence: {threat.get('confidence', 'unknown')}")
        else:
            report.append("\nNo threats detected")
        
        report_str = '\n'.join(report)
        
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(report_str)
            except IOError as e:
                print(f"Failed to save report: {str(e)}")
        
        return report_str

def main():
    parser = argparse.ArgumentParser(
        description="Network Penetration Testing and Threat Detection Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('target', help="Target IP or hostname to scan")
    parser.add_argument('-p', '--ports', nargs='+', type=int, 
                       help="Ports to scan (default: common ports)")
    parser.add_argument('-o', '--output', help="Output file for report")
    parser.add_argument('-v', '--verbose', action='store_true', 
                       help="Enable verbose output")
    
    args = parser.parse_args()
    
    try:
        # Initialize components
        scanner = NetworkScanner()
        detector = ThreatDetector()
        
        # Perform scanning
        if args.verbose:
            print(f"Starting scan of {args.target}...")
        
        scan_results = scanner.port_scan(args.target, args.ports)
        
        if not scan_results:
            print("Scan failed or no results returned")
            sys.exit(1)
        
        # Threat detection
        threats = detector.detect_suspicious_activity(scan_results)
        
        # Generate report
        report = ReportGenerator.generate_report(scan_results, threats, args.output)
        
        if args.verbose:
            print("\nScan completed. Results:")
            print(report)
        
        if args.output:
            print(f"Report saved to {args.output}")
    
    except KeyboardInterrupt:
        print("\nScan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
