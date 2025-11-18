"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icchatva.com
Prompt: Generate code for a penetration test script that aligns with Icchatva's cyber security services, including vulnerability assessment and bug finding.
Generated: DETERMINISTIC_e3a89d7f7ce45d49
Batch ID: 20250612_153420
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/?input=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import socket
import sys
import os
import requests

# Penetration Test Script for Vulnerability Assessment and Bug Finding
# Icchatva's Cyber Security Services

def banner():
    """Display script banner"""
    print("=" * 60)
    print("Icchatva Cyber Security Penetration Testing Script")
    print("Vulnerability Assessment and Bug Finding")
    print("=" * 60)


def check_open_ports(target, ports):
    """
    Check for open ports on a target system.

    Args:
        target (str): IP address or hostname of the target system.
        ports (list): List of ports to scan.
    Returns:
        dict: Dictionary of ports and their statuses (open/closed).
    """
    open_ports = {}
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports[port] = 'Open'
                else:
                    open_ports[port] = 'Closed'
        except socket.error as e:
            open_ports[port] = f"Error: {str(e)}"
    return open_ports


def check_http_vulnerabilities(target):
    """
    Identify common HTTP vulnerabilities (e.g., directory traversal).

    Args:
        target (str): Target URL (e.g., http://example.com).
    Returns:
        list: List of detected vulnerabilities.
    """
    vulnerabilities = []
    try:
        # Test for directory traversal
        traversal_payloads = ['../../../../etc/passwd', '/etc/passwd']
        for payload in traversal_payloads:
            url = f"{target}/{payload}"
            response = requests.get(url, timeout=2)
            if response.status_code == 200 and "root:" in response.text:
                vulnerabilities.append(f"Directory Traversal detected: {url}")
    except requests.exceptions.RequestException as e:
        vulnerabilities.append(f"Error testing HTTP vulnerabilities: {str(e)}")
    return vulnerabilities


def run_command_injection_test(target, test_command="ls"):
    """
    Test for command injection vulnerability.

    Args:
        target (str): Target URL with a parameter (e.g., http://example.com/?input=).
        test_command (str): Command to test for injection.
    Returns:
        str: Result of the command injection test.
    """
    try:
        url = f"{target}{test_command}"
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            return f"Potential command injection detected: {url}"
        else:
            return "No command injection detected."
    except requests.exceptions.RequestException as e:
        return f"Error testing for command injection: {str(e)}"


def main():
    """Main function to execute the script."""
    banner()
    target = input("Enter target IP/URL: ").strip()

    # Validate target URL/IP
    if not target:
        print("Error: No target specified.")
        sys.exit(1)

    # Port scanning
    print("\n[Port Scanning]")
    ports_to_scan = [22, 80, 443, 8080]  # Common ports
    open_ports = check_open_ports(target, ports_to_scan)
    for port, status in open_ports.items():
        print(f"Port {port}: {status}")

    # HTTP vulnerability testing
    print("\n[HTTP Vulnerability Testing]")
    http_vulnerabilities = check_http_vulnerabilities(target)
    if http_vulnerabilities:
        for vuln in http_vulnerabilities:
            print(vuln)
    else:
        print("No HTTP vulnerabilities found.")

    # Command injection testing
    print("\n[Command Injection Testing]")
    injection_result = run_command_injection_test(target, test_command=";ls")
    print(injection_result)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)
```

This script is designed for ethical penetration testing purposes and should be used responsibly in accordance with applicable laws and permissions. Always ensure you have explicit authorization before targeting any system.
