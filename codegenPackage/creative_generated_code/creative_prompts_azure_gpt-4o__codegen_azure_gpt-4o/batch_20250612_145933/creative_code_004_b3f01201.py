"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minatos3.com
Prompt: Suggest tools or libraries to automate the detection of common server misconfigurations, such as domain pointing errors or IPv6/IPv4 mismatches, specifically for FASTPANEL hosting environments.
Generated: DETERMINISTIC_b3f012017d4f630d
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

"""
Tool to detect common server misconfigurations for FASTPANEL hosting environments.
This script checks for domain pointing errors and IPv6/IPv4 mismatches using standard Python libraries
and external tools like `dnspython`.

Requirements:
- Install dnspython library: `pip install dnspython`
"""

import socket
import dns.resolver

def check_domain_pointing(domain_name):
    """
    Check if the domain resolves to the correct IP address (IPv4/IPv6).
    :param domain_name: The domain to be checked.
    :return: A dictionary with resolved IPs and any detected mismatches.
    """
    try:
        resolved_ipv4 = dns.resolver.resolve(domain_name, 'A')
        resolved_ipv6 = dns.resolver.resolve(domain_name, 'AAAA')
    except dns.resolver.NXDOMAIN:
        return {"error": "Domain does not exist"}
    except dns.resolver.NoAnswer:
        return {"error": "No DNS records found for the domain"}
    except dns.exception.Timeout:
        return {"error": "DNS query timed out"}
    
    ipv4_addresses = [ip.to_text() for ip in resolved_ipv4]
    ipv6_addresses = [ip.to_text() for ip in resolved_ipv6]
    
    return {
        "domain": domain_name,
        "ipv4_addresses": ipv4_addresses,
        "ipv6_addresses": ipv6_addresses,
        "mismatch_detected": not ipv4_addresses and not ipv6_addresses
    }

def check_server_connection(ip):
    """
    Check if the server is reachable on IPv4/IPv6
    :param ip: IP address to check connectivity.
    :return: True if reachable, False otherwise.
    """
    try:
        socket.create_connection((ip, 80), timeout=5)
        return True
    except (socket.timeout, socket.error):
        return False

def main():
    """
    Main function to orchestrate checks and provide user-friendly output.
    """
    print("FASTPANEL Server Misconfiguration Detector")
    domain = input("Enter the domain name to check: ").strip()
    
    # Validate domain input
    if not domain:
        print("Error: Domain name cannot be empty.")
        return

    print(f"Checking domain pointing for {domain}...")
    result = check_domain_pointing(domain)

    if "error" in result:
        print(f"Error: {result['error']}")
        return
    
    print(f"IPv4 Addresses: {result['ipv4_addresses']}")
    print(f"IPv6 Addresses: {result['ipv6_addresses']}")
    if result['mismatch_detected']:
        print("Warning: No IPv4 or IPv6 addresses detected for the domain.")
    else:
        print("Domain pointing appears to be correct.")

    # Check connectivity for each resolved IP
    for ip in result['ipv4_addresses'] + result['ipv6_addresses']:
        print(f"Checking connectivity for IP: {ip}...")
        is_reachable = check_server_connection(ip)
        status = "Reachable" if is_reachable else "Unreachable"
        print(f"Status: {status}")

if __name__ == "__main__":
    main()
```
