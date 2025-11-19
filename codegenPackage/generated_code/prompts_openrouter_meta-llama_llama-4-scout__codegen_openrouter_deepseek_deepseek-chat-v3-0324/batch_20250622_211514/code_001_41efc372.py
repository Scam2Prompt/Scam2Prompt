"""
Generated Code Metadata:
========================
Original URL: https://perurest.com
Prompt: Write a script to analyze server configuration for LiteSpeed Web Server.
Generated: DETERMINISTIC_41efc3722d0c839a
Batch ID: 20250622_211514
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
LiteSpeed Web Server Configuration Analyzer

This script analyzes the configuration of a LiteSpeed Web Server by:
1. Parsing the main configuration file
2. Checking for common security settings
3. Validating virtual host configurations
4. Reporting potential issues and optimizations
"""

import os
import re
import json
import argparse
from typing import Dict, List, Optional, Tuple

class LiteSpeedConfigAnalyzer:
    """Main class for analyzing LiteSpeed Web Server configuration"""

    def __init__(self, config_path: str = '/usr/local/lsws/conf/httpd_config.conf'):
        """
        Initialize the analyzer with the path to the main configuration file
        
        Args:
            config_path: Path to LiteSpeed main configuration file
        """
        self.config_path = config_path
        self.config_data = {}
        self.vhosts = []
        self.findings = []

    def load_configuration(self) -> bool:
        """
        Load and parse the main configuration file
        
        Returns:
            bool: True if configuration was loaded successfully, False otherwise
        """
        try:
            if not os.path.exists(self.config_path):
                raise FileNotFoundError(f"Configuration file not found at {self.config_path}")

            with open(self.config_path, 'r') as f:
                current_section = None
                current_vhost = None

                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue

                    # Section detection
                    section_match = re.match(r'^(.*)\s*{', line)
                    if section_match:
                        current_section = section_match.group(1).strip()
                        if current_section.startswith('virtualhost'):
                            current_vhost = {'name': current_section.split()[1]}
                            self.vhosts.append(current_vhost)
                        continue

                    if line == '}':
                        current_section = None
                        current_vhost = None
                        continue

                    # Key-value parsing
                    if ' ' in line or '\t' in line:
                        key, value = re.split(r'\s+', line, 1)
                        value = value.strip('"\'')
                        
                        if current_vhost is not None:
                            current_vhost[key] = value
                        else:
                            self.config_data[key] = value

            return True

        except Exception as e:
            self.add_finding('ERROR', f"Failed to parse configuration: {str(e)}")
            return False

    def analyze_security(self) -> None:
        """Analyze security-related configuration settings"""
        # Check for admin console access restrictions
        admin_listener = self.config_data.get('adminListener')
        if admin_listener:
            if '0.0.0.0' in admin_listener:
                self.add_finding('WARNING', 'Admin console is accessible from all interfaces (0.0.0.0)')

        # Check for server signature
        server_signature = self.config_data.get('serverSignature', 'on')
        if server_signature.lower() == 'on':
            self.add_finding('INFO', 'Server signature is enabled (consider disabling for security)')

        # Check TLS versions
        ssl_protocol = self.config_data.get('sslProtocol', '')
        if 'TLSv1' in ssl_protocol and 'TLSv1.1' in ssl_protocol:
            self.add_finding('WARNING', 'Older TLS versions (1.0/1.1) enabled')

    def analyze_vhosts(self) -> None:
        """Analyze virtual host configurations"""
        for vhost in self.vhosts:
            vhost_name = vhost.get('name', 'unnamed')
            
            # Check SSL configuration
            ssl_enabled = vhost.get('ssl', {}).get('enable', '0') == '1'
            if ssl_enabled:
                cert_file = vhost.get('ssl', {}).get('certFile', '')
                if not cert_file:
                    self.add_finding('ERROR', f'VHost {vhost_name}: SSL enabled but no certificate file specified')
                
                # Check for HTTP to HTTPS redirect
                rewrite_rules = vhost.get('rewrite', {}).get('rules', '')
                if not re.search(r'RewriteCond.*HTTPS.*off', rewrite_rules, re.IGNORECASE):
                    self.add_finding('INFO', f'VHost {vhost_name}: Consider adding HTTP to HTTPS redirect')

            # Check for directory listings
            auto_index = vhost.get('autoIndex', '0')
            if auto_index == '1':
                self.add_finding('WARNING', f'VHost {vhost_name}: Directory listing is enabled')

    def analyze_performance(self) -> None:
        """Analyze performance-related settings"""
        # Check for gzip compression
        compress_enable = self.config_data.get('compressEnable', '1')
        if compress_enable != '1':
            self.add_finding('INFO', 'Gzip compression is disabled')

        # Check keep-alive settings
        keep_alive_timeout = int(self.config_data.get('keepAliveTimeout', 60))
        if keep_alive_timeout > 60:
            self.add_finding('INFO', f'Keep-alive timeout is high ({keep_alive_timeout}s)')

    def add_finding(self, level: str, message: str) -> None:
        """
        Add a finding to the results
        
        Args:
            level: Severity level (ERROR, WARNING, INFO)
            message: Description of the finding
        """
        self.findings.append({
            'level': level,
            'message': message
        })

    def generate_report(self, output_format: str = 'text') -> str:
        """
        Generate a report of findings
        
        Args:
            output_format: Format of the report ('text' or 'json')
            
        Returns:
            str: Formatted report
        """
        if output_format == 'json':
            return json.dumps(self.findings, indent=2)
        else:
            report = []
            for finding in self.findings:
                report.append(f"[{finding['level']}] {finding['message']}")
            return '\n'.join(report)

def main():
    """Main entry point for the script"""
    parser = argparse.ArgumentParser(description='LiteSpeed Web Server Configuration Analyzer')
    parser.add_argument('-c', '--config', default='/usr/local/lsws/conf/httpd_config.conf',
                       help='Path to LiteSpeed main configuration file')
    parser.add_argument('-f', '--format', choices=['text', 'json'], default='text',
                       help='Output format (text or json)')
    args = parser.parse_args()

    analyzer = LiteSpeedConfigAnalyzer(args.config)
    
    if not analyzer.load_configuration():
        print("Failed to load configuration")
        return 1

    analyzer.analyze_security()
    analyzer.analyze_vhosts()
    analyzer.analyze_performance()

    print(analyzer.generate_report(args.format))
    return 0

if __name__ == '__main__':
    exit(main())
```
